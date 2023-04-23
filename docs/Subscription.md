# Subscription

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique UUID value that specifies the identifier by which this Subscription can be referenced in requests or in other defined objects. | [optional] 
**owner** | **str** | A string value that specifies the owner of the Subscription. | [optional] 
**is_data_driven** | **bool** | A boolean value that specifies whether the members of the distribution list for the subscription are computed based on data. | [optional] 
**description** | **str** | A string value that contains descriptive text about the Subscription. | [optional] 
**report** | **str** | A string value that specifies the path of the report for this Subscription. | [optional] 
**is_active** | **bool** | A boolean value that specifies whether the Subscription is currently active. | [optional] 
**event_type** | **str** | A string specifying the type of event that triggers the Subscription. | [optional] 
**schedule_description** | **str** | A string value that contains descriptive text about the schedule referenced in the Schedule property. | [optional] 
**last_run_time** | **datetime** | A string value that contains the date-time that the schedule was last run. | [optional] 
**last_status** | **str** | A string specifying the Status of the last run. | [optional] 
**extension_settings** | [**ExtensionSettings**](ExtensionSettings.md) |  | [optional] 
**delivery_extension** | **str** | An object that specifies the DeliveryExtension that will be used with this Schedule&#39;s report delivery. | [optional] 
**localized_delivery_extension_name** | **str** | Localized version of extension name when available. | [optional] 
**modified_by** | **str** | A string value that contains the network user name of the last user to modify the subscription. | [optional] 
**modified_date** | **datetime** | A string value that contains the date-time of the last modification to the subscription. | [optional] 
**parameter_values** | [**list[ParameterValue]**](ParameterValue.md) | An array of items of type ParameterValue that specify the parameter values for the subscription. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


