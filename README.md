# corellium-api
REST API to manage your virtual devices.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.11.0-13642
- Package version: 0.1.0
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

## Documentation for API Endpoints

All URIs are relative to *https://app.corellium.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CorelliumApi* | [**v1_add_project_key**](docs/CorelliumApi.md#v1_add_project_key) | **POST** /v1/projects/{projectId}/keys | Add Project Authorized Key
*CorelliumApi* | [**v1_agent_app_ready**](docs/CorelliumApi.md#v1_agent_app_ready) | **GET** /v1/instances/{instanceId}/agent/v1/app/ready | Check if App subsystem is ready
*CorelliumApi* | [**v1_agent_delete_file**](docs/CorelliumApi.md#v1_agent_delete_file) | **DELETE** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Delete a File on VM
*CorelliumApi* | [**v1_agent_get_file**](docs/CorelliumApi.md#v1_agent_get_file) | **GET** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Download a File from VM
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
*CorelliumApi* | [**v1_agent_system_shutdown**](docs/CorelliumApi.md#v1_agent_system_shutdown) | **POST** /v1/instances/{instanceId}/agent/v1/system/shutdown | Instruct VM to halt
*CorelliumApi* | [**v1_agent_system_unlock**](docs/CorelliumApi.md#v1_agent_system_unlock) | **POST** /v1/instances/{instanceId}/agent/v1/system/unlock | Unlock Device (iOS Only)
*CorelliumApi* | [**v1_agent_uninstall_app**](docs/CorelliumApi.md#v1_agent_uninstall_app) | **POST** /v1/instances/{instanceId}/agent/v1/app/apps/{bundleId}/uninstall | Uninstall an App
*CorelliumApi* | [**v1_agent_uninstall_profile**](docs/CorelliumApi.md#v1_agent_uninstall_profile) | **DELETE** /v1/instances/{instanceId}/agent/v1/profile/profiles/{profileId} | Uninstall a Profile from VM
*CorelliumApi* | [**v1_agent_upload_file**](docs/CorelliumApi.md#v1_agent_upload_file) | **PUT** /v1/instances/{instanceId}/agent/v1/file/device/{filePath} | Upload a file to VM
*CorelliumApi* | [**v1_auth_login**](docs/CorelliumApi.md#v1_auth_login) | **POST** /v1/auth/login | Log In
*CorelliumApi* | [**v1_clear_core_trace**](docs/CorelliumApi.md#v1_clear_core_trace) | **DELETE** /v1/instances/{instanceId}/strace | Clear CoreTrace logs
*CorelliumApi* | [**v1_clear_instance_panics**](docs/CorelliumApi.md#v1_clear_instance_panics) | **DELETE** /v1/instances/{instanceId}/panics | Clear Panics
*CorelliumApi* | [**v1_create_image**](docs/CorelliumApi.md#v1_create_image) | **POST** /v1/images | Create a new Image
*CorelliumApi* | [**v1_create_instance**](docs/CorelliumApi.md#v1_create_instance) | **POST** /v1/instances | Create Instance
*CorelliumApi* | [**v1_create_project**](docs/CorelliumApi.md#v1_create_project) | **POST** /v1/projects | Create a Project
*CorelliumApi* | [**v1_create_snapshot**](docs/CorelliumApi.md#v1_create_snapshot) | **POST** /v1/instances/{instanceId}/snapshots | Create Instance Snapshot
*CorelliumApi* | [**v1_create_user**](docs/CorelliumApi.md#v1_create_user) | **POST** /v1/users | Create User
*CorelliumApi* | [**v1_delete_image**](docs/CorelliumApi.md#v1_delete_image) | **DELETE** /v2/images/{imageId} | Delete Image
*CorelliumApi* | [**v1_delete_instance**](docs/CorelliumApi.md#v1_delete_instance) | **DELETE** /v1/instances/{instanceId} | Remove Instance
*CorelliumApi* | [**v1_delete_instance_snapshot**](docs/CorelliumApi.md#v1_delete_instance_snapshot) | **DELETE** /v1/instances/{instanceId}/snapshots/{snapshotId} | Delete a Snapshot
*CorelliumApi* | [**v1_delete_snapshot**](docs/CorelliumApi.md#v1_delete_snapshot) | **DELETE** /v1/snapshots/{snapshotId} | Delete a Snapshot
*CorelliumApi* | [**v1_delete_user**](docs/CorelliumApi.md#v1_delete_user) | **DELETE** /v1/users/{userId} | Delete User
*CorelliumApi* | [**v1_deny_trial_request**](docs/CorelliumApi.md#v1_deny_trial_request) | **DELETE** /v1/billing/trial-requests/{requestEmail} | Deny Trial Request
*CorelliumApi* | [**v1_disable_expose_port**](docs/CorelliumApi.md#v1_disable_expose_port) | **POST** /v1/instances/{instanceId}/exposeport/disable | Disable an exposed port on an instance for device access.
*CorelliumApi* | [**v1_enable_expose_port**](docs/CorelliumApi.md#v1_enable_expose_port) | **POST** /v1/instances/{instanceId}/exposeport/enable | Enable an exposed port on an instance for device access.
*CorelliumApi* | [**v1_get_image**](docs/CorelliumApi.md#v1_get_image) | **GET** /v1/images/{imageId} | Get Image Metadata
*CorelliumApi* | [**v1_get_images**](docs/CorelliumApi.md#v1_get_images) | **GET** /v1/images | Get all Images Metadata
*CorelliumApi* | [**v1_get_instance**](docs/CorelliumApi.md#v1_get_instance) | **GET** /v1/instances/{instanceId} | Get Instance
*CorelliumApi* | [**v1_get_instance_console**](docs/CorelliumApi.md#v1_get_instance_console) | **GET** /v1/instances/{instanceId}/console | Get console websocket URL
*CorelliumApi* | [**v1_get_instance_console_log**](docs/CorelliumApi.md#v1_get_instance_console_log) | **GET** /v1/instances/{instanceId}/consoleLog | Get Console Log
*CorelliumApi* | [**v1_get_instance_gpios**](docs/CorelliumApi.md#v1_get_instance_gpios) | **GET** /v1/instances/{instanceId}/gpios | Get Instance GPIOs
*CorelliumApi* | [**v1_get_instance_panics**](docs/CorelliumApi.md#v1_get_instance_panics) | **GET** /v1/instances/{instanceId}/panics | Get Panics
*CorelliumApi* | [**v1_get_instance_peripherals**](docs/CorelliumApi.md#v1_get_instance_peripherals) | **GET** /v1/instances/{instanceId}/peripherals | Get Instance Peripherals
*CorelliumApi* | [**v1_get_instance_rate**](docs/CorelliumApi.md#v1_get_instance_rate) | **GET** /v1/instances/{instanceId}/rate | Get rate information
*CorelliumApi* | [**v1_get_instance_screenshot**](docs/CorelliumApi.md#v1_get_instance_screenshot) | **GET** /v1/instances/{instanceId}/screenshot.{format} | Get Instance Screenshot
*CorelliumApi* | [**v1_get_instance_snapshot**](docs/CorelliumApi.md#v1_get_instance_snapshot) | **GET** /v1/instances/{instanceId}/snapshots/{snapshotId} | Get Instance Snapshot
*CorelliumApi* | [**v1_get_instance_snapshots**](docs/CorelliumApi.md#v1_get_instance_snapshots) | **GET** /v1/instances/{instanceId}/snapshots | Get Instance Snapshots
*CorelliumApi* | [**v1_get_instance_state**](docs/CorelliumApi.md#v1_get_instance_state) | **GET** /v1/instances/{instanceId}/state | Get state of Instance
*CorelliumApi* | [**v1_get_instances**](docs/CorelliumApi.md#v1_get_instances) | **GET** /v1/instances | Get Instances
*CorelliumApi* | [**v1_get_model_software**](docs/CorelliumApi.md#v1_get_model_software) | **GET** /v1/models/{model}/software | Get Software for Model
*CorelliumApi* | [**v1_get_models**](docs/CorelliumApi.md#v1_get_models) | **GET** /v1/models | Get Supported Models
*CorelliumApi* | [**v1_get_project**](docs/CorelliumApi.md#v1_get_project) | **GET** /v1/projects/{projectId} | Get a Project
*CorelliumApi* | [**v1_get_project_instances**](docs/CorelliumApi.md#v1_get_project_instances) | **GET** /v1/projects/{projectId}/instances | Get Instances in Project
*CorelliumApi* | [**v1_get_project_keys**](docs/CorelliumApi.md#v1_get_project_keys) | **GET** /v1/projects/{projectId}/keys | Get Project Authorized Keys
*CorelliumApi* | [**v1_get_project_vpn_config**](docs/CorelliumApi.md#v1_get_project_vpn_config) | **GET** /v1/projects/{projectId}/vpnconfig/{format} | Get Project VPN Configuration
*CorelliumApi* | [**v1_get_projects**](docs/CorelliumApi.md#v1_get_projects) | **GET** /v1/projects | Get Projects
*CorelliumApi* | [**v1_get_reset_link_info**](docs/CorelliumApi.md#v1_get_reset_link_info) | **GET** /v1/users/reset-link-info | Send Password Reset Link Info
*CorelliumApi* | [**v1_get_snapshot**](docs/CorelliumApi.md#v1_get_snapshot) | **GET** /v1/snapshots/{snapshotId} | Get Snapshot
*CorelliumApi* | [**v1_get_trial_requests**](docs/CorelliumApi.md#v1_get_trial_requests) | **GET** /v1/billing/trial-requests | Get Trial Requests
*CorelliumApi* | [**v1_grant_trial_request**](docs/CorelliumApi.md#v1_grant_trial_request) | **POST** /v1/billing/trial-requests/{requestEmail}/grant | Grant Trial Request
*CorelliumApi* | [**v1_instances_instance_id_agent_agent_path_delete**](docs/CorelliumApi.md#v1_instances_instance_id_agent_agent_path_delete) | **DELETE** /v1/instances/{instanceId}/agent/{agentPath} | DELETE proxy to VM Agent
*CorelliumApi* | [**v1_instances_instance_id_agent_agent_path_patch**](docs/CorelliumApi.md#v1_instances_instance_id_agent_agent_path_patch) | **PATCH** /v1/instances/{instanceId}/agent/{agentPath} | PATCH proxy to VM Agent
*CorelliumApi* | [**v1_instances_instance_id_message_post**](docs/CorelliumApi.md#v1_instances_instance_id_message_post) | **POST** /v1/instances/{instanceId}/message | Receive a message on an iOS vm
*CorelliumApi* | [**v1_list_threads**](docs/CorelliumApi.md#v1_list_threads) | **GET** /v1/instances/{instanceId}/strace/thread-list | Get Running Threads (CoreTrace)
*CorelliumApi* | [**v1_media_play**](docs/CorelliumApi.md#v1_media_play) | **POST** /v1/instances/{instanceId}/media/play | Play an image or URL
*CorelliumApi* | [**v1_patch_instance**](docs/CorelliumApi.md#v1_patch_instance) | **PATCH** /v1/instances/{instanceId} | Update Instance
*CorelliumApi* | [**v1_pause_instance**](docs/CorelliumApi.md#v1_pause_instance) | **POST** /v1/instances/{instanceId}/pause | Pause an Instance
*CorelliumApi* | [**v1_post_instance_input**](docs/CorelliumApi.md#v1_post_instance_input) | **POST** /v1/instances/{instanceId}/input | Provide Instance Input
*CorelliumApi* | [**v1_projects_project_id_delete**](docs/CorelliumApi.md#v1_projects_project_id_delete) | **DELETE** /v1/projects/{projectId} | Delete a Project
*CorelliumApi* | [**v1_ready**](docs/CorelliumApi.md#v1_ready) | **GET** /v1/ready | API Status
*CorelliumApi* | [**v1_reboot_instance**](docs/CorelliumApi.md#v1_reboot_instance) | **POST** /v1/instances/{instanceId}/reboot | Reboot an Instance
*CorelliumApi* | [**v1_remove_project_key**](docs/CorelliumApi.md#v1_remove_project_key) | **DELETE** /v1/projects/{projectId}/keys/{keyId} | Delete Project Authorized Key
*CorelliumApi* | [**v1_rename_instance_snapshot**](docs/CorelliumApi.md#v1_rename_instance_snapshot) | **PATCH** /v1/instances/{instanceId}/snapshots/{snapshotId} | Rename a Snapshot
*CorelliumApi* | [**v1_reset_user_password**](docs/CorelliumApi.md#v1_reset_user_password) | **POST** /v1/users/reset-password | Reset User Password
*CorelliumApi* | [**v1_restore_instance_snapshot**](docs/CorelliumApi.md#v1_restore_instance_snapshot) | **POST** /v1/instances/{instanceId}/snapshots/{snapshotId}/restore | Restore a Snapshot
*CorelliumApi* | [**v1_rotate_instance**](docs/CorelliumApi.md#v1_rotate_instance) | **POST** /v1/instances/{instanceId}/rotate | Rotate device to specified orientation
*CorelliumApi* | [**v1_send_user_reset_link**](docs/CorelliumApi.md#v1_send_user_reset_link) | **POST** /v1/users/send-reset-link | Send Password Reset Link
*CorelliumApi* | [**v1_set_instance_gpios**](docs/CorelliumApi.md#v1_set_instance_gpios) | **PUT** /v1/instances/{instanceId}/gpios | Set Instance GPIOs
*CorelliumApi* | [**v1_set_instance_peripherals**](docs/CorelliumApi.md#v1_set_instance_peripherals) | **PUT** /v1/instances/{instanceId}/peripherals | Set Instance Peripherals
*CorelliumApi* | [**v1_set_instance_state**](docs/CorelliumApi.md#v1_set_instance_state) | **PUT** /v1/instances/{instanceId}/state | Set state of Instance
*CorelliumApi* | [**v1_snapshot_rename**](docs/CorelliumApi.md#v1_snapshot_rename) | **PATCH** /v1/snapshots/{snapshotId} | Rename a Snapshot
*CorelliumApi* | [**v1_start_core_trace**](docs/CorelliumApi.md#v1_start_core_trace) | **POST** /v1/instances/{instanceId}/strace/enable | Start CoreTrace on an instance
*CorelliumApi* | [**v1_start_instance**](docs/CorelliumApi.md#v1_start_instance) | **POST** /v1/instances/{instanceId}/start | Start an Instance
*CorelliumApi* | [**v1_start_network_monitor**](docs/CorelliumApi.md#v1_start_network_monitor) | **POST** /v1/instances/{instanceId}/sslsplit/enable | Start Network Monitor on an instance.
*CorelliumApi* | [**v1_stop_core_trace**](docs/CorelliumApi.md#v1_stop_core_trace) | **POST** /v1/instances/{instanceId}/strace/disable | Stop CoreTrace on an instance.
*CorelliumApi* | [**v1_stop_instance**](docs/CorelliumApi.md#v1_stop_instance) | **POST** /v1/instances/{instanceId}/stop | Stop an Instance
*CorelliumApi* | [**v1_stop_network_monitor**](docs/CorelliumApi.md#v1_stop_network_monitor) | **POST** /v1/instances/{instanceId}/sslsplit/disable | Stop Network Monitor on an instance.
*CorelliumApi* | [**v1_trial_requests**](docs/CorelliumApi.md#v1_trial_requests) | **POST** /v1/billing/trial-requests | Create Trial Request
*CorelliumApi* | [**v1_trial_requests_v3**](docs/CorelliumApi.md#v1_trial_requests_v3) | **POST** /v1/billing/trial-requests-v3 | Create Trial Request (v1.3)
*CorelliumApi* | [**v1_unpause_instance**](docs/CorelliumApi.md#v1_unpause_instance) | **POST** /v1/instances/{instanceId}/unpause | Unpause an Instance
*CorelliumApi* | [**v1_update_current_domain**](docs/CorelliumApi.md#v1_update_current_domain) | **PATCH** /v1/domain | Update Current Domain
*CorelliumApi* | [**v1_update_project**](docs/CorelliumApi.md#v1_update_project) | **PATCH** /v1/projects/{projectId} | Update a Project
*CorelliumApi* | [**v1_update_project_settings**](docs/CorelliumApi.md#v1_update_project_settings) | **PATCH** /v1/projects/{projectId}/settings | Change Project Settings
*CorelliumApi* | [**v1_update_user**](docs/CorelliumApi.md#v1_update_user) | **PATCH** /v1/users/{userId} | Update User
*CorelliumApi* | [**v1_upload_image_data**](docs/CorelliumApi.md#v1_upload_image_data) | **POST** /v1/images/{imageId} | Upload Image Data
*CorelliumApi* | [**v1_user_agree_terms**](docs/CorelliumApi.md#v1_user_agree_terms) | **POST** /v1/users/agree | Consent to the current terms and conditions
*CorelliumApi* | [**v1_users_change_password_post**](docs/CorelliumApi.md#v1_users_change_password_post) | **POST** /v1/users/change-password | Authenticated solely by the old-password.
*CorelliumApi* | [**v1_users_login**](docs/CorelliumApi.md#v1_users_login) | **POST** /v1/users/login | Log In
*CorelliumApi* | [**v2_trial_requests**](docs/CorelliumApi.md#v2_trial_requests) | **POST** /v2/billing/trial-requests | Create Trial Request (v2)


## Documentation For Models

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
 - [AgentValueReturn](docs/AgentValueReturn.md)
 - [AgreedAck](docs/AgreedAck.md)
 - [ApiConflictError](docs/ApiConflictError.md)
 - [ApiError](docs/ApiError.md)
 - [ApiInternalConsistencyError](docs/ApiInternalConsistencyError.md)
 - [ApiNotFoundError](docs/ApiNotFoundError.md)
 - [ApiToken](docs/ApiToken.md)
 - [Bit](docs/Bit.md)
 - [Button](docs/Button.md)
 - [Credentials](docs/Credentials.md)
 - [DomainOptions](docs/DomainOptions.md)
 - [FileChanges](docs/FileChanges.md)
 - [Firmware](docs/Firmware.md)
 - [GpioStateDefinition](docs/GpioStateDefinition.md)
 - [GrantTrialRequestResponse](docs/GrantTrialRequestResponse.md)
 - [Image](docs/Image.md)
 - [Instance](docs/Instance.md)
 - [InstanceBootOptions](docs/InstanceBootOptions.md)
 - [InstanceConsoleEndpoint](docs/InstanceConsoleEndpoint.md)
 - [InstanceCreateOptions](docs/InstanceCreateOptions.md)
 - [InstanceInput](docs/InstanceInput.md)
 - [InstanceNetmonState](docs/InstanceNetmonState.md)
 - [InstanceReturn](docs/InstanceReturn.md)
 - [InstanceServices](docs/InstanceServices.md)
 - [InstanceStartOptions](docs/InstanceStartOptions.md)
 - [InstanceState](docs/InstanceState.md)
 - [InstanceStopOptions](docs/InstanceStopOptions.md)
 - [KernelTask](docs/KernelTask.md)
 - [KernelThread](docs/KernelThread.md)
 - [MediaPlayBody](docs/MediaPlayBody.md)
 - [Model](docs/Model.md)
 - [ModelSoftware](docs/ModelSoftware.md)
 - [PasswordChangeBody](docs/PasswordChangeBody.md)
 - [PasswordResetBody](docs/PasswordResetBody.md)
 - [PatchInstanceOptions](docs/PatchInstanceOptions.md)
 - [PeripheralsData](docs/PeripheralsData.md)
 - [Project](docs/Project.md)
 - [ProjectKey](docs/ProjectKey.md)
 - [ProjectQuota](docs/ProjectQuota.md)
 - [ProjectSettings](docs/ProjectSettings.md)
 - [ProjectUsage](docs/ProjectUsage.md)
 - [RateInfo](docs/RateInfo.md)
 - [ResetLinkBody](docs/ResetLinkBody.md)
 - [RotateBody](docs/RotateBody.md)
 - [Snapshot](docs/Snapshot.md)
 - [SnapshotCreationOptions](docs/SnapshotCreationOptions.md)
 - [SnapshotStatus](docs/SnapshotStatus.md)
 - [TeamCreate](docs/TeamCreate.md)
 - [TextInput](docs/TextInput.md)
 - [Token](docs/Token.md)
 - [TouchCurveInput](docs/TouchCurveInput.md)
 - [TouchInput](docs/TouchInput.md)
 - [TrialExtension](docs/TrialExtension.md)
 - [TrialRequestMetadata](docs/TrialRequestMetadata.md)
 - [TrialRequestOptions](docs/TrialRequestOptions.md)
 - [UserError](docs/UserError.md)
 - [V1SetStateBody](docs/V1SetStateBody.md)
 - [ValidationError](docs/ValidationError.md)
 - [VolumeOptions](docs/VolumeOptions.md)
 - [VpnDefinition](docs/VpnDefinition.md)


## Documentation For Authorization


## BearerAuth

- **Type**: Bearer authentication (ApiToken or JWT)


## Author




