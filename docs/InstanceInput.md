# InstanceInput



## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**position** | **object** | Finger Positions | 
**buttons** | [**list[TouchInputButtonsInner]**](TouchInputButtonsInner.md) | Buttons to be held when this position is reached. Either a Button enum object or an ASCII character. No change if not defined. | [optional] 
**normalized** | **bool** | true if you want to use normalized x,y coordinates from 0-10000 (eg 5000,5000 is always center of screen) | [optional] 
**wait** | **float** | Duration to wait before this input is executed.  Instant if not defined. | [optional] 
**start** | **object** | Finger Positions | 
**end** | **object** | Finger Positions | 
**bezier_points** | **list[object]** | array of per-finger intermediate touch positions, up to 10 depending on model.  Straight line if not defined. | [optional] 
**start_buttons** | [**list[TouchInputButtonsInner]**](TouchInputButtonsInner.md) | Buttons to be held during this curve. | 
**end_buttons** | [**list[TouchInputButtonsInner]**](TouchInputButtonsInner.md) | Buttons to be left held after this curve.  Same as startButtons if not defined. | [optional] 
**duration** | **float** | Duration to execute this curve over. | 
**required** | **str** | text to type | 
**key_duration** | **float** | How long to take to type each key.  150ms if not defined. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


