# TouchInput



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **object** | Finger Positions | 
**buttons** | [**list[TouchInputButtonsInner]**](TouchInputButtonsInner.md) | Buttons to be held when this position is reached. Either a Button enum object or an ASCII character. No change if not defined. | [optional] 
**normalized** | **bool** | true if you want to use normalized x,y coordinates from 0-10000 (eg 5000,5000 is always center of screen) | [optional] 
**wait** | **float** | Duration to wait before this input is executed.  Instant if not defined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


