# swagger_client.CatalogItemsApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_catalog_item**](CatalogItemsApi.md#add_catalog_item) | **POST** /CatalogItems | Creates a new CatalogItem.
[**delete_catalog_item**](CatalogItemsApi.md#delete_catalog_item) | **DELETE** /CatalogItems({Id}) | Deletes the specified CatalogItem.
[**delete_catalog_items**](CatalogItemsApi.md#delete_catalog_items) | **POST** /CatalogItems/Model.DeleteItems | Deletes the given list of items
[**get_catalog_item**](CatalogItemsApi.md#get_catalog_item) | **GET** /CatalogItems({Id}) | Gets a CatalogItem specified by the Id.
[**get_catalog_item_content**](CatalogItemsApi.md#get_catalog_item_content) | **GET** /CatalogItems({Id})/Content/$value | Gets the content of the specified CatalogItem specified by the Id.
[**get_catalog_item_policies**](CatalogItemsApi.md#get_catalog_item_policies) | **GET** /CatalogItems({Id})/Policies | Gets ItemPolicies associated with the specified CatalogItem.
[**get_catalog_item_properties**](CatalogItemsApi.md#get_catalog_item_properties) | **GET** /CatalogItems({Id})/Properties | Gets the specified Properties for the CatalogItem (takes list of Property names to retrieve the values)
[**get_catalog_item_roles**](CatalogItemsApi.md#get_catalog_item_roles) | **GET** /CatalogItems({Id})/Roles | Gets the list of available Roles for the CatalogItem
[**get_catalog_items**](CatalogItemsApi.md#get_catalog_items) | **GET** /CatalogItems | Gets an array of CatalogItems.
[**move_catalog_items**](CatalogItemsApi.md#move_catalog_items) | **POST** /CatalogItems/Model.MoveItems | Moves given list of items to target folder.
[**set_catalog_item_policies**](CatalogItemsApi.md#set_catalog_item_policies) | **PUT** /CatalogItems({Id})/Policies | Replaces ItemPolicies associated with the specified CatalogItem.
[**update_catalog_item**](CatalogItemsApi.md#update_catalog_item) | **PATCH** /CatalogItems({Id}) | Updates the specified CatalogItem using the provided definition.
[**update_catalog_item_properties**](CatalogItemsApi.md#update_catalog_item_properties) | **PUT** /CatalogItems({Id})/Properties | Updates a CatalogItem&#39;s Properties with the list of given properties.


# **add_catalog_item**
> CatalogItem add_catalog_item(catalog_item)

Creates a new CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
catalog_item = swagger_client.CatalogItem() # CatalogItem | The definition of the new CatalogItem.

try:
    # Creates a new CatalogItem.
    api_response = api_instance.add_catalog_item(catalog_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->add_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **catalog_item** | [**CatalogItem**](CatalogItem.md)| The definition of the new CatalogItem. | 

### Return type

[**CatalogItem**](CatalogItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_catalog_item**
> delete_catalog_item(id)

Deletes the specified CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Deletes the specified CatalogItem.
    api_instance.delete_catalog_item(id)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->delete_catalog_item: %s\n" % e)
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

# **delete_catalog_items**
> BulkOperationsResult delete_catalog_items(delete_items_request)

Deletes the given list of items

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
delete_items_request = swagger_client.DeleteItemsRequest() # DeleteItemsRequest | List of catalog item paths to delete.

try:
    # Deletes the given list of items
    api_response = api_instance.delete_catalog_items(delete_items_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->delete_catalog_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delete_items_request** | [**DeleteItemsRequest**](DeleteItemsRequest.md)| List of catalog item paths to delete. | 

### Return type

[**BulkOperationsResult**](BulkOperationsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_item**
> CatalogItem get_catalog_item(id)

Gets a CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a CatalogItem specified by the Id.
    api_response = api_instance.get_catalog_item(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->get_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**CatalogItem**](CatalogItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_item_content**
> file get_catalog_item_content(id)

Gets the content of the specified CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the content of the specified CatalogItem specified by the Id.
    api_response = api_instance.get_catalog_item_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->get_catalog_item_content: %s\n" % e)
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

# **get_catalog_item_policies**
> list[ItemPolicy] get_catalog_item_policies(id)

Gets ItemPolicies associated with the specified CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets ItemPolicies associated with the specified CatalogItem.
    api_response = api_instance.get_catalog_item_policies(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->get_catalog_item_policies: %s\n" % e)
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

# **get_catalog_item_properties**
> ODataProperties get_catalog_item_properties(id, properties=properties)

Gets the specified Properties for the CatalogItem (takes list of Property names to retrieve the values)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = ['properties_example'] # list[str] | Comma-separated list of Property names to be returned. (optional)

try:
    # Gets the specified Properties for the CatalogItem (takes list of Property names to retrieve the values)
    api_response = api_instance.get_catalog_item_properties(id, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->get_catalog_item_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **properties** | [**list[str]**](str.md)| Comma-separated list of Property names to be returned. | [optional] 

### Return type

[**ODataProperties**](ODataProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_item_roles**
> ODataProperties1 get_catalog_item_roles(id)

Gets the list of available Roles for the CatalogItem

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the list of available Roles for the CatalogItem
    api_response = api_instance.get_catalog_item_roles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->get_catalog_item_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataProperties1**](ODataProperties1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_catalog_items**
> ODataCatalogItems get_catalog_items(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)

Gets an array of CatalogItems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)
order_by = 'order_by_example' # str | Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) (optional)
select = 'select_example' # str | Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) (optional)

try:
    # Gets an array of CatalogItems.
    api_response = api_instance.get_catalog_items(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->get_catalog_items: %s\n" % e)
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

[**ODataCatalogItems**](ODataCatalogItems.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_catalog_items**
> BulkOperationsResult move_catalog_items(move_items_request)

Moves given list of items to target folder.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
move_items_request = swagger_client.MoveItemsRequest() # MoveItemsRequest | List of catalog item paths and target folder.

try:
    # Moves given list of items to target folder.
    api_response = api_instance.move_catalog_items(move_items_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->move_catalog_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **move_items_request** | [**MoveItemsRequest**](MoveItemsRequest.md)| List of catalog item paths and target folder. | 

### Return type

[**BulkOperationsResult**](BulkOperationsResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_catalog_item_policies**
> set_catalog_item_policies(id, catalog_item)

Replaces ItemPolicies associated with the specified CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
catalog_item = [swagger_client.ItemPolicy()] # list[ItemPolicy] | The ItemPolicy definitions that will be replaced.

try:
    # Replaces ItemPolicies associated with the specified CatalogItem.
    api_instance.set_catalog_item_policies(id, catalog_item)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->set_catalog_item_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **catalog_item** | [**list[ItemPolicy]**](ItemPolicy.md)| The ItemPolicy definitions that will be replaced. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_item**
> update_catalog_item(id, catalog_item)

Updates the specified CatalogItem using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
catalog_item = swagger_client.CatalogItem() # CatalogItem | Definition of the CatalogItem that updates the current item on the server. The type for the defintion can be any of the supported CatalogItemTypes. It is only necessary to include properties to be updated. All other property values will be left unchanged.

try:
    # Updates the specified CatalogItem using the provided definition.
    api_instance.update_catalog_item(id, catalog_item)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->update_catalog_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **catalog_item** | [**CatalogItem**](CatalogItem.md)| Definition of the CatalogItem that updates the current item on the server. The type for the defintion can be any of the supported CatalogItemTypes. It is only necessary to include properties to be updated. All other property values will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_catalog_item_properties**
> update_catalog_item_properties(id, properties)

Updates a CatalogItem's Properties with the list of given properties.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = [swagger_client.ModelProperty()] # list[ModelProperty] | The Properties that will be updated. It is only necessary to include properties to be updated. All other property values will be left unchanged.

try:
    # Updates a CatalogItem's Properties with the list of given properties.
    api_instance.update_catalog_item_properties(id, properties)
except ApiException as e:
    print("Exception when calling CatalogItemsApi->update_catalog_item_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **properties** | [**list[ModelProperty]**](ModelProperty.md)| The Properties that will be updated. It is only necessary to include properties to be updated. All other property values will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

