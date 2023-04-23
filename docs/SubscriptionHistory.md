# SubscriptionHistory

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | A unique identifier by which this Subscription History record can be referenced in requests or in other defined objects. | [optional] 
**subscription_id** | **str** | A unique UUID value that identifies the Subscription that this record is associated with. | [optional] 
**type** | **str** | A string value that specifies the type of subscription execution. | [optional] 
**start_time** | **datetime** | A string that contains the date-time for when the subscription execution started. | [optional] 
**end_time** | **datetime** | A string that contains the date-time for when the subscription execution ended. | [optional] 
**subscription_status** | **str** | A string value that represents the status of the subscription execution. | [optional] 
**message** | **str** | A string value that contains message that describes the status of the subscription execution. | [optional] 
**details** | **str** | A JSON string value that contains the session information and error details when a subscription execution fails. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


