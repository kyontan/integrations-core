# (C) Datadog, Inc. 2020-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
from datadog_checks.dev.jmx import JVM_E2E_METRICS_NEW

METRICS = [
    'hazelcast.imap.local_backup_count',
    'hazelcast.imap.local_backup_entry_count',
    'hazelcast.imap.local_backup_entry_memory_cost',
    'hazelcast.imap.local_creation_time',
    'hazelcast.imap.local_dirty_entry_count',
    'hazelcast.imap.local_event_operation_count',
    'hazelcast.imap.local_get_operation_count',
    'hazelcast.imap.local_heap_cost',
    'hazelcast.imap.local_hits',
    'hazelcast.imap.local_last_access_time',
    'hazelcast.imap.local_last_update_time',
    'hazelcast.imap.local_locked_entry_count',
    'hazelcast.imap.local_max_get_latency',
    'hazelcast.imap.local_max_put_latency',
    'hazelcast.imap.local_max_remove_latency',
    'hazelcast.imap.local_other_operation_count',
    'hazelcast.imap.local_owned_entry_count',
    'hazelcast.imap.local_owned_entry_memory_cost',
    'hazelcast.imap.local_put_operation_count',
    'hazelcast.imap.local_remove_operation_count',
    'hazelcast.imap.local_total',
    'hazelcast.imap.local_total_get_latency',
    'hazelcast.imap.local_total_put_latency',
    'hazelcast.imap.local_total_remove_latency',
    'hazelcast.imap.size',
    'hazelcast.instance.managed_executor_service.completed_task_count',
    'hazelcast.instance.managed_executor_service.is_shutdown',
    'hazelcast.instance.managed_executor_service.is_terminated',
    'hazelcast.instance.managed_executor_service.maximum_pool_size',
    'hazelcast.instance.managed_executor_service.pool_size',
    'hazelcast.instance.managed_executor_service.queue_size',
    'hazelcast.instance.managed_executor_service.remaining_queue_capacity',
    'hazelcast.instance.member_count',
    'hazelcast.instance.partition_service.active_partition_count',
    'hazelcast.instance.partition_service.is_cluster_safe',
    'hazelcast.instance.partition_service.is_local_member_safe',
    'hazelcast.instance.partition_service.partition_count',
    'hazelcast.instance.running',
    'hazelcast.mc.license_expiration_time',
    'hazelcast.member.accepted_socket_count',
    'hazelcast.member.active_count',
    'hazelcast.member.active_members',
    'hazelcast.member.active_members_commit_index',
    'hazelcast.member.async_operations',
    'hazelcast.member.available_processors',
    'hazelcast.member.backup_timeout_millis',
    'hazelcast.member.backup_timeouts',
    'hazelcast.member.bytes_transceived',
    'hazelcast.member.call_timeout_count',
    'hazelcast.member.client_count',
    'hazelcast.instance.cluster_time',
    'hazelcast.member.cluster_time_diff',
    'hazelcast.member.cluster_up_time',
    'hazelcast.member.commit_count',
    'hazelcast.member.committed_heap',
    'hazelcast.member.committed_native',
    'hazelcast.member.committed_virtual_memory_size',
    'hazelcast.member.completed_count',
    'hazelcast.member.completed_migrations',
    'hazelcast.member.completed_operation_batch_count',
    'hazelcast.member.completed_operation_count',
    'hazelcast.member.completed_packet_count',
    'hazelcast.member.completed_partition_specific_runnable_count',
    'hazelcast.member.completed_runnable_count',
    'hazelcast.member.completed_task_count',
    'hazelcast.member.completed_tasks',
    'hazelcast.member.completed_total_count',
    'hazelcast.member.count',
    'hazelcast.member.created_count',
    'hazelcast.member.daemon_thread_count',
    'hazelcast.member.delayed_execution_count',
    'hazelcast.member.destroyed_count',
    'hazelcast.member.destroyed_group_ids',
    'hazelcast.member.elapsed_destination_commit_time',
    'hazelcast.member.elapsed_migration_operation_time',
    'hazelcast.member.elapsed_migration_time',
    'hazelcast.member.error_count',
    'hazelcast.member.event_count',
    'hazelcast.member.event_queue_size',
    'hazelcast.member.events_processed',
    'hazelcast.member.failed_backups',
    'hazelcast.member.frames_transceived',
    'hazelcast.member.free_heap',
    'hazelcast.member.free_memory',
    'hazelcast.member.free_native',
    'hazelcast.member.free_physical',
    'hazelcast.member.free_physical_memory_size',
    'hazelcast.member.free_space',
    'hazelcast.member.free_swap_space_size',
    'hazelcast.member.generic_priority_queue_size',
    'hazelcast.member.generic_queue_size',
    'hazelcast.member.generic_thread_count',
    'hazelcast.member.groups',
    'hazelcast.member.heartbeat_broadcast_period_millis',
    'hazelcast.member.heartbeat_packets_received',
    'hazelcast.member.heartbeat_packets_sent',
    'hazelcast.member.idle_time_millis',
    'hazelcast.member.invocation_scan_period_millis',
    'hazelcast.member.invocation_timeout_millis',
    'hazelcast.member.invocations.last_call_id',
    'hazelcast.member.invocations.pending',
    'hazelcast.member.invocations.used_percentage',
    'hazelcast.member.io_thread_id',
    'hazelcast.member.last_heartbeat',
    'hazelcast.member.last_repartition_time',
    'hazelcast.member.listener_count',
    'hazelcast.member.loaded_classes_count',
    'hazelcast.member.local_partition_count',
    'hazelcast.member.major_count',
    'hazelcast.member.major_time',
    'hazelcast.member.max_backup_count',
    'hazelcast.member.max_cluster_time_diff',
    'hazelcast.member.max_file_descriptor_count',
    'hazelcast.member.max_heap',
    'hazelcast.member.max_memory',
    'hazelcast.member.max_metadata',
    'hazelcast.member.max_native',
    'hazelcast.member.maximum_pool_size',
    'hazelcast.member.member_groups_size',
    'hazelcast.member.migration_active',
    'hazelcast.member.migration_queue_size',
    'hazelcast.member.minor_count',
    'hazelcast.member.minor_time',
    'hazelcast.member.missing_members',
    'hazelcast.member.nodes',
    'hazelcast.member.normal_pending_count',
    'hazelcast.member.normal_timeouts',
    'hazelcast.member.open_file_descriptor_count',
    'hazelcast.member.operation_timeout_count',
    'hazelcast.member.park_queue_count',
    'hazelcast.member.partition_thread_count',
    'hazelcast.member.peak_thread_count',
    'hazelcast.member.planned_migrations',
    'hazelcast.member.pool_size',
    'hazelcast.member.priority_frames_transceived',
    'hazelcast.member.priority_pending_count',
    'hazelcast.member.priority_queue_size',
    'hazelcast.member.process_count',
    'hazelcast.member.process_cpu_load',
    'hazelcast.member.process_cpu_time',
    'hazelcast.member.proxy_count',
    'hazelcast.member.publication_count',
    'hazelcast.member.queue_capacity',
    'hazelcast.member.queue_size',
    'hazelcast.member.rejected_count',
    'hazelcast.member.remaining_queue_capacity',
    'hazelcast.member.replica_sync_requests_counter',
    'hazelcast.member.replica_sync_semaphore',
    'hazelcast.member.response_queue_size',
    'hazelcast.member.responses.backup_count',
    'hazelcast.member.responses.error_count',
    'hazelcast.member.responses.missing_count',
    'hazelcast.member.responses.normal_count',
    'hazelcast.member.responses.timeout_count',
    'hazelcast.member.retry_count',
    'hazelcast.member.rollback_count',
    'hazelcast.member.running_count',
    'hazelcast.member.running_generic_count',
    'hazelcast.member.running_partition_count',
    'hazelcast.member.selector_i_o_exception_count',
    'hazelcast.member.selector_rebuild_count',
    'hazelcast.member.size',
    'hazelcast.member.start_count',
    'hazelcast.member.sync_delivery_failure_count',
    'hazelcast.member.system_cpu_load',
    'hazelcast.member.system_load_average',
    'hazelcast.member.task_queue_size',
    'hazelcast.member.terminated_raft_node_group_ids',
    'hazelcast.member.text_count',
    'hazelcast.member.thread_count',
    'hazelcast.member.total_completed_migrations',
    'hazelcast.member.total_elapsed_destination_commit_time',
    'hazelcast.member.total_elapsed_migration_operation_time',
    'hazelcast.member.total_elapsed_migration_time',
    'hazelcast.member.total_failure_count',
    'hazelcast.member.total_loaded_classes_count',
    'hazelcast.member.total_memory',
    'hazelcast.member.total_parked_operation_count',
    'hazelcast.member.total_physical',
    'hazelcast.member.total_physical_memory_size',
    'hazelcast.member.total_registrations',
    'hazelcast.member.total_space',
    'hazelcast.member.total_started_thread_count',
    'hazelcast.member.total_swap_space_size',
    'hazelcast.member.unknown_count',
    'hazelcast.member.unknown_time',
    'hazelcast.member.unloaded_classes_count',
    'hazelcast.member.uptime',
    'hazelcast.member.usable_space',
    'hazelcast.member.used_heap',
    'hazelcast.member.used_memory',
    'hazelcast.member.used_metadata',
    'hazelcast.member.used_native',
    'hazelcast.member.write_queue_size',
    'hazelcast.iqueue.minimum_age',
    'hazelcast.iqueue.maximum_age',
    'hazelcast.iqueue.average_age',
    'hazelcast.iqueue.owned_item_count',
    'hazelcast.iqueue.backup_item_count',
    'hazelcast.iqueue.offer_operation_count',
    'hazelcast.iqueue.rejected_offer_operation_count',
    'hazelcast.iqueue.poll_operation_count',
    'hazelcast.iqueue.empty_poll_operation_count',
    'hazelcast.iqueue.other_operation_count',
    'hazelcast.iqueue.event_operation_count',
    'hazelcast.reliabletopic.creation_time',
    'hazelcast.reliabletopic.publish_operation_count',
    'hazelcast.reliabletopic.receive_operation_count',
    'hazelcast.topic.creation_time',
    'hazelcast.topic.publish_operation_count',
    'hazelcast.topic.receive_operation_count',
] + JVM_E2E_METRICS_NEW

