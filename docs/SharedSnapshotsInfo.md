# SharedSnapshotsInfo



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | UUID of the snapshot | 
**name** | **str** | Snapshot name | 
**model** | **str** | Device model | 
**shared_on** | **float** | UNIX Date of when the snapshot was first shared with member | 
**shared_with_member** | **str** | The member who the snapshot was shared with. Only present in sharedWithUser | [optional] 
**shared_by** | [**SnapshotOwner**](SnapshotOwner.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


