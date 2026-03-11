# SnapshotRequest



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limit** | **float** | Number of entries to return, defaults to 100 | [optional] 
**offset** | **float** | Number of rows to skip, defaults to 0 | [optional] 
**springboard** | **bool** | Denotes whether snapshot was a springboard snapshot | [optional] 
**live** | **bool** | Denotes whether snapshot was a live snapshot | [optional] 
**fresh** | **bool** | Denotes whether snapshot was created immediately after the device was restored | [optional] 
**device_name** | **str** | Name of device | [optional] 
**task** | **str** | Task being executed on snapshot | [optional] 
**to** | **str** | Date to filter to, keyed off of createdAt | [optional] 
**_from** | **str** | Date to filter from, keyed off of createdAt | [optional] 
**order_by** | **str** | Sorting order (&#39;-createdAt&#39; or &#39;createdAt&#39;), defaults to -createdAt | [optional] 
**search** | **str** | Last filter applied and searches on snapshot / associated instance name and snapshot / instance id | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


