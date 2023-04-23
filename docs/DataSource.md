# DataSource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** | A Boolean value that specifies whether the DataSource is enabled for use. | [optional] 
**connection_string** | **str** | A string value that can be passed to a data source in order to begin the process of establishing connection. | [optional] 
**data_model_data_source** | [**DataModelDataSource**](DataModelDataSource.md) |  | [optional] 
**data_source_sub_type** | **str** | Subtype of the datasource type. Applies to PowerBIReports. Ignored when used with DataSets, LinkedReports, and Reports. | [optional] 
**data_source_type** | **str** | DataSource extension such as &#39;SQL&#39;. Applies to DataSets, LinkedReports, and Reports. Ignored when used with PowerBIReports. For PowerBIReports, use DataSourceSubType &#x3D; DataModel and DataModelDataSource.Type. | [optional] 
**is_original_connection_string_expression_based** | **bool** | Indicates whether the original connection string for the datasource was expression-based. Applies to DataSets, LinkedReports, and Reports. Ignored when used with PowerBIReports. | [optional] 
**is_connection_string_overridden** | **bool** | Specifies whether the original connection string is overridden. Applies to DataSets, LinkedReports, and Reports. Ignored when used with PowerBIReports. | [optional] 
**credentials_by_user** | [**CredentialsSuppliedByUser**](CredentialsSuppliedByUser.md) |  | [optional] 
**credentials_in_server** | [**CredentialsStoredInServer**](CredentialsStoredInServer.md) |  | [optional] 
**is_reference** | **bool** | Indicates whether this is a reference to a shared data source or an embedded data source. Applies to DataSets, LinkedReports, and Reports. Ignored when used with PowerBIReports. | [optional] 
**subscriptions** | [**Subscription**](Subscription.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


