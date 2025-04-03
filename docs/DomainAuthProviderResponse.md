# DomainAuthProviderResponse



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Provider ID | 
**id** | **str** | Provider ID for backward compatibility with frontend | [optional] 
**provider_type** | **str** | Provider Type | 
**provider** | **str** | Provider Type for backward compatibility with frontend | [optional] 
**label** | **str** | Login Button Text | 
**name** | **str** | Title Text for the Frontend&#39;s Provider Configuration Form | [optional] 
**authorization_url** | **str** | Coordinator endpoint for Authorizing with this provider | [optional] 
**default** | **bool** | True: Configured in coordinator.json, False: Custom Domain Provider | 
**enabled** | **bool** | Enabled/Disabled | 
**config** | [**OpenIDConfig**](OpenIDConfig.md) |  | [optional] 
**created_by** | **str** | Optional User ID of creator | [optional] 
**created_at** | **str** | Created Date in ISO-8601 format e.g. 2022-05-06T02:39:23.000Z | 
**updated_at** | **str** | Updated Date in ISO-8601 format e.g. 2022-05-06T02:39:23.000Z | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


