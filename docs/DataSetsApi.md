# swagger_client.DataSetsApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_set**](DataSetsApi.md#add_data_set) | **POST** /DataSets | Creates a new DataSet CatalogItem.
[**delete_data_set**](DataSetsApi.md#delete_data_set) | **DELETE** /DataSets({Id}) | Deletes the specified DataSet.
[**get_data_set**](DataSetsApi.md#get_data_set) | **GET** /DataSets({Id}) | Gets a DataSet CatalogItem specified by the Id.
[**get_data_set_aggregated_value**](DataSetsApi.md#get_data_set_aggregated_value) | **POST** /DataSets({Id})/Model.GetAggregatedValue | Gets the value for the specified DataSet column using the given aggregation type.
[**get_data_set_allowed_actions**](DataSetsApi.md#get_data_set_allowed_actions) | **GET** /DataSets({Id})/AllowedActions | Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
[**get_data_set_cache_options**](DataSetsApi.md#get_data_set_cache_options) | **GET** /DataSets({Id})/CacheOptions | Gets the CacheOption&#39;s content for a given DataSet.
[**get_data_set_cache_refresh_plans**](DataSetsApi.md#get_data_set_cache_refresh_plans) | **GET** /DataSets({Id})/CacheRefreshPlans | Gets the CacheRefreshPlans for a given DataSet.
[**get_data_set_content**](DataSetsApi.md#get_data_set_content) | **GET** /DataSets({Id})/Content/$value | Gets the content of the specified DataSet CatalogItem specified by the Id.
[**get_data_set_data**](DataSetsApi.md#get_data_set_data) | **POST** /DataSets({Id})/Model.GetData | Gets the query results for the specified DataSet.
[**get_data_set_data_source**](DataSetsApi.md#get_data_set_data_source) | **GET** /DataSets({Id})/DataSources({DataSourceId}) | Gets the DataSource specified by the DataSourceId that is associated with the DataSet.
[**get_data_set_data_sources**](DataSetsApi.md#get_data_set_data_sources) | **GET** /DataSets({Id})/DataSources | Gets the DataSources associated with the specified DataSet.
[**get_data_set_dependent_items**](DataSetsApi.md#get_data_set_dependent_items) | **GET** /DataSets({Id})/DependentItems | Returns a list of CatalogItems that reference the specified DataSet.
[**get_data_set_o_data_feed**](DataSetsApi.md#get_data_set_o_data_feed) | **GET** /DataSets({Id})/Data | Gets the data for a given DataSet. With the exception of the ID property, columns that are defined in the DataSet will be returned as open or dynamic types in the result.
[**get_data_set_parameter_definitions**](DataSetsApi.md#get_data_set_parameter_definitions) | **GET** /DataSets({Id})/ParameterDefinitions | Gets the ParameterDefinitions associated with the specified DataSet.
[**get_data_set_policies**](DataSetsApi.md#get_data_set_policies) | **GET** /DataSets({Id})/Policies | Gets ItemPolicies associated with the specified DataSet CatalogItem.
[**get_data_set_schema**](DataSetsApi.md#get_data_set_schema) | **GET** /DataSets({Id})/Model.GetSchema | Gets the schema for the specified DataSet.
[**get_data_sets**](DataSetsApi.md#get_data_sets) | **GET** /DataSets | Gets an array of DataSet CatalogItems.
[**get_dataset_properties**](DataSetsApi.md#get_dataset_properties) | **GET** /DataSets({Id})/Properties | Gets DataSet Properties (takes list of property names to retrieve the values)
[**set_data_set_cache_options**](DataSetsApi.md#set_data_set_cache_options) | **PUT** /DataSets({Id})/CacheOptions | Replaces the CacheOption&#39;s content for a given DataSet using the provided definition.
[**set_data_set_data_source**](DataSetsApi.md#set_data_set_data_source) | **PUT** /DataSets({Id})/DataSources({DataSourceId}) | Updates the DataSource specified by the DataSourceId that is associated with the DataSet.
[**set_data_set_data_sources**](DataSetsApi.md#set_data_set_data_sources) | **PUT** /DataSets({Id})/DataSources | Updates the DataSource definition associated with the specified DataSet.
[**set_data_set_policies**](DataSetsApi.md#set_data_set_policies) | **PUT** /DataSets({Id})/Policies | Replaces ItemPolicies associated with the specified DataSet item.
[**update_data_set**](DataSetsApi.md#update_data_set) | **PATCH** /DataSets({Id}) | Updates the specified DataSet CatalogItem using the provided definition.
[**update_data_set_parameter_definitions**](DataSetsApi.md#update_data_set_parameter_definitions) | **PATCH** /DataSets({Id})/ParameterDefinitions | Updates the ParameterDefinitions associated with the DataSet specified.
[**update_dataset_properties**](DataSetsApi.md#update_dataset_properties) | **PUT** /DataSets({Id})/Properties | Updates the DataSet Properties included in the given list.
[**upload_data_set**](DataSetsApi.md#upload_data_set) | **POST** /DataSets({Id})/Model.Upload | Does an efficient binary upload of a new or existing DataSet CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.


# **add_data_set**
> DataSet add_data_set(data_set)

Creates a new DataSet CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
data_set = swagger_client.DataSet() # DataSet | The definition of the new DataSet CatalogItem.

try:
    # Creates a new DataSet CatalogItem.
    api_response = api_instance.add_data_set(data_set)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->add_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_set** | [**DataSet**](DataSet.md)| The definition of the new DataSet CatalogItem. | 

### Return type

[**DataSet**](DataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_set**
> delete_data_set(id)

Deletes the specified DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Deletes the specified DataSet.
    api_instance.delete_data_set(id)
except ApiException as e:
    print("Exception when calling DataSetsApi->delete_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set**
> DataSet get_data_set(id)

Gets a DataSet CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a DataSet CatalogItem specified by the Id.
    api_response = api_instance.get_data_set(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**DataSet**](DataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_aggregated_value**
> list[float] get_data_set_aggregated_value(id, column_name, aggregation, parameters=parameters)

Gets the value for the specified DataSet column using the given aggregation type.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
column_name = 'column_name_example' # str | The name of the DataSet column to aggregate the value for.
aggregation = 'aggregation_example' # str | The type of aggregation to use on the specified column. Values come from the KpiSharedDataItemAggregation enum.
parameters = swagger_client.DataSetAggregateValueParameters() # DataSetAggregateValueParameters | An array of DataSet parameters to use when executing the query. (optional)

try:
    # Gets the value for the specified DataSet column using the given aggregation type.
    api_response = api_instance.get_data_set_aggregated_value(id, column_name, aggregation, parameters=parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_aggregated_value: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **column_name** | **str**| The name of the DataSet column to aggregate the value for. | 
 **aggregation** | **str**| The type of aggregation to use on the specified column. Values come from the KpiSharedDataItemAggregation enum. | 
 **parameters** | [**DataSetAggregateValueParameters**](DataSetAggregateValueParameters.md)| An array of DataSet parameters to use when executing the query. | [optional] 

### Return type

**list[float]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_allowed_actions**
> ODataAllowedActions get_data_set_allowed_actions(id)

Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
    api_response = api_instance.get_data_set_allowed_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_allowed_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataAllowedActions**](ODataAllowedActions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_cache_options**
> CacheOptions get_data_set_cache_options(id)

Gets the CacheOption's content for a given DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the CacheOption's content for a given DataSet.
    api_response = api_instance.get_data_set_cache_options(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_cache_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**CacheOptions**](CacheOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_cache_refresh_plans**
> ODataCacheRefreshPlans get_data_set_cache_refresh_plans(id)

Gets the CacheRefreshPlans for a given DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the CacheRefreshPlans for a given DataSet.
    api_response = api_instance.get_data_set_cache_refresh_plans(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_cache_refresh_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataCacheRefreshPlans**](ODataCacheRefreshPlans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_content**
> file get_data_set_content(id)

Gets the content of the specified DataSet CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the content of the specified DataSet CatalogItem specified by the Id.
    api_response = api_instance.get_data_set_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_data**
> DataSetData get_data_set_data(id, max_rows=max_rows, parameters=parameters)

Gets the query results for the specified DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
max_rows = 8.14 # float | Specifies the maximum number of rows to return from the query. (optional)
parameters = swagger_client.DataSetDataParameters() # DataSetDataParameters | An array of DataSet parameters to use when executing the query. (optional)

try:
    # Gets the query results for the specified DataSet.
    api_response = api_instance.get_data_set_data(id, max_rows=max_rows, parameters=parameters)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **max_rows** | **float**| Specifies the maximum number of rows to return from the query. | [optional] 
 **parameters** | [**DataSetDataParameters**](DataSetDataParameters.md)| An array of DataSet parameters to use when executing the query. | [optional] 

### Return type

[**DataSetData**](DataSetData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_data_source**
> DataSource get_data_set_data_source(id, data_source_id)

Gets the DataSource specified by the DataSourceId that is associated with the DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_source_id = 'data_source_id_example' # str | The Id of the DataSource associated with the DataSet.

try:
    # Gets the DataSource specified by the DataSourceId that is associated with the DataSet.
    api_response = api_instance.get_data_set_data_source(id, data_source_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_source_id** | **str**| The Id of the DataSource associated with the DataSet. | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_data_sources**
> list[DataSource] get_data_set_data_sources(id)

Gets the DataSources associated with the specified DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the DataSources associated with the specified DataSet.
    api_response = api_instance.get_data_set_data_sources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_data_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**list[DataSource]**](DataSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_dependent_items**
> ODataDependentItems get_data_set_dependent_items(id)

Returns a list of CatalogItems that reference the specified DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Returns a list of CatalogItems that reference the specified DataSet.
    api_response = api_instance.get_data_set_dependent_items(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_dependent_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataDependentItems**](ODataDependentItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_o_data_feed**
> ODataDataSetRows get_data_set_o_data_feed(id)

Gets the data for a given DataSet. With the exception of the ID property, columns that are defined in the DataSet will be returned as open or dynamic types in the result.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the data for a given DataSet. With the exception of the ID property, columns that are defined in the DataSet will be returned as open or dynamic types in the result.
    api_response = api_instance.get_data_set_o_data_feed(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_o_data_feed: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataDataSetRows**](ODataDataSetRows.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_parameter_definitions**
> ODataReportParameterDefinitions get_data_set_parameter_definitions(id)

Gets the ParameterDefinitions associated with the specified DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the ParameterDefinitions associated with the specified DataSet.
    api_response = api_instance.get_data_set_parameter_definitions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_parameter_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataReportParameterDefinitions**](ODataReportParameterDefinitions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_policies**
> list[ItemPolicy] get_data_set_policies(id)

Gets ItemPolicies associated with the specified DataSet CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets ItemPolicies associated with the specified DataSet CatalogItem.
    api_response = api_instance.get_data_set_policies(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**list[ItemPolicy]**](ItemPolicy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_set_schema**
> DataSetSchema get_data_set_schema(id)

Gets the schema for the specified DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the schema for the specified DataSet.
    api_response = api_instance.get_data_set_schema(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_set_schema: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**DataSetSchema**](DataSetSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_sets**
> ODataDataSets get_data_sets(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)

Gets an array of DataSet CatalogItems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)
order_by = 'order_by_example' # str | Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) (optional)
select = 'select_example' # str | Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) (optional)

try:
    # Gets an array of DataSet CatalogItems.
    api_response = api_instance.get_data_sets(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_data_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top** | **int**| Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) | [optional] 
 **skip** | **int**| Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) | [optional] 
 **filter** | **str**| Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) | [optional] 
 **count** | **str**| Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) | [optional] 
 **order_by** | **str**| Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) | [optional] 
 **select** | **str**| Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) | [optional] 

### Return type

[**ODataDataSets**](ODataDataSets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_properties**
> ODataProperties get_dataset_properties(id, properties=properties)

Gets DataSet Properties (takes list of property names to retrieve the values)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = ['properties_example'] # list[str] | Names for the Properties to be returned. (optional)

try:
    # Gets DataSet Properties (takes list of property names to retrieve the values)
    api_response = api_instance.get_dataset_properties(id, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->get_dataset_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **properties** | [**list[str]**](str.md)| Names for the Properties to be returned. | [optional] 

### Return type

[**ODataProperties**](ODataProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_set_cache_options**
> set_data_set_cache_options(id, cache_options)

Replaces the CacheOption's content for a given DataSet using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
cache_options = swagger_client.CacheOptions() # CacheOptions | Updated definition for the CacheOption's content associated with the given DataSet.

try:
    # Replaces the CacheOption's content for a given DataSet using the provided definition.
    api_instance.set_data_set_cache_options(id, cache_options)
except ApiException as e:
    print("Exception when calling DataSetsApi->set_data_set_cache_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **cache_options** | [**CacheOptions**](CacheOptions.md)| Updated definition for the CacheOption&#39;s content associated with the given DataSet. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_set_data_source**
> set_data_set_data_source(id, data_source_id, data_source)

Updates the DataSource specified by the DataSourceId that is associated with the DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_source_id = 'data_source_id_example' # str | The Id of the DataSource associated with the DataSet.
data_source = swagger_client.DataSource() # DataSource | Updated definition for the DataSource associated with the DataSet.

try:
    # Updates the DataSource specified by the DataSourceId that is associated with the DataSet.
    api_instance.set_data_set_data_source(id, data_source_id, data_source)
except ApiException as e:
    print("Exception when calling DataSetsApi->set_data_set_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_source_id** | **str**| The Id of the DataSource associated with the DataSet. | 
 **data_source** | [**DataSource**](DataSource.md)| Updated definition for the DataSource associated with the DataSet. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_set_data_sources**
> set_data_set_data_sources(id, data_source)

Updates the DataSource definition associated with the specified DataSet.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_source = swagger_client.DataSource() # DataSource | Updated definition for the DataSource associated with the specified DataSet CatalogItem.

try:
    # Updates the DataSource definition associated with the specified DataSet.
    api_instance.set_data_set_data_sources(id, data_source)
except ApiException as e:
    print("Exception when calling DataSetsApi->set_data_set_data_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_source** | [**DataSource**](DataSource.md)| Updated definition for the DataSource associated with the specified DataSet CatalogItem. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_data_set_policies**
> set_data_set_policies(id, item_policy)

Replaces ItemPolicies associated with the specified DataSet item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
item_policy = [swagger_client.ItemPolicy()] # list[ItemPolicy] | The ItemPolicy definitions that will be replaced.

try:
    # Replaces ItemPolicies associated with the specified DataSet item.
    api_instance.set_data_set_policies(id, item_policy)
except ApiException as e:
    print("Exception when calling DataSetsApi->set_data_set_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **item_policy** | [**list[ItemPolicy]**](ItemPolicy.md)| The ItemPolicy definitions that will be replaced. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_set**
> update_data_set(id, data_set)

Updates the specified DataSet CatalogItem using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_set = swagger_client.DataSet() # DataSet | Definition of the DataSet item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged.

try:
    # Updates the specified DataSet CatalogItem using the provided definition.
    api_instance.update_data_set(id, data_set)
except ApiException as e:
    print("Exception when calling DataSetsApi->update_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_set** | [**DataSet**](DataSet.md)| Definition of the DataSet item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_data_set_parameter_definitions**
> update_data_set_parameter_definitions(id, parameter_definitions)

Updates the ParameterDefinitions associated with the DataSet specified.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
parameter_definitions = [swagger_client.ReportParameterDefinitionPatch()] # list[ReportParameterDefinitionPatch] | Updated definitions for the ParameterDefinitions associated with the DataSet, represented as ParameterDefinitionsPatch objects. It is only necessary to include properties to be updated. All other property valueswill be left unchanged.

try:
    # Updates the ParameterDefinitions associated with the DataSet specified.
    api_instance.update_data_set_parameter_definitions(id, parameter_definitions)
except ApiException as e:
    print("Exception when calling DataSetsApi->update_data_set_parameter_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **parameter_definitions** | [**list[ReportParameterDefinitionPatch]**](ReportParameterDefinitionPatch.md)| Updated definitions for the ParameterDefinitions associated with the DataSet, represented as ParameterDefinitionsPatch objects. It is only necessary to include properties to be updated. All other property valueswill be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset_properties**
> update_dataset_properties(id, properties)

Updates the DataSet Properties included in the given list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = [swagger_client.ModelProperty()] # list[ModelProperty] | The Properties that will be updated.

try:
    # Updates the DataSet Properties included in the given list.
    api_instance.update_dataset_properties(id, properties)
except ApiException as e:
    print("Exception when calling DataSetsApi->update_dataset_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **properties** | [**list[ModelProperty]**](ModelProperty.md)| The Properties that will be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_data_set**
> DataSet upload_data_set(id, file)

Does an efficient binary upload of a new or existing DataSet CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSetsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
file = '/path/to/file.txt' # file | The file contents.

try:
    # Does an efficient binary upload of a new or existing DataSet CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.
    api_response = api_instance.upload_data_set(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSetsApi->upload_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **file** | **file**| The file contents. | 

### Return type

[**DataSet**](DataSet.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