HAZELCAST_4_ONLY_METRICS = [
    'hazelcast.member.connection_type',
    'hazelcast.member.monitor_count',
    'hazelcast.member.packets_received',
    'hazelcast.member.packets_send',
    'hazelcast.member.state_version',
    # these following metrics are documented in hazelcast 5 too but they are not available in the dev env
    # https://docs.hazelcast.com/hazelcast/5.0/list-of-metrics
    'hazelcast.member.local_clock_time',
    'hazelcast.member.priority_frames_read',
    'hazelcast.member.priority_write_queue_size',
    'hazelcast.member.priority_frames_written',
    'hazelcast.member.migration_completed_count',
    'hazelcast.member.cluster_start_time',
    'hazelcast.member.closed_count',
    'hazelcast.member.selector_recreate_count',
    'hazelcast.member.exception_count',
    'hazelcast.member.started_migrations',
    'hazelcast.member.bytes_received',
    'hazelcast.member.bytes_written',
    'hazelcast.member.in_progress_count',
    'hazelcast.member.normal_frames_read',
    'hazelcast.member.connection_listener_count',
    'hazelcast.member.normal_frames_written',
    'hazelcast.member.bytes_read',
    'hazelcast.member.bytes_send',
    'hazelcast.member.idle_time_ms',
    'hazelcast.member.imbalance_detected_count',
    'hazelcast.member.owner_id',
    'hazelcast.member.opened_count',
    'hazelcast.member.scheduled',
    'hazelcast.member.cluster_time',
]
