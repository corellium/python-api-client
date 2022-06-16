# corellium_api.CorelliumApi

All URIs are relative to *https://app.corellium.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_add_project_key**](CorelliumApi.md#v1_add_project_key) | **POST** /v1/projects/{projectId}/keys | Add Project Authorized Key
[**v1_agent_app_ready**](CorelliumApi.md#v1_agent_app_ready) | **GET** /v1/instances/{instanceId}/agent/v1/app/ready | Check if App subsystem is ready
[**v1_agent_delete_file**](CorelliumApi.md#v1_agent_delete_file) | **DELETE** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Delete a File on VM
[**v1_agent_get_file**](CorelliumApi.md#v1_agent_get_file) | **GET** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Download a File from VM
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
[**v1_agent_system_shutdown**](CorelliumApi.md#v1_agent_system_shutdown) | **POST** /v1/instances/{instanceId}/agent/v1/system/shutdown | Instruct VM to halt
[**v1_agent_system_unlock**](CorelliumApi.md#v1_agent_system_unlock) | **POST** /v1/instances/{instanceId}/agent/v1/system/unlock | Unlock Device (iOS Only)
[**v1_agent_uninstall_app**](CorelliumApi.md#v1_agent_uninstall_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/apps/{bundleId}/uninstall | Uninstall an App
[**v1_agent_uninstall_profile**](CorelliumApi.md#v1_agent_uninstall_profile) | **DELETE** /v1/instances/{instanceId}/agent/v1/profile/profiles/{profileId} | Uninstall a Profile from VM
[**v1_agent_upload_file**](CorelliumApi.md#v1_agent_upload_file) | **PUT** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Upload a file to VM
[**v1_auth_login**](CorelliumApi.md#v1_auth_login) | **POST** /v1/auth/login | Log In
[**v1_clear_core_trace**](CorelliumApi.md#v1_clear_core_trace) | **DELETE** /v1/instances/{instanceId}/strace | Clear CoreTrace logs
[**v1_clear_instance_panics**](CorelliumApi.md#v1_clear_instance_panics) | **DELETE** /v1/instances/{instanceId}/panics | Clear Panics
[**v1_create_image**](CorelliumApi.md#v1_create_image) | **POST** /v1/images | Create a new Image
[**v1_create_instance**](CorelliumApi.md#v1_create_instance) | **POST** /v1/instances | Create Instance
[**v1_create_project**](CorelliumApi.md#v1_create_project) | **POST** /v1/projects | Create a Project
[**v1_create_snapshot**](CorelliumApi.md#v1_create_snapshot) | **POST** /v1/instances/{instanceId}/snapshots | Create Instance Snapshot
[**v1_create_user**](CorelliumApi.md#v1_create_user) | **POST** /v1/users | Create User
[**v1_delete_image**](CorelliumApi.md#v1_delete_image) | **DELETE** /v2/images/{imageId} | Delete Image
[**v1_delete_instance**](CorelliumApi.md#v1_delete_instance) | **DELETE** /v1/instances/{instanceId} | Remove Instance
[**v1_delete_instance_snapshot**](CorelliumApi.md#v1_delete_instance_snapshot) | **DELETE** /v1/instances/{instanceId}/snapshots/{snapshotId} | Delete a Snapshot
[**v1_delete_snapshot**](CorelliumApi.md#v1_delete_snapshot) | **DELETE** /v1/snapshots/{snapshotId} | Delete a Snapshot
[**v1_delete_user**](CorelliumApi.md#v1_delete_user) | **DELETE** /v1/users/{userId} | Delete User
[**v1_deny_trial_request**](CorelliumApi.md#v1_deny_trial_request) | **DELETE** /v1/billing/trial-requests/{requestEmail} | Deny Trial Request
[**v1_disable_expose_port**](CorelliumApi.md#v1_disable_expose_port) | **POST** /v1/instances/{instanceId}/exposeport/disable | Disable an exposed port on an instance for device access.
[**v1_enable_expose_port**](CorelliumApi.md#v1_enable_expose_port) | **POST** /v1/instances/{instanceId}/exposeport/enable | Enable an exposed port on an instance for device access.
[**v1_get_image**](CorelliumApi.md#v1_get_image) | **GET** /v1/images/{imageId} | Get Image Metadata
[**v1_get_images**](CorelliumApi.md#v1_get_images) | **GET** /v1/images | Get all Images Metadata
[**v1_get_instance**](CorelliumApi.md#v1_get_instance) | **GET** /v1/instances/{instanceId} | Get Instance
[**v1_get_instance_console**](CorelliumApi.md#v1_get_instance_console) | **GET** /v1/instances/{instanceId}/console | Get console websocket URL
[**v1_get_instance_console_log**](CorelliumApi.md#v1_get_instance_console_log) | **GET** /v1/instances/{instanceId}/consoleLog | Get Console Log
[**v1_get_instance_gpios**](CorelliumApi.md#v1_get_instance_gpios) | **GET** /v1/instances/{instanceId}/gpios | Get Instance GPIOs
[**v1_get_instance_panics**](CorelliumApi.md#v1_get_instance_panics) | **GET** /v1/instances/{instanceId}/panics | Get Panics
[**v1_get_instance_peripherals**](CorelliumApi.md#v1_get_instance_peripherals) | **GET** /v1/instances/{instanceId}/peripherals | Get Instance Peripherals
[**v1_get_instance_rate**](CorelliumApi.md#v1_get_instance_rate) | **GET** /v1/instances/{instanceId}/rate | Get rate information
[**v1_get_instance_screenshot**](CorelliumApi.md#v1_get_instance_screenshot) | **GET** /v1/instances/{instanceId}/screenshot.{format} | Get Instance Screenshot
[**v1_get_instance_snapshot**](CorelliumApi.md#v1_get_instance_snapshot) | **GET** /v1/instances/{instanceId}/snapshots/{snapshotId} | Get Instance Snapshot
[**v1_get_instance_snapshots**](CorelliumApi.md#v1_get_instance_snapshots) | **GET** /v1/instances/{instanceId}/snapshots | Get Instance Snapshots
[**v1_get_instance_state**](CorelliumApi.md#v1_get_instance_state) | **GET** /v1/instances/{instanceId}/state | Get state of Instance
[**v1_get_instances**](CorelliumApi.md#v1_get_instances) | **GET** /v1/instances | Get Instances
[**v1_get_model_software**](CorelliumApi.md#v1_get_model_software) | **GET** /v1/models/{model}/software | Get Software for Model
[**v1_get_models**](CorelliumApi.md#v1_get_models) | **GET** /v1/models | Get Supported Models
[**v1_get_project**](CorelliumApi.md#v1_get_project) | **GET** /v1/projects/{projectId} | Get a Project
[**v1_get_project_instances**](CorelliumApi.md#v1_get_project_instances) | **GET** /v1/projects/{projectId}/instances | Get Instances in Project
[**v1_get_project_keys**](CorelliumApi.md#v1_get_project_keys) | **GET** /v1/projects/{projectId}/keys | Get Project Authorized Keys
[**v1_get_project_vpn_config**](CorelliumApi.md#v1_get_project_vpn_config) | **GET** /v1/projects/{projectId}/vpnconfig/{format} | Get Project VPN Configuration
[**v1_get_projects**](CorelliumApi.md#v1_get_projects) | **GET** /v1/projects | Get Projects
[**v1_get_reset_link_info**](CorelliumApi.md#v1_get_reset_link_info) | **GET** /v1/users/reset-link-info | Send Password Reset Link Info
[**v1_get_snapshot**](CorelliumApi.md#v1_get_snapshot) | **GET** /v1/snapshots/{snapshotId} | Get Snapshot
[**v1_get_trial_requests**](CorelliumApi.md#v1_get_trial_requests) | **GET** /v1/billing/trial-requests | Get Trial Requests
[**v1_grant_trial_request**](CorelliumApi.md#v1_grant_trial_request) | **POST** /v1/billing/trial-requests/{requestEmail}/grant | Grant Trial Request
[**v1_instances_instance_id_agent_agent_path_delete**](CorelliumApi.md#v1_instances_instance_id_agent_agent_path_delete) | **DELETE** /v1/instances/{instanceId}/agent/{agentPath} | DELETE proxy to VM Agent
[**v1_instances_instance_id_agent_agent_path_patch**](CorelliumApi.md#v1_instances_instance_id_agent_agent_path_patch) | **PATCH** /v1/instances/{instanceId}/agent/{agentPath} | PATCH proxy to VM Agent
[**v1_instances_instance_id_message_post**](CorelliumApi.md#v1_instances_instance_id_message_post) | **POST** /v1/instances/{instanceId}/message | Receive a message on an iOS vm
[**v1_list_threads**](CorelliumApi.md#v1_list_threads) | **GET** /v1/instances/{instanceId}/strace/thread-list | Get Running Threads (CoreTrace)
[**v1_media_play**](CorelliumApi.md#v1_media_play) | **POST** /v1/instances/{instanceId}/media/play | Start playing media
[**v1_media_stop**](CorelliumApi.md#v1_media_stop) | **POST** /v1/instances/{instanceId}/media/stop | Stop playing media
[**v1_patch_instance**](CorelliumApi.md#v1_patch_instance) | **PATCH** /v1/instances/{instanceId} | Update Instance
[**v1_pause_instance**](CorelliumApi.md#v1_pause_instance) | **POST** /v1/instances/{instanceId}/pause | Pause an Instance
[**v1_post_instance_input**](CorelliumApi.md#v1_post_instance_input) | **POST** /v1/instances/{instanceId}/input | Provide Instance Input
[**v1_projects_project_id_delete**](CorelliumApi.md#v1_projects_project_id_delete) | **DELETE** /v1/projects/{projectId} | Delete a Project
[**v1_ready**](CorelliumApi.md#v1_ready) | **GET** /v1/ready | API Status
[**v1_reboot_instance**](CorelliumApi.md#v1_reboot_instance) | **POST** /v1/instances/{instanceId}/reboot | Reboot an Instance
[**v1_remove_project_key**](CorelliumApi.md#v1_remove_project_key) | **DELETE** /v1/projects/{projectId}/keys/{keyId} | Delete Project Authorized Key
[**v1_rename_instance_snapshot**](CorelliumApi.md#v1_rename_instance_snapshot) | **PATCH** /v1/instances/{instanceId}/snapshots/{snapshotId} | Rename a Snapshot
[**v1_reset_user_password**](CorelliumApi.md#v1_reset_user_password) | **POST** /v1/users/reset-password | Reset User Password
[**v1_restore_instance_snapshot**](CorelliumApi.md#v1_restore_instance_snapshot) | **POST** /v1/instances/{instanceId}/snapshots/{snapshotId}/restore | Restore a Snapshot
[**v1_rotate_instance**](CorelliumApi.md#v1_rotate_instance) | **POST** /v1/instances/{instanceId}/rotate | Rotate device to specified orientation
[**v1_send_user_reset_link**](CorelliumApi.md#v1_send_user_reset_link) | **POST** /v1/users/send-reset-link | Send Password Reset Link
[**v1_set_instance_gpios**](CorelliumApi.md#v1_set_instance_gpios) | **PUT** /v1/instances/{instanceId}/gpios | Set Instance GPIOs
[**v1_set_instance_peripherals**](CorelliumApi.md#v1_set_instance_peripherals) | **PUT** /v1/instances/{instanceId}/peripherals | Set Instance Peripherals
[**v1_set_instance_state**](CorelliumApi.md#v1_set_instance_state) | **PUT** /v1/instances/{instanceId}/state | Set state of Instance
[**v1_snapshot_rename**](CorelliumApi.md#v1_snapshot_rename) | **PATCH** /v1/snapshots/{snapshotId} | Rename a Snapshot
[**v1_start_core_trace**](CorelliumApi.md#v1_start_core_trace) | **POST** /v1/instances/{instanceId}/strace/enable | Start CoreTrace on an instance
[**v1_start_instance**](CorelliumApi.md#v1_start_instance) | **POST** /v1/instances/{instanceId}/start | Start an Instance
[**v1_start_network_monitor**](CorelliumApi.md#v1_start_network_monitor) | **POST** /v1/instances/{instanceId}/sslsplit/enable | Start Network Monitor on an instance.
[**v1_stop_core_trace**](CorelliumApi.md#v1_stop_core_trace) | **POST** /v1/instances/{instanceId}/strace/disable | Stop CoreTrace on an instance.
[**v1_stop_instance**](CorelliumApi.md#v1_stop_instance) | **POST** /v1/instances/{instanceId}/stop | Stop an Instance
[**v1_stop_network_monitor**](CorelliumApi.md#v1_stop_network_monitor) | **POST** /v1/instances/{instanceId}/sslsplit/disable | Stop Network Monitor on an instance.
[**v1_trial_requests**](CorelliumApi.md#v1_trial_requests) | **POST** /v1/billing/trial-requests | Create Trial Request
[**v1_trial_requests_v3**](CorelliumApi.md#v1_trial_requests_v3) | **POST** /v1/billing/trial-requests-v3 | Create Trial Request (v1.3)
[**v1_unpause_instance**](CorelliumApi.md#v1_unpause_instance) | **POST** /v1/instances/{instanceId}/unpause | Unpause an Instance
[**v1_update_current_domain**](CorelliumApi.md#v1_update_current_domain) | **PATCH** /v1/domain | Update Current Domain
[**v1_update_project**](CorelliumApi.md#v1_update_project) | **PATCH** /v1/projects/{projectId} | Update a Project
[**v1_update_project_settings**](CorelliumApi.md#v1_update_project_settings) | **PATCH** /v1/projects/{projectId}/settings | Change Project Settings
[**v1_update_user**](CorelliumApi.md#v1_update_user) | **PATCH** /v1/users/{userId} | Update User
[**v1_upload_image_data**](CorelliumApi.md#v1_upload_image_data) | **POST** /v1/images/{imageId} | Upload Image Data
[**v1_user_agree_terms**](CorelliumApi.md#v1_user_agree_terms) | **POST** /v1/users/agree | Consent to the current terms and conditions
[**v1_users_change_password_post**](CorelliumApi.md#v1_users_change_password_post) | **POST** /v1/users/change-password | Authenticated solely by the old-password.
[**v1_users_login**](CorelliumApi.md#v1_users_login) | **POST** /v1/users/login | Log In
[**v2_trial_requests**](CorelliumApi.md#v2_trial_requests) | **POST** /v2/billing/trial-requests | Create Trial Request (v2)


# **v1_add_project_key**
> str v1_add_project_key(project_id, project_key)

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
  "type": "ssh",
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

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorized Keys |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_app_ready**
> AgentAppReadyResponse v1_agent_app_ready(instance_id)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_install_profile**
> v1_agent_install_profile(instance_id, body)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list_app_icons**
> list[AgentIcons] v1_agent_list_app_icons(instance_id, bundle_id)

List App Icons

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list_apps**
> AgentAppsList v1_agent_list_apps(instance_id)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list_apps_status**
> AgentAppsList v1_agent_list_apps_status(instance_id)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_list_profiles**
> AgentProfilesReturn v1_agent_list_profiles(instance_id)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_set_file_attributes**
> v1_agent_set_file_attributes(instance_id, file_path, file_changes)

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
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_get_adb_auth**
> AgentSystemAdbAuth v1_agent_system_get_adb_auth(instance_id)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_system_lock**
> v1_agent_system_lock(instance_id)

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

# **v1_agent_system_shutdown**
> v1_agent_system_shutdown(instance_id)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_agent_uninstall_profile**
> v1_agent_uninstall_profile(instance_id, profile_id)

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
**200** | No content |  -  |
**400** | Agent Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_auth_login**
> Token v1_auth_login(body)

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

# **v1_clear_core_trace**
> v1_clear_core_trace(instance_id)

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

# **v1_clear_instance_panics**
> v1_clear_instance_panics(instance_id)

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

# **v1_create_image**
> Image v1_create_image(type, encoding, name=name, project=project, instance=instance, file=file)

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
name = 'name_example' # str | Image name (optional)
project = 'project_example' # str | Project ID (optional)
instance = 'instance_example' # str | Instance ID (optional)
file = '/path/to/file' # file | Optionally the actual file (optional)

        try:
            # Create a new Image
            api_response = await api_instance.v1_create_image(type, encoding, name=name, project=project, instance=instance, file=file)
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
**404** | application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_create_instance**
> InstanceReturn v1_create_instance(instance_create_options)

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

# **v1_create_project**
> Project v1_create_project(project)

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
    "version": 1,
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
> object v1_create_user(body)

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
        body = None # object | User data

        try:
            # Create User
            api_response = await api_instance.v1_create_user(body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_create_user: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**| User data | 

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
**200** | User |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_delete_image**
> v1_delete_image(image_id)

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
        instance_id = 'instance_id_example' # str | Instance ID - uuid
snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid

        try:
            # Delete a Snapshot
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

# **v1_delete_snapshot**
> v1_delete_snapshot(snapshot_id)

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

# **v1_delete_user**
> object v1_delete_user(user_id)

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
            api_response = await api_instance.v1_delete_user(user_id)
            pprint(api_response)
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

**object**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_deny_trial_request**
> object v1_deny_trial_request(request_email)

Deny Trial Request

Allow cloud administrators to deny an invite.

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
        request_email = 'request_email_example' # str | Email address

        try:
            # Deny Trial Request
            api_response = await api_instance.v1_deny_trial_request(request_email)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_deny_trial_request: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_email** | **str**| Email address | 

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
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_disable_expose_port**
> v1_disable_expose_port(instance_id)

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

# **v1_enable_expose_port**
> v1_enable_expose_port(instance_id)

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

# **v1_get_image**
> Image v1_get_image(image_id)

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
> Image v1_get_images(project=project)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance**
> Instance v1_get_instance(instance_id, return_attr=return_attr)

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
> dict(str, GpioStateDefinition) v1_get_instance_gpios(instance_id)

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

[**dict(str, GpioStateDefinition)**](GpioStateDefinition.md)

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

# **v1_get_instance_rate**
> RateInfo v1_get_instance_rate(instance_id)

Get rate information

Returns the cost, in microcents, for the instance in the on and off state. Instances are charged $0.25 / day for storage (off) and $0.25 per core per hour (on).

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
            # Get rate information
            api_response = await api_instance.v1_get_instance_rate(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_rate: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

### Return type

[**RateInfo**](RateInfo.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rate Information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_instance_screenshot**
> file v1_get_instance_screenshot(instance_id, format, scale=scale)

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
scale = 56 # int | Screenshot scale 1:N (optional)

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
 **scale** | **int**| Screenshot scale 1:N | [optional] 

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

# **v1_get_instance_state**
> InstanceState v1_get_instance_state(instance_id)

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

        try:
            # Get state of Instance
            api_response = await api_instance.v1_get_instance_state(instance_id)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_instance_state: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 

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

# **v1_get_instances**
> list[Instance] v1_get_instances(name=name, return_attr=return_attr)

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
        name = 'name_example' # str | Optionally filter by project name (optional)
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
 **name** | **str**| Optionally filter by project name | [optional] 
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

# **v1_get_project**
> Project v1_get_project(project_id)

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

# **v1_get_project_vpn_config**
> str v1_get_project_vpn_config(project_id, format)

Get Project VPN Configuration

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
 - **Accept**: application/x-openvpn-profile, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OpenVPN Configuration |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_get_projects**
> list[Project] v1_get_projects(name=name, ids_only=ids_only)

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
> object v1_get_reset_link_info(token)

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

**object**

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

# **v1_get_snapshot**
> Snapshot v1_get_snapshot(snapshot_id)

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

# **v1_get_trial_requests**
> object v1_get_trial_requests()

Get Trial Requests

Allow cloud administrators to list trial requests.

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
            # Get Trial Requests
            api_response = await api_instance.v1_get_trial_requests()
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_get_trial_requests: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters
This endpoint does not need any parameter.

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
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_grant_trial_request**
> GrantTrialRequestResponse v1_grant_trial_request(request_email)

Grant Trial Request

Allow cloud administrators grant an early access request, generating an invite and e-mailing the recipient.

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
        request_email = 'request_email_example' # str | Email address

        try:
            # Grant Trial Request
            api_response = await api_instance.v1_grant_trial_request(request_email)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_grant_trial_request: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_email** | **str**| Email address | 

### Return type

[**GrantTrialRequestResponse**](GrantTrialRequestResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_instances_instance_id_agent_agent_path_delete**
> str v1_instances_instance_id_agent_agent_path_delete(instance_id, agent_path)

DELETE proxy to VM Agent

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
agent_path = 'agent_path_example' # str | Path to DELETE

        try:
            # DELETE proxy to VM Agent
            api_response = await api_instance.v1_instances_instance_id_agent_agent_path_delete(instance_id, agent_path)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_instances_instance_id_agent_agent_path_delete: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **agent_path** | **str**| Path to DELETE | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: binary, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_instances_instance_id_agent_agent_path_patch**
> str v1_instances_instance_id_agent_agent_path_patch(instance_id, agent_path, body=body)

PATCH proxy to VM Agent

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
agent_path = 'agent_path_example' # str | Path to PATCH
body = None # object | PATCH Body (optional)

        try:
            # PATCH proxy to VM Agent
            api_response = await api_instance.v1_instances_instance_id_agent_agent_path_patch(instance_id, agent_path, body=body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_instances_instance_id_agent_agent_path_patch: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Instance ID - uuid | 
 **agent_path** | **str**| Path to PATCH | 
 **body** | **object**| PATCH Body | [optional] 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: binary, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_instances_instance_id_message_post**
> v1_instances_instance_id_message_post(instance_id)

Receive a message on an iOS vm

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
            # Receive a message on an iOS vm
            api_instance.v1_instances_instance_id_message_post(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_instances_instance_id_message_post: %s\n" % e)

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

# **v1_list_threads**
> list[KernelTask] v1_list_threads(instance_id)

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

# **v1_media_play**
> v1_media_play(instance_id, media_play_body)

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

# **v1_patch_instance**
> Instance v1_patch_instance(instance_id, patch_instance_options)

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

# **v1_pause_instance**
> v1_pause_instance(instance_id)

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
> int v1_post_instance_input(instance_id, instance_input)

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

**int**

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

# **v1_projects_project_id_delete**
> v1_projects_project_id_delete(project_id)

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
            api_instance.v1_projects_project_id_delete(project_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_projects_project_id_delete: %s\n" % e)

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
 - **Accept**: Not defined


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

# **v1_rename_instance_snapshot**
> Snapshot v1_rename_instance_snapshot(instance_id, snapshot_id, snapshot_creation_options)

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
        instance_id = 'instance_id_example' # str | Instance ID - uuid
snapshot_id = 'snapshot_id_example' # str | Snapshot ID - uuid
snapshot_creation_options = corellium_api.SnapshotCreationOptions() # SnapshotCreationOptions | 

        try:
            # Rename a Snapshot
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

# **v1_restore_instance_snapshot**
> v1_restore_instance_snapshot(instance_id, snapshot_id)

Restore a Snapshot

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
            # Restore a Snapshot
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
> dict(str, GpioStateDefinition) v1_set_instance_gpios(instance_id, request_body)

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
request_body = {
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
} # dict(str, GpioStateDefinition) | New GPIO state

        try:
            # Set Instance GPIOs
            api_response = await api_instance.v1_set_instance_gpios(instance_id, request_body)
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
 **request_body** | [**dict(str, GpioStateDefinition)**](GpioStateDefinition.md)| New GPIO state | 

### Return type

[**dict(str, GpioStateDefinition)**](GpioStateDefinition.md)

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
  "magnetic": [0, 45, 0 ],
  "orientation": [0, 0, 0 ],
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

# **v1_snapshot_rename**
> Snapshot v1_snapshot_rename(snapshot_id, snapshot_creation_options)

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

# **v1_start_instance**
> v1_start_instance(instance_id, instance_start_options=instance_start_options)

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

# **v1_start_network_monitor**
> v1_start_network_monitor(instance_id)

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

        try:
            # Start Network Monitor on an instance.
            api_instance.v1_start_network_monitor(instance_id)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_start_network_monitor: %s\n" % e)

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

# **v1_stop_core_trace**
> v1_stop_core_trace(instance_id)

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

# **v1_stop_instance**
> v1_stop_instance(instance_id, instance_stop_options=instance_stop_options)

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

# **v1_stop_network_monitor**
> v1_stop_network_monitor(instance_id)

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

# **v1_trial_requests**
> object v1_trial_requests(trial_request_options)

Create Trial Request

Allow third party integrations to create trial requests

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
        trial_request_options = {
    "email": "user@example.com"
} # TrialRequestOptions | Trial Request Options

        try:
            # Create Trial Request
            api_response = await api_instance.v1_trial_requests(trial_request_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_trial_requests: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trial_request_options** | [**TrialRequestOptions**](TrialRequestOptions.md)| Trial Request Options | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_trial_requests_v3**
> object v1_trial_requests_v3(trial_request_options)

Create Trial Request (v1.3)

Allow third party integrations to create trial requests

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
        trial_request_options = {
    "email": "user@example.com",
    "name": "Jane Doe"
} # TrialRequestOptions | Trial Request Options

        try:
            # Create Trial Request (v1.3)
            api_response = await api_instance.v1_trial_requests_v3(trial_request_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_trial_requests_v3: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trial_request_options** | [**TrialRequestOptions**](TrialRequestOptions.md)| Trial Request Options | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_unpause_instance**
> v1_unpause_instance(instance_id)

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

# **v1_update_current_domain**
> object v1_update_current_domain(domain_options)

Update Current Domain

Update the domain for the current user

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
        domain_options = {
    "totpRequired": false,
    "trialExtension": {
        "duration": 7,
        "reason": "I need another week"
    }
} # DomainOptions | Domain Options

        try:
            # Update Current Domain
            api_response = await api_instance.v1_update_current_domain(domain_options)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_current_domain: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_options** | [**DomainOptions**](DomainOptions.md)| Domain Options | 

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
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_project**
> Project v1_update_project(project_id, project)

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_update_user**
> object v1_update_user(user_id, body)

Update User

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
body = None # object | User data

        try:
            # Update User
            api_response = await api_instance.v1_update_user(user_id, body)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v1_update_user: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| userId - uuid | 
 **body** | **object**| User data | 

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
**200** | User |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_upload_image_data**
> Image v1_upload_image_data(image_id, body)

Upload Image Data

If the active project has enough remaining quota, updates an Image with the contents of the request body.

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
body = 'body_example' # str | Uploaded Image

        try:
            # Upload Image Data
            api_response = await api_instance.v1_upload_image_data(image_id, body)
            pprint(api_response)
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

[**Image**](Image.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: binary
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | application/json |  -  |
**404** | application/json |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_user_agree_terms**
> AgreedAck v1_user_agree_terms()

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
            # Authenticated solely by the old-password.
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

# **v2_trial_requests**
> v2_trial_requests(trial_request_options)

Create Trial Request (v2)

Allow third party integrations to create trial requests

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
        trial_request_options = {
    "email": "user@example.com",
    "name": "Jane Doe"
} # TrialRequestOptions | Trial Request Options

        try:
            # Create Trial Request (v2)
            api_instance.v2_trial_requests(trial_request_options)
        except ApiException as e:
            print("Exception when calling CorelliumApi->v2_trial_requests: %s\n" % e)

if __name__ == "__main__":
    asyncio.run(main())
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trial_request_options** | [**TrialRequestOptions**](TrialRequestOptions.md)| Trial Request Options | 

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
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

