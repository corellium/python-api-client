# ActivityRequest



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource** | **str** | Resource filter | [optional] 
**limit** | **float** | Number of entries to return, defaults to 10 | [optional] 
**order_by** | **str** | Sorting order (&#39;-createdAt&#39; or &#39;createdAt&#39;) | [optional] 
**page** | **float** | Paginated results. Must be a positive integer. If not provided, defaults to the first page. | [optional] 
**instance** | **str** | Instance identifier used to filter instance resources | [optional] 
**project** | **str** | Instance identifier used to filter instance resources | [optional] 
**actor** | **str** | Actor identifier used to filter actor resources | [optional] 
**search** | **str** | Last filter applied and is a fuzzy match on results | [optional] 
**to** | **str** | Date to filter to, keyed off of createdAt | [optional] 
**_from** | **str** | Date to filter from, keyed off of createdAt | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


