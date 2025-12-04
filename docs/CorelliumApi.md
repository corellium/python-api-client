# corellium_api.CorelliumApi

All URIs are relative to *https://app.corellium.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_v1_cluster_nodes_node_id_console_get**](CorelliumApi.md#api_v1_cluster_nodes_node_id_console_get) | **GET** /api/v1/cluster/nodes/:nodeId/console | Access node console via SSH
[**api_v1_interconnects_get**](CorelliumApi.md#api_v1_interconnects_get) | **GET** /api/v1/interconnects | Get all I/O Interconnects
[**api_v1_interconnects_interconnect_id_delete**](CorelliumApi.md#api_v1_interconnects_interconnect_id_delete) | **DELETE** /api/v1/interconnects/:interconnectId | Delete I/O Interconnect
[**api_v1_interconnects_interconnect_id_get**](CorelliumApi.md#api_v1_interconnects_interconnect_id_get) | **GET** /api/v1/interconnects/:interconnectId | Get Interconnect
[**api_v1_interconnects_interconnect_id_patch**](CorelliumApi.md#api_v1_interconnects_interconnect_id_patch) | **PATCH** /api/v1/interconnects/:interconnectId | Partial Update Interconnect
[**api_v1_interconnects_interconnect_id_put**](CorelliumApi.md#api_v1_interconnects_interconnect_id_put) | **PUT** /api/v1/interconnects/:interconnectId | Update Interconnect
[**api_v1_interconnects_post**](CorelliumApi.md#api_v1_interconnects_post) | **POST** /api/v1/interconnects | Create I/O Interconnect
[**create_assessment**](CorelliumApi.md#create_assessment) | **POST** /v1/services/matrix/{instanceId}/assessments | Create assessment
[**delete_assessment**](CorelliumApi.md#delete_assessment) | **DELETE** /v1/services/matrix/{instanceId}/assessments/{assessmentId} | Delete assessment
[**download_report**](CorelliumApi.md#download_report) | **GET** /v1/services/matrix/{instanceId}/assessments/{assessmentId}/download | Download report
[**get_assessment_by_id**](CorelliumApi.md#get_assessment_by_id) | **GET** /v1/services/matrix/{instanceId}/assessments/{assessmentId} | Get assessment by ID
[**get_assessments_by_instance_id**](CorelliumApi.md#get_assessments_by_instance_id) | **GET** /v1/services/matrix/{instanceId}/instances/{instanceId}/assessments | Get assessments by instanceId
[**run_tests**](CorelliumApi.md#run_tests) | **POST** /v1/services/matrix/{instanceId}/assessments/{assessmentId}/test | Update assessment state and execute MATRIX tests
[**start_monitoring**](CorelliumApi.md#start_monitoring) | **POST** /v1/services/matrix/{instanceId}/assessments/{assessmentId}/start | Update assessment state and begin device monitoring
[**stop_monitoring**](CorelliumApi.md#stop_monitoring) | **POST** /v1/services/matrix/{instanceId}/assessments/{assessmentId}/stop | Update assessment state and stop device monitoring
[**v1_accept_shared_snapshot**](CorelliumApi.md#v1_accept_shared_snapshot) | **POST** /v1/snapshots/accept | Accept a snapshot shared with you
[**v1_activity_export**](CorelliumApi.md#v1_activity_export) | **POST** /v1/activity/export | Start activity export
[**v1_activity_list**](CorelliumApi.md#v1_activity_list) | **GET** /v1/activity | Get resource activities
[**v1_add_project_key**](CorelliumApi.md#v1_add_project_key) | **POST** /v1/projects/{projectId}/keys | Add Project Authorized Key
[**v1_add_team_role_to_project**](CorelliumApi.md#v1_add_team_role_to_project) | **PUT** /v1/roles/projects/{projectId}/teams/{teamId}/roles/{roleId} | Add team role to project
[**v1_add_user_role_to_project**](CorelliumApi.md#v1_add_user_role_to_project) | **PUT** /v1/roles/projects/{projectId}/users/{userId}/roles/{roleId} | Add user role to project
[**v1_add_user_to_team**](CorelliumApi.md#v1_add_user_to_team) | **PUT** /v1/teams/{teamId}/users/{userId} | Add user to team
[**v1_agent_app_ready**](CorelliumApi.md#v1_agent_app_ready) | **GET** /v1/instances/{instanceId}/agent/v1/app/ready | Check if App subsystem is ready
[**v1_agent_delete_file**](CorelliumApi.md#v1_agent_delete_file) | **DELETE** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Delete a File on VM
[**v1_agent_get_file**](CorelliumApi.md#v1_agent_get_file) | **GET** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Download a File from VM
[**v1_agent_get_temp_filename**](CorelliumApi.md#v1_agent_get_temp_filename) | **POST** /v1/instances/{instanceId}/agent/v1/file/temp | Get the path for a new temp file
[**v1_agent_install_app**](CorelliumApi.md#v1_agent_install_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/install | Install App at path
[**v1_agent_install_profile**](CorelliumApi.md#v1_agent_install_profile) | **POST** /v1/instances/{instanceId}/agent/v1/profile/install | Install a Profile to VM
[**v1_agent_kill_app**](CorelliumApi.md#v1_agent_kill_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/apps/{bundleId}/kill | Kill an App
[**v1_agent_list_app_icons**](CorelliumApi.md#v1_agent_list_app_icons) | **GET** /v1/instances/{instanceId}/agent/v1/app/icons | List App Icons
[**v1_agent_list_apps**](CorelliumApi.md#v1_agent_list_apps) | **GET** /v1/instances/{instanceId}/agent/v1/app/apps | List Apps
[**v1_agent_list_apps_status**](CorelliumApi.md#v1_agent_list_apps_status) | **GET** /v1/instances/{instanceId}/agent/v1/app/apps/update | List Apps Status
[**v1_agent_list_profiles**](CorelliumApi.md#v1_agent_list_profiles) | **GET** /v1/instances/{instanceId}/agent/v1/profile/profiles | List Profiles
[**v1_agent_run_app**](CorelliumApi.md#v1_agent_run_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/apps/{bundleId}/run | Run an App
[**v1_agent_set_file_attributes**](CorelliumApi.md#v1_agent_set_file_attributes) | **PATCH** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Change Attrs of a File on VM
[**v1_agent_system_get_adb_auth**](CorelliumApi.md#v1_agent_system_get_adb_auth) | **GET** /v1/instances/{instanceId}/agent/v1/system/adbauth | Get ADB Auth Setting (AOSP only)
[**v1_agent_system_get_network**](CorelliumApi.md#v1_agent_system_get_network) | **GET** /v1/instances/{instanceId}/agent/v1/system/network | Get IP of eth0 (AOSP only)
[**v1_agent_system_get_prop**](CorelliumApi.md#v1_agent_system_get_prop) | **POST** /v1/instances/{instanceId}/agent/v1/system/getprop | Get System Property (AOSP only)
[**v1_agent_system_install_open_g_apps**](CorelliumApi.md#v1_agent_system_install_open_g_apps) | **POST** /v1/instances/{instanceId}/agent/v1/system/install-opengapps | Install OpenGApps (AOSP only)
[**v1_agent_system_lock**](CorelliumApi.md#v1_agent_system_lock) | **POST** /v1/instances/{instanceId}/agent/v1/system/lock | Lock Device (iOS Only)
[**v1_agent_system_set_adb_auth**](CorelliumApi.md#v1_agent_system_set_adb_auth) | **PUT** /v1/instances/{instanceId}/agent/v1/system/adbauth | Set ADB Auth Setting (AOSP only)
[**v1_agent_system_set_hostname**](CorelliumApi.md#v1_agent_system_set_hostname) | **POST** /v1/instances/{instanceId}/agent/v1/system/setHostname | Set Hostname of instance
[**v1_agent_system_shutdown**](CorelliumApi.md#v1_agent_system_shutdown) | **POST** /v1/instances/{instanceId}/agent/v1/system/shutdown | Instruct VM to halt
[**v1_agent_system_unlock**](CorelliumApi.md#v1_agent_system_unlock) | **POST** /v1/instances/{instanceId}/agent/v1/system/unlock | Unlock Device (iOS Only)
[**v1_agent_uninstall_app**](CorelliumApi.md#v1_agent_uninstall_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/apps/{bundleId}/uninstall | Uninstall an App
[**v1_agent_uninstall_profile**](CorelliumApi.md#v1_agent_uninstall_profile) | **DELETE** /v1/instances/{instanceId}/agent/v1/profile/profiles/{profileId} | Uninstall a Profile from VM
[**v1_agent_upload_file**](CorelliumApi.md#v1_agent_upload_file) | **PUT** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Upload a file to VM
[**v1_attach_instance_interface**](CorelliumApi.md#v1_attach_instance_interface) | **POST** /v1/instances/{instanceId}/interfaces | Attach I/O Interface
[**v1_auth_login**](CorelliumApi.md#v1_auth_login) | **POST** /v1/auth/login | Log In
[**v1_btrace_preauthorize**](CorelliumApi.md#v1_btrace_preauthorize) | **GET** /v1/instances/{instanceId}/btrace-authorize | Pre-authorize an btrace download
[**v1_clear_core_trace**](CorelliumApi.md#v1_clear_core_trace) | **DELETE** /v1/instances/{instanceId}/strace | Clear CoreTrace logs
[**v1_clear_hyper_trace**](CorelliumApi.md#v1_clear_hyper_trace) | **DELETE** /v1/instances/{instanceId}/btrace | Clear HyperTrace logs
[**v1_clear_hyper_trace_hooks**](CorelliumApi.md#v1_clear_hyper_trace_hooks) | **POST** /v1/instances/{instanceId}/hooks/clear | Clear Hooks on an instance
[**v1_clear_instance_panics**](CorelliumApi.md#v1_clear_instance_panics) | **DELETE** /v1/instances/{instanceId}/panics | Clear Panics
[**v1_cluster_firmware_service_devices_get**](CorelliumApi.md#v1_cluster_firmware_service_devices_get) | **GET** /v1/cluster/firmware-service/devices | Fetch devices from the firmware service
[**v1_cluster_firmware_service_firmware_assets_asset_url_delete**](CorelliumApi.md#v1_cluster_firmware_service_firmware_assets_asset_url_delete) | **DELETE** /v1/cluster/firmware-service/firmware-assets/{assetURL} | Delete a firmware asset by its URL
[**v1_cluster_firmware_service_firmware_assets_asset_url_extended_get**](CorelliumApi.md#v1_cluster_firmware_service_firmware_assets_asset_url_extended_get) | **GET** /v1/cluster/firmware-service/firmware-assets/{assetURL}/extended | Fetch extended firmware-asset details including instances and associated IPSWs
[**v1_cluster_firmware_service_firmware_assets_get**](CorelliumApi.md#v1_cluster_firmware_service_firmware_assets_get) | **GET** /v1/cluster/firmware-service/firmware-assets | Fetch firmware assets from the firmware service
[**v1_cluster_firmware_service_firmware_assets_post**](CorelliumApi.md#v1_cluster_firmware_service_firmware_assets_post) | **POST** /v1/cluster/firmware-service/firmware-assets | Add firmware assets via the firmware service
[**v1_cluster_firmware_service_firmwares_filename_delete**](CorelliumApi.md#v1_cluster_firmware_service_firmwares_filename_delete) | **DELETE** /v1/cluster/firmware-service/firmwares/{filename} | Delete a firmware by filename from the firmware service
[**v1_cluster_firmware_service_firmwares_get**](CorelliumApi.md#v1_cluster_firmware_service_firmwares_get) | **GET** /v1/cluster/firmware-service/firmwares | Fetch firmwares from the firmware service
[**v1_cluster_nodes_get**](CorelliumApi.md#v1_cluster_nodes_get) | **GET** /v1/cluster/nodes | List servers in the cluster
[**v1_cluster_nodes_node_id_get**](CorelliumApi.md#v1_cluster_nodes_node_id_get) | **GET** /v1/cluster/nodes/:nodeId | Get node details by ID
[**v1_create_domain_auth_provider**](CorelliumApi.md#v1_create_domain_auth_provider) | **POST** /v1/domain/{domainId}/auth | Create a new auth provider for a domain
[**v1_create_hook**](CorelliumApi.md#v1_create_hook) | **POST** /v1/instances/{instanceId}/hooks | Create hypervisor hook for Instance
[**v1_create_image**](CorelliumApi.md#v1_create_image) | **POST** /v1/images | Create a new Image
[**v1_create_instance**](CorelliumApi.md#v1_create_instance) | **POST** /v1/instances | Create Instance
[**v1_create_network_connection**](CorelliumApi.md#v1_create_network_connection) | **POST** /v1/network/connections | Create a new Network Connection
[**v1_create_project**](CorelliumApi.md#v1_create_project) | **POST** /v1/projects | Create a Project
[**v1_create_snapshot**](CorelliumApi.md#v1_create_snapshot) | **POST** /v1/instances/{instanceId}/snapshots | Create Instance Snapshot
[**v1_create_user**](CorelliumApi.md#v1_create_user) | **POST** /v1/users | Create User
[**v1_delete_domain_auth_provider**](CorelliumApi.md#v1_delete_domain_auth_provider) | **DELETE** /v1/domain/{domainId}/auth/{providerId} | Delete an auth provider from a domain
[**v1_delete_extension**](CorelliumApi.md#v1_delete_extension) | **DELETE** /v1/extensions/{extensionId} | Delete an existing extension
[**v1_delete_hook**](CorelliumApi.md#v1_delete_hook) | **DELETE** /v1/hooks/{hookId} | Delete an existing hypervisor hook
[**v1_delete_image**](CorelliumApi.md#v1_delete_image) | **DELETE** /v2/images/{imageId} | Delete Image
[**v1_delete_instance**](CorelliumApi.md#v1_delete_instance) | **DELETE** /v1/instances/{instanceId} | Remove Instance
[**v1_delete_instance_snapshot**](CorelliumApi.md#v1_delete_instance_snapshot) | **DELETE** /v1/instances/{instanceId}/snapshots/{snapshotId} | Delete an Instance Snapshot
[**v1_delete_network_connection**](CorelliumApi.md#v1_delete_network_connection) | **DELETE** /v1/network/connections/{id} | Delete an existing Network Connection
[**v1_delete_project**](CorelliumApi.md#v1_delete_project) | **DELETE** /v1/projects/{projectId} | Delete a Project
[**v1_delete_snapshot**](CorelliumApi.md#v1_delete_snapshot) | **DELETE** /v1/snapshots/{snapshotId} | Delete a Snapshot
[**v1_delete_snapshot_permissions**](CorelliumApi.md#v1_delete_snapshot_permissions) | **DELETE** /v1/snapshots/{snapshotId}/permissions | Delete member(s)
[**v1_delete_user**](CorelliumApi.md#v1_delete_user) | **DELETE** /v1/users/{userId} | Delete User
[**v1_detach_instance_interface**](CorelliumApi.md#v1_detach_instance_interface) | **DELETE** /v1/instances/{instanceId}/interfaces/{interfaceId} | Detach I/O Interface
[**v1_disable_expose_port**](CorelliumApi.md#v1_disable_expose_port) | **POST** /v1/instances/{instanceId}/exposeport/disable | Disable an exposed port on an instance for device access.
[**v1_download_activity**](CorelliumApi.md#v1_download_activity) | **GET** /v1/activity/export/{taskId}/download | Download activity
[**v1_enable_expose_port**](CorelliumApi.md#v1_enable_expose_port) | **POST** /v1/instances/{instanceId}/exposeport/enable | Enable an exposed port on an instance for device access.
[**v1_execute_hyper_trace_hooks**](CorelliumApi.md#v1_execute_hyper_trace_hooks) | **POST** /v1/instances/{instanceId}/hooks/execute | Execute Hooks on an instance
[**v1_get_activity_export_status**](CorelliumApi.md#v1_get_activity_export_status) | **GET** /v1/activity/export/{taskId} | Get export task status
[**v1_get_activity_export_tasks**](CorelliumApi.md#v1_get_activity_export_tasks) | **GET** /v1/activity/export | Get all export tasks for user
[**v1_get_config**](CorelliumApi.md#v1_get_config) | **GET** /v1/config | Get all configs
[**v1_get_domain_auth_providers**](CorelliumApi.md#v1_get_domain_auth_providers) | **GET** /v1/domain/{domainId}/auth | Return all configured auth providers for a domain (including globally configured providers)
[**v1_get_extension_by_id**](CorelliumApi.md#v1_get_extension_by_id) | **GET** /v1/extensions/{extensionId} | Get extension by id
[**v1_get_extensions**](CorelliumApi.md#v1_get_extensions) | **GET** /v1/extensions | Get all extensions
[**v1_get_hook_by_id**](CorelliumApi.md#v1_get_hook_by_id) | **GET** /v1/hooks/{hookId} | Get hypervisor hook by id
[**v1_get_hooks**](CorelliumApi.md#v1_get_hooks) | **GET** /v1/instances/{instanceId}/hooks | Get all hypervisor hooks for Instance
[**v1_get_image**](CorelliumApi.md#v1_get_image) | **GET** /v1/images/{imageId} | Get Image Metadata
[**v1_get_images**](CorelliumApi.md#v1_get_images) | **GET** /v1/images | Get all Images Metadata
[**v1_get_install_firmware_status**](CorelliumApi.md#v1_get_install_firmware_status) | **GET** /v1/images/install-firmware/:taskId | Query install firmware request status.
[**v1_get_instance**](CorelliumApi.md#v1_get_instance) | **GET** /v1/instances/{instanceId} | Get Instance
[**v1_get_instance_console**](CorelliumApi.md#v1_get_instance_console) | **GET** /v1/instances/{instanceId}/console | Get console websocket URL
[**v1_get_instance_console_log**](CorelliumApi.md#v1_get_instance_console_log) | **GET** /v1/instances/{instanceId}/consoleLog | Get Console Log
[**v1_get_instance_gpios**](CorelliumApi.md#v1_get_instance_gpios) | **GET** /v1/instances/{instanceId}/gpios | Get Instance GPIOs
[**v1_get_instance_panics**](CorelliumApi.md#v1_get_instance_panics) | **GET** /v1/instances/{instanceId}/panics | Get Panics
[**v1_get_instance_peripherals**](CorelliumApi.md#v1_get_instance_peripherals) | **GET** /v1/instances/{instanceId}/peripherals | Get Instance Peripherals
[**v1_get_instance_screenshot**](CorelliumApi.md#v1_get_instance_screenshot) | **GET** /v1/instances/{instanceId}/screenshot.{format} | Get Instance Screenshot
[**v1_get_instance_snapshot**](CorelliumApi.md#v1_get_instance_snapshot) | **GET** /v1/instances/{instanceId}/snapshots/{snapshotId} | Get Instance Snapshot
[**v1_get_instance_snapshots**](CorelliumApi.md#v1_get_instance_snapshots) | **GET** /v1/instances/{instanceId}/snapshots | Get Instance Snapshots
[**v1_get_instances**](CorelliumApi.md#v1_get_instances) | **GET** /v1/instances | Get Instances
[**v1_get_model_software**](CorelliumApi.md#v1_get_model_software) | **GET** /v1/models/{model}/software | Get Software for Model
[**v1_get_models**](CorelliumApi.md#v1_get_models) | **GET** /v1/models | Get Supported Models
[**v1_get_network_connection**](CorelliumApi.md#v1_get_network_connection) | **GET** /v1/network/connections/{id} | Return the configuration and per project statuses for a single network provider.
[**v1_get_project**](CorelliumApi.md#v1_get_project) | **GET** /v1/projects/{projectId} | Get a Project
[**v1_get_project_instances**](CorelliumApi.md#v1_get_project_instances) | **GET** /v1/projects/{projectId}/instances | Get Instances in Project
[**v1_get_project_keys**](CorelliumApi.md#v1_get_project_keys) | **GET** /v1/projects/{projectId}/keys | Get Project Authorized Keys
[**v1_get_project_network_log**](CorelliumApi.md#v1_get_project_network_log) | **GET** /v1/projects/{projectId}/network/log | Retrieve the network connection log for a project
[**v1_get_project_network_status**](CorelliumApi.md#v1_get_project_network_status) | **GET** /v1/projects/{projectId}/network/status | Retrieve the network connection status for a project
[**v1_get_project_vpn_config**](CorelliumApi.md#v1_get_project_vpn_config) | **GET** /v1/projects/{projectId}/vpnconfig/{format} | Get Project VPN Configuration
[**v1_get_projects**](CorelliumApi.md#v1_get_projects) | **GET** /v1/projects | Get Projects
[**v1_get_reset_link_info**](CorelliumApi.md#v1_get_reset_link_info) | **GET** /v1/users/reset-link-info | Send Password Reset Link Info
[**v1_get_shared_snapshots**](CorelliumApi.md#v1_get_shared_snapshots) | **GET** /v1/snapshots/shared | Fetch shared snapshots
[**v1_get_snapshot**](CorelliumApi.md#v1_get_snapshot) | **GET** /v1/snapshots/{snapshotId} | Get Snapshot
[**v1_install_firmware**](CorelliumApi.md#v1_install_firmware) | **POST** /v1/images/install-firmware | Installs a firmware for cluster-wide use
[**v1_instances_instance_id_message_post**](CorelliumApi.md#v1_instances_instance_id_message_post) | **POST** /v1/instances/{instanceId}/message | Inject a message into an iOS VM
[**v1_instances_instance_id_netdump_pcap_get**](CorelliumApi.md#v1_instances_instance_id_netdump_pcap_get) | **GET** /v1/instances/{instanceId}/netdump.pcap | Download a netdump pcap file
[**v1_instances_instance_id_network_monitor_pcap_get**](CorelliumApi.md#v1_instances_instance_id_network_monitor_pcap_get) | **GET** /v1/instances/{instanceId}/networkMonitor.pcap | Download a Network Monitor pcap file
[**v1_kcrange**](CorelliumApi.md#v1_kcrange) | **GET** /v1/instances/{instanceId}/btrace-kcrange | Get Kernel extension ranges
[**v1_list_network_connections**](CorelliumApi.md#v1_list_network_connections) | **GET** /v1/network/connections | List available network connections
[**v1_list_network_interfaces**](CorelliumApi.md#v1_list_network_interfaces) | **GET** /v1/network/interfaces | List available physical network interfaces
[**v1_list_network_providers**](CorelliumApi.md#v1_list_network_providers) | **GET** /v1/network/providers | List available network providers
[**v1_list_threads**](CorelliumApi.md#v1_list_threads) | **GET** /v1/instances/{instanceId}/strace/thread-list | Get Running Threads (CoreTrace)
[**v1_load_extension**](CorelliumApi.md#v1_load_extension) | **POST** /v1/extensions | Load an extension
[**v1_media_play**](CorelliumApi.md#v1_media_play) | **POST** /v1/instances/{instanceId}/media/play | Start playing media
[**v1_media_stop**](CorelliumApi.md#v1_media_stop) | **POST** /v1/instances/{instanceId}/media/stop | Stop playing media
[**v1_parse_extension_json**](CorelliumApi.md#v1_parse_extension_json) | **POST** /v1/extensions/parse/extension.json | Validates extension.json
[**v1_partial_update_network_connection**](CorelliumApi.md#v1_partial_update_network_connection) | **PATCH** /v1/network/connections/{id} | Update Network Connection (partial)
[**v1_patch_instance**](CorelliumApi.md#v1_patch_instance) | **PATCH** /v1/instances/{instanceId} | Update Instance
[**v1_patch_instance_read_only**](CorelliumApi.md#v1_patch_instance_read_only) | **PATCH** /v1/instances/{instanceId}/read-only | Update Instance Read Only
[**v1_pause_instance**](CorelliumApi.md#v1_pause_instance) | **POST** /v1/instances/{instanceId}/pause | Pause an Instance
[**v1_post_instance_input**](CorelliumApi.md#v1_post_instance_input) | **POST** /v1/instances/{instanceId}/input | Provide Instance Input
[**v1_ready**](CorelliumApi.md#v1_ready) | **GET** /v1/ready | API Status
[**v1_reboot_instance**](CorelliumApi.md#v1_reboot_instance) | **POST** /v1/instances/{instanceId}/reboot | Reboot an Instance
[**v1_remove_project_key**](CorelliumApi.md#v1_remove_project_key) | **DELETE** /v1/projects/{projectId}/keys/{keyId} | Delete Project Authorized Key
[**v1_remove_team_role_from_project**](CorelliumApi.md#v1_remove_team_role_from_project) | **DELETE** /v1/roles/projects/{projectId}/teams/{teamId}/roles/{roleId} | Remove team role from project
[**v1_remove_user_from_team**](CorelliumApi.md#v1_remove_user_from_team) | **DELETE** /v1/teams/{teamId}/users/{userId} | Remove user from team
[**v1_remove_user_role_from_project**](CorelliumApi.md#v1_remove_user_role_from_project) | **DELETE** /v1/roles/projects/{projectId}/users/{userId}/roles/{roleId} | Remove user role from project
[**v1_rename_instance_snapshot**](CorelliumApi.md#v1_rename_instance_snapshot) | **PATCH** /v1/instances/{instanceId}/snapshots/{snapshotId} | Rename an Instance Snapshot
[**v1_reset_user_password**](CorelliumApi.md#v1_reset_user_password) | **POST** /v1/users/reset-password | Reset User Password
[**v1_restore_backup**](CorelliumApi.md#v1_restore_backup) | **POST** /v1/instances/{instanceId}/restoreBackup | Restore backup
[**v1_restore_instance_snapshot**](CorelliumApi.md#v1_restore_instance_snapshot) | **POST** /v1/instances/{instanceId}/snapshots/{snapshotId}/restore | Restore an Instance Snapshot
[**v1_roles**](CorelliumApi.md#v1_roles) | **GET** /v1/roles | Get all roles
[**v1_rotate_instance**](CorelliumApi.md#v1_rotate_instance) | **POST** /v1/instances/{instanceId}/rotate | Rotate device to specified orientation
[**v1_send_user_reset_link**](CorelliumApi.md#v1_send_user_reset_link) | **POST** /v1/users/send-reset-link | Send Password Reset Link
[**v1_set_instance_gpios**](CorelliumApi.md#v1_set_instance_gpios) | **PUT** /v1/instances/{instanceId}/gpios | Set Instance GPIOs
[**v1_set_instance_peripherals**](CorelliumApi.md#v1_set_instance_peripherals) | **PUT** /v1/instances/{instanceId}/peripherals | Set Instance Peripherals
[**v1_set_instance_state**](CorelliumApi.md#v1_set_instance_state) | **PUT** /v1/instances/{instanceId}/state | Set state of Instance
[**v1_set_snapshot_permissions**](CorelliumApi.md#v1_set_snapshot_permissions) | **POST** /v1/snapshots/{snapshotId}/permissions | Set member list
[**v1_share_snapshot**](CorelliumApi.md#v1_share_snapshot) | **POST** /v1/snapshots/{snapshotId}/share | Share snapshot
[**v1_snapshot_rename**](CorelliumApi.md#v1_snapshot_rename) | **PATCH** /v1/snapshots/{snapshotId} | Rename a Snapshot
[**v1_start_core_trace**](CorelliumApi.md#v1_start_core_trace) | **POST** /v1/instances/{instanceId}/strace/enable | Start CoreTrace on an instance
[**v1_start_hyper_trace**](CorelliumApi.md#v1_start_hyper_trace) | **POST** /v1/instances/{instanceId}/btrace/enable | Start HyperTrace on an instance
[**v1_start_instance**](CorelliumApi.md#v1_start_instance) | **POST** /v1/instances/{instanceId}/start | Start an Instance
[**v1_start_netdump**](CorelliumApi.md#v1_start_netdump) | **POST** /v1/instances/{instanceId}/netdump/enable | Start Enhanced Network Monitor on an instance.
[**v1_start_network_monitor**](CorelliumApi.md#v1_start_network_monitor) | **POST** /v1/instances/{instanceId}/sslsplit/enable | Start Network Monitor on an instance.
[**v1_stop_core_trace**](CorelliumApi.md#v1_stop_core_trace) | **POST** /v1/instances/{instanceId}/strace/disable | Stop CoreTrace on an instance.
[**v1_stop_hyper_trace**](CorelliumApi.md#v1_stop_hyper_trace) | **POST** /v1/instances/{instanceId}/btrace/disable | Stop HyperTrace on an instance.
[**v1_stop_instance**](CorelliumApi.md#v1_stop_instance) | **POST** /v1/instances/{instanceId}/stop | Stop an Instance
[**v1_stop_netdump**](CorelliumApi.md#v1_stop_netdump) | **POST** /v1/instances/{instanceId}/netdump/disable | Stop Enhanced Network Monitor on an instance.
[**v1_stop_network_monitor**](CorelliumApi.md#v1_stop_network_monitor) | **POST** /v1/instances/{instanceId}/sslsplit/disable | Stop Network Monitor on an instance.
[**v1_team_change**](CorelliumApi.md#v1_team_change) | **PATCH** /v1/teams/{teamId} | Update team
[**v1_team_create**](CorelliumApi.md#v1_team_create) | **POST** /v1/teams | Create team
[**v1_team_delete**](CorelliumApi.md#v1_team_delete) | **DELETE** /v1/teams/{teamId} | Delete team
[**v1_teams**](CorelliumApi.md#v1_teams) | **GET** /v1/teams | Get teams
[**v1_unpause_instance**](CorelliumApi.md#v1_unpause_instance) | **POST** /v1/instances/{instanceId}/unpause | Unpause an Instance
[**v1_update_domain_auth_provider**](CorelliumApi.md#v1_update_domain_auth_provider) | **PUT** /v1/domain/{domainId}/auth/{providerId} | Update an auth provider for a domain
[**v1_update_extension**](CorelliumApi.md#v1_update_extension) | **PUT** /v1/extensions/{extensionId} | Update an existing extension
[**v1_update_hook**](CorelliumApi.md#v1_update_hook) | **PUT** /v1/hooks/{hookId} | Update an existing hypervisor hook
[**v1_update_network_connection**](CorelliumApi.md#v1_update_network_connection) | **PUT** /v1/network/connections/{id} | Update Network Connection
[**v1_update_project**](CorelliumApi.md#v1_update_project) | **PATCH** /v1/projects/{projectId} | Update a Project
[**v1_update_project_settings**](CorelliumApi.md#v1_update_project_settings) | **PATCH** /v1/projects/{projectId}/settings | Change Project Settings
[**v1_update_user**](CorelliumApi.md#v1_update_user) | **PATCH** /v1/users/{userId} | Update User
[**v1_upgrade_instance**](CorelliumApi.md#v1_upgrade_instance) | **POST** /v1/instances/{instanceId}/upgrade | Upgrade iOS version
[**v1_upload_image_data**](CorelliumApi.md#v1_upload_image_data) | **POST** /v1/images/{imageId} | Upload Image Data
[**v1_user_agree_terms**](CorelliumApi.md#v1_user_agree_terms) | **POST** /v1/users/agree | Consent to the current terms and conditions
[**v1_users_change_password_post**](CorelliumApi.md#v1_users_change_password_post) | **POST** /v1/users/change-password | Change User Password
[**v1_users_login**](CorelliumApi.md#v1_users_login) | **POST** /v1/users/login | Log In
[**v1_web_player_allowed_domains**](CorelliumApi.md#v1_web_player_allowed_domains) | **GET** /v1/webplayer/allowedDomains | Retrieve the list of allowed domains for all Webplayer sessions
[**v1_web_player_create_session**](CorelliumApi.md#v1_web_player_create_session) | **POST** /v1/webplayer | Create a new Webplayer Session
[**v1_web_player_destroy_session**](CorelliumApi.md#v1_web_player_destroy_session) | **DELETE** /v1/webplayer/{sessionId} | Tear down a Webplayer Session
[**v1_web_player_list_sessions**](CorelliumApi.md#v1_web_player_list_sessions) | **GET** /v1/webplayer | List all Webplayer sessions
[**v1_web_player_session_info**](CorelliumApi.md#v1_web_player_session_info) | **GET** /v1/webplayer/{sessionId} | Retrieve Webplayer Session Information
[**v2_get_instance_quick_connect_command**](CorelliumApi.md#v2_get_instance_quick_connect_command) | **GET** /v2/instances/{instanceId}/quickConnectCommand | Recommended SSH Command for Quick Connect
[**v2_get_instance_state**](CorelliumApi.md#v2_get_instance_state) | **GET** /v2/instances/{instanceId}/state | Get state of Instance


# **api_v1_cluster_nodes_node_id_console_get**
> api_v1_cluster_nodes_node_id_console_get(node_id)

Access node console via SSH

Access node console via SSH (WebSocket upgrade)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        node_id = 'node_id_example' # str | Node ID

        try:
            # Access node console via SSH
            api_instance.api_v1_cluster_nodes_node_id_console_get(node_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->api_v1_cluster_nodes_node_id_console_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**101** | WebSocket connection upgraded |  -  |
**403** | Forbidden |  -  |
**404** | Node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interconnects_get**
> GetInterconnectsResponse api_v1_interconnects_get(limit=limit, offset=offset, name=name, protocol=protocol, type=type, status=status, project=project, sort=sort)

Get all I/O Interconnects

Get all I/O Interconnects

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        limit = 3.4 # float | Maximum number of results to return (1-1000, default: 100) (optional)
offset = 3.4 # float | Number of results to skip (default: 0) (optional)
name = 'name_example' # str | Filter by interconnect name (case insensitive) (optional)
protocol = 'protocol_example' # str | Filter by protocol (comma separated) (optional)
type = 'type_example' # str | Filter by type (comma separated) (optional)
status = 'status_example' # str | Filter by status (comma separated) (optional)
project = 'project_example' # str | Filter by project ID (comma separated) (optional)
sort = 'sort_example' # str | Sort order (e.g. \"name\" for ascending, \"-name\" for descending, comma separated) (optional)

        try:
            # Get all I/O Interconnects
            api_response = await api_instance.api_v1_interconnects_get(limit=limit, offset=offset, name=name, protocol=protocol, type=type, status=status, project=project, sort=sort)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->api_v1_interconnects_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Maximum number of results to return (1-1000, default: 100) | [optional] 
 **offset** | **float**| Number of results to skip (default: 0) | [optional] 
 **name** | **str**| Filter by interconnect name (case insensitive) | [optional] 
 **protocol** | **str**| Filter by protocol (comma separated) | [optional] 
 **type** | **str**| Filter by type (comma separated) | [optional] 
 **status** | **str**| Filter by status (comma separated) | [optional] 
 **project** | **str**| Filter by project ID (comma separated) | [optional] 
 **sort** | **str**| Sort order (e.g. \&quot;name\&quot; for ascending, \&quot;-name\&quot; for descending, comma separated) | [optional] 

### Return type

[**GetInterconnectsResponse**](GetInterconnectsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved interconnects |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interconnects_interconnect_id_delete**
> api_v1_interconnects_interconnect_id_delete(interconnect_id)

Delete I/O Interconnect

Delete I/O Interconnect

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        interconnect_id = 'interconnect_id_example' # str | The interconnect identifier

        try:
            # Delete I/O Interconnect
            api_instance.api_v1_interconnects_interconnect_id_delete(interconnect_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->api_v1_interconnects_interconnect_id_delete: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interconnect_id** | **str**| The interconnect identifier | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully deleted interconnect |  -  |
**401** | Unauthorized |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interconnects_interconnect_id_get**
> InterconnectResponse api_v1_interconnects_interconnect_id_get(interconnect_id)

Get Interconnect

Get Interconnect

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        interconnect_id = 'interconnect_id_example' # str | The interconnect identifier

        try:
            # Get Interconnect
            api_response = await api_instance.api_v1_interconnects_interconnect_id_get(interconnect_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->api_v1_interconnects_interconnect_id_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interconnect_id** | **str**| The interconnect identifier | 

### Return type

[**InterconnectResponse**](InterconnectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved interconnect details |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interconnects_interconnect_id_patch**
> InterconnectResponse api_v1_interconnects_interconnect_id_patch(interconnect_id, partial_update_interconnect_request)

Partial Update Interconnect

Update some interconnect details for the specified interconnect identifier.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        interconnect_id = 'interconnect_id_example' # str | The interconnect identifier
partial_update_interconnect_request = {
  "name": "My Can Bus 2 is new to you"
} # PartialUpdateInterconnectRequest | The interconnect details to update

        try:
            # Partial Update Interconnect
            api_response = await api_instance.api_v1_interconnects_interconnect_id_patch(interconnect_id, partial_update_interconnect_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->api_v1_interconnects_interconnect_id_patch: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interconnect_id** | **str**| The interconnect identifier | 
 **partial_update_interconnect_request** | [**PartialUpdateInterconnectRequest**](PartialUpdateInterconnectRequest.md)| The interconnect details to update | 

### Return type

[**InterconnectResponse**](InterconnectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated interconnect |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interconnects_interconnect_id_put**
> InterconnectResponse api_v1_interconnects_interconnect_id_put(interconnect_id, update_interconnect_request)

Update Interconnect

Update interconnect details for the specified interconnect identifier.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        interconnect_id = 'interconnect_id_example' # str | The interconnect identifier
update_interconnect_request = {
  "name": "My Can Bus 2",
  "interfaces": [
    {
      "deviceId": "fa783ebb-b020-47fb-af74-6898ed59b068",
      "interfaceId": "can1:0"
    },
    {
      "deviceId": "58db550e-bb96-403a-bcf0-86ff33e5e61d",
      "interfaceId": "can1:0"
    },
    {
      "deviceId": "bd576aca-9e31-4c6a-817e-f2a38122536e",
      "interfaceId": "can1:0"
    }
  ]
} # UpdateInterconnectRequest | The interconnect details to update

        try:
            # Update Interconnect
            api_response = await api_instance.api_v1_interconnects_interconnect_id_put(interconnect_id, update_interconnect_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->api_v1_interconnects_interconnect_id_put: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interconnect_id** | **str**| The interconnect identifier | 
 **update_interconnect_request** | [**UpdateInterconnectRequest**](UpdateInterconnectRequest.md)| The interconnect details to update | 

### Return type

[**InterconnectResponse**](InterconnectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated interconnect |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_v1_interconnects_post**
> InterconnectResponse api_v1_interconnects_post(create_interconnect_request)

Create I/O Interconnect

Create an I/O Interconnect for the specified project and attach virtual device interfaces.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        create_interconnect_request = {
  "name": "My Interconnect",
  "protocol": "TCP",
  "type": "hub",
  "project": "123e4567-e89b-12d3-a456-426614174000",
  "interfaces": [{
     "deviceId": "2b331aaa-de76-4169-8442-9910e9c436fb",
     "interfaceId": "gpio:7"
  }]
} # CreateInterconnectRequest | The interconnect details

        try:
            # Create I/O Interconnect
            api_response = await api_instance.api_v1_interconnects_post(create_interconnect_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->api_v1_interconnects_post: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_interconnect_request** | [**CreateInterconnectRequest**](CreateInterconnectRequest.md)| The interconnect details | 

### Return type

[**InterconnectResponse**](InterconnectResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created interconnect |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_assessment**
> AssessmentIdStatus create_assessment(instance_id, create_assessment_dto)

Create assessment

Create assessment

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | ID of instance
create_assessment_dto = corellium_api.CreateAssessmentDto() # CreateAssessmentDto | Create a new assessment

        try:
            # Create assessment
            api_response = await api_instance.create_assessment(instance_id, create_assessment_dto)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->create_assessment: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of instance | 
 **create_assessment_dto** | [**CreateAssessmentDto**](CreateAssessmentDto.md)| Create a new assessment | 

### Return type

[**AssessmentIdStatus**](AssessmentIdStatus.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Invalid body |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assessment**
> delete_assessment(instance_id, assessment_id)

Delete assessment

Delete assessment

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | ID of instance
assessment_id = 'assessment_id_example' # str | ID of assessment

        try:
            # Delete assessment
            api_instance.delete_assessment(instance_id, assessment_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->delete_assessment: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of instance | 
 **assessment_id** | **str**| ID of assessment | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**404** | Assessment not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_report**
> str download_report(instance_id, assessment_id, format)

Download report

Download report

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | ID of instance
assessment_id = 'assessment_id_example' # str | ID of assessment
format = 'html' # str | Assessment report download format (default to 'html')

        try:
            # Download report
            api_response = await api_instance.download_report(instance_id, assessment_id, format)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->download_report: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of instance | 
 **assessment_id** | **str**| ID of assessment | 
 **format** | **str**| Assessment report download format | [default to &#39;html&#39;]

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns the HTML file of the report |  -  |
**400** | Assessment status invalid |  -  |
**404** | Assessment not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assessment_by_id**
> Assessment get_assessment_by_id(instance_id, assessment_id)

Get assessment by ID

Get assessment by ID

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | ID of instance
assessment_id = 'assessment_id_example' # str | ID of assessment

        try:
            # Get assessment by ID
            api_response = await api_instance.get_assessment_by_id(instance_id, assessment_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->get_assessment_by_id: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of instance | 
 **assessment_id** | **str**| ID of assessment | 

### Return type

[**Assessment**](Assessment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**404** | Assessment not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assessments_by_instance_id**
> list[Assessment] get_assessments_by_instance_id(instance_id)

Get assessments by instanceId

Get assessments by instanceId

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | ID of instance

        try:
            # Get assessments by instanceId
            api_response = await api_instance.get_assessments_by_instance_id(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->get_assessments_by_instance_id: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of instance | 

### Return type

[**list[Assessment]**](Assessment.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns array of assessments |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_tests**
> AssessmentIdStatus run_tests(instance_id, assessment_id, test_assessment_dto=test_assessment_dto)

Update assessment state and execute MATRIX tests

Update assessment state and execute MATRIX tests

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | ID of instance
assessment_id = 'assessment_id_example' # str | ID of assessment
test_assessment_dto = corellium_api.TestAssessmentDto() # TestAssessmentDto | Execute MATRIX tests (optional)

        try:
            # Update assessment state and execute MATRIX tests
            api_response = await api_instance.run_tests(instance_id, assessment_id, test_assessment_dto=test_assessment_dto)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->run_tests: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of instance | 
 **assessment_id** | **str**| ID of assessment | 
 **test_assessment_dto** | [**TestAssessmentDto**](TestAssessmentDto.md)| Execute MATRIX tests | [optional] 

### Return type

[**AssessmentIdStatus**](AssessmentIdStatus.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful operation |  -  |
**400** | Assessment status invalid |  -  |
**404** | Assessment not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_monitoring**
> start_monitoring(instance_id, assessment_id)

Update assessment state and begin device monitoring

Update assessment state and begin device monitoring

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | ID of instance
assessment_id = 'assessment_id_example' # str | ID of assessment

        try:
            # Update assessment state and begin device monitoring
            api_instance.start_monitoring(instance_id, assessment_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->start_monitoring: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of instance | 
 **assessment_id** | **str**| ID of assessment | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**404** | Assessment not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_monitoring**
> stop_monitoring(instance_id, assessment_id)

Update assessment state and stop device monitoring

Update assessment state and stop device monitoring

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | ID of instance
assessment_id = 'assessment_id_example' # str | ID of assessment

        try:
            # Update assessment state and stop device monitoring
            api_instance.stop_monitoring(instance_id, assessment_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->stop_monitoring: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| ID of instance | 
 **assessment_id** | **str**| ID of assessment | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful operation |  -  |
**404** | Assessment not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_accept_shared_snapshot**
> Snapshot v1_accept_shared_snapshot(post_share_snapshot_request_payload)

Accept a snapshot shared with you

Accept a snapshot shared with you

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        post_share_snapshot_request_payload = {
  "accessCode": "1S33IA5G71YJ5",
  "password": "password"
} # PostShareSnapshotRequestPayload | 

        try:
            # Accept a snapshot shared with you
            api_response = await api_instance.v1_accept_shared_snapshot(post_share_snapshot_request_payload)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_accept_shared_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **post_share_snapshot_request_payload** | [**PostShareSnapshotRequestPayload**](PostShareSnapshotRequestPayload.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_activity_export**
> ActivityExportResponse v1_activity_export(activity_export_dto)

Start activity export

Start activity export

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        activity_export_dto = corellium_api.ActivityExportDto() # ActivityExportDto | 

        try:
            # Start activity export
            api_response = await api_instance.v1_activity_export(activity_export_dto)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_activity_export: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activity_export_dto** | [**ActivityExportDto**](ActivityExportDto.md)|  | 

### Return type

[**ActivityExportResponse**](ActivityExportResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_activity_list**
> ActivityList v1_activity_list(request=request)

Get resource activities

Get resource activities

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        request = {'key': corellium_api.ActivityRequest()} # ActivityRequest |  (optional)

        try:
            # Get resource activities
            api_response = await api_instance.v1_activity_list(request=request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_activity_list: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ActivityRequest**](.md)|  | [optional] 

### Return type

[**ActivityList**](ActivityList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_add_project_key**
> ProjectKey v1_add_project_key(project_id, project_key)

Add Project Authorized Key

Add Project Authorized Key

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
project_key = {
  "kind": "ssh",
  "label": "My New Key",
  "key": "ssh-ed25519 <key>"
} # ProjectKey | Key to add

        try:
            # Add Project Authorized Key
            api_response = await api_instance.v1_add_project_key(project_id, project_key)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_add_project_key: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **project_key** | [**ProjectKey**](ProjectKey.md)| Key to add | 

### Return type

[**ProjectKey**](ProjectKey.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorized Key |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_add_team_role_to_project**
> v1_add_team_role_to_project(project_id, team_id, role_id)

Add team role to project

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
team_id = 'team_id_example' # str | Team ID - uuid
role_id = 'role_id_example' # str | Role ID

        try:
            # Add team role to project
            api_instance.v1_add_team_role_to_project(project_id, team_id, role_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_add_team_role_to_project: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **team_id** | **str**| Team ID - uuid | 
 **role_id** | **str**| Role ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_add_user_role_to_project**
> v1_add_user_role_to_project(project_id, user_id, role_id)

Add user role to project

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
user_id = 'user_id_example' # str | User ID - uuid
role_id = 'role_id_example' # str | Role ID

        try:
            # Add user role to project
            api_instance.v1_add_user_role_to_project(project_id, user_id, role_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_add_user_role_to_project: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **user_id** | **str**| User ID - uuid | 
 **role_id** | **str**| Role ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_add_user_to_team**
> v1_add_user_to_team(team_id, user_id)

Add user to team

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        team_id = 'team_id_example' # str | Team ID - uuid
user_id = 'user_id_example' # str | User ID - uuid

        try:
            # Add user to team
            api_instance.v1_add_user_to_team(team_id, user_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_add_user_to_team: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team ID - uuid | 
 **user_id** | **str**| User ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_app_ready**
> AgentAppReadyResponse v1_agent_app_ready(instance_id)

Check if App subsystem is ready

Check if App subsystem is ready

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Check if App subsystem is ready
            api_response = await api_instance.v1_agent_app_ready(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_app_ready: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**AgentAppReadyResponse**](AgentAppReadyResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | App Agent State |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_delete_file**
> v1_agent_delete_file(instance_id, file_path)

Delete a File on VM

Delete a File on VM

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
file_path = 'file_path_example' # str | File Path on VM

        try:
            # Delete a File on VM
            api_instance.v1_agent_delete_file(instance_id, file_path)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_delete_file: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **file_path** | **str**| File Path on VM | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_get_file**
> file v1_agent_get_file(instance_id, file_path)

Download a File from VM

Download a File from VM

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
file_path = 'file_path_example' # str | File Path on VM

        try:
            # Download a File from VM
            api_response = await api_instance.v1_agent_get_file(instance_id, file_path)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_get_file: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **file_path** | **str**| File Path on VM | 

### Return type

**file**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File Contents |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_get_temp_filename**
> str v1_agent_get_temp_filename(instance_id)

Get the path for a new temp file

Returns a temporary random filename that is guranteed to be unique on the VMs filesystem at the time of invocation of this method.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get the path for a new temp file
            api_response = await api_instance.v1_agent_get_temp_filename(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_get_temp_filename: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The temp file path |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_install_app**
> v1_agent_install_app(instance_id, agent_install_body)

Install App at path

Installs the app located at path which must be present on the VM filesystem

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
agent_install_body = {
  "path": "/tmp/test.ipa"
} # AgentInstallBody | App parameters

        try:
            # Install App at path
            api_instance.v1_agent_install_app(instance_id, agent_install_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_install_app: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **agent_install_body** | [**AgentInstallBody**](AgentInstallBody.md)| App parameters | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_install_profile**
> v1_agent_install_profile(instance_id, body)

Install a Profile to VM

Install a Profile to VM

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
body = '/path/to/file' # file | Profile to Install

        try:
            # Install a Profile to VM
            api_instance.v1_agent_install_profile(instance_id, body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_install_profile: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **body** | **file**| Profile to Install | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_kill_app**
> object v1_agent_kill_app(instance_id, bundle_id)

Kill an App

Kill an App

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
bundle_id = 'bundle_id_example' # str | App Bundle ID

        try:
            # Kill an App
            api_response = await api_instance.v1_agent_kill_app(instance_id, bundle_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_kill_app: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **bundle_id** | **str**| App Bundle ID | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list_app_icons**
> list[AgentIcons] v1_agent_list_app_icons(instance_id, bundle_id)

List App Icons

List App Icons as base64 data

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
bundle_id = ['bundle_id_example'] # list[str] | App Bundle ID

        try:
            # List App Icons
            api_response = await api_instance.v1_agent_list_app_icons(instance_id, bundle_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_list_app_icons: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **bundle_id** | [**list[str]**](str.md)| App Bundle ID | 

### Return type

[**list[AgentIcons]**](AgentIcons.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installed Apps Icons |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list_apps**
> AgentAppsList v1_agent_list_apps(instance_id)

List Apps

List Apps

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # List Apps
            api_response = await api_instance.v1_agent_list_apps(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_list_apps: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**AgentAppsList**](AgentAppsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installed Apps Info |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list_apps_status**
> AgentAppsList v1_agent_list_apps_status(instance_id)

List Apps Status

List Apps Status

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # List Apps Status
            api_response = await api_instance.v1_agent_list_apps_status(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_list_apps_status: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**AgentAppsList**](AgentAppsList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installed Apps Status Info |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list_profiles**
> AgentProfilesReturn v1_agent_list_profiles(instance_id)

List Profiles

List Profiles

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # List Profiles
            api_response = await api_instance.v1_agent_list_profiles(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_list_profiles: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**AgentProfilesReturn**](AgentProfilesReturn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Installed Profiles |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_run_app**
> object v1_agent_run_app(instance_id, bundle_id)

Run an App

Run an App

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
bundle_id = 'bundle_id_example' # str | App Bundle ID

        try:
            # Run an App
            api_response = await api_instance.v1_agent_run_app(instance_id, bundle_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_run_app: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **bundle_id** | **str**| App Bundle ID | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_set_file_attributes**
> v1_agent_set_file_attributes(instance_id, file_path, file_changes)

Change Attrs of a File on VM

Change Attrs of a File on VM

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
file_path = 'file_path_example' # str | File Path on VM
file_changes = corellium_api.FileChanges() # FileChanges | New attrs

        try:
            # Change Attrs of a File on VM
            api_instance.v1_agent_set_file_attributes(instance_id, file_path, file_changes)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_set_file_attributes: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **file_path** | **str**| File Path on VM | 
 **file_changes** | [**FileChanges**](FileChanges.md)| New attrs | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_get_adb_auth**
> AgentSystemAdbAuth v1_agent_system_get_adb_auth(instance_id)

Get ADB Auth Setting (AOSP only)

Get ADB Auth Setting (AOSP only)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get ADB Auth Setting (AOSP only)
            api_response = await api_instance.v1_agent_system_get_adb_auth(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_get_adb_auth: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**AgentSystemAdbAuth**](AgentSystemAdbAuth.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current ADB Auth setting |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_get_network**
> AgentValueReturn v1_agent_system_get_network(instance_id)

Get IP of eth0 (AOSP only)

Get IP of eth0 (AOSP only)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get IP of eth0 (AOSP only)
            api_response = await api_instance.v1_agent_system_get_network(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_get_network: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**AgentValueReturn**](AgentValueReturn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | IP Address of eth0 |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_get_prop**
> AgentValueReturn v1_agent_system_get_prop(instance_id, agent_system_get_prop_body)

Get System Property (AOSP only)

Get System Property (AOSP only)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
agent_system_get_prop_body = {
  "property": "corellium.opengapps"
} # AgentSystemGetPropBody | Parameters

        try:
            # Get System Property (AOSP only)
            api_response = await api_instance.v1_agent_system_get_prop(instance_id, agent_system_get_prop_body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_get_prop: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **agent_system_get_prop_body** | [**AgentSystemGetPropBody**](AgentSystemGetPropBody.md)| Parameters | 

### Return type

[**AgentValueReturn**](AgentValueReturn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Value of requested property |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_install_open_g_apps**
> v1_agent_system_install_open_g_apps(instance_id, body)

Install OpenGApps (AOSP only)

Install OpenGApps (AOSP only)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
body = {
    "url": "http://downloads.sourceforge.net/project/opengapps/arm64/20220119/open_gapps-arm64-11.0-pico-20220119.zip?r=&ts=1653516572&use_mirror=gigenet",
    "hash": "58398bf7628f38ef07eaeb3abe26f3ebf0474f4d5ecdac0852bd5de3c15cc828",
    "fingerprint": "google/flame/flame:11/RP1A.200720.009/6720564:user/release-keys__2020-09-05"
} # object | Installation parameters

        try:
            # Install OpenGApps (AOSP only)
            api_instance.v1_agent_system_install_open_g_apps(instance_id, body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_install_open_g_apps: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **body** | **object**| Installation parameters | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_lock**
> v1_agent_system_lock(instance_id)

Lock Device (iOS Only)

Lock Device (iOS Only)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Lock Device (iOS Only)
            api_instance.v1_agent_system_lock(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_lock: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_set_adb_auth**
> v1_agent_system_set_adb_auth(instance_id, agent_system_adb_auth)

Set ADB Auth Setting (AOSP only)

Set ADB Auth Setting (AOSP only)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
agent_system_adb_auth = {
  "enabled": true
} # AgentSystemAdbAuth | Desired ADB Auth Setting

        try:
            # Set ADB Auth Setting (AOSP only)
            api_instance.v1_agent_system_set_adb_auth(instance_id, agent_system_adb_auth)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_set_adb_auth: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **agent_system_adb_auth** | [**AgentSystemAdbAuth**](AgentSystemAdbAuth.md)| Desired ADB Auth Setting | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_set_hostname**
> v1_agent_system_set_hostname(instance_id, agent_system_set_hostname_body)

Set Hostname of instance

Set Hostname of instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
agent_system_set_hostname_body = corellium_api.AgentSystemSetHostnameBody() # AgentSystemSetHostnameBody | New hostname

        try:
            # Set Hostname of instance
            api_instance.v1_agent_system_set_hostname(instance_id, agent_system_set_hostname_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_set_hostname: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **agent_system_set_hostname_body** | [**AgentSystemSetHostnameBody**](AgentSystemSetHostnameBody.md)| New hostname | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_shutdown**
> v1_agent_system_shutdown(instance_id)

Instruct VM to halt

Instruct VM to halt

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Instruct VM to halt
            api_instance.v1_agent_system_shutdown(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_shutdown: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_unlock**
> v1_agent_system_unlock(instance_id)

Unlock Device (iOS Only)

Unlock Device (iOS Only)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Unlock Device (iOS Only)
            api_instance.v1_agent_system_unlock(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_system_unlock: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_uninstall_app**
> object v1_agent_uninstall_app(instance_id, bundle_id)

Uninstall an App

Uninstall an App

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
bundle_id = 'bundle_id_example' # str | App Bundle ID

        try:
            # Uninstall an App
            api_response = await api_instance.v1_agent_uninstall_app(instance_id, bundle_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_uninstall_app: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **bundle_id** | **str**| App Bundle ID | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_uninstall_profile**
> v1_agent_uninstall_profile(instance_id, profile_id)

Uninstall a Profile from VM

Uninstall a Profile from VM

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
profile_id = 'profile_id_example' # str | Instance ID - uuid

        try:
            # Uninstall a Profile from VM
            api_instance.v1_agent_uninstall_profile(instance_id, profile_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_uninstall_profile: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **profile_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_upload_file**
> v1_agent_upload_file(instance_id, file_path, body)

Upload a file to VM

Upload a file to VM

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
file_path = 'file_path_example' # str | File Path on VM to write to
body = '/path/to/file' # file | Uploaded File Contents

        try:
            # Upload a file to VM
            api_instance.v1_agent_upload_file(instance_id, file_path, body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_agent_upload_file: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **file_path** | **str**| File Path on VM to write to | 
 **body** | **file**| Uploaded File Contents | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |
**400** | Agent Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_attach_instance_interface**
> v1_attach_instance_interface(instance_id, attach_interface_request)

Attach I/O Interface

Attach an I/O interface to an I/O interconnect for the specified instance identifier.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
attach_interface_request = corellium_api.AttachInterfaceRequest() # AttachInterfaceRequest | Interface attachment request

        try:
            # Attach I/O Interface
            api_instance.v1_attach_instance_interface(instance_id, attach_interface_request)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_attach_instance_interface: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **attach_interface_request** | [**AttachInterfaceRequest**](AttachInterfaceRequest.md)| Interface attachment request | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_login**
> Token v1_auth_login(body)

Log In

Log In

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        body = {
  "username": "admin",
  "password": "password"
} # object | Authorization data ( Credentials|ApiToken )

        try:
            # Log In
            api_response = await api_instance.v1_auth_login(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_auth_login: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Authorization data ( Credentials|ApiToken ) | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Authorization |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_btrace_preauthorize**
> Token v1_btrace_preauthorize(instance_id)

Pre-authorize an btrace download

Pre-authorize an btrace download

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Pre-authorize an btrace download
            api_response = await api_instance.v1_btrace_preauthorize(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_btrace_preauthorize: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**Token**](Token.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Token |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_clear_core_trace**
> v1_clear_core_trace(instance_id)

Clear CoreTrace logs

Clear CoreTrace logs

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Clear CoreTrace logs
            api_instance.v1_clear_core_trace(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_clear_core_trace: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_clear_hyper_trace**
> v1_clear_hyper_trace(instance_id)

Clear HyperTrace logs

Clear HyperTrace logs

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Clear HyperTrace logs
            api_instance.v1_clear_hyper_trace(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_clear_hyper_trace: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_clear_hyper_trace_hooks**
> v1_clear_hyper_trace_hooks(instance_id)

Clear Hooks on an instance

Clear Hooks on an instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Clear Hooks on an instance
            api_instance.v1_clear_hyper_trace_hooks(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_clear_hyper_trace_hooks: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_clear_instance_panics**
> v1_clear_instance_panics(instance_id)

Clear Panics

Clear Panics

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Clear Panics
            api_instance.v1_clear_instance_panics(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_clear_instance_panics: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_firmware_service_devices_get**
> list[Device] v1_cluster_firmware_service_devices_get(limit=limit, offset=offset, search=search, order=order, type=type, model=model, name=name, platform=platform)

Fetch devices from the firmware service

Proxies a request to the firmware service to retrieve a list of devices.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        limit = 3.4 # float | Number of results to return (min: 1, max: 10000, default: 100) (optional)
offset = 3.4 # float | Index of the first row to return (default: 0) (optional)
search = 'search_example' # str | Case-insensitive partial match across name, model, platform, and hwmodel fields (optional)
order = 'order_example' # str | Comma-separated field names for sorting. Prefix with '-' for ascending order (e.g., 'name,-platform'). Allowed fields: name, model, type, platform, hwmodel  Filtering options: (optional)
type = 'type_example' # str | Filter by exact type. Example: coreimg (optional)
model = 'model_example' # str | Filter by exact model. Example: Example: iPhone8,1 (optional)
name = 'name_example' # str | Filter by exact name. Example: iPhone6s (optional)
platform = 'platform_example' # str | Filter by exact platform. Example: s5l8960x (optional)

        try:
            # Fetch devices from the firmware service
            api_response = await api_instance.v1_cluster_firmware_service_devices_get(limit=limit, offset=offset, search=search, order=order, type=type, model=model, name=name, platform=platform)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_firmware_service_devices_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Number of results to return (min: 1, max: 10000, default: 100) | [optional] 
 **offset** | **float**| Index of the first row to return (default: 0) | [optional] 
 **search** | **str**| Case-insensitive partial match across name, model, platform, and hwmodel fields | [optional] 
 **order** | **str**| Comma-separated field names for sorting. Prefix with &#39;-&#39; for ascending order (e.g., &#39;name,-platform&#39;). Allowed fields: name, model, type, platform, hwmodel  Filtering options: | [optional] 
 **type** | **str**| Filter by exact type. Example: coreimg | [optional] 
 **model** | **str**| Filter by exact model. Example: Example: iPhone8,1 | [optional] 
 **name** | **str**| Filter by exact name. Example: iPhone6s | [optional] 
 **platform** | **str**| Filter by exact platform. Example: s5l8960x | [optional] 

### Return type

[**list[Device]**](Device.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_firmware_service_firmware_assets_asset_url_delete**
> v1_cluster_firmware_service_firmware_assets_asset_url_delete(asset_url)

Delete a firmware asset by its URL

Proxies a request to the firmware service to delete a firmware asset by URL.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        asset_url = 'asset_url_example' # str | The URL-encoded firmware asset URL to delete - format:uri - pattern:^[A-Za-z0-9\\-._~:/?#[\\]@!$&'()*+,;=%]+$

        try:
            # Delete a firmware asset by its URL
            api_instance.v1_cluster_firmware_service_firmware_assets_asset_url_delete(asset_url)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_firmware_service_firmware_assets_asset_url_delete: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_url** | **str**| The URL-encoded firmware asset URL to delete - format:uri - pattern:^[A-Za-z0-9\\-._~:/?#[\\]@!$&amp;&#39;()*+,;&#x3D;%]+$ | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_firmware_service_firmware_assets_asset_url_extended_get**
> ExtendedFirmwareAssetInfo v1_cluster_firmware_service_firmware_assets_asset_url_extended_get(asset_url)

Fetch extended firmware-asset details including instances and associated IPSWs

Retrieves extended information about a firmware including all instances using it and associated firmware assets.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        asset_url = 'asset_url_example' # str | The URL-encoded firmware asset to delete. Example: H4RUO0MX-Fz0ka2Q2vCfvP-27ElNZw5bWJEfyF04AxA=

        try:
            # Fetch extended firmware-asset details including instances and associated IPSWs
            api_response = await api_instance.v1_cluster_firmware_service_firmware_assets_asset_url_extended_get(asset_url)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_firmware_service_firmware_assets_asset_url_extended_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_url** | **str**| The URL-encoded firmware asset to delete. Example: H4RUO0MX-Fz0ka2Q2vCfvP-27ElNZw5bWJEfyF04AxA&#x3D; | 

### Return type

[**ExtendedFirmwareAssetInfo**](ExtendedFirmwareAssetInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_firmware_service_firmware_assets_get**
> list[FirmwareAsset] v1_cluster_firmware_service_firmware_assets_get(limit=limit, offset=offset, order=order, search=search)

Fetch firmware assets from the firmware service

Proxies a request to the firmware service to retrieve a list of firmware assets.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        limit = 3.4 # float | Number of results to return (min: 1, max: 10000, default: 100) (optional)
offset = 3.4 # float | Index of the first row to return (default: 0) (optional)
order = 'order_example' # str | Comma-separated field names for sorting. Prefix with '-' for ascending order (e.g., 'url,-domain'). Allowed fields: url, domain (optional)
search = 'search_example' # str | Case-insensitive partial match across url, domain (optional)

        try:
            # Fetch firmware assets from the firmware service
            api_response = await api_instance.v1_cluster_firmware_service_firmware_assets_get(limit=limit, offset=offset, order=order, search=search)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_firmware_service_firmware_assets_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Number of results to return (min: 1, max: 10000, default: 100) | [optional] 
 **offset** | **float**| Index of the first row to return (default: 0) | [optional] 
 **order** | **str**| Comma-separated field names for sorting. Prefix with &#39;-&#39; for ascending order (e.g., &#39;url,-domain&#39;). Allowed fields: url, domain | [optional] 
 **search** | **str**| Case-insensitive partial match across url, domain | [optional] 

### Return type

[**list[FirmwareAsset]**](FirmwareAsset.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_firmware_service_firmware_assets_post**
> str v1_cluster_firmware_service_firmware_assets_post(body)

Add firmware assets via the firmware service

Proxies a request to the firmware service to add firmware assets.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        body = {
  "https://wkms-public.apple.com/fcs-keys/0-rpBmpVnBmLtxdIwb97a_jAodE52Gv8Al_CN8DdwzQ=": "LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JR0hBZ0VBTUJNR0J5cUdTTTQ5QWdFR0NDcUdTTTQ5QXdFSEJHMHdhd0lCQVFRZ1plQ25uTW5CZEx3RkM1K2EKUU9ITGswQ1Z1aGJHWE1kUlBiekJOMTREOWp1aFJBTkNBQVRLT3NyZUc4VG1XbExTeU1KUnBSWTA2N1NudFhmZgpkakhWenQwN1ZZVm1wZ1dGZEJGUERGTFdiQkYrYlpQeGRJVW14dzFMN3NlMEUrdE1DcTk4bkEyMQotLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tCg==",
  "https://wkms-public.apple.com/fcs-keys/09QNzDMRwGnqUMjbRQcsH7sHx2GJUub-NmLLpIsd8Yc=": "LS0tLS1CRUdJTiBQUklWQVRFIEtFWS0tLS0tCk1JR0hBZ0VBTUJNR0J5cUdTTTQ5QWdFR0NDcUdTTTQ5QXdFSEJHMHdhd0lCQVFRZ0QyeTRzZE1QNXE2eHZ4NTIKMFNqaCt1S0JkcWVTRlF2T083Rm9PaHg1RHZxaFJBTkNBQVRLbEMvdXhKa3Q4d0FhS1Fzd3paeVJ4WWVTN0pOVAowRlFsS0w3S0hZb1k0U1FWekZWNTBkQkhGeGRVMHVaeGN3Rk9MaW1MTVZZaHBtREQ0enFpZGtPeAotLS0tLUVORCBQUklWQVRFIEtFWS0tLS0tCg=="
} # object | Firmware assets payload

        try:
            # Add firmware assets via the firmware service
            api_response = await api_instance.v1_cluster_firmware_service_firmware_assets_post(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_firmware_service_firmware_assets_post: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| Firmware assets payload | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_firmware_service_firmwares_filename_delete**
> v1_cluster_firmware_service_firmwares_filename_delete(filename)

Delete a firmware by filename from the firmware service

Proxies a request to the firmware service to delete a firmware by filename.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        filename = 'filename_example' # str | The filename of the firmware to delete

        try:
            # Delete a firmware by filename from the firmware service
            api_instance.v1_cluster_firmware_service_firmwares_filename_delete(filename)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_firmware_service_firmwares_filename_delete: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filename** | **str**| The filename of the firmware to delete | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_firmware_service_firmwares_get**
> list[Firmware] v1_cluster_firmware_service_firmwares_get(limit=limit, offset=offset, search=search, order=order, filename=filename, model=model, type=type, version=version, buildid=buildid, firmware_assets=firmware_assets)

Fetch firmwares from the firmware service

Proxies a request to the firmware service to retrieve a list of firmwares.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        limit = 3.4 # float | Number of results to return (min: 1, max: 10000, default: 100) (optional)
offset = 3.4 # float | Index of the first row to return (default: 0) (optional)
search = 'search_example' # str | Case-insensitive partial match across filename, model, type, version and buildid fields (optional)
order = 'order_example' # str | Comma-separated field names for sorting. Prefix with '-' for ascending order (e.g., 'name,-platform'). Allowed fields: filename, model, type, version, buildid  Filtering options: (optional)
filename = 'filename_example' # str | Filter by exact filename. Example: iPhone_4.7_P3_12.1.4_16D57_Restore.ipsw (optional)
model = 'model_example' # str | Filter by exact model. Example: iPhone10,4 (optional)
type = 'type_example' # str | Filter by exact type. Example: ipsw (optional)
version = 'version_example' # str | Filter by exact version. Example: 12.1.4 (optional)
buildid = 'buildid_example' # str | Filter by exact buildid. Example: 16D57 (optional)
firmware_assets = 'firmware_assets_example' # str | Filter by exact asset URL/ID. Example: https://wkms-public.apple.com/fcs-keys/rl_td3o_0EtXT8t6HvVJoeWXnoBuzumHyUTD8-MUaF8= -OR- rl_td3o_0EtXT8t6HvVJoeWXnoBuzumHyUTD8-MUaF8= (optional)

        try:
            # Fetch firmwares from the firmware service
            api_response = await api_instance.v1_cluster_firmware_service_firmwares_get(limit=limit, offset=offset, search=search, order=order, filename=filename, model=model, type=type, version=version, buildid=buildid, firmware_assets=firmware_assets)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_firmware_service_firmwares_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| Number of results to return (min: 1, max: 10000, default: 100) | [optional] 
 **offset** | **float**| Index of the first row to return (default: 0) | [optional] 
 **search** | **str**| Case-insensitive partial match across filename, model, type, version and buildid fields | [optional] 
 **order** | **str**| Comma-separated field names for sorting. Prefix with &#39;-&#39; for ascending order (e.g., &#39;name,-platform&#39;). Allowed fields: filename, model, type, version, buildid  Filtering options: | [optional] 
 **filename** | **str**| Filter by exact filename. Example: iPhone_4.7_P3_12.1.4_16D57_Restore.ipsw | [optional] 
 **model** | **str**| Filter by exact model. Example: iPhone10,4 | [optional] 
 **type** | **str**| Filter by exact type. Example: ipsw | [optional] 
 **version** | **str**| Filter by exact version. Example: 12.1.4 | [optional] 
 **buildid** | **str**| Filter by exact buildid. Example: 16D57 | [optional] 
 **firmware_assets** | **str**| Filter by exact asset URL/ID. Example: https://wkms-public.apple.com/fcs-keys/rl_td3o_0EtXT8t6HvVJoeWXnoBuzumHyUTD8-MUaF8&#x3D; -OR- rl_td3o_0EtXT8t6HvVJoeWXnoBuzumHyUTD8-MUaF8&#x3D; | [optional] 

### Return type

[**list[Firmware]**](Firmware.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_nodes_get**
> list[NodeInformation] v1_cluster_nodes_get(limit=limit, offset=offset)

List servers in the cluster

List servers in the cluster

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        limit = 3.4 # float | limit for pagination results, defaults to 100 (optional)
offset = 3.4 # float | offset for pagination results, defaults to 0 (optional)

        try:
            # List servers in the cluster
            api_response = await api_instance.v1_cluster_nodes_get(limit=limit, offset=offset)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_nodes_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| limit for pagination results, defaults to 100 | [optional] 
 **offset** | **float**| offset for pagination results, defaults to 0 | [optional] 

### Return type

[**list[NodeInformation]**](NodeInformation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_cluster_nodes_node_id_get**
> NodeInformation v1_cluster_nodes_node_id_get(node_id)

Get node details by ID

Get node details by ID

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        node_id = 'node_id_example' # str | Node ID

        try:
            # Get node details by ID
            api_response = await api_instance.v1_cluster_nodes_node_id_get(node_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_cluster_nodes_node_id_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| Node ID | 

### Return type

[**NodeInformation**](NodeInformation.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Node not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_domain_auth_provider**
> DomainAuthProviderResponse v1_create_domain_auth_provider(domain_id, domain_auth_provider_request)

Create a new auth provider for a domain

Create a new auth provider for a domain

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        domain_id = 'domain_id_example' # str | Domain ID - uuid
domain_auth_provider_request = {
  "enabled": true,
  "providerType": "open-id-connect",
  "label": "Login with Custom Auth0",
  "config": {
    "discoveryUrl": "http://localhost:8080/realms/Corellium/.well-known/openid-configuration",
    "clientId": "B5GhRzrVn19adO1a1vJ6aZRYdNY9jSP4",
    "clientSecret": "itsasecret",
    "invitedOnly": false
  }
} # DomainAuthProviderRequest | Request Data

        try:
            # Create a new auth provider for a domain
            api_response = await api_instance.v1_create_domain_auth_provider(domain_id, domain_auth_provider_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_domain_auth_provider: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID - uuid | 
 **domain_auth_provider_request** | [**DomainAuthProviderRequest**](DomainAuthProviderRequest.md)| Request Data | 

### Return type

[**DomainAuthProviderResponse**](DomainAuthProviderResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_hook**
> Hook v1_create_hook(instance_id, v1_create_hook_parameters)

Create hypervisor hook for Instance

Create hypervisor hook for Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
v1_create_hook_parameters = corellium_api.V1CreateHookParameters() # V1CreateHookParameters | application/json

        try:
            # Create hypervisor hook for Instance
            api_response = await api_instance.v1_create_hook(instance_id, v1_create_hook_parameters)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_hook: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **v1_create_hook_parameters** | [**V1CreateHookParameters**](V1CreateHookParameters.md)| application/json | 

### Return type

[**Hook**](Hook.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Hook |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_image**
> Image v1_create_image(type, encoding, encapsulated=encapsulated, name=name, project=project, instance=instance, file=file)

Create a new Image

Create a new Image

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        type = 'type_example' # str | Image type
encoding = 'encoding_example' # str | How the file is stored
encapsulated = True # bool | set to false if the uploaded file is not encapsulated inside an outer zipfile (optional)
name = 'name_example' # str | Image name (optional)
project = 'project_example' # str | Project ID (optional)
instance = 'instance_example' # str | Instance ID (optional)
file = '/path/to/file' # file | Optionally the actual file (optional)

        try:
            # Create a new Image
            api_response = await api_instance.v1_create_image(type, encoding, encapsulated=encapsulated, name=name, project=project, instance=instance, file=file)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_image: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Image type | 
 **encoding** | **str**| How the file is stored | 
 **encapsulated** | **bool**| set to false if the uploaded file is not encapsulated inside an outer zipfile | [optional] 
 **name** | **str**| Image name | [optional] 
 **project** | **str**| Project ID | [optional] 
 **instance** | **str**| Instance ID | [optional] 
 **file** | **file**| Optionally the actual file | [optional] 

### Return type

[**Image**](Image.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**201** | application/json |  -  |
**404** | application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_instance**
> InstanceReturn v1_create_instance(instance_create_options)

Create Instance

Create Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_create_options = {
  "project": "<your_project_id>",
  "name": "rpi4b Created via API",
  "flavor": "rpi4b",
  "os": "11.2.0"
} # InstanceCreateOptions | The vm definition to create

        try:
            # Create Instance
            api_response = await api_instance.v1_create_instance(instance_create_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_create_options** | [**InstanceCreateOptions**](InstanceCreateOptions.md)| The vm definition to create | 

### Return type

[**InstanceReturn**](InstanceReturn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_network_connection**
> NetworkConnection v1_create_network_connection(create_network_connection_options)

Create a new Network Connection

You must have the domain administrator role to create a network connection. VLAN networks are only supported in bridged networking mode.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        create_network_connection_options = {
  "provider": "openvpn",
  "name": "My OpenVPN Connection",
  "config": {
    "config": "client\ndev tun\nproto tcp\nremote my-server-1 1194\nresolv-retry infinite\nnobind\npersist-key\npersist-tun\nremote-cert-tls server\ntls-auth ta.key 1\ncipher AES-256-CBC\nverb 3\n"
  }
} # CreateNetworkConnectionOptions | Network Connection Options

        try:
            # Create a new Network Connection
            api_response = await api_instance.v1_create_network_connection(create_network_connection_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_network_connection: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_network_connection_options** | [**CreateNetworkConnectionOptions**](CreateNetworkConnectionOptions.md)| Network Connection Options | 

### Return type

[**NetworkConnection**](NetworkConnection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_project**
> Project v1_create_project(project)

Create a Project

Create a Project

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project = {
  "name": "New Project",
  "settings": {
    "internet-access": true
  },
  "quotas": {
    "cores": 8,
    "instances": 2,
    "ram": 16384
  }
} # Project | Project

        try:
            # Create a Project
            api_response = await api_instance.v1_create_project(project)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_project: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | [**Project**](Project.md)| Project | 

### Return type

[**Project**](Project.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_snapshot**
> Snapshot v1_create_snapshot(instance_id, snapshot_creation_options)

Create Instance Snapshot

Create Instance Snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
snapshot_creation_options = corellium_api.SnapshotCreationOptions() # SnapshotCreationOptions | 

        try:
            # Create Instance Snapshot
            api_response = await api_instance.v1_create_snapshot(instance_id, snapshot_creation_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **snapshot_creation_options** | [**SnapshotCreationOptions**](SnapshotCreationOptions.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_user**
> UserCreateReturn v1_create_user(user_create)

Create User

Create User

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        user_create = {
  "name": "test",
  "label": "Project Admin",
} # UserCreate | User data

        try:
            # Create User
            api_response = await api_instance.v1_create_user(user_create)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_user: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)| User data | 

### Return type

[**UserCreateReturn**](UserCreateReturn.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_domain_auth_provider**
> v1_delete_domain_auth_provider(domain_id, provider_id)

Delete an auth provider from a domain

Delete an auth provider from a domain

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        domain_id = 'domain_id_example' # str | Domain ID - uuid
provider_id = 'provider_id_example' # str | Provider ID - uuid

        try:
            # Delete an auth provider from a domain
            api_instance.v1_delete_domain_auth_provider(domain_id, provider_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_domain_auth_provider: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID - uuid | 
 **provider_id** | **str**| Provider ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_extension**
> v1_delete_extension(extension_id)

Delete an existing extension

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        extension_id = 'extension_id_example' # str | Extension ID

        try:
            # Delete an existing extension
            api_instance.v1_delete_extension(extension_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_extension: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| Extension ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_hook**
> v1_delete_hook(hook_id)

Delete an existing hypervisor hook

Delete an existing hypervisor hook

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        hook_id = 'hook_id_example' # str | Hook ID

        try:
            # Delete an existing hypervisor hook
            api_instance.v1_delete_hook(hook_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_hook: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| Hook ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_image**
> v1_delete_image(image_id)

Delete Image

Delete Image

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        image_id = 'image_id_example' # str | Image ID - uuid

        try:
            # Delete Image
            api_instance.v1_delete_image(image_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_image: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Image ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_instance**
> v1_delete_instance(instance_id)

Remove Instance

Remove Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID

        try:
            # Remove Instance
            api_instance.v1_delete_instance(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_instance_snapshot**
> v1_delete_instance_snapshot(instance_id, snapshot_id)

Delete an Instance Snapshot

Delete an Instance Snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid

        try:
            # Delete an Instance Snapshot
            api_instance.v1_delete_instance_snapshot(instance_id, snapshot_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_instance_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **snapshot_id** | **str**| Snapshot ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_network_connection**
> v1_delete_network_connection(id, force=force)

Delete an existing Network Connection

You must have the domain administrator role to delete a network connection.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        id = 'id_example' # str | Network Connection Identifier - uuid
force = True # bool | Force deletion (true only or not present) (optional)

        try:
            # Delete an existing Network Connection
            api_instance.v1_delete_network_connection(id, force=force)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_network_connection: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Network Connection Identifier - uuid | 
 **force** | **bool**| Force deletion (true only or not present) | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_project**
> v1_delete_project(project_id)

Delete a Project

Delete a Project

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid

        try:
            # Delete a Project
            api_instance.v1_delete_project(project_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_project: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_snapshot**
> v1_delete_snapshot(snapshot_id)

Delete a Snapshot

Delete a Snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid

        try:
            # Delete a Snapshot
            api_instance.v1_delete_snapshot(snapshot_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_snapshot_permissions**
> Snapshot v1_delete_snapshot_permissions(snapshot_id, snapshot_permissions_request_payload)

Delete member(s)

Deletes one or more members from the list of members who have access to the snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid
snapshot_permissions_request_payload = {
  "members": [
    "newuser1@domain.com",
    "newuser2@domain.com"
  ]
} # SnapshotPermissionsRequestPayload | 

        try:
            # Delete member(s)
            api_response = await api_instance.v1_delete_snapshot_permissions(snapshot_id, snapshot_permissions_request_payload)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_snapshot_permissions: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot ID - uuid | 
 **snapshot_permissions_request_payload** | [**SnapshotPermissionsRequestPayload**](SnapshotPermissionsRequestPayload.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_user**
> v1_delete_user(user_id)

Delete User

Delete User

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        user_id = 'user_id_example' # str | userId - uuid

        try:
            # Delete User
            api_instance.v1_delete_user(user_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_delete_user: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_detach_instance_interface**
> v1_detach_instance_interface(instance_id, interface_id, detach_interface_request)

Detach I/O Interface

Detach an I/O interface from an I/O interconnect for the specified instance identifier.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
interface_id = 'interface_id_example' # str | Interface ID
detach_interface_request = corellium_api.DetachInterfaceRequest() # DetachInterfaceRequest | Interface detachment request

        try:
            # Detach I/O Interface
            api_instance.v1_detach_instance_interface(instance_id, interface_id, detach_interface_request)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_detach_instance_interface: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **interface_id** | **str**| Interface ID | 
 **detach_interface_request** | [**DetachInterfaceRequest**](DetachInterfaceRequest.md)| Interface detachment request | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_disable_expose_port**
> v1_disable_expose_port(instance_id)

Disable an exposed port on an instance for device access.

Disable an exposed port on an instance for device access.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Disable an exposed port on an instance for device access.
            api_instance.v1_disable_expose_port(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_disable_expose_port: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_download_activity**
> ActivityList v1_download_activity(task_id)

Download activity

Download activity for a given task

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        task_id = 'task_id_example' # str | Export ID

        try:
            # Download activity
            api_response = await api_instance.v1_download_activity(task_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_download_activity: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Export ID | 

### Return type

[**ActivityList**](ActivityList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_enable_expose_port**
> v1_enable_expose_port(instance_id)

Enable an exposed port on an instance for device access.

Enable an exposed port on an instance for device access.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Enable an exposed port on an instance for device access.
            api_instance.v1_enable_expose_port(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_enable_expose_port: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_execute_hyper_trace_hooks**
> v1_execute_hyper_trace_hooks(instance_id)

Execute Hooks on an instance

Execute Hooks on an instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Execute Hooks on an instance
            api_instance.v1_execute_hyper_trace_hooks(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_execute_hyper_trace_hooks: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_activity_export_status**
> ActivityList v1_get_activity_export_status(task_id)

Get export task status

Get export task status

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        task_id = 'task_id_example' # str | Export ID

        try:
            # Get export task status
            api_response = await api_instance.v1_get_activity_export_status(task_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_activity_export_status: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Export ID | 

### Return type

[**ActivityList**](ActivityList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_activity_export_tasks**
> ActivityList v1_get_activity_export_tasks()

Get all export tasks for user

Get all export tasks for user

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # Get all export tasks for user
            api_response = await api_instance.v1_get_activity_export_tasks()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_activity_export_tasks: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ActivityList**](ActivityList.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_config**
> ConfigResponse v1_get_config()

Get all configs

Get all configs

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # Get all configs
            api_response = await api_instance.v1_get_config()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_config: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ConfigResponse**](ConfigResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_domain_auth_providers**
> list[DomainAuthProviderResponse] v1_get_domain_auth_providers(domain_id)

Return all configured auth providers for a domain (including globally configured providers)

Return all configured auth providers for a domain (including globally configured providers)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        domain_id = 'domain_id_example' # str | Domain ID - uuid

        try:
            # Return all configured auth providers for a domain (including globally configured providers)
            api_response = await api_instance.v1_get_domain_auth_providers(domain_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_domain_auth_providers: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID - uuid | 

### Return type

[**list[DomainAuthProviderResponse]**](DomainAuthProviderResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_extension_by_id**
> Extension v1_get_extension_by_id(extension_id)

Get extension by id

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        extension_id = 'extension_id_example' # str | Extension Id

        try:
            # Get extension by id
            api_response = await api_instance.v1_get_extension_by_id(extension_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_extension_by_id: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| Extension Id | 

### Return type

[**Extension**](Extension.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extension |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_extensions**
> list[Extension] v1_get_extensions(limit=limit, offset=offset, if_none_match=if_none_match)

Get all extensions

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        limit = 3.4 # float | limit for pagination results, defaults to 20 (optional)
offset = 3.4 # float | offset for pagination results, defaults to 0 (optional)
if_none_match = 'if_none_match_example' # str | sha256sum of the last response with the same parameters (optional) (optional)

        try:
            # Get all extensions
            api_response = await api_instance.v1_get_extensions(limit=limit, offset=offset, if_none_match=if_none_match)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_extensions: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| limit for pagination results, defaults to 20 | [optional] 
 **offset** | **float**| offset for pagination results, defaults to 0 | [optional] 
 **if_none_match** | **str**| sha256sum of the last response with the same parameters (optional) | [optional] 

### Return type

[**list[Extension]**](Extension.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extensions |  -  |
**304** | No changes |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_hook_by_id**
> Hook v1_get_hook_by_id(hook_id)

Get hypervisor hook by id

Get hypervisor hook by id

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        hook_id = 'hook_id_example' # str | Hook Id

        try:
            # Get hypervisor hook by id
            api_response = await api_instance.v1_get_hook_by_id(hook_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_hook_by_id: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| Hook Id | 

### Return type

[**Hook**](Hook.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_hooks**
> list[Hook] v1_get_hooks(instance_id, limit=limit, offset=offset, sort=sort)

Get all hypervisor hooks for Instance

Get all hypervisor hooks for Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
limit = 3.4 # float | limit for pagination results, defaults to 20 (optional)
offset = 3.4 # float | offset for pagination results, defaults to 0 (optional)
sort = 'sort_example' # str | sort ASC or DESC, defaults to DESC (optional)

        try:
            # Get all hypervisor hooks for Instance
            api_response = await api_instance.v1_get_hooks(instance_id, limit=limit, offset=offset, sort=sort)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_hooks: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **limit** | **float**| limit for pagination results, defaults to 20 | [optional] 
 **offset** | **float**| offset for pagination results, defaults to 0 | [optional] 
 **sort** | **str**| sort ASC or DESC, defaults to DESC | [optional] 

### Return type

[**list[Hook]**](Hook.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hooks |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_image**
> Image v1_get_image(image_id)

Get Image Metadata

Get Image Metadata

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        image_id = 'image_id_example' # str | Image ID - uuid

        try:
            # Get Image Metadata
            api_response = await api_instance.v1_get_image(image_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_image: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Image ID - uuid | 

### Return type

[**Image**](Image.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**404** | application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_images**
> list[Image] v1_get_images(project=project)

Get all Images Metadata

Get all Images Metadata

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project = 'project_example' # str | Optionally filter by project - uuid (optional)

        try:
            # Get all Images Metadata
            api_response = await api_instance.v1_get_images(project=project)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_images: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project** | **str**| Optionally filter by project - uuid | [optional] 

### Return type

[**list[Image]**](Image.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_install_firmware_status**
> InstallFirmwareResponse v1_get_install_firmware_status(task_id)

Query install firmware request status.

Returns the status of an install firmware request.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        task_id = 'task_id_example' # str | Task ID - uuid

        try:
            # Query install firmware request status.
            api_response = await api_instance.v1_get_install_firmware_status(task_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_install_firmware_status: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**| Task ID - uuid | 

### Return type

[**InstallFirmwareResponse**](InstallFirmwareResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance**
> Instance v1_get_instance(instance_id, return_attr=return_attr)

Get Instance

Get Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID
return_attr = ['return_attr_example'] # list[str] | Attributes to include in instance return (optional)

        try:
            # Get Instance
            api_response = await api_instance.v1_get_instance(instance_id, return_attr=return_attr)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID | 
 **return_attr** | [**list[str]**](str.md)| Attributes to include in instance return | [optional] 

### Return type

[**Instance**](Instance.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_console**
> InstanceConsoleEndpoint v1_get_instance_console(instance_id)

Get console websocket URL

Get console websocket URL

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get console websocket URL
            api_response = await api_instance.v1_get_instance_console(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_console: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**InstanceConsoleEndpoint**](InstanceConsoleEndpoint.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_console_log**
> str v1_get_instance_console_log(instance_id)

Get Console Log

Get Console Log

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get Console Log
            api_response = await api_instance.v1_get_instance_console_log(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_console_log: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current console log |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_gpios**
> GpiosState v1_get_instance_gpios(instance_id)

Get Instance GPIOs

Get Instance GPIOs

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get Instance GPIOs
            api_response = await api_instance.v1_get_instance_gpios(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_gpios: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**GpiosState**](GpiosState.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current GPIO State |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_panics**
> list[object] v1_get_instance_panics(instance_id)

Get Panics

Get Panics

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get Panics
            api_response = await api_instance.v1_get_instance_panics(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_panics: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

**list[object]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Array of panics |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_peripherals**
> PeripheralsData v1_get_instance_peripherals(instance_id)

Get Instance Peripherals

Get Instance Peripherals

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get Instance Peripherals
            api_response = await api_instance.v1_get_instance_peripherals(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_peripherals: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**PeripheralsData**](PeripheralsData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current Peripherals State |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_screenshot**
> file v1_get_instance_screenshot(instance_id, format, scale=scale)

Get Instance Screenshot

Get Instance Screenshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
format = 'format_example' # str | New peripherals state
scale = 3.4 # float | Screenshot scale 1:N (optional)

        try:
            # Get Instance Screenshot
            api_response = await api_instance.v1_get_instance_screenshot(instance_id, format, scale=scale)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_screenshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **format** | **str**| New peripherals state | 
 **scale** | **float**| Screenshot scale 1:N | [optional] 

### Return type

**file**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/png, image/jpeg, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Screenshot |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_snapshot**
> Snapshot v1_get_instance_snapshot(instance_id, snapshot_id)

Get Instance Snapshot

Get Instance Snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid

        try:
            # Get Instance Snapshot
            api_response = await api_instance.v1_get_instance_snapshot(instance_id, snapshot_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **snapshot_id** | **str**| Snapshot ID - uuid | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_snapshots**
> list[Snapshot] v1_get_instance_snapshots(instance_id)

Get Instance Snapshots

Get Instance Snapshots

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get Instance Snapshots
            api_response = await api_instance.v1_get_instance_snapshots(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_snapshots: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**list[Snapshot]**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instances**
> list[Instance] v1_get_instances(name=name, return_attr=return_attr)

Get Instances

Get Instances

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        name = 'name_example' # str | Optionally filter by instance name (optional)
return_attr = ['return_attr_example'] # list[str] | Attributes to include in instance return (optional)

        try:
            # Get Instances
            api_response = await api_instance.v1_get_instances(name=name, return_attr=return_attr)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instances: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Optionally filter by instance name | [optional] 
 **return_attr** | [**list[str]**](str.md)| Attributes to include in instance return | [optional] 

### Return type

[**list[Instance]**](Instance.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_model_software**
> list[Firmware] v1_get_model_software(model)

Get Software for Model

Get Software for Model

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        model = 'model_example' # str | Model to list available software for

        try:
            # Get Software for Model
            api_response = await api_instance.v1_get_model_software(model)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_model_software: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | **str**| Model to list available software for | 

### Return type

[**list[Firmware]**](Firmware.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported software loads for this model |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_models**
> list[Model] v1_get_models()

Get Supported Models

Get Supported Models

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # Get Supported Models
            api_response = await api_instance.v1_get_models()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_models: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Model]**](Model.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Supported device configurations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_network_connection**
> NetworkConnection v1_get_network_connection(id)

Return the configuration and per project statuses for a single network provider.

You must have the domain administrator or project administrator role to fetch a network connection.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        id = 'id_example' # str | Network Connection Identifier - uuid

        try:
            # Return the configuration and per project statuses for a single network provider.
            api_response = await api_instance.v1_get_network_connection(id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_network_connection: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Network Connection Identifier - uuid | 

### Return type

[**NetworkConnection**](NetworkConnection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_project**
> Project v1_get_project(project_id)

Get a Project

Get a Project

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid

        try:
            # Get a Project
            api_response = await api_instance.v1_get_project(project_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_project: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 

### Return type

[**Project**](Project.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_project_instances**
> list[Instance] v1_get_project_instances(project_id, name=name, return_attr=return_attr)

Get Instances in Project

Get Instances in Project

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
name = 'name_example' # str | Filter by project name (optional)
return_attr = ['return_attr_example'] # list[str] | Attributes to include in instance return (optional)

        try:
            # Get Instances in Project
            api_response = await api_instance.v1_get_project_instances(project_id, name=name, return_attr=return_attr)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_project_instances: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **name** | **str**| Filter by project name | [optional] 
 **return_attr** | [**list[str]**](str.md)| Attributes to include in instance return | [optional] 

### Return type

[**list[Instance]**](Instance.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_project_keys**
> list[ProjectKey] v1_get_project_keys(project_id)

Get Project Authorized Keys

Get Project Authorized Keys

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid

        try:
            # Get Project Authorized Keys
            api_response = await api_instance.v1_get_project_keys(project_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_project_keys: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 

### Return type

[**list[ProjectKey]**](ProjectKey.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorized Keys |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_project_network_log**
> str v1_get_project_network_log(project_id)

Retrieve the network connection log for a project

Retrieve the network connection log for a project

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID (must be a valid UUID)

        try:
            # Retrieve the network connection log for a project
            api_response = await api_instance.v1_get_project_network_log(project_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_project_network_log: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID (must be a valid UUID) | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_project_network_status**
> NetworkStatusResponse v1_get_project_network_status(project_id)

Retrieve the network connection status for a project

Retrieve the network connection status for a project

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid

        try:
            # Retrieve the network connection status for a project
            api_response = await api_instance.v1_get_project_network_status(project_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_project_network_status: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 

### Return type

[**NetworkStatusResponse**](NetworkStatusResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_project_vpn_config**
> str v1_get_project_vpn_config(project_id, format)

Get Project VPN Configuration

A Project VPN allows connection _into_ virtual devices in the project (e.g., connecting a researcher's computer as a VPN client to a virtual device within the project). If a Project VPN has been defined, this will return the configuration.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
format = 'format_example' # str | VPN Config format

        try:
            # Get Project VPN Configuration
            api_response = await api_instance.v1_get_project_vpn_config(project_id, format)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_project_vpn_config: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **format** | **str**| VPN Config format | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenVPN Configuration |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_projects**
> list[Project] v1_get_projects(name=name, ids_only=ids_only)

Get Projects

Get Projects

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        name = 'name_example' # str | Filter by project name (optional)
ids_only = True # bool | Only include id of project in results (optional)

        try:
            # Get Projects
            api_response = await api_instance.v1_get_projects(name=name, ids_only=ids_only)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_projects: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Filter by project name | [optional] 
 **ids_only** | **bool**| Only include id of project in results | [optional] 

### Return type

[**list[Project]**](Project.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Projects |  -  |
**403** | Forbidden |  -  |
**404** | No Projects Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_reset_link_info**
> ResetLinkInfoReturn v1_get_reset_link_info(token)

Send Password Reset Link Info

Send Password Reset Link Info

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        token = 'token_example' # str | Reset token

        try:
            # Send Password Reset Link Info
            api_response = await api_instance.v1_get_reset_link_info(token)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_reset_link_info: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Reset token | 

### Return type

[**ResetLinkInfoReturn**](ResetLinkInfoReturn.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Reset Link Info |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_shared_snapshots**
> UserSnapshots v1_get_shared_snapshots()

Fetch shared snapshots

Fetch snapshots shared with and shared by the requesting user

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # Fetch shared snapshots
            api_response = await api_instance.v1_get_shared_snapshots()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_shared_snapshots: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserSnapshots**](UserSnapshots.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_snapshot**
> Snapshot v1_get_snapshot(snapshot_id)

Get Snapshot

Get Snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid

        try:
            # Get Snapshot
            api_response = await api_instance.v1_get_snapshot(snapshot_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot ID - uuid | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_install_firmware**
> InstallFirmwareResponse v1_install_firmware(install_firmware_request)

Installs a firmware for cluster-wide use

Takes an uploaded firmware image and installs it for cluster-wide use.  The firmware is then removed from Images.  In order to install a firmware, you need to follow a 4-step process. First, POST /v1/images/ with { name: string, type: 'fw' } using content-type application/json to acquire an imageId.  Second, upload the firmware file via a multipart/form-data POST to /v1/images/:imageId.  Third, POST /v1/cluster/firmware-service/firmware with { imageId: string; filename: string } using content-type application/json to acquire a taskId.    The 'filename' must be an exact match for the filename in the firmware service that you're uploading this image for.  Fourth, you can poll the state of the installation via GET /v1/images/install-firmware/:taskId.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        install_firmware_request = corellium_api.InstallFirmwareRequest() # InstallFirmwareRequest | User data

        try:
            # Installs a firmware for cluster-wide use
            api_response = await api_instance.v1_install_firmware(install_firmware_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_install_firmware: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_firmware_request** | [**InstallFirmwareRequest**](InstallFirmwareRequest.md)| User data | 

### Return type

[**InstallFirmwareResponse**](InstallFirmwareResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | application/json |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_instances_instance_id_message_post**
> v1_instances_instance_id_message_post(instance_id, body)

Inject a message into an iOS VM

Given a message and source phone number, place this message as an incoming SMS message on the iOS VM. For advanced usage, a raw message of bytes may be sent. In this case, the parameter should provide hex encoded bytes  (0x00 0x11 0x22 0x33 in the example below) which are sent verbatim.  The user must ensure that the body is the correct format for the underlying device stack.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
body = {
  "number": "+19997776666",
  "message": "the SMS message body goes here"
} # object | Message data

        try:
            # Inject a message into an iOS VM
            api_instance.v1_instances_instance_id_message_post(instance_id, body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_instances_instance_id_message_post: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **body** | **object**| Message data | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_instances_instance_id_netdump_pcap_get**
> file v1_instances_instance_id_netdump_pcap_get(instance_id)

Download a netdump pcap file

Download a netdump pcap file

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Download a netdump pcap file
            api_response = await api_instance.v1_instances_instance_id_netdump_pcap_get(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_instances_instance_id_netdump_pcap_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

**file**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tcpdump.pcap, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | pcapng file |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_instances_instance_id_network_monitor_pcap_get**
> file v1_instances_instance_id_network_monitor_pcap_get(instance_id)

Download a Network Monitor pcap file

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Download a Network Monitor pcap file
            api_response = await api_instance.v1_instances_instance_id_network_monitor_pcap_get(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_instances_instance_id_network_monitor_pcap_get: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

**file**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.tcpdump.pcap, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | pcap file |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_kcrange**
> list[Kcrange] v1_kcrange(instance_id)

Get Kernel extension ranges

Get Kernel extension ranges

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get Kernel extension ranges
            api_response = await api_instance.v1_kcrange(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_kcrange: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**list[Kcrange]**](Kcrange.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Kcranges |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_network_connections**
> NetworkConnectionOffsetPaginationResult v1_list_network_connections(limit=limit, offset=offset)

List available network connections

You must have the domain administrator or project administrator role to list network connections.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        limit = 3.4 # float | The maximum number of items to return. (optional)
offset = 3.4 # float | The starting index of the items to return. (optional)

        try:
            # List available network connections
            api_response = await api_instance.v1_list_network_connections(limit=limit, offset=offset)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_list_network_connections: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **float**| The maximum number of items to return. | [optional] 
 **offset** | **float**| The starting index of the items to return. | [optional] 

### Return type

[**NetworkConnectionOffsetPaginationResult**](NetworkConnectionOffsetPaginationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_network_interfaces**
> list[str] v1_list_network_interfaces()

List available physical network interfaces

Lists available physical network interfaces that can be used for VLAN configuration. You must have the domain administrator role to list network interfaces.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # List available physical network interfaces
            api_response = await api_instance.v1_list_network_interfaces()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_list_network_interfaces: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_network_providers**
> NetworkConnectionProviderOffsetPaginationResult v1_list_network_providers()

List available network providers

Provides a list of registered network providers to be used when [creating network connections](#post-/v1/network/connections). You must have the domain administrator role to list network providers.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # List available network providers
            api_response = await api_instance.v1_list_network_providers()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_list_network_providers: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**NetworkConnectionProviderOffsetPaginationResult**](NetworkConnectionProviderOffsetPaginationResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_list_threads**
> list[KernelTask] v1_list_threads(instance_id)

Get Running Threads (CoreTrace)

Get Running Threads (CoreTrace)

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Get Running Threads (CoreTrace)
            api_response = await api_instance.v1_list_threads(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_list_threads: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**list[KernelTask]**](KernelTask.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Threads |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_load_extension**
> Extension v1_load_extension(v1_load_extension_parameters)

Load an extension

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        v1_load_extension_parameters = corellium_api.V1LoadExtensionParameters() # V1LoadExtensionParameters | application/json

        try:
            # Load an extension
            api_response = await api_instance.v1_load_extension(v1_load_extension_parameters)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_load_extension: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **v1_load_extension_parameters** | [**V1LoadExtensionParameters**](V1LoadExtensionParameters.md)| application/json | 

### Return type

[**Extension**](Extension.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Extension |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_media_play**
> v1_media_play(instance_id, media_play_body)

Start playing media

Start playing media

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
media_play_body = {
  "url": "http://null.to/test.mp4"
} # MediaPlayBody | Request Body

        try:
            # Start playing media
            api_instance.v1_media_play(instance_id, media_play_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_media_play: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **media_play_body** | [**MediaPlayBody**](MediaPlayBody.md)| Request Body | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_media_stop**
> v1_media_stop(instance_id)

Stop playing media

Stop playing media

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Stop playing media
            api_instance.v1_media_stop(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_media_stop: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success response |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_parse_extension_json**
> object v1_parse_extension_json(extension)

Validates extension.json

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        extension = {
    "parserVersion": 1,
    "version": "1.0.0",
    "identifier": "mach-rpi4b",
    "definitions": [{
      "type": "iot",
      "flavor": "Raspberry Pi 4",
      "flavorId": "rpi4b",
      "cores": 4,
      "bootargs": [],
      "volume": {
        "allocate": 1
      },
      "ram": 4096,
      "supportsGDB": true,
      "supportsSerialConsole": true,
      "supportsPresetBootOptions": true
    }]
} # Extension | extension.json contents

        try:
            # Validates extension.json
            api_response = await api_instance.v1_parse_extension_json(extension)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_parse_extension_json: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension** | [**Extension**](Extension.md)| extension.json contents | 

### Return type

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_partial_update_network_connection**
> NetworkConnection v1_partial_update_network_connection(id, update_network_connection_options, force=force)

Update Network Connection (partial)

Only updates the specified attributes. You must have the domain administrator role to update a network connection.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        id = 'id_example' # str | Network Connection Identifier - uuid
update_network_connection_options = {
  "name": "My Renamed OpenVPN Connection"
} # UpdateNetworkConnectionOptions | Network Connection Options
force = True # bool | Force deletion (true only or not present) (optional)

        try:
            # Update Network Connection (partial)
            api_response = await api_instance.v1_partial_update_network_connection(id, update_network_connection_options, force=force)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_partial_update_network_connection: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Network Connection Identifier - uuid | 
 **update_network_connection_options** | [**UpdateNetworkConnectionOptions**](UpdateNetworkConnectionOptions.md)| Network Connection Options | 
 **force** | **bool**| Force deletion (true only or not present) | [optional] 

### Return type

[**NetworkConnection**](NetworkConnection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_patch_instance**
> Instance v1_patch_instance(instance_id, patch_instance_options)

Update Instance

Update Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID
patch_instance_options = {
 "name": "New Name"
} # PatchInstanceOptions | 

        try:
            # Update Instance
            api_response = await api_instance.v1_patch_instance(instance_id, patch_instance_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_patch_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID | 
 **patch_instance_options** | [**PatchInstanceOptions**](PatchInstanceOptions.md)|  | 

### Return type

[**Instance**](Instance.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_patch_instance_read_only**
> Instance v1_patch_instance_read_only(instance_id, patch_instance_read_only)

Update Instance Read Only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID
patch_instance_read_only = {
 "readOnly": "disabled"
} # PatchInstanceReadOnly | 

        try:
            # Update Instance Read Only
            api_response = await api_instance.v1_patch_instance_read_only(instance_id, patch_instance_read_only)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_patch_instance_read_only: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID | 
 **patch_instance_read_only** | [**PatchInstanceReadOnly**](PatchInstanceReadOnly.md)|  | 

### Return type

[**Instance**](Instance.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_pause_instance**
> v1_pause_instance(instance_id)

Pause an Instance

Pause an Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Pause an Instance
            api_instance.v1_pause_instance(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_pause_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_post_instance_input**
> InputResponse v1_post_instance_input(instance_id, instance_input)

Provide Instance Input

Sends a touch or button event to the VM.  - Buttons (or keys) to be held during the input are specified as an array of strings, each string must be either a single ascii character or one of the following keywords:   - VM Buttons: finger, homeButton, holdButton, volumeUp, volumeDown, ringerSwitch, backButton, overviewButton   - Keyboard Buttons: again, alt, alterase, apostrophe, back, backslash, backspace, bassboost, bookmarks, bsp, calc, camera, cancel, caps, capslock, chat, close, closecd, comma, compose, computer, config, connect, copy, ctrl, cut, cyclewindows, dashboard, del, delete, deletefile, dot, down, edit, eject, ejectclose, email, end, enter, equal, esc, escape, exit, f1, f10, f11, f12, f13, f14, f15, f16, f17, f18, f19, f2, f20, f21, f22, f23, f24, f3, f4, f5, f6, f7, f8, f9, fastfwd, file, finance, find, forward, front, grave, hangeul, hanja, help, henkan, home, homepage, hp, hrgn, ins, insert, iso, k102, kp0, kp1, kp2, kp3, kp4, kp5, kp6, kp7, kp8, kp9, kpasterisk, kpcomma, kpdot, kpenter, kpequal, kpjpcomma, kpleftparen, kpminus, kpplus, kpplusminus, kprightparen, kpslash, ktkn, ktknhrgn, left, leftalt, leftbrace, leftctrl, leftmeta, leftshift, linefeed, macro, mail, menu, meta, minus, move, msdos, muhenkan, mute, new, next, numlock, open, pagedown, pageup, paste, pause, pausecd, pgdn, pgup, phone, play, playcd, playpause, power, previous, print, prog1, prog2, prog3, prog4, props, question, record, redo, refresh, return, rewind, right, rightalt, rightbrace, rightctrl, rightmeta, rightshift, ro, rotate, scale, screenlock, scrolldown, scrolllock, scrollup, search, semicolon, sendfile, setup, shift, shop, slash, sleep, sound, space, sport, stop, stopcd, suspend, sysrq, tab, undo, up, voldown, volup, wakeup, www, xfer, yen, zkhk

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
instance_input = [
  {
    "buttons": ["finger"],
    "position": [
      [300, 600]
    ],
    "wait": 0
  },
  {
    "buttons": [],
    "wait": 100
  }
] # list[InstanceInput] | The input to send to the VM

        try:
            # Provide Instance Input
            api_response = await api_instance.v1_post_instance_input(instance_id, instance_input)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_post_instance_input: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **instance_input** | [**list[InstanceInput]**](InstanceInput.md)| The input to send to the VM | 

### Return type

[**InputResponse**](InputResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ETA of input completion in milliseconds |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_ready**
> v1_ready()

API Status

Check if  API is ready for queries

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # API Status
            api_instance.v1_ready()
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_ready: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | API is ready for queries |  -  |
**503** | API is not ready |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_reboot_instance**
> v1_reboot_instance(instance_id)

Reboot an Instance

Reboot an Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Reboot an Instance
            api_instance.v1_reboot_instance(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_reboot_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_remove_project_key**
> v1_remove_project_key(project_id, key_id)

Delete Project Authorized Key

Delete Project Authorized Key

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
key_id = 'key_id_example' # str | Key ID - uuid

        try:
            # Delete Project Authorized Key
            api_instance.v1_remove_project_key(project_id, key_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_remove_project_key: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **key_id** | **str**| Key ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Deleted |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_remove_team_role_from_project**
> v1_remove_team_role_from_project(project_id, team_id, role_id)

Remove team role from project

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
team_id = 'team_id_example' # str | Team ID - uuid
role_id = 'role_id_example' # str | Role ID

        try:
            # Remove team role from project
            api_instance.v1_remove_team_role_from_project(project_id, team_id, role_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_remove_team_role_from_project: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **team_id** | **str**| Team ID - uuid | 
 **role_id** | **str**| Role ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_remove_user_from_team**
> v1_remove_user_from_team(team_id, user_id)

Remove user from team

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        team_id = 'team_id_example' # str | Team ID - uuid
user_id = 'user_id_example' # str | User ID - uuid

        try:
            # Remove user from team
            api_instance.v1_remove_user_from_team(team_id, user_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_remove_user_from_team: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team ID - uuid | 
 **user_id** | **str**| User ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_remove_user_role_from_project**
> v1_remove_user_role_from_project(project_id, user_id, role_id)

Remove user role from project

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
user_id = 'user_id_example' # str | User ID - uuid
role_id = 'role_id_example' # str | Role ID

        try:
            # Remove user role from project
            api_instance.v1_remove_user_role_from_project(project_id, user_id, role_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_remove_user_role_from_project: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **user_id** | **str**| User ID - uuid | 
 **role_id** | **str**| Role ID | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_rename_instance_snapshot**
> Snapshot v1_rename_instance_snapshot(instance_id, snapshot_id, snapshot_creation_options)

Rename an Instance Snapshot

Rename an Instance Snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid
snapshot_creation_options = corellium_api.SnapshotCreationOptions() # SnapshotCreationOptions | 

        try:
            # Rename an Instance Snapshot
            api_response = await api_instance.v1_rename_instance_snapshot(instance_id, snapshot_id, snapshot_creation_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_rename_instance_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **snapshot_id** | **str**| Snapshot ID - uuid | 
 **snapshot_creation_options** | [**SnapshotCreationOptions**](SnapshotCreationOptions.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_reset_user_password**
> v1_reset_user_password(password_reset_body)

Reset User Password

Reset User Password

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        password_reset_body = {
  "token": "<token>",
  "totpToken": "<totpToken>",
  "new-password": "password"
} # PasswordResetBody | application/json

        try:
            # Reset User Password
            api_instance.v1_reset_user_password(password_reset_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_reset_user_password: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_reset_body** | [**PasswordResetBody**](PasswordResetBody.md)| application/json | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_restore_backup**
> v1_restore_backup(instance_id, restore_backup_data=restore_backup_data)

Restore backup

Restore backup

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
restore_backup_data = {
  "password": "12345678"
} # RestoreBackupData | Restore backup data (optional)

        try:
            # Restore backup
            api_instance.v1_restore_backup(instance_id, restore_backup_data=restore_backup_data)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_restore_backup: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **restore_backup_data** | [**RestoreBackupData**](RestoreBackupData.md)| Restore backup data | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_restore_instance_snapshot**
> v1_restore_instance_snapshot(instance_id, snapshot_id)

Restore an Instance Snapshot

Restore an Instance Snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid

        try:
            # Restore an Instance Snapshot
            api_instance.v1_restore_instance_snapshot(instance_id, snapshot_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_restore_instance_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **snapshot_id** | **str**| Snapshot ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_roles**
> list[Role] v1_roles()

Get all roles

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # Get all roles
            api_response = await api_instance.v1_roles()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_roles: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Role]**](Role.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Roles |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_rotate_instance**
> v1_rotate_instance(instance_id, rotate_body)

Rotate device to specified orientation

Rotate device to orientation.  Accepted orientations: 1. Portrait 2. Portrait vertically inverted (up-side-down) 3. Landscape with top of the device to the left 4. Landscape with top of the device to the right

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | 
rotate_body = {
  "orientation": 1
} # RotateBody | 

        try:
            # Rotate device to specified orientation
            api_instance.v1_rotate_instance(instance_id, rotate_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_rotate_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **rotate_body** | [**RotateBody**](RotateBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_send_user_reset_link**
> v1_send_user_reset_link(reset_link_body)

Send Password Reset Link

Send Password Reset Link

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        reset_link_body = corellium_api.ResetLinkBody() # ResetLinkBody | application/json

        try:
            # Send Password Reset Link
            api_instance.v1_send_user_reset_link(reset_link_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_send_user_reset_link: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_link_body** | [**ResetLinkBody**](ResetLinkBody.md)| application/json | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_instance_gpios**
> GpiosState v1_set_instance_gpios(instance_id, gpios_state)

Set Instance GPIOs

Set Instance GPIOs

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
gpios_state = {
  "button": {
    "bitCount": 2,
    "banks": [
      [0,1],
      [1,0]
    ]
  },
  "switch": {
    "bitCount": 8,
    "banks": [
      [0,1,0,1,0,1,0,1]
    ]
  }
} # GpiosState | New GPIO state

        try:
            # Set Instance GPIOs
            api_response = await api_instance.v1_set_instance_gpios(instance_id, gpios_state)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_set_instance_gpios: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **gpios_state** | [**GpiosState**](GpiosState.md)| New GPIO state | 

### Return type

[**GpiosState**](GpiosState.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current GPIOs State |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_instance_peripherals**
> PeripheralsData v1_set_instance_peripherals(instance_id, peripherals_data)

Set Instance Peripherals

Set Instance Peripherals

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
peripherals_data = {
  "acceleration": [0, 9.81, 0],
  "gyroscope": [0, 0, 0],
  "magnetic": [0, 45, 0],
  "orientation": [0, 0, 0],
  "temperature": 25,
  "proximity": 50,
  "light": 20,
  "pressure": 1013.25,
  "humidity": 55
} # PeripheralsData | New peripherals state

        try:
            # Set Instance Peripherals
            api_response = await api_instance.v1_set_instance_peripherals(instance_id, peripherals_data)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_set_instance_peripherals: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **peripherals_data** | [**PeripheralsData**](PeripheralsData.md)| New peripherals state | 

### Return type

[**PeripheralsData**](PeripheralsData.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current Peripherals State |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_instance_state**
> v1_set_instance_state(instance_id, v1_set_state_body)

Set state of Instance

Set state of Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
v1_set_state_body = corellium_api.V1SetStateBody() # V1SetStateBody | Desired State

        try:
            # Set state of Instance
            api_instance.v1_set_instance_state(instance_id, v1_set_state_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_set_instance_state: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **v1_set_state_body** | [**V1SetStateBody**](V1SetStateBody.md)| Desired State | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_set_snapshot_permissions**
> Snapshot v1_set_snapshot_permissions(snapshot_id, snapshot_permissions_request_payload)

Set member list

Sets the list of members who have access to the snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid
snapshot_permissions_request_payload = {
  "members": [
    "newuser1@domain.com",
    "newuser2@domain.com"
  ]
} # SnapshotPermissionsRequestPayload | 

        try:
            # Set member list
            api_response = await api_instance.v1_set_snapshot_permissions(snapshot_id, snapshot_permissions_request_payload)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_set_snapshot_permissions: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot ID - uuid | 
 **snapshot_permissions_request_payload** | [**SnapshotPermissionsRequestPayload**](SnapshotPermissionsRequestPayload.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_share_snapshot**
> Snapshot v1_share_snapshot(snapshot_id, post_share_snapshot_request_payload)

Share snapshot

Share a snapshot

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid
post_share_snapshot_request_payload = {
  "sharingType": "passwordPublicLink",
  "password": "password"
} # PostShareSnapshotRequestPayload | 

        try:
            # Share snapshot
            api_response = await api_instance.v1_share_snapshot(snapshot_id, post_share_snapshot_request_payload)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_share_snapshot: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot ID - uuid | 
 **post_share_snapshot_request_payload** | [**PostShareSnapshotRequestPayload**](PostShareSnapshotRequestPayload.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_snapshot_rename**
> Snapshot v1_snapshot_rename(snapshot_id, snapshot_creation_options)

Rename a Snapshot

Rename a Snapshot

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid
snapshot_creation_options = corellium_api.SnapshotCreationOptions() # SnapshotCreationOptions | 

        try:
            # Rename a Snapshot
            api_response = await api_instance.v1_snapshot_rename(snapshot_id, snapshot_creation_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_snapshot_rename: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapshot_id** | **str**| Snapshot ID - uuid | 
 **snapshot_creation_options** | [**SnapshotCreationOptions**](SnapshotCreationOptions.md)|  | 

### Return type

[**Snapshot**](Snapshot.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_start_core_trace**
> v1_start_core_trace(instance_id)

Start CoreTrace on an instance

Start CoreTrace on an instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Start CoreTrace on an instance
            api_instance.v1_start_core_trace(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_start_core_trace: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_start_hyper_trace**
> v1_start_hyper_trace(instance_id, btrace_enable_options)

Start HyperTrace on an instance

Start HyperTrace on an instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
btrace_enable_options = corellium_api.BtraceEnableOptions() # BtraceEnableOptions | 

        try:
            # Start HyperTrace on an instance
            api_instance.v1_start_hyper_trace(instance_id, btrace_enable_options)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_start_hyper_trace: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **btrace_enable_options** | [**BtraceEnableOptions**](BtraceEnableOptions.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_start_instance**
> v1_start_instance(instance_id, instance_start_options=instance_start_options)

Start an Instance

Start an Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
instance_start_options = corellium_api.InstanceStartOptions() # InstanceStartOptions | Start options (optional)

        try:
            # Start an Instance
            api_instance.v1_start_instance(instance_id, instance_start_options=instance_start_options)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_start_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **instance_start_options** | [**InstanceStartOptions**](InstanceStartOptions.md)| Start options | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_start_netdump**
> v1_start_netdump(instance_id, netdump_filter=netdump_filter)

Start Enhanced Network Monitor on an instance.

Start Enhanced Network Monitor on an instance.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
netdump_filter = { } # NetdumpFilter |  (optional)

        try:
            # Start Enhanced Network Monitor on an instance.
            api_instance.v1_start_netdump(instance_id, netdump_filter=netdump_filter)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_start_netdump: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **netdump_filter** | [**NetdumpFilter**](NetdumpFilter.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_start_network_monitor**
> v1_start_network_monitor(instance_id, sslsplit_filter=sslsplit_filter)

Start Network Monitor on an instance.

Start Network Monitor on an instance.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
sslsplit_filter = corellium_api.SslsplitFilter() # SslsplitFilter |  (optional)

        try:
            # Start Network Monitor on an instance.
            api_instance.v1_start_network_monitor(instance_id, sslsplit_filter=sslsplit_filter)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_start_network_monitor: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **sslsplit_filter** | [**SslsplitFilter**](SslsplitFilter.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stop_core_trace**
> v1_stop_core_trace(instance_id)

Stop CoreTrace on an instance.

Stop CoreTrace on an instance.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Stop CoreTrace on an instance.
            api_instance.v1_stop_core_trace(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_stop_core_trace: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stop_hyper_trace**
> v1_stop_hyper_trace(instance_id)

Stop HyperTrace on an instance.

Stop HyperTrace on an instance.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Stop HyperTrace on an instance.
            api_instance.v1_stop_hyper_trace(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_stop_hyper_trace: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stop_instance**
> v1_stop_instance(instance_id, instance_stop_options=instance_stop_options)

Stop an Instance

Stop an Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
instance_stop_options = corellium_api.InstanceStopOptions() # InstanceStopOptions | Stop options (optional)

        try:
            # Stop an Instance
            api_instance.v1_stop_instance(instance_id, instance_stop_options=instance_stop_options)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_stop_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **instance_stop_options** | [**InstanceStopOptions**](InstanceStopOptions.md)| Stop options | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stop_netdump**
> v1_stop_netdump(instance_id)

Stop Enhanced Network Monitor on an instance.

Stop Enhanced Network Monitor on an instance.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Stop Enhanced Network Monitor on an instance.
            api_instance.v1_stop_netdump(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_stop_netdump: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_stop_network_monitor**
> v1_stop_network_monitor(instance_id)

Stop Network Monitor on an instance.

Stop Network Monitor on an instance.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Stop Network Monitor on an instance.
            api_instance.v1_stop_network_monitor(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_stop_network_monitor: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_team_change**
> v1_team_change(team_id, create_team)

Update team

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        team_id = 'team_id_example' # str | Team ID - uuid
create_team = { "name": "Test Team"} # CreateTeam | 

        try:
            # Update team
            api_instance.v1_team_change(team_id, create_team)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_team_change: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team ID - uuid | 
 **create_team** | [**CreateTeam**](CreateTeam.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_team_create**
> TeamCreate v1_team_create(create_team)

Create team

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        create_team = { "name": "Test Team"} # CreateTeam | 

        try:
            # Create team
            api_response = await api_instance.v1_team_create(create_team)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_team_create: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_team** | [**CreateTeam**](CreateTeam.md)|  | 

### Return type

[**TeamCreate**](TeamCreate.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_team_delete**
> v1_team_delete(team_id)

Delete team

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        team_id = 'team_id_example' # str | Team ID - uuid

        try:
            # Delete team
            api_instance.v1_team_delete(team_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_team_delete: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| Team ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**403** | Forbidden |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_teams**
> list[Team] v1_teams()

Get teams

This endpoint is available for Enterprise accounts only

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # Get teams
            api_response = await api_instance.v1_teams()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_teams: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Team]**](Team.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Teams |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_unpause_instance**
> v1_unpause_instance(instance_id)

Unpause an Instance

Unpause an Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Unpause an Instance
            api_instance.v1_unpause_instance(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_unpause_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_domain_auth_provider**
> DomainAuthProviderResponse v1_update_domain_auth_provider(domain_id, provider_id, domain_auth_provider_request)

Update an auth provider for a domain

Update an auth provider for a domain

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        domain_id = 'domain_id_example' # str | Domain ID - uuid
provider_id = 'provider_id_example' # str | Provider ID - uuid
domain_auth_provider_request = {
  "enabled": false,
  "providerType": "open-id-connect",
  "label": "Login with Custom Auth0",
  "config": {
    "discoveryUrl": "http://localhost:8080/realms/Corellium/.well-known/openid-configuration",
    "clientId": "B5GhRzrVn19adO1a1vJ6aZRYdNY9jSP4",
    "clientSecret": "itsasecret",
    "invitedOnly": true
  }
} # DomainAuthProviderRequest | Request Data

        try:
            # Update an auth provider for a domain
            api_response = await api_instance.v1_update_domain_auth_provider(domain_id, provider_id, domain_auth_provider_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_domain_auth_provider: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**| Domain ID - uuid | 
 **provider_id** | **str**| Provider ID - uuid | 
 **domain_auth_provider_request** | [**DomainAuthProviderRequest**](DomainAuthProviderRequest.md)| Request Data | 

### Return type

[**DomainAuthProviderResponse**](DomainAuthProviderResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_extension**
> v1_update_extension(extension_id, update_extension)

Update an existing extension

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        extension_id = 'extension_id_example' # str | Extension ID
update_extension = { "enabled": false} # UpdateExtension | application/json

        try:
            # Update an existing extension
            api_instance.v1_update_extension(extension_id, update_extension)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_extension: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_id** | **str**| Extension ID | 
 **update_extension** | [**UpdateExtension**](UpdateExtension.md)| application/json | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_hook**
> Hook v1_update_hook(hook_id, v1_update_hook_parameters)

Update an existing hypervisor hook

Update an existing hypervisor hook

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        hook_id = 'hook_id_example' # str | Hook ID
v1_update_hook_parameters = { "enabled": false} # V1UpdateHookParameters | application/json

        try:
            # Update an existing hypervisor hook
            api_response = await api_instance.v1_update_hook(hook_id, v1_update_hook_parameters)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_hook: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| Hook ID | 
 **v1_update_hook_parameters** | [**V1UpdateHookParameters**](V1UpdateHookParameters.md)| application/json | 

### Return type

[**Hook**](Hook.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Hook |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_network_connection**
> NetworkConnection v1_update_network_connection(id, update_network_connection_options, force=force)

Update Network Connection

You must have the domain administrator role to update a network connection.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        id = 'id_example' # str | Network Connection Identifier - uuid
update_network_connection_options = {
  "type": "openvpn",
  "name": "My Renamed OpenVPN Connection",
  "config": {
    "config": "client\ndev tun\nproto tcp\nremote my-server-1 1194\nresolv-retry infinite\nnobind\npersist-key\npersist-tun\nremote-cert-tls server\ntls-auth ta.key 1\ncipher AES-256-CBC\nverb 3\n"
  }
} # UpdateNetworkConnectionOptions | Network Connection Options
force = True # bool | Force deletion (true only or not present) (optional)

        try:
            # Update Network Connection
            api_response = await api_instance.v1_update_network_connection(id, update_network_connection_options, force=force)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_network_connection: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Network Connection Identifier - uuid | 
 **update_network_connection_options** | [**UpdateNetworkConnectionOptions**](UpdateNetworkConnectionOptions.md)| Network Connection Options | 
 **force** | **bool**| Force deletion (true only or not present) | [optional] 

### Return type

[**NetworkConnection**](NetworkConnection.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_project**
> Project v1_update_project(project_id, project)

Update a Project

Update a Project

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
project = corellium_api.Project() # Project | Updated Project Settings

        try:
            # Update a Project
            api_response = await api_instance.v1_update_project(project_id, project)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_project: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **project** | [**Project**](Project.md)| Updated Project Settings | 

### Return type

[**Project**](Project.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_project_settings**
> v1_update_project_settings(project_id, project_settings)

Change Project Settings

Change Project Settings

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        project_id = 'project_id_example' # str | Project ID - uuid
project_settings = corellium_api.ProjectSettings() # ProjectSettings | New settings

        try:
            # Change Project Settings
            api_instance.v1_update_project_settings(project_id, project_settings)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_project_settings: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Project ID - uuid | 
 **project_settings** | [**ProjectSettings**](ProjectSettings.md)| New settings | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |
**400** | Validation Error |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_user**
> v1_update_user(user_id, user_update)

Update User

Update a user. Fields such as `name`, `label`, `password`, and `clusterAdministrator` can be updated.  Only users with the Cluster Administrator role can set or modify the `clusterAdministrator` flag.

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        user_id = 'user_id_example' # str | userId - uuid
user_update = {
  "name": "test",
  "label": "Project Admin",
  "password": "new-password",
  "clusterAdministrator": true
} # UserUpdate | User data

        try:
            # Update User
            api_instance.v1_update_user(user_id, user_update)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_user: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId - uuid | 
 **user_update** | [**UserUpdate**](UserUpdate.md)| User data | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_upgrade_instance**
> v1_upgrade_instance(instance_id, instance_upgrade_body)

Upgrade iOS version

Upgrade iOS version

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | 
instance_upgrade_body = {
  "os":"16.1",
  "osbuild":"20B79"
} # InstanceUpgradeBody | 

        try:
            # Upgrade iOS version
            api_instance.v1_upgrade_instance(instance_id, instance_upgrade_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_upgrade_instance: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**|  | 
 **instance_upgrade_body** | [**InstanceUpgradeBody**](InstanceUpgradeBody.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_upload_image_data**
> v1_upload_image_data(image_id, body)

Upload Image Data

If the active project has enough remaining quota, updates an Image with the contents of the request body.

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        image_id = 'image_id_example' # str | Image ID - uuid
body = 'body_example' # str | Uploaded Image

        try:
            # Upload Image Data
            api_instance.v1_upload_image_data(image_id, body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_upload_image_data: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image_id** | **str**| Image ID - uuid | 
 **body** | **str**| Uploaded Image | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: binary
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_agree_terms**
> AgreedAck v1_user_agree_terms()

Consent to the current terms and conditions

Consent to the current terms and conditions

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # Consent to the current terms and conditions
            api_response = await api_instance.v1_user_agree_terms()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_user_agree_terms: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AgreedAck**](AgreedAck.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_change_password_post**
> v1_users_change_password_post(password_change_body)

Change User Password

Authenticated solely by the old-password.

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        password_change_body = {
  "user": "<userId>",
  "old-password": "Password1",
  "new-password": "Password2"
} # PasswordChangeBody | 

        try:
            # Change User Password
            api_instance.v1_users_change_password_post(password_change_body)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_users_change_password_post: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_change_body** | [**PasswordChangeBody**](PasswordChangeBody.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Accepted |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_users_login**
> Token v1_users_login(credentials)

Log In

### Example

```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        credentials = {
  "username": "admin",
  "password": "password"
} # Credentials | Authorization data

        try:
            # Log In
            api_response = await api_instance.v1_users_login(credentials)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_users_login: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credentials** | [**Credentials**](Credentials.md)| Authorization data | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User Authorization |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_web_player_allowed_domains**
> v1_web_player_allowed_domains()

Retrieve the list of allowed domains for all Webplayer sessions

Retrieve the list of allowed domains for all Webplayer sessions

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # Retrieve the list of allowed domains for all Webplayer sessions
            api_instance.v1_web_player_allowed_domains()
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_web_player_allowed_domains: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_web_player_create_session**
> WebPlayerSession v1_web_player_create_session(web_player_create_session_request)

Create a new Webplayer Session

Create a new Webplayer Session

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        web_player_create_session_request = {
  "projectId": "0fc719fc-335d-458c-a424-51a550a73d12",
  "instanceId": "fbd94550-3f74-4d46-a6ed-c26cbfb23340",
  "expiresIn": 18000,
  "features": {
    "apps": true,
    "files": true
  }
} # WebPlayerCreateSessionRequest | Request Data

        try:
            # Create a new Webplayer Session
            api_response = await api_instance.v1_web_player_create_session(web_player_create_session_request)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_web_player_create_session: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_player_create_session_request** | [**WebPlayerCreateSessionRequest**](WebPlayerCreateSessionRequest.md)| Request Data | 

### Return type

[**WebPlayerSession**](WebPlayerSession.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_web_player_destroy_session**
> list[str] v1_web_player_destroy_session(session_id)

Tear down a Webplayer Session

Tear down a Webplayer Session

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        session_id = 'session_id_example' # str | Webplayer Session identifier

        try:
            # Tear down a Webplayer Session
            api_response = await api_instance.v1_web_player_destroy_session(session_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_web_player_destroy_session: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Webplayer Session identifier | 

### Return type

**list[str]**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_web_player_list_sessions**
> list[WebPlayerSession] v1_web_player_list_sessions()

List all Webplayer sessions

List all Webplayer sessions

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        
        try:
            # List all Webplayer sessions
            api_response = await api_instance.v1_web_player_list_sessions()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_web_player_list_sessions: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[WebPlayerSession]**](WebPlayerSession.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_web_player_session_info**
> WebPlayerSession v1_web_player_session_info(session_id)

Retrieve Webplayer Session Information

Retrieve Webplayer Session Information

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        session_id = 'session_id_example' # str | Webplayer Session identifier

        try:
            # Retrieve Webplayer Session Information
            api_response = await api_instance.v1_web_player_session_info(session_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_web_player_session_info: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_id** | **str**| Webplayer Session identifier | 

### Return type

[**WebPlayerSession**](WebPlayerSession.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_instance_quick_connect_command**
> str v2_get_instance_quick_connect_command(instance_id)

Recommended SSH Command for Quick Connect

Recommended SSH Command for Quick Connect

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid

        try:
            # Recommended SSH Command for Quick Connect
            api_response = await api_instance.v2_get_instance_quick_connect_command(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v2_get_instance_quick_connect_command: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Quick Connect Command |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v2_get_instance_state**
> InstanceState v2_get_instance_state(instance_id, return_attr=return_attr)

Get state of Instance

Get state of Instance

### Example

* Bearer (ApiToken or JWT) Authentication (BearerAuth):
```python
from __future__ import print_function
import time
import asyncio
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint
# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (ApiToken or JWT): BearerAuth
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'


async def main():
    # Enter a context with an instance of the API client
    async with corellium_api.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = corellium_api.CorelliumApi(api_client)
        instance_id = 'instance_id_example' # str | Instance ID - uuid
return_attr = ['return_attr_example'] # list[str] | The attributes to return. (optional)

        try:
            # Get state of Instance
            api_response = await api_instance.v2_get_instance_state(instance_id, return_attr=return_attr)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v2_get_instance_state: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **return_attr** | [**list[str]**](str.md)| The attributes to return. | [optional] 

### Return type

[**InstanceState**](InstanceState.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Current Instance State |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

