# CacheRefreshPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique UUID value that specifies the identifier by which this CacheRefreshPlan can be referenced in the definition of other items. | [optional] 
**owner** | **str** | A string value that specifies the owner of the CacheRefreshPlan. | [optional] 
**description** | **str** | A string value that contains descriptive text about the CacheRefreshPlan. | [optional] 
**catalog_item_path** | **str** | A string value that contains the fully qualified URL path location of the CatalogItem that represents the CacheRefreshPlan. | [optional] 
**event_type** | **str** | A string value that specifies which EventType to use for logging. | [optional] 
**schedule** | [**ScheduleReference**](ScheduleReference.md) |  | [optional] 
**last_run_time** | **datetime** | A date-time value that specifies the date-time of the last run of the CacheRefreshPlan. | [optional] 
**last_status** | **str** | A string value that contains the network username of the last user to modify the CacheRefreshPlan. | [optional] 
**modified_by** | **str** | A string value that contains the network user name of the last user to modify the CacheRefreshPlan | [optional] 
**modified_date** | **datetime** | A string value that contains the date-time of the last modification to the CacheRefreshPlan. | [optional] 
**parameter_values** | [**list[ParameterValue]**](ParameterValue.md) | An array of parameter values for the CacheRefreshPlan. All parameters without a default value MUST have a value specified. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


