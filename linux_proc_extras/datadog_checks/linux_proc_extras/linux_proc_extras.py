# (C) Cory Watson <cory@stripe.com> 2016
# (C) Datadog, Inc. 2016-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)

from collections import defaultdict

from datadog_checks.base import AgentCheck
from datadog_checks.base.utils.subprocess_output import get_subprocess_output

try:
    import datadog_agent
except ImportError:
    from datadog_checks.base.stubs import datadog_agent


PROCESS_STATES = {
    'D': 'uninterruptible',
    'R': 'runnable',
    'S': 'sleeping',
    'T': 'stopped',
    'W': 'paging',
    'X': 'dead',
    'Z': 'zombie',
}

PROCESS_PRIOS = {'<': 'high', 'N': 'low', 'L': 'locked'}


class MoreUnixCheck(AgentCheck):
    def __init__(self, *args, **kwargs):
        super(MoreUnixCheck, self).__init__(*args, **kwargs)
        self.tags = self.instance.get('tags', [])
        self.set_paths()

    def check(self, instance):
        self.get_inode_info()
        self.get_stat_info()
        self.get_entropy_info()
        self.get_process_states()
        if self.instance.get('include_interrupt_metrics', False):
            self.get_interrupts_info()

    def set_paths(self):
        proc_location = (datadog_agent.get_config('procfs_path') or '/proc').rstrip('/')

        self.proc_path_map = {
            "inode_info": "sys/fs/inode-nr",
            "stat_info": "stat",
            "entropy_info": "sys/kernel/random/entropy_avail",
            "interrupts_info": "interrupts",
        }

        for key, path in self.proc_path_map.items():
            self.proc_path_map[key] = "{procfs}/{path}".format(procfs=proc_location, path=path)

    def get_inode_info(self):
        with open(self.proc_path_map['inode_info'], 'r') as inode_info:
            inode_stats = inode_info.readline().split()
            self.gauge('system.inodes.total', float(inode_stats[0]), tags=self.tags)
            self.gauge('system.inodes.used', float(inode_stats[1]), tags=self.tags)

    def get_stat_info(self):
        with open(self.proc_path_map['stat_info'], 'r') as stat_info:
            lines = [line.strip() for line in stat_info.readlines()]
            for line in lines:
                if line.startswith('ctxt'):
                    ctxt_count = float(line.split(' ')[1])
                    self.monotonic_count('system.linux.context_switches', ctxt_count, tags=self.tags)
                elif line.startswith('processes'):
                    process_count = int(line.split(' ')[1])
                    self.monotonic_count('system.linux.processes_created', process_count, tags=self.tags)
                elif line.startswith('intr'):
                    interrupts = int(line.split(' ')[1])
                    self.monotonic_count('system.linux.interrupts', interrupts, tags=self.tags)

    def get_entropy_info(self):
        with open(self.proc_path_map['entropy_info'], 'r') as entropy_info:
            entropy = entropy_info.readline()
            self.gauge('system.entropy.available', float(entropy), tags=self.tags)

    def get_process_states(self):
        state_counts = defaultdict(int)
        prio_counts = defaultdict(int)
        ps = get_subprocess_output(['ps', '--no-header', '-eo', 'stat'], self.log)
        for state in ps[0]:
            # Each process state is a flag in a list of characters. See ps(1) for details.
            for _ in list(state):
                if state in PROCESS_STATES:
                    state_counts[PROCESS_STATES[state]] += 1
                elif state in PROCESS_PRIOS:
                    prio_counts[PROCESS_PRIOS[state]] += 1

        for state in state_counts:
            state_tags = list(self.tags)
            state_tags.append("state:" + state)
            self.gauge('system.processes.states', float(state_counts[state]), state_tags)

        for prio in prio_counts:
            prio_tags = list(self.tags)
            prio_tags.append("priority:" + prio)
            self.gauge('system.processes.priorities', float(prio_counts[prio]), prio_tags)

    def get_interrupts_info(self):
        with open(self.proc_path_map['interrupts_info'], 'r') as interrupts_info:
            lines = [line.strip() for line in interrupts_info.readlines()]
            cpu_count = len(lines[0].split())
            for line in lines[1:]:
                parts = line.split()
                irq_id = parts[0].replace(":", "")
                for cpu_id, part in enumerate(parts[1 : cpu_count + 1]):
                    irq_count = int(part)
                    tags = self.tags + ['irq:{}'.format(irq_id), 'cpu_id:{}'.format(cpu_id)]
                    self.monotonic_count("system.linux.irq", irq_count, tags=tags)
