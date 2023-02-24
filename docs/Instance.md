# Instance



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Instance Identifier | [optional] 
**name** | **str** | Instance Name | [optional] 
**key** | **str** | Key used to encrypt the Instance | [optional] 
**flavor** | **str** | The type of virtual machine this is | [optional] 
**type** | **str** |  | [optional] 
**project** | **str** | The projectId of the project this instance belongs to | [optional] 
**state** | [**InstanceState**](InstanceState.md) |  | [optional] 
**state_changed** | **datetime** | Time the state of the instance last changed | [optional] 
**started_at** | **str** | Time the instance was started | [optional] 
**user_task** | **str** | Currently executing User Task | [optional] 
**task_state** | **str** | Current task state if any | [optional] 
**error** | **str** | Current error state if any | [optional] 
**boot_options** | [**InstanceBootOptions**](InstanceBootOptions.md) |  | [optional] 
**service_ip** | **str** | Services IP Address | [optional] 
**wifi_ip** | **str** | LAN IP Address | [optional] 
**secondary_ip** | **str** | Secondary Inteface LAN IP Address (if supported) | [optional] 
**services** | [**InstanceServices**](InstanceServices.md) |  | [optional] 
**panicked** | **bool** |  | [optional] 
**created** | **datetime** | Time instance was created | [optional] 
**model** | **str** | Model of virtual machine device | [optional] 
**fwpackage** | **str** | URL that package used to create this instance is available at | [optional] 
**os** | **str** |  | [optional] 
**agent** | [**InstanceAgentState**](InstanceAgentState.md) |  | [optional] 
**netmon** | [**InstanceNetmonState**](InstanceNetmonState.md) |  | [optional] 
**expose_port** | **str** |  | [optional] 
**fault** | **bool** |  | [optional] 
**patches** | **list[str]** |  | [optional] 
**created_by** | [**CreatedBy**](CreatedBy.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


