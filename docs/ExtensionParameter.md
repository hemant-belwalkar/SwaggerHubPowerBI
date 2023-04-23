# ExtensionParameter

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | A string value that specifies the name for the ExtensionParameter. | [optional] 
**display_name** | **str** | The name of the extension setting that is displayed to the user. | [optional] 
**required** | **bool** | Indicates whether the value is required. | [optional] 
**read_only** | **bool** | Indicates whether the setting is read-only. | [optional] 
**value** | **str** | A string that represents the value of an extension parameter. | [optional] 
**error** | **str** | An error that describes a problem with the value of the setting. | [optional] 
**encrypted** | **bool** | Indicates whether the extension parameter value should be encrypted in the Report Server database. | [optional] 
**is_password** | **bool** | A Boolean value that indicates whether the ExtensionParameter is a password. | [optional] 
**valid_values** | [**list[ValidValue]**](ValidValue.md) | A set of values that can be configured for the setting. | [optional] 
**valid_values_is_null** | **bool** | A Boolean value that indicates whether the ValidValues property is null. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


