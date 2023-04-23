# swagger_client.DataSourcesApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_data_source**](DataSourcesApi.md#add_data_source) | **POST** /DataSources | Creates a new DataSource CatalogItem.
[**check_existing_data_source_connection**](DataSourcesApi.md#check_existing_data_source_connection) | **POST** /DataSources({Id})/Model.CheckConnection | Tests the connection for a data source. This method supports the testing of published data sources that are used by reports and shared data sources
[**check_new_data_source_connection**](DataSourcesApi.md#check_new_data_source_connection) | **POST** /DataSources/Model.CheckConnection | Tests the connection for a data source. This method supports the direct testing of the unsaved data source.
[**delete_data_source**](DataSourcesApi.md#delete_data_source) | **DELETE** /DataSources({Id}) | Deletes the specified DataSource.
[**get_data_source**](DataSourcesApi.md#get_data_source) | **GET** /DataSources({Id}) | Gets a DataSource CatalogItem specified by the Id.
[**get_data_source_allowed_actions**](DataSourcesApi.md#get_data_source_allowed_actions) | **GET** /DataSources({Id})/AllowedActions | Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
[**get_data_source_content**](DataSourcesApi.md#get_data_source_content) | **GET** /DataSources({Id})/Content/$value | Gets the content of the DataSource CatalogItem specified by the Id.
[**get_data_source_dependent_items**](DataSourcesApi.md#get_data_source_dependent_items) | **GET** /DataSources({Id})/DependentItems | Returns a list of CatalogItems that reference the DataSource specified by the Id.
[**get_data_source_policies**](DataSourcesApi.md#get_data_source_policies) | **GET** /DataSources({Id})/Policies | Gets ItemPolicies associated with the DataSource specified by the Id.
[**get_data_source_query_fields**](DataSourcesApi.md#get_data_source_query_fields) | **POST** /DataSources/Model.GetQueryFields | Retrieves a dataset that contains the fields retrieved by the delivery query for a data-driven subscription.
[**get_data_sources**](DataSourcesApi.md#get_data_sources) | **GET** /DataSources | Gets an array of DataSource CatalogItems.
[**get_datasource_properties**](DataSourcesApi.md#get_datasource_properties) | **GET** /DataSources({Id})/Properties | Gets DataSource Properties (takes list of property names to retrieve the values)
[**set_data_source_policies**](DataSourcesApi.md#set_data_source_policies) | **PUT** /DataSources({Id})/Policies | Replaces ItemPolicies associated with the DataSource specified by the Id.
[**update_data_source**](DataSourcesApi.md#update_data_source) | **PATCH** /DataSources({Id}) | Updates the DataSource CatalogItem specified by the Id using the provided definition.
[**update_datasource_properties**](DataSourcesApi.md#update_datasource_properties) | **PUT** /DataSources({Id})/Properties | Updates the DataSource Properties included in the given list.
[**upload_data_source**](DataSourcesApi.md#upload_data_source) | **POST** /DataSources({Id})/Model.Upload | Does an efficient binary upload of a new or existing DataSource CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.


# **add_data_source**
> DataSource add_data_source(data_source)

Creates a new DataSource CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
data_source = swagger_client.DataSource() # DataSource | The definition of the new DataSource CatalogItem.

try:
    # Creates a new DataSource CatalogItem.
    api_response = api_instance.add_data_source(data_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->add_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source** | [**DataSource**](DataSource.md)| The definition of the new DataSource CatalogItem. | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_existing_data_source_connection**
> DataSourceCheckResult check_existing_data_source_connection(id)

Tests the connection for a data source. This method supports the testing of published data sources that are used by reports and shared data sources

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Tests the connection for a data source. This method supports the testing of published data sources that are used by reports and shared data sources
    api_response = api_instance.check_existing_data_source_connection(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->check_existing_data_source_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**DataSourceCheckResult**](DataSourceCheckResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_new_data_source_connection**
> DataSourceCheckResult check_new_data_source_connection(data_source)

Tests the connection for a data source. This method supports the direct testing of the unsaved data source.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
data_source = swagger_client.DataSource() # DataSource | The definition of data source.  Must contain connectionstring, data provider, and credentials to connect to the data source. In case of embedded data sources, Name will be null.

try:
    # Tests the connection for a data source. This method supports the direct testing of the unsaved data source.
    api_response = api_instance.check_new_data_source_connection(data_source)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->check_new_data_source_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source** | [**DataSource**](DataSource.md)| The definition of data source.  Must contain connectionstring, data provider, and credentials to connect to the data source. In case of embedded data sources, Name will be null. | 

### Return type

[**DataSourceCheckResult**](DataSourceCheckResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_source**
> delete_data_source(id)

Deletes the specified DataSource.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Deletes the specified DataSource.
    api_instance.delete_data_source(id)
except ApiException as e:
    print("Exception when calling DataSourcesApi->delete_data_source: %s\n" % e)
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

# **get_data_source**
> DataSource get_data_source(id)

Gets a DataSource CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a DataSource CatalogItem specified by the Id.
    api_response = api_instance.get_data_source(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_source_allowed_actions**
> ODataAllowedActions get_data_source_allowed_actions(id)

Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
    api_response = api_instance.get_data_source_allowed_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_data_source_allowed_actions: %s\n" % e)
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

# **get_data_source_content**
> file get_data_source_content(id)

Gets the content of the DataSource CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the content of the DataSource CatalogItem specified by the Id.
    api_response = api_instance.get_data_source_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_data_source_content: %s\n" % e)
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

# **get_data_source_dependent_items**
> ODataDependentItems get_data_source_dependent_items(id)

Returns a list of CatalogItems that reference the DataSource specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Returns a list of CatalogItems that reference the DataSource specified by the Id.
    api_response = api_instance.get_data_source_dependent_items(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_data_source_dependent_items: %s\n" % e)
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

# **get_data_source_policies**
> list[ItemPolicy] get_data_source_policies(id)

Gets ItemPolicies associated with the DataSource specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets ItemPolicies associated with the DataSource specified by the Id.
    api_response = api_instance.get_data_source_policies(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_data_source_policies: %s\n" % e)
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

# **get_data_source_query_fields**
> ODataQueryFields get_data_source_query_fields(query_fields_request=query_fields_request)

Retrieves a dataset that contains the fields retrieved by the delivery query for a data-driven subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
query_fields_request = swagger_client.QueryFieldsRequest() # QueryFieldsRequest |  (optional)

try:
    # Retrieves a dataset that contains the fields retrieved by the delivery query for a data-driven subscription.
    api_response = api_instance.get_data_source_query_fields(query_fields_request=query_fields_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_data_source_query_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_fields_request** | [**QueryFieldsRequest**](QueryFieldsRequest.md)|  | [optional] 

### Return type

[**ODataQueryFields**](ODataQueryFields.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_data_sources**
> ODataDataSources get_data_sources(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)

Gets an array of DataSource CatalogItems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)
order_by = 'order_by_example' # str | Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) (optional)
select = 'select_example' # str | Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) (optional)

try:
    # Gets an array of DataSource CatalogItems.
    api_response = api_instance.get_data_sources(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_data_sources: %s\n" % e)
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

[**ODataDataSources**](ODataDataSources.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasource_properties**
> ODataProperties get_datasource_properties(id, properties=properties)

Gets DataSource Properties (takes list of property names to retrieve the values)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = ['properties_example'] # list[str] | Names for the Properties to be returned. (optional)

try:
    # Gets DataSource Properties (takes list of property names to retrieve the values)
    api_response = api_instance.get_datasource_properties(id, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->get_datasource_properties: %s\n" % e)
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

# **set_data_source_policies**
> set_data_source_policies(id, item_policy)

Replaces ItemPolicies associated with the DataSource specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
item_policy = [swagger_client.ItemPolicy()] # list[ItemPolicy] | The ItemPolicy definitions that will be replaced.

try:
    # Replaces ItemPolicies associated with the DataSource specified by the Id.
    api_instance.set_data_source_policies(id, item_policy)
except ApiException as e:
    print("Exception when calling DataSourcesApi->set_data_source_policies: %s\n" % e)
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

# **update_data_source**
> update_data_source(id, data_source)

Updates the DataSource CatalogItem specified by the Id using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_source = swagger_client.DataSource() # DataSource | Definition of the DataSource item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged.

try:
    # Updates the DataSource CatalogItem specified by the Id using the provided definition.
    api_instance.update_data_source(id, data_source)
except ApiException as e:
    print("Exception when calling DataSourcesApi->update_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_source** | [**DataSource**](DataSource.md)| Definition of the DataSource item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_datasource_properties**
> update_datasource_properties(id, properties)

Updates the DataSource Properties included in the given list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = [swagger_client.ModelProperty()] # list[ModelProperty] | The Properties that will be updated.

try:
    # Updates the DataSource Properties included in the given list.
    api_instance.update_datasource_properties(id, properties)
except ApiException as e:
    print("Exception when calling DataSourcesApi->update_datasource_properties: %s\n" % e)
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

# **upload_data_source**
> DataSource upload_data_source(id, file)

Does an efficient binary upload of a new or existing DataSource CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataSourcesApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
file = '/path/to/file.txt' # file | The file contents.

try:
    # Does an efficient binary upload of a new or existing DataSource CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.
    api_response = api_instance.upload_data_source(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataSourcesApi->upload_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **file** | **file**| The file contents. | 

### Return type

[**DataSource**](DataSource.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

