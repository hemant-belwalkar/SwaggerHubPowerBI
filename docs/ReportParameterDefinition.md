# ReportParameterDefinition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_blank** | **bool** | A boolean value that indicates whether the ReportParamter is allowed to be blank. | [optional] 
**default_values** | **list[str]** | An array of string values that specify the ReportParameter&#39;s default values. If the parameter is multi-valued then the array can have more than one entry. | [optional] 
**default_values_is_null** | **bool** |  A boolean value that indicates whether the DefaultValues property is NULL. | [optional] 
**default_values_query_based** | **bool** | A boolean value that indicates whether the ReportParamter&#39;s default values are obtained from a query (instead of being static specified values). | [optional] 
**dependencies** | **list[str]** | An array of string values that specify the dependencies for the ReportParameter. | [optional] 
**error_message** | **str** | Error returned when validating parameters. | [optional] 
**multi_value** | **bool** | A boolean value that indicates whether the ReportParameter is multivalued. | [optional] 
**name** | **str** | A string value that specifies the name for the ReportParameter. This name will typically be displayed in the user interface. | [optional] 
**nullable** | **bool** | A boolean value that indicates whether the ReportParameter is allowed to be null. | [optional] 
**parameter_state** | [**ReportParameterState**](ReportParameterState.md) |  | [optional] 
**parameter_type** | [**ReportParameterType**](ReportParameterType.md) |  | [optional] 
**parameter_visibility** | [**ReportParameterVisibility**](ReportParameterVisibility.md) |  | [optional] 
**prompt** | **str** | A string value that specifies text used to prompt a user for the value of the ReportParameter. | [optional] 
**prompt_user** | **bool** | A boolean value that indicates whether the user should be prompted for the value for the ReportParameter. | [optional] 
**query_parameter** | **bool** | A boolean value that indicates whether the ReportParamter is query based. | [optional] 
**valid_values** | [**list[ValidValue]**](ValidValue.md) |  | [optional] 
**valid_values_is_null** | **bool** | A boolean value that indicates whether the ValidValues property is NULL. | [optional] 
**valid_values_query_based** | **bool** | A boolean value that indicates whether the ReportParameter&#39;s valid values are obtained from a query (instead of being static specified values). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


