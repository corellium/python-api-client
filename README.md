# corellium-api
REST API to manage your virtual devices.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 7.3.0
- Package version: 0.4.0
- Build package: org.openapitools.codegen.languages.PythonLegacyClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import corellium_api
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import corellium_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://app.corellium.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CorelliumApi* | [**create_assessment**](docs/CorelliumApi.md#create_assessment) | **POST** /v1/services/matrix/{instanceId}/assessments | Create assessment
*CorelliumApi* | [**delete_assessment**](docs/CorelliumApi.md#delete_assessment) | **DELETE** /v1/services/matrix/{instanceId}/assessments/{assessmentId} | Delete assessment
*CorelliumApi* | [**download_report**](docs/CorelliumApi.md#download_report) | **GET** /v1/services/matrix/{instanceId}/assessments/{assessmentId}/download | Download report
*CorelliumApi* | [**get_assessment_by_id**](docs/CorelliumApi.md#get_assessment_by_id) | **GET** /v1/services/matrix/{instanceId}/assessments/{assessmentId} | Get assessment by ID
*CorelliumApi* | [**get_assessments_by_instance_id**](docs/CorelliumApi.md#get_assessments_by_instance_id) | **GET** /v1/services/matrix/{instanceId}/instances/{instanceId}/assessments | Get assessments by instanceId
*CorelliumApi* | [**run_tests**](docs/CorelliumApi.md#run_tests) | **POST** /v1/services/matrix/{instanceId}/assessments/{assessmentId}/test | Update assessment state and execute MATRIX tests
*CorelliumApi* | [**start_monitoring**](docs/CorelliumApi.md#start_monitoring) | **POST** /v1/services/matrix/{instanceId}/assessments/{assessmentId}/start | Update assessment state and begin device monitoring
*CorelliumApi* | [**stop_monitoring**](docs/CorelliumApi.md#stop_monitoring) | **POST** /v1/services/matrix/{instanceId}/assessments/{assessmentId}/stop | Update assessment state and stop device monitoring
*CorelliumApi* | [**v1_accept_shared_snapshot**](docs/CorelliumApi.md#v1_accept_shared_snapshot) | **POST** /v1/snapshots/accept | Accept a snapshot shared with you
*CorelliumApi* | [**v1_activity_export**](docs/CorelliumApi.md#v1_activity_export) | **POST** /v1/activity/export | Start activity export
*CorelliumApi* | [**v1_activity_list**](docs/CorelliumApi.md#v1_activity_list) | **GET** /v1/activity | Get resource activities
*CorelliumApi* | [**v1_add_project_key**](docs/CorelliumApi.md#v1_add_project_key) | **POST** /v1/projects/{projectId}/keys | Add Project Authorized Key
*CorelliumApi* | [**v1_add_team_role_to_project**](docs/CorelliumApi.md#v1_add_team_role_to_project) | **PUT** /v1/roles/projects/{projectId}/teams/{teamId}/roles/{roleId} | Add team role to project
*CorelliumApi* | [**v1_add_user_role_to_project**](docs/CorelliumApi.md#v1_add_user_role_to_project) | **PUT** /v1/roles/projects/{projectId}/users/{userId}/roles/{roleId} | Add user role to project
*CorelliumApi* | [**v1_add_user_to_team**](docs/CorelliumApi.md#v1_add_user_to_team) | **PUT** /v1/teams/{teamId}/users/{userId} | Add user to team
*CorelliumApi* | [**v1_agent_app_ready**](docs/CorelliumApi.md#v1_agent_app_ready) | **GET** /v1/instances/{instanceId}/agent/v1/app/ready | Check if App subsystem is ready
*CorelliumApi* | [**v1_agent_delete_file**](docs/CorelliumApi.md#v1_agent_delete_file) | **DELETE** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Delete a File on VM
*CorelliumApi* | [**v1_agent_get_file**](docs/CorelliumApi.md#v1_agent_get_file) | **GET** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Download a File from VM
*CorelliumApi* | [**v1_agent_get_temp_filename**](docs/CorelliumApi.md#v1_agent_get_temp_filename) | **POST** /v1/instances/{instanceId}/agent/v1/file/temp | Get the path for a new temp file
*CorelliumApi* | [**v1_agent_install_app**](docs/CorelliumApi.md#v1_agent_install_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/install | Install App at path
*CorelliumApi* | [**v1_agent_install_profile**](docs/CorelliumApi.md#v1_agent_install_profile) | **POST** /v1/instances/{instanceId}/agent/v1/profile/install | Install a Profile to VM
*CorelliumApi* | [**v1_agent_kill_app**](docs/CorelliumApi.md#v1_agent_kill_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/apps/{bundleId}/kill | Kill an App
*CorelliumApi* | [**v1_agent_list_app_icons**](docs/CorelliumApi.md#v1_agent_list_app_icons) | **GET** /v1/instances/{instanceId}/agent/v1/app/icons | List App Icons
*CorelliumApi* | [**v1_agent_list_apps**](docs/CorelliumApi.md#v1_agent_list_apps) | **GET** /v1/instances/{instanceId}/agent/v1/app/apps | List Apps
*CorelliumApi* | [**v1_agent_list_apps_status**](docs/CorelliumApi.md#v1_agent_list_apps_status) | **GET** /v1/instances/{instanceId}/agent/v1/app/apps/update | List Apps Status
*CorelliumApi* | [**v1_agent_list_profiles**](docs/CorelliumApi.md#v1_agent_list_profiles) | **GET** /v1/instances/{instanceId}/agent/v1/profile/profiles | List Profiles
*CorelliumApi* | [**v1_agent_run_app**](docs/CorelliumApi.md#v1_agent_run_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/apps/{bundleId}/run | Run an App
*CorelliumApi* | [**v1_agent_set_file_attributes**](docs/CorelliumApi.md#v1_agent_set_file_attributes) | **PATCH** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Change Attrs of a File on VM
*CorelliumApi* | [**v1_agent_system_get_adb_auth**](docs/CorelliumApi.md#v1_agent_system_get_adb_auth) | **GET** /v1/instances/{instanceId}/agent/v1/system/adbauth | Get ADB Auth Setting (AOSP only)
*CorelliumApi* | [**v1_agent_system_get_network**](docs/CorelliumApi.md#v1_agent_system_get_network) | **GET** /v1/instances/{instanceId}/agent/v1/system/network | Get IP of eth0 (AOSP only)
*CorelliumApi* | [**v1_agent_system_get_prop**](docs/CorelliumApi.md#v1_agent_system_get_prop) | **POST** /v1/instances/{instanceId}/agent/v1/system/getprop | Get System Property (AOSP only)
*CorelliumApi* | [**v1_agent_system_install_open_g_apps**](docs/CorelliumApi.md#v1_agent_system_install_open_g_apps) | **POST** /v1/instances/{instanceId}/agent/v1/system/install-opengapps | Install OpenGApps (AOSP only)
*CorelliumApi* | [**v1_agent_system_lock**](docs/CorelliumApi.md#v1_agent_system_lock) | **POST** /v1/instances/{instanceId}/agent/v1/system/lock | Lock Device (iOS Only)
*CorelliumApi* | [**v1_agent_system_set_adb_auth**](docs/CorelliumApi.md#v1_agent_system_set_adb_auth) | **PUT** /v1/instances/{instanceId}/agent/v1/system/adbauth | Set ADB Auth Setting (AOSP only)
*CorelliumApi* | [**v1_agent_system_set_hostname**](docs/CorelliumApi.md#v1_agent_system_set_hostname) | **POST** /v1/instances/{instanceId}/agent/v1/system/setHostname | Set Hostname of instance
*CorelliumApi* | [**v1_agent_system_shutdown**](docs/CorelliumApi.md#v1_agent_system_shutdown) | **POST** /v1/instances/{instanceId}/agent/v1/system/shutdown | Instruct VM to halt
*CorelliumApi* | [**v1_agent_system_unlock**](docs/CorelliumApi.md#v1_agent_system_unlock) | **POST** /v1/instances/{instanceId}/agent/v1/system/unlock | Unlock Device (iOS Only)
*CorelliumApi* | [**v1_agent_uninstall_app**](docs/CorelliumApi.md#v1_agent_uninstall_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/apps/{bundleId}/uninstall | Uninstall an App
*CorelliumApi* | [**v1_agent_uninstall_profile**](docs/CorelliumApi.md#v1_agent_uninstall_profile) | **DELETE** /v1/instances/{instanceId}/agent/v1/profile/profiles/{profileId} | Uninstall a Profile from VM
*CorelliumApi* | [**v1_agent_upload_file**](docs/CorelliumApi.md#v1_agent_upload_file) | **PUT** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Upload a file to VM
*CorelliumApi* | [**v1_auth_login**](docs/CorelliumApi.md#v1_auth_login) | **POST** /v1/auth/login | Log In
*CorelliumApi* | [**v1_btrace_preauthorize**](docs/CorelliumApi.md#v1_btrace_preauthorize) | **GET** /v1/instances/{instanceId}/btrace-authorize | Pre-authorize an btrace download
*CorelliumApi* | [**v1_check_subdomain_existence**](docs/CorelliumApi.md#v1_check_subdomain_existence) | **POST** /v1/domain/check | Check the existence of a subdomain
*CorelliumApi* | [**v1_clear_core_trace**](docs/CorelliumApi.md#v1_clear_core_trace) | **DELETE** /v1/instances/{instanceId}/strace | Clear CoreTrace logs
*CorelliumApi* | [**v1_clear_hyper_trace**](docs/CorelliumApi.md#v1_clear_hyper_trace) | **DELETE** /v1/instances/{instanceId}/btrace | Clear HyperTrace logs
*CorelliumApi* | [**v1_clear_hyper_trace_hooks**](docs/CorelliumApi.md#v1_clear_hyper_trace_hooks) | **POST** /v1/instances/{instanceId}/hooks/clear | Clear Hooks on an instance
*CorelliumApi* | [**v1_clear_instance_panics**](docs/CorelliumApi.md#v1_clear_instance_panics) | **DELETE** /v1/instances/{instanceId}/panics | Clear Panics
*CorelliumApi* | [**v1_create_domain_auth_provider**](docs/CorelliumApi.md#v1_create_domain_auth_provider) | **POST** /v1/domain/{domainId}/auth | Create a new auth provider for a domain
*CorelliumApi* | [**v1_create_hook**](docs/CorelliumApi.md#v1_create_hook) | **POST** /v1/instances/{instanceId}/hooks | Create hypervisor hook for Instance
*CorelliumApi* | [**v1_create_image**](docs/CorelliumApi.md#v1_create_image) | **POST** /v1/images | Create a new Image
*CorelliumApi* | [**v1_create_instance**](docs/CorelliumApi.md#v1_create_instance) | **POST** /v1/instances | Create Instance
*CorelliumApi* | [**v1_create_network_connection**](docs/CorelliumApi.md#v1_create_network_connection) | **POST** /v1/network/connections | Create a new Network Connection
*CorelliumApi* | [**v1_create_project**](docs/CorelliumApi.md#v1_create_project) | **POST** /v1/projects | Create a Project
*CorelliumApi* | [**v1_create_snapshot**](docs/CorelliumApi.md#v1_create_snapshot) | **POST** /v1/instances/{instanceId}/snapshots | Create Instance Snapshot
*CorelliumApi* | [**v1_create_user**](docs/CorelliumApi.md#v1_create_user) | **POST** /v1/users | Create User
*CorelliumApi* | [**v1_delete_domain_auth_provider**](docs/CorelliumApi.md#v1_delete_domain_auth_provider) | **DELETE** /v1/domain/{domainId}/auth/{providerId} | Delete an auth provider from a domain
*CorelliumApi* | [**v1_delete_hook**](docs/CorelliumApi.md#v1_delete_hook) | **DELETE** /v1/hooks/{hookId} | Delete an existing hypervisor hook
*CorelliumApi* | [**v1_delete_image**](docs/CorelliumApi.md#v1_delete_image) | **DELETE** /v2/images/{imageId} | Delete Image
*CorelliumApi* | [**v1_delete_instance**](docs/CorelliumApi.md#v1_delete_instance) | **DELETE** /v1/instances/{instanceId} | Remove Instance
*CorelliumApi* | [**v1_delete_instance_snapshot**](docs/CorelliumApi.md#v1_delete_instance_snapshot) | **DELETE** /v1/instances/{instanceId}/snapshots/{snapshotId} | Delete an Instance Snapshot
*CorelliumApi* | [**v1_delete_network_connection**](docs/CorelliumApi.md#v1_delete_network_connection) | **DELETE** /v1/network/connections/{id} | Delete an existing Network Connection
*CorelliumApi* | [**v1_delete_project**](docs/CorelliumApi.md#v1_delete_project) | **DELETE** /v1/projects/{projectId} | Delete a Project
*CorelliumApi* | [**v1_delete_snapshot**](docs/CorelliumApi.md#v1_delete_snapshot) | **DELETE** /v1/snapshots/{snapshotId} | Delete a Snapshot
*CorelliumApi* | [**v1_delete_snapshot_permissions**](docs/CorelliumApi.md#v1_delete_snapshot_permissions) | **DELETE** /v1/snapshots/{snapshotId}/permissions | Delete member(s)
*CorelliumApi* | [**v1_delete_user**](docs/CorelliumApi.md#v1_delete_user) | **DELETE** /v1/users/{userId} | Delete User
*CorelliumApi* | [**v1_disable_expose_port**](docs/CorelliumApi.md#v1_disable_expose_port) | **POST** /v1/instances/{instanceId}/exposeport/disable | Disable an exposed port on an instance for device access.
*CorelliumApi* | [**v1_download_activity**](docs/CorelliumApi.md#v1_download_activity) | **GET** /v1/activity/export/{taskId}/download | Download activity
*CorelliumApi* | [**v1_enable_expose_port**](docs/CorelliumApi.md#v1_enable_expose_port) | **POST** /v1/instances/{instanceId}/exposeport/enable | Enable an exposed port on an instance for device access.
*CorelliumApi* | [**v1_execute_hyper_trace_hooks**](docs/CorelliumApi.md#v1_execute_hyper_trace_hooks) | **POST** /v1/instances/{instanceId}/hooks/execute | Execute Hooks on an instance
*CorelliumApi* | [**v1_get_activity_export_status**](docs/CorelliumApi.md#v1_get_activity_export_status) | **GET** /v1/activity/export/{taskId} | Get export task status
*CorelliumApi* | [**v1_get_activity_export_tasks**](docs/CorelliumApi.md#v1_get_activity_export_tasks) | **GET** /v1/activity/export | Get all export tasks for user
*CorelliumApi* | [**v1_get_config**](docs/CorelliumApi.md#v1_get_config) | **GET** /v1/config | Get all configs
*CorelliumApi* | [**v1_get_domain_auth_providers**](docs/CorelliumApi.md#v1_get_domain_auth_providers) | **GET** /v1/domain/{domainId}/auth | Return all configured auth providers for a domain (including globally configured providers)
*CorelliumApi* | [**v1_get_hook_by_id**](docs/CorelliumApi.md#v1_get_hook_by_id) | **GET** /v1/hooks/{hookId} | Get hypervisor hook by id
*CorelliumApi* | [**v1_get_hooks**](docs/CorelliumApi.md#v1_get_hooks) | **GET** /v1/instances/{instanceId}/hooks | Get all hypervisor hooks for Instance
*CorelliumApi* | [**v1_get_image**](docs/CorelliumApi.md#v1_get_image) | **GET** /v1/images/{imageId} | Get Image Metadata
*CorelliumApi* | [**v1_get_images**](docs/CorelliumApi.md#v1_get_images) | **GET** /v1/images | Get all Images Metadata
*CorelliumApi* | [**v1_get_instance**](docs/CorelliumApi.md#v1_get_instance) | **GET** /v1/instances/{instanceId} | Get Instance
*CorelliumApi* | [**v1_get_instance_console**](docs/CorelliumApi.md#v1_get_instance_console) | **GET** /v1/instances/{instanceId}/console | Get console websocket URL
*CorelliumApi* | [**v1_get_instance_console_log**](docs/CorelliumApi.md#v1_get_instance_console_log) | **GET** /v1/instances/{instanceId}/consoleLog | Get Console Log
*CorelliumApi* | [**v1_get_instance_gpios**](docs/CorelliumApi.md#v1_get_instance_gpios) | **GET** /v1/instances/{instanceId}/gpios | Get Instance GPIOs
*CorelliumApi* | [**v1_get_instance_panics**](docs/CorelliumApi.md#v1_get_instance_panics) | **GET** /v1/instances/{instanceId}/panics | Get Panics
*CorelliumApi* | [**v1_get_instance_peripherals**](docs/CorelliumApi.md#v1_get_instance_peripherals) | **GET** /v1/instances/{instanceId}/peripherals | Get Instance Peripherals
*CorelliumApi* | [**v1_get_instance_screenshot**](docs/CorelliumApi.md#v1_get_instance_screenshot) | **GET** /v1/instances/{instanceId}/screenshot.{format} | Get Instance Screenshot
*CorelliumApi* | [**v1_get_instance_snapshot**](docs/CorelliumApi.md#v1_get_instance_snapshot) | **GET** /v1/instances/{instanceId}/snapshots/{snapshotId} | Get Instance Snapshot
*CorelliumApi* | [**v1_get_instance_snapshots**](docs/CorelliumApi.md#v1_get_instance_snapshots) | **GET** /v1/instances/{instanceId}/snapshots | Get Instance Snapshots
*CorelliumApi* | [**v1_get_instances**](docs/CorelliumApi.md#v1_get_instances) | **GET** /v1/instances | Get Instances
*CorelliumApi* | [**v1_get_model_software**](docs/CorelliumApi.md#v1_get_model_software) | **GET** /v1/models/{model}/software | Get Software for Model
*CorelliumApi* | [**v1_get_models**](docs/CorelliumApi.md#v1_get_models) | **GET** /v1/models | Get Supported Models
*CorelliumApi* | [**v1_get_network_connection**](docs/CorelliumApi.md#v1_get_network_connection) | **GET** /v1/network/connections/{id} | Return the configuration and per project statuses for a single network provider.
*CorelliumApi* | [**v1_get_project**](docs/CorelliumApi.md#v1_get_project) | **GET** /v1/projects/{projectId} | Get a Project
*CorelliumApi* | [**v1_get_project_instances**](docs/CorelliumApi.md#v1_get_project_instances) | **GET** /v1/projects/{projectId}/instances | Get Instances in Project
*CorelliumApi* | [**v1_get_project_keys**](docs/CorelliumApi.md#v1_get_project_keys) | **GET** /v1/projects/{projectId}/keys | Get Project Authorized Keys
*CorelliumApi* | [**v1_get_project_network_log**](docs/CorelliumApi.md#v1_get_project_network_log) | **GET** /v1/projects/{projectId}/network/log | Retrieve the network connection log for a project
*CorelliumApi* | [**v1_get_project_network_status**](docs/CorelliumApi.md#v1_get_project_network_status) | **GET** /v1/projects/{projectId}/network/status | Retrieve the network connection status for a project
*CorelliumApi* | [**v1_get_project_vpn_config**](docs/CorelliumApi.md#v1_get_project_vpn_config) | **GET** /v1/projects/{projectId}/vpnconfig/{format} | Get Project VPN Configuration
*CorelliumApi* | [**v1_get_projects**](docs/CorelliumApi.md#v1_get_projects) | **GET** /v1/projects | Get Projects
*CorelliumApi* | [**v1_get_reset_link_info**](docs/CorelliumApi.md#v1_get_reset_link_info) | **GET** /v1/users/reset-link-info | Send Password Reset Link Info
*CorelliumApi* | [**v1_get_service_provider_metadata**](docs/CorelliumApi.md#v1_get_service_provider_metadata) | **GET** /v1/auth/providers/:providerId/spmetadata | Get service provider metadata xml from an auth provider
*CorelliumApi* | [**v1_get_shared_snapshots**](docs/CorelliumApi.md#v1_get_shared_snapshots) | **GET** /v1/snapshots/shared | Fetch shared snapshots
*CorelliumApi* | [**v1_get_snapshot**](docs/CorelliumApi.md#v1_get_snapshot) | **GET** /v1/snapshots/{snapshotId} | Get Snapshot
*CorelliumApi* | [**v1_instances_instance_id_message_post**](docs/CorelliumApi.md#v1_instances_instance_id_message_post) | **POST** /v1/instances/{instanceId}/message | Inject a message into an iOS VM
*CorelliumApi* | [**v1_instances_instance_id_netdump_pcap_get**](docs/CorelliumApi.md#v1_instances_instance_id_netdump_pcap_get) | **GET** /v1/instances/{instanceId}/netdump.pcap | Download a netdump pcap file
*CorelliumApi* | [**v1_instances_instance_id_network_monitor_pcap_get**](docs/CorelliumApi.md#v1_instances_instance_id_network_monitor_pcap_get) | **GET** /v1/instances/{instanceId}/networkMonitor.pcap | Download a Network Monitor pcap file
*CorelliumApi* | [**v1_kcrange**](docs/CorelliumApi.md#v1_kcrange) | **GET** /v1/instances/{instanceId}/btrace-kcrange | Get Kernel extension ranges
*CorelliumApi* | [**v1_list_network_connections**](docs/CorelliumApi.md#v1_list_network_connections) | **GET** /v1/network/connections | List available network connections
*CorelliumApi* | [**v1_list_network_interfaces**](docs/CorelliumApi.md#v1_list_network_interfaces) | **GET** /v1/network/interfaces | List available physical network interfaces
*CorelliumApi* | [**v1_list_network_providers**](docs/CorelliumApi.md#v1_list_network_providers) | **GET** /v1/network/providers | List available network providers
*CorelliumApi* | [**v1_list_threads**](docs/CorelliumApi.md#v1_list_threads) | **GET** /v1/instances/{instanceId}/strace/thread-list | Get Running Threads (CoreTrace)
*CorelliumApi* | [**v1_media_play**](docs/CorelliumApi.md#v1_media_play) | **POST** /v1/instances/{instanceId}/media/play | Start playing media
*CorelliumApi* | [**v1_media_stop**](docs/CorelliumApi.md#v1_media_stop) | **POST** /v1/instances/{instanceId}/media/stop | Stop playing media
*CorelliumApi* | [**v1_partial_update_network_connection**](docs/CorelliumApi.md#v1_partial_update_network_connection) | **PATCH** /v1/network/connections/{id} | Update Network Connection (partial)
*CorelliumApi* | [**v1_patch_instance**](docs/CorelliumApi.md#v1_patch_instance) | **PATCH** /v1/instances/{instanceId} | Update Instance
*CorelliumApi* | [**v1_pause_instance**](docs/CorelliumApi.md#v1_pause_instance) | **POST** /v1/instances/{instanceId}/pause | Pause an Instance
*CorelliumApi* | [**v1_post_instance_input**](docs/CorelliumApi.md#v1_post_instance_input) | **POST** /v1/instances/{instanceId}/input | Provide Instance Input
*CorelliumApi* | [**v1_ready**](docs/CorelliumApi.md#v1_ready) | **GET** /v1/ready | API Status
*CorelliumApi* | [**v1_reboot_instance**](docs/CorelliumApi.md#v1_reboot_instance) | **POST** /v1/instances/{instanceId}/reboot | Reboot an Instance
*CorelliumApi* | [**v1_remove_project_key**](docs/CorelliumApi.md#v1_remove_project_key) | **DELETE** /v1/projects/{projectId}/keys/{keyId} | Delete Project Authorized Key
*CorelliumApi* | [**v1_remove_team_role_from_project**](docs/CorelliumApi.md#v1_remove_team_role_from_project) | **DELETE** /v1/roles/projects/{projectId}/teams/{teamId}/roles/{roleId} | Remove team role from project
*CorelliumApi* | [**v1_remove_user_from_team**](docs/CorelliumApi.md#v1_remove_user_from_team) | **DELETE** /v1/teams/{teamId}/users/{userId} | Remove user from team
*CorelliumApi* | [**v1_remove_user_role_from_project**](docs/CorelliumApi.md#v1_remove_user_role_from_project) | **DELETE** /v1/roles/projects/{projectId}/users/{userId}/roles/{roleId} | Remove user role from project
*CorelliumApi* | [**v1_rename_instance_snapshot**](docs/CorelliumApi.md#v1_rename_instance_snapshot) | **PATCH** /v1/instances/{instanceId}/snapshots/{snapshotId} | Rename an Instance Snapshot
*CorelliumApi* | [**v1_reset_user_password**](docs/CorelliumApi.md#v1_reset_user_password) | **POST** /v1/users/reset-password | Reset User Password
*CorelliumApi* | [**v1_restore_backup**](docs/CorelliumApi.md#v1_restore_backup) | **POST** /v1/instances/{instanceId}/restoreBackup | Restore backup
*CorelliumApi* | [**v1_restore_instance_snapshot**](docs/CorelliumApi.md#v1_restore_instance_snapshot) | **POST** /v1/instances/{instanceId}/snapshots/{snapshotId}/restore | Restore an Instance Snapshot
*CorelliumApi* | [**v1_roles**](docs/CorelliumApi.md#v1_roles) | **GET** /v1/roles | Get all roles
*CorelliumApi* | [**v1_rotate_instance**](docs/CorelliumApi.md#v1_rotate_instance) | **POST** /v1/instances/{instanceId}/rotate | Rotate device to specified orientation
*CorelliumApi* | [**v1_send_user_reset_link**](docs/CorelliumApi.md#v1_send_user_reset_link) | **POST** /v1/users/send-reset-link | Send Password Reset Link
*CorelliumApi* | [**v1_set_instance_gpios**](docs/CorelliumApi.md#v1_set_instance_gpios) | **PUT** /v1/instances/{instanceId}/gpios | Set Instance GPIOs
*CorelliumApi* | [**v1_set_instance_peripherals**](docs/CorelliumApi.md#v1_set_instance_peripherals) | **PUT** /v1/instances/{instanceId}/peripherals | Set Instance Peripherals
*CorelliumApi* | [**v1_set_instance_state**](docs/CorelliumApi.md#v1_set_instance_state) | **PUT** /v1/instances/{instanceId}/state | Set state of Instance
*CorelliumApi* | [**v1_set_snapshot_permissions**](docs/CorelliumApi.md#v1_set_snapshot_permissions) | **POST** /v1/snapshots/{snapshotId}/permissions | Set member list
*CorelliumApi* | [**v1_share_snapshot**](docs/CorelliumApi.md#v1_share_snapshot) | **POST** /v1/snapshots/{snapshotId}/share | Share snapshot
*CorelliumApi* | [**v1_snapshot_rename**](docs/CorelliumApi.md#v1_snapshot_rename) | **PATCH** /v1/snapshots/{snapshotId} | Rename a Snapshot
*CorelliumApi* | [**v1_start_core_trace**](docs/CorelliumApi.md#v1_start_core_trace) | **POST** /v1/instances/{instanceId}/strace/enable | Start CoreTrace on an instance
*CorelliumApi* | [**v1_start_hyper_trace**](docs/CorelliumApi.md#v1_start_hyper_trace) | **POST** /v1/instances/{instanceId}/btrace/enable | Start HyperTrace on an instance
*CorelliumApi* | [**v1_start_instance**](docs/CorelliumApi.md#v1_start_instance) | **POST** /v1/instances/{instanceId}/start | Start an Instance
*CorelliumApi* | [**v1_start_netdump**](docs/CorelliumApi.md#v1_start_netdump) | **POST** /v1/instances/{instanceId}/netdump/enable | Start Enhanced Network Monitor on an instance.
*CorelliumApi* | [**v1_start_network_monitor**](docs/CorelliumApi.md#v1_start_network_monitor) | **POST** /v1/instances/{instanceId}/sslsplit/enable | Start Network Monitor on an instance.
*CorelliumApi* | [**v1_stop_core_trace**](docs/CorelliumApi.md#v1_stop_core_trace) | **POST** /v1/instances/{instanceId}/strace/disable | Stop CoreTrace on an instance.
*CorelliumApi* | [**v1_stop_hyper_trace**](docs/CorelliumApi.md#v1_stop_hyper_trace) | **POST** /v1/instances/{instanceId}/btrace/disable | Stop HyperTrace on an instance.
*CorelliumApi* | [**v1_stop_instance**](docs/CorelliumApi.md#v1_stop_instance) | **POST** /v1/instances/{instanceId}/stop | Stop an Instance
*CorelliumApi* | [**v1_stop_netdump**](docs/CorelliumApi.md#v1_stop_netdump) | **POST** /v1/instances/{instanceId}/netdump/disable | Stop Enhanced Network Monitor on an instance.
*CorelliumApi* | [**v1_stop_network_monitor**](docs/CorelliumApi.md#v1_stop_network_monitor) | **POST** /v1/instances/{instanceId}/sslsplit/disable | Stop Network Monitor on an instance.
*CorelliumApi* | [**v1_team_change**](docs/CorelliumApi.md#v1_team_change) | **PATCH** /v1/teams/{teamId} | Update team
*CorelliumApi* | [**v1_team_create**](docs/CorelliumApi.md#v1_team_create) | **POST** /v1/teams | Create team
*CorelliumApi* | [**v1_team_delete**](docs/CorelliumApi.md#v1_team_delete) | **DELETE** /v1/teams/{teamId} | Delete team
*CorelliumApi* | [**v1_teams**](docs/CorelliumApi.md#v1_teams) | **GET** /v1/teams | Get teams
*CorelliumApi* | [**v1_unpause_instance**](docs/CorelliumApi.md#v1_unpause_instance) | **POST** /v1/instances/{instanceId}/unpause | Unpause an Instance
*CorelliumApi* | [**v1_update_domain_auth_provider**](docs/CorelliumApi.md#v1_update_domain_auth_provider) | **PUT** /v1/domain/{domainId}/auth/{providerId} | Update an auth provider for a domain
*CorelliumApi* | [**v1_update_hook**](docs/CorelliumApi.md#v1_update_hook) | **PUT** /v1/hooks/{hookId} | Update an existing hypervisor hook
*CorelliumApi* | [**v1_update_network_connection**](docs/CorelliumApi.md#v1_update_network_connection) | **PUT** /v1/network/connections/{id} | Update Network Connection
*CorelliumApi* | [**v1_update_project**](docs/CorelliumApi.md#v1_update_project) | **PATCH** /v1/projects/{projectId} | Update a Project
*CorelliumApi* | [**v1_update_project_settings**](docs/CorelliumApi.md#v1_update_project_settings) | **PATCH** /v1/projects/{projectId}/settings | Change Project Settings
*CorelliumApi* | [**v1_update_user**](docs/CorelliumApi.md#v1_update_user) | **PATCH** /v1/users/{userId} | Update User
*CorelliumApi* | [**v1_upgrade_instance**](docs/CorelliumApi.md#v1_upgrade_instance) | **POST** /v1/instances/{instanceId}/upgrade | Upgrade iOS version
*CorelliumApi* | [**v1_upload_image_data**](docs/CorelliumApi.md#v1_upload_image_data) | **POST** /v1/images/{imageId} | Upload Image Data
*CorelliumApi* | [**v1_user_agree_terms**](docs/CorelliumApi.md#v1_user_agree_terms) | **POST** /v1/users/agree | Consent to the current terms and conditions
*CorelliumApi* | [**v1_users_change_password_post**](docs/CorelliumApi.md#v1_users_change_password_post) | **POST** /v1/users/change-password | Change User Password
*CorelliumApi* | [**v1_users_login**](docs/CorelliumApi.md#v1_users_login) | **POST** /v1/users/login | Log In
*CorelliumApi* | [**v1_web_player_allowed_domains**](docs/CorelliumApi.md#v1_web_player_allowed_domains) | **GET** /v1/webplayer/allowedDomains | Retrieve the list of allowed domains for all Webplayer sessions
*CorelliumApi* | [**v1_web_player_create_session**](docs/CorelliumApi.md#v1_web_player_create_session) | **POST** /v1/webplayer | Create a new Webplayer Session
*CorelliumApi* | [**v1_web_player_destroy_session**](docs/CorelliumApi.md#v1_web_player_destroy_session) | **DELETE** /v1/webplayer/{sessionId} | Tear down a Webplayer Session
*CorelliumApi* | [**v1_web_player_list_sessions**](docs/CorelliumApi.md#v1_web_player_list_sessions) | **GET** /v1/webplayer | List all Webplayer sessions
*CorelliumApi* | [**v1_web_player_session_info**](docs/CorelliumApi.md#v1_web_player_session_info) | **GET** /v1/webplayer/{sessionId} | Retrieve Webplayer Session Information
*CorelliumApi* | [**v2_get_instance_quick_connect_command**](docs/CorelliumApi.md#v2_get_instance_quick_connect_command) | **GET** /v2/instances/{instanceId}/quickConnectCommand | Recommended SSH Command for Quick Connect
*CorelliumApi* | [**v2_get_instance_state**](docs/CorelliumApi.md#v2_get_instance_state) | **GET** /v2/instances/{instanceId}/state | Get state of Instance


## Documentation For Models

 - [Activity](docs/Activity.md)
 - [ActivityExportDto](docs/ActivityExportDto.md)
 - [ActivityExportResponse](docs/ActivityExportResponse.md)
 - [ActivityList](docs/ActivityList.md)
 - [ActivityRequest](docs/ActivityRequest.md)
 - [Address](docs/Address.md)
 - [AgentApp](docs/AgentApp.md)
 - [AgentAppReadyResponse](docs/AgentAppReadyResponse.md)
 - [AgentAppStatus](docs/AgentAppStatus.md)
 - [AgentAppsList](docs/AgentAppsList.md)
 - [AgentAppsStatusList](docs/AgentAppsStatusList.md)
 - [AgentError](docs/AgentError.md)
 - [AgentIcons](docs/AgentIcons.md)
 - [AgentInstallBody](docs/AgentInstallBody.md)
 - [AgentProfilesReturn](docs/AgentProfilesReturn.md)
 - [AgentSystemAdbAuth](docs/AgentSystemAdbAuth.md)
 - [AgentSystemGetPropBody](docs/AgentSystemGetPropBody.md)
 - [AgentSystemSetHostnameBody](docs/AgentSystemSetHostnameBody.md)
 - [AgentValueReturn](docs/AgentValueReturn.md)
 - [AgreedAck](docs/AgreedAck.md)
 - [ApiConflictError](docs/ApiConflictError.md)
 - [ApiError](docs/ApiError.md)
 - [ApiInternalConsistencyError](docs/ApiInternalConsistencyError.md)
 - [ApiNotFoundError](docs/ApiNotFoundError.md)
 - [ApiToken](docs/ApiToken.md)
 - [Assessment](docs/Assessment.md)
 - [AssessmentIdStatus](docs/AssessmentIdStatus.md)
 - [AuthProvider](docs/AuthProvider.md)
 - [Bit](docs/Bit.md)
 - [BtraceEnableOptions](docs/BtraceEnableOptions.md)
 - [Button](docs/Button.md)
 - [CheckSubdomainResponse](docs/CheckSubdomainResponse.md)
 - [ConfigResponse](docs/ConfigResponse.md)
 - [ConfigResponseMaintenance](docs/ConfigResponseMaintenance.md)
 - [CouponOptions](docs/CouponOptions.md)
 - [CreateAssessmentDto](docs/CreateAssessmentDto.md)
 - [CreateNetworkConnectionOptions](docs/CreateNetworkConnectionOptions.md)
 - [CreateTeam](docs/CreateTeam.md)
 - [CreatedBy](docs/CreatedBy.md)
 - [Credentials](docs/Credentials.md)
 - [DomainAuthProviderRequest](docs/DomainAuthProviderRequest.md)
 - [DomainAuthProviderResponse](docs/DomainAuthProviderResponse.md)
 - [DomainOptions](docs/DomainOptions.md)
 - [Extension](docs/Extension.md)
 - [Features](docs/Features.md)
 - [FileChanges](docs/FileChanges.md)
 - [Firmware](docs/Firmware.md)
 - [GetAssessmentsByInstanceId500Response](docs/GetAssessmentsByInstanceId500Response.md)
 - [GpioStateDefinition](docs/GpioStateDefinition.md)
 - [GpiosState](docs/GpiosState.md)
 - [GrantTrialRequestResponse](docs/GrantTrialRequestResponse.md)
 - [Hook](docs/Hook.md)
 - [Image](docs/Image.md)
 - [InputResponse](docs/InputResponse.md)
 - [Instance](docs/Instance.md)
 - [InstanceAgentState](docs/InstanceAgentState.md)
 - [InstanceBootOptions](docs/InstanceBootOptions.md)
 - [InstanceBootOptionsAdditionalTag](docs/InstanceBootOptionsAdditionalTag.md)
 - [InstanceConsoleEndpoint](docs/InstanceConsoleEndpoint.md)
 - [InstanceCreateOptions](docs/InstanceCreateOptions.md)
 - [InstanceInput](docs/InstanceInput.md)
 - [InstanceNetdumpState](docs/InstanceNetdumpState.md)
 - [InstanceNetmonState](docs/InstanceNetmonState.md)
 - [InstanceReturn](docs/InstanceReturn.md)
 - [InstanceServices](docs/InstanceServices.md)
 - [InstanceStartOptions](docs/InstanceStartOptions.md)
 - [InstanceState](docs/InstanceState.md)
 - [InstanceStopOptions](docs/InstanceStopOptions.md)
 - [InstanceUpgradeBody](docs/InstanceUpgradeBody.md)
 - [Invitation](docs/Invitation.md)
 - [InviteRevokeParams](docs/InviteRevokeParams.md)
 - [InviteRevokeParamsIds](docs/InviteRevokeParamsIds.md)
 - [Kcrange](docs/Kcrange.md)
 - [KernelTask](docs/KernelTask.md)
 - [KernelThread](docs/KernelThread.md)
 - [Logging](docs/Logging.md)
 - [Maintenance](docs/Maintenance.md)
 - [MediaPlayBody](docs/MediaPlayBody.md)
 - [MeteredSubscriptionUsage](docs/MeteredSubscriptionUsage.md)
 - [Model](docs/Model.md)
 - [ModelSoftware](docs/ModelSoftware.md)
 - [NetdumpFilter](docs/NetdumpFilter.md)
 - [NetworkConnection](docs/NetworkConnection.md)
 - [NetworkConnectionOffsetPaginationResult](docs/NetworkConnectionOffsetPaginationResult.md)
 - [NetworkConnectionProvider](docs/NetworkConnectionProvider.md)
 - [NetworkConnectionProviderOffsetPaginationResult](docs/NetworkConnectionProviderOffsetPaginationResult.md)
 - [NetworkStatusResponse](docs/NetworkStatusResponse.md)
 - [OpenIDConfig](docs/OpenIDConfig.md)
 - [Pagination](docs/Pagination.md)
 - [PasswordChangeBody](docs/PasswordChangeBody.md)
 - [PasswordResetBody](docs/PasswordResetBody.md)
 - [PatchInstanceOptions](docs/PatchInstanceOptions.md)
 - [PeripheralsData](docs/PeripheralsData.md)
 - [Plan](docs/Plan.md)
 - [PostShareSnapshotRequestPayload](docs/PostShareSnapshotRequestPayload.md)
 - [Project](docs/Project.md)
 - [ProjectKey](docs/ProjectKey.md)
 - [ProjectNetworkState](docs/ProjectNetworkState.md)
 - [ProjectQuota](docs/ProjectQuota.md)
 - [ProjectSettings](docs/ProjectSettings.md)
 - [ProjectUsage](docs/ProjectUsage.md)
 - [ProxyConfig](docs/ProxyConfig.md)
 - [ResetLinkBody](docs/ResetLinkBody.md)
 - [Role](docs/Role.md)
 - [RotateBody](docs/RotateBody.md)
 - [SharedSnapshotsInfo](docs/SharedSnapshotsInfo.md)
 - [Snapshot](docs/Snapshot.md)
 - [SnapshotCreationOptions](docs/SnapshotCreationOptions.md)
 - [SnapshotMember](docs/SnapshotMember.md)
 - [SnapshotOwner](docs/SnapshotOwner.md)
 - [SnapshotPermissionsRequestPayload](docs/SnapshotPermissionsRequestPayload.md)
 - [SnapshotSharing](docs/SnapshotSharing.md)
 - [SnapshotSharingPermissions](docs/SnapshotSharingPermissions.md)
 - [SnapshotStatus](docs/SnapshotStatus.md)
 - [SslsplitFilter](docs/SslsplitFilter.md)
 - [SubscriberInvite](docs/SubscriberInvite.md)
 - [Team](docs/Team.md)
 - [TeamCreate](docs/TeamCreate.md)
 - [TestAssessmentDto](docs/TestAssessmentDto.md)
 - [TextInput](docs/TextInput.md)
 - [Token](docs/Token.md)
 - [TouchCurveInput](docs/TouchCurveInput.md)
 - [TouchInput](docs/TouchInput.md)
 - [TouchInputButtonsInner](docs/TouchInputButtonsInner.md)
 - [Trial](docs/Trial.md)
 - [TrialExtension](docs/TrialExtension.md)
 - [TrialRequestMetadata](docs/TrialRequestMetadata.md)
 - [TrialRequestOptions](docs/TrialRequestOptions.md)
 - [UpdateAssessmentDto](docs/UpdateAssessmentDto.md)
 - [UpdateExtension](docs/UpdateExtension.md)
 - [UpdateNetworkConnectionOptions](docs/UpdateNetworkConnectionOptions.md)
 - [User](docs/User.md)
 - [UserError](docs/UserError.md)
 - [UserSnapshots](docs/UserSnapshots.md)
 - [V1CheckSubdomainExistenceParameters](docs/V1CheckSubdomainExistenceParameters.md)
 - [V1CreateHookParameters](docs/V1CreateHookParameters.md)
 - [V1LoadExtensionParameters](docs/V1LoadExtensionParameters.md)
 - [V1SetStateBody](docs/V1SetStateBody.md)
 - [ValidationError](docs/ValidationError.md)
 - [VolumeOptions](docs/VolumeOptions.md)
 - [VpnDefinition](docs/VpnDefinition.md)
 - [WebPlayerCreateSessionRequest](docs/WebPlayerCreateSessionRequest.md)
 - [WebPlayerSession](docs/WebPlayerSession.md)


## Documentation For Authorization


## BearerAuth

- **Type**: Bearer authentication (ApiToken or JWT)


## Author




