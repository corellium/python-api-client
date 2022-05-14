# corellium-api
REST API to manage your virtual devices.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 3.10.0-13354
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
import corellium_api
from corellium_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.corellium.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = corellium_api.Configuration(
    host = "https://app.corellium.com/api"
)



# Enter a context with an instance of the API client
with corellium_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = corellium_api.CorelliumApi(api_client)
    body = {
  "username": "admin",
  "password": "password"
} # object | Authorization data ( Credentials|ApiToken )

    try:
        # Log In
        api_response = api_instance.v1_auth_login(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CorelliumApi->v1_auth_login: %s\n" % e)
    
```

## Documentation for API Endpoints

All URIs are relative to *https://app.corellium.com/api*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CorelliumApi* | [**v1_auth_login**](docs/CorelliumApi.md#v1_auth_login) | **POST** /v1/auth/login | Log In
*CorelliumApi* | [**v1_create_image**](docs/CorelliumApi.md#v1_create_image) | **POST** /v1/images | Create a new Image
*CorelliumApi* | [**v1_create_instance**](docs/CorelliumApi.md#v1_create_instance) | **POST** /v1/instances | Create Instance
*CorelliumApi* | [**v1_create_snapshot**](docs/CorelliumApi.md#v1_create_snapshot) | **POST** /v1/instances/{instanceId}/snapshots | Create Instance Snapshot
*CorelliumApi* | [**v1_delete_image**](docs/CorelliumApi.md#v1_delete_image) | **DELETE** /v2/images/{imageId} | Delete Image
*CorelliumApi* | [**v1_delete_instance**](docs/CorelliumApi.md#v1_delete_instance) | **DELETE** /v1/instances/{instanceId} | Remove Instance
*CorelliumApi* | [**v1_get_image**](docs/CorelliumApi.md#v1_get_image) | **GET** /v1/images/{imageId} | Get Image Metadata
*CorelliumApi* | [**v1_get_images**](docs/CorelliumApi.md#v1_get_images) | **GET** /v1/images | Get all Images Metadata
*CorelliumApi* | [**v1_get_instance**](docs/CorelliumApi.md#v1_get_instance) | **GET** /v1/instances/{instanceId} | Get Instance
*CorelliumApi* | [**v1_get_instance_console**](docs/CorelliumApi.md#v1_get_instance_console) | **GET** /v1/instances/{instanceId}/console | Get console websocket URL
*CorelliumApi* | [**v1_get_instance_gpios**](docs/CorelliumApi.md#v1_get_instance_gpios) | **GET** /v1/instances/{instanceId}/gpios | Get Instance GPIOs
*CorelliumApi* | [**v1_get_instance_peripherals**](docs/CorelliumApi.md#v1_get_instance_peripherals) | **GET** /v1/instances/{instanceId}/peripherals | Get Instance Peripherals
*CorelliumApi* | [**v1_get_instance_screenshot**](docs/CorelliumApi.md#v1_get_instance_screenshot) | **GET** /v1/instances/{instanceId}/screenshot.{format} | Get Instance Screenshot
*CorelliumApi* | [**v1_get_instance_state**](docs/CorelliumApi.md#v1_get_instance_state) | **GET** /v1/instances/{instanceId}/state | Get state of Instance
*CorelliumApi* | [**v1_get_instances**](docs/CorelliumApi.md#v1_get_instances) | **GET** /v1/instances | Get Instances
*CorelliumApi* | [**v1_get_model_software**](docs/CorelliumApi.md#v1_get_model_software) | **GET** /v1/models/{model}/software | Get Software for Model
*CorelliumApi* | [**v1_get_models**](docs/CorelliumApi.md#v1_get_models) | **GET** /v1/models | Get Supported Models
*CorelliumApi* | [**v1_get_project**](docs/CorelliumApi.md#v1_get_project) | **GET** /v1/projects/{projectId} | Get Project
*CorelliumApi* | [**v1_get_project_instances**](docs/CorelliumApi.md#v1_get_project_instances) | **GET** /v1/projects/{projectId}/instances | Get Instances in Project
*CorelliumApi* | [**v1_get_project_vpn_config**](docs/CorelliumApi.md#v1_get_project_vpn_config) | **GET** /v1/projects/{projectId}/vpnconfig/{format} | Get Project VPN Configuration
*CorelliumApi* | [**v1_get_projects**](docs/CorelliumApi.md#v1_get_projects) | **GET** /v1/projects | Get Projects
*CorelliumApi* | [**v1_get_snapshot**](docs/CorelliumApi.md#v1_get_snapshot) | **GET** /v1/instances/{instanceId}/snapshots/{snapshotId} | Get Instance Snapshots
*CorelliumApi* | [**v1_get_snapshots**](docs/CorelliumApi.md#v1_get_snapshots) | **GET** /v1/instances/{instanceId}/snapshots | Get Instance Snapshots
*CorelliumApi* | [**v1_patch_instance**](docs/CorelliumApi.md#v1_patch_instance) | **PATCH** /v1/instances/{instanceId} | Update Instance
*CorelliumApi* | [**v1_pause_instance**](docs/CorelliumApi.md#v1_pause_instance) | **POST** /v1/instances/{instanceId}/pause | Pause an Instance
*CorelliumApi* | [**v1_ready**](docs/CorelliumApi.md#v1_ready) | **GET** /v1/ready | API Status
*CorelliumApi* | [**v1_reboot_instance**](docs/CorelliumApi.md#v1_reboot_instance) | **POST** /v1/instances/{instanceId}/reboot | Reboot an Instance
*CorelliumApi* | [**v1_restore_snapshot**](docs/CorelliumApi.md#v1_restore_snapshot) | **POST** /v1/instances/{instanceId}/snapshots/{snapshotId}/restore | Restore a Snapshot
*CorelliumApi* | [**v1_set_instance_gpios**](docs/CorelliumApi.md#v1_set_instance_gpios) | **PUT** /v1/instances/{instanceId}/gpios | Set Instance GPIOs
*CorelliumApi* | [**v1_set_instance_peripherals**](docs/CorelliumApi.md#v1_set_instance_peripherals) | **PUT** /v1/instances/{instanceId}/peripherals | Set Instance Peripherals
*CorelliumApi* | [**v1_set_instance_state**](docs/CorelliumApi.md#v1_set_instance_state) | **PUT** /v1/instances/{instanceId}/state | Set state of Instance
*CorelliumApi* | [**v1_snapshot_delete**](docs/CorelliumApi.md#v1_snapshot_delete) | **DELETE** /v1/instances/{instanceId}/snapshots/{snapshotId} | Delete a Snapshot
*CorelliumApi* | [**v1_snapshot_rename**](docs/CorelliumApi.md#v1_snapshot_rename) | **PATCH** /v1/instances/{instanceId}/snapshots/{snapshotId} | Rename a Snapshot
*CorelliumApi* | [**v1_start_instance**](docs/CorelliumApi.md#v1_start_instance) | **POST** /v1/instances/{instanceId}/start | Start an Instance
*CorelliumApi* | [**v1_stop_instance**](docs/CorelliumApi.md#v1_stop_instance) | **POST** /v1/instances/{instanceId}/stop | Stop an Instance
*CorelliumApi* | [**v1_unpause_instance**](docs/CorelliumApi.md#v1_unpause_instance) | **POST** /v1/instances/{instanceId}/unpause | Unpause an Instance
*CorelliumApi* | [**v1_upload_image_data**](docs/CorelliumApi.md#v1_upload_image_data) | **POST** /v1/images/{imageId} | Upload Image Data
*CorelliumApi* | [**v1_users_login**](docs/CorelliumApi.md#v1_users_login) | **POST** /v1/users/login | Log In


## Documentation For Models

 - [ApiConflictError](docs/ApiConflictError.md)
 - [ApiError](docs/ApiError.md)
 - [ApiNotFoundError](docs/ApiNotFoundError.md)
 - [ApiToken](docs/ApiToken.md)
 - [Bit](docs/Bit.md)
 - [Credentials](docs/Credentials.md)
 - [Firmware](docs/Firmware.md)
 - [GpioStateDefinition](docs/GpioStateDefinition.md)
 - [Image](docs/Image.md)
 - [Instance](docs/Instance.md)
 - [InstanceBootOptions](docs/InstanceBootOptions.md)
 - [InstanceConsoleEndpoint](docs/InstanceConsoleEndpoint.md)
 - [InstanceCreateOptions](docs/InstanceCreateOptions.md)
 - [InstanceNetmonState](docs/InstanceNetmonState.md)
 - [InstanceReturn](docs/InstanceReturn.md)
 - [InstanceServices](docs/InstanceServices.md)
 - [InstanceStartOptions](docs/InstanceStartOptions.md)
 - [InstanceState](docs/InstanceState.md)
 - [InstanceStopOptions](docs/InstanceStopOptions.md)
 - [Model](docs/Model.md)
 - [ModelSoftware](docs/ModelSoftware.md)
 - [PeripheralsData](docs/PeripheralsData.md)
 - [Project](docs/Project.md)
 - [ProjectQuota](docs/ProjectQuota.md)
 - [ProjectSettings](docs/ProjectSettings.md)
 - [ProjectUsage](docs/ProjectUsage.md)
 - [Snapshot](docs/Snapshot.md)
 - [SnapshotCreationOptions](docs/SnapshotCreationOptions.md)
 - [SnapshotStatus](docs/SnapshotStatus.md)
 - [Token](docs/Token.md)
 - [UserError](docs/UserError.md)
 - [V1SetStateBody](docs/V1SetStateBody.md)
 - [VolumeOptions](docs/VolumeOptions.md)
 - [VpnDefinition](docs/VpnDefinition.md)


## Documentation For Authorization


## BearerAuth

- **Type**: Bearer authentication (ApiToken or JWT)


## Author



