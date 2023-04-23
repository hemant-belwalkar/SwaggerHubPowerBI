# swagger_client.ExcelWorkbooksApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_excel_workbook**](ExcelWorkbooksApi.md#add_excel_workbook) | **POST** /ExcelWorkbooks | Creates a new ExcelWorkbook CatalogItem.
[**add_excel_workbook_comment**](ExcelWorkbooksApi.md#add_excel_workbook_comment) | **POST** /ExcelWorkbooks({Id})/Comments | Creates a new Comment associated to the specified ExcelWorkbook.
[**delete_excel_workbook**](ExcelWorkbooksApi.md#delete_excel_workbook) | **DELETE** /ExcelWorkbooks({Id}) | Deletes the specified ExcelWorkbook.
[**delete_excel_workbook_comment**](ExcelWorkbooksApi.md#delete_excel_workbook_comment) | **DELETE** /ExcelWorkbooks({Id})/Comments({CommentId}) | Deletes the specified Comment associated to the ExcelWorkbook.
[**get_excel_workbook**](ExcelWorkbooksApi.md#get_excel_workbook) | **GET** /ExcelWorkbooks({Id}) | Gets the ExcelWorkbook CatalogItem specified by the Id.
[**get_excel_workbook_allowed_actions**](ExcelWorkbooksApi.md#get_excel_workbook_allowed_actions) | **GET** /ExcelWorkbooks({Id})/AllowedActions | Gets a list of actions allowed in the current session, user permissions and product edition capabilities are considered when querying.
[**get_excel_workbook_comments**](ExcelWorkbooksApi.md#get_excel_workbook_comments) | **GET** /ExcelWorkbooks({Id})/Comments | Gets the Comments for a ExcelWorkbook specified by the Id.
[**get_excel_workbook_content**](ExcelWorkbooksApi.md#get_excel_workbook_content) | **GET** /ExcelWorkbooks({Id})/Content/$value | Gets the content of the specified ExcelWorkbook CatalogItem specified by the Id.
[**get_excel_workbook_policies**](ExcelWorkbooksApi.md#get_excel_workbook_policies) | **GET** /ExcelWorkbooks({Id})/Policies | Gets policies associated with the specified ExcelWorkbook CatalogItem.
[**get_excel_workbook_properties**](ExcelWorkbooksApi.md#get_excel_workbook_properties) | **GET** /ExcelWorkbooks({Id})/Properties | Gets ExcelWorkbook properties (takes list of property names to retrieve the values)
[**get_excel_workbooks**](ExcelWorkbooksApi.md#get_excel_workbooks) | **GET** /ExcelWorkbooks | Gets an array of ExcelWorkbook CatalogItems.
[**set_excel_workbook_policies**](ExcelWorkbooksApi.md#set_excel_workbook_policies) | **PUT** /ExcelWorkbooks({Id})/Policies | Replaces ItemPolicies associated with the specified ExcelWorkbook item.
[**update_excel_workbook**](ExcelWorkbooksApi.md#update_excel_workbook) | **PATCH** /ExcelWorkbooks({Id}) | Updates the specified ExcelWorkbook CatalogItem using the provided definition.
[**update_excel_workbook_comment**](ExcelWorkbooksApi.md#update_excel_workbook_comment) | **PUT** /ExcelWorkbooks({Id})/Comments({CommentId}) | Updates the Comment specified by CommentId in the associated ExcelWorkbook.
[**update_excel_workbook_properties**](ExcelWorkbooksApi.md#update_excel_workbook_properties) | **PUT** /ExcelWorkbooks({Id})/Properties | Updates the ExcelWorkbook properties included in the given list.
[**upload_excel_workbook**](ExcelWorkbooksApi.md#upload_excel_workbook) | **POST** /ExcelWorkbooks({Id})/Model.Upload | Creates a new ExcelWorkbook CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.


# **add_excel_workbook**
> ExcelWorkbook add_excel_workbook(excel_workbook)

Creates a new ExcelWorkbook CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
excel_workbook = swagger_client.ExcelWorkbook() # ExcelWorkbook | The definition of the new ExcelWorkbook CatalogItem.

try:
    # Creates a new ExcelWorkbook CatalogItem.
    api_response = api_instance.add_excel_workbook(excel_workbook)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->add_excel_workbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **excel_workbook** | [**ExcelWorkbook**](ExcelWorkbook.md)| The definition of the new ExcelWorkbook CatalogItem. | 

### Return type

[**ExcelWorkbook**](ExcelWorkbook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_excel_workbook_comment**
> add_excel_workbook_comment(id, comment)

Creates a new Comment associated to the specified ExcelWorkbook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment = swagger_client.Comment() # Comment | The Comment to be created

try:
    # Creates a new Comment associated to the specified ExcelWorkbook.
    api_instance.add_excel_workbook_comment(id, comment)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->add_excel_workbook_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **comment** | [**Comment**](Comment.md)| The Comment to be created | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_excel_workbook**
> delete_excel_workbook(id)

Deletes the specified ExcelWorkbook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Deletes the specified ExcelWorkbook.
    api_instance.delete_excel_workbook(id)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->delete_excel_workbook: %s\n" % e)
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

# **delete_excel_workbook_comment**
> delete_excel_workbook_comment(id, comment_id)

Deletes the specified Comment associated to the ExcelWorkbook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment_id = 'comment_id_example' # str | The Id of the Comment.

try:
    # Deletes the specified Comment associated to the ExcelWorkbook.
    api_instance.delete_excel_workbook_comment(id, comment_id)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->delete_excel_workbook_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **comment_id** | **str**| The Id of the Comment. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excel_workbook**
> ExcelWorkbook get_excel_workbook(id)

Gets the ExcelWorkbook CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the ExcelWorkbook CatalogItem specified by the Id.
    api_response = api_instance.get_excel_workbook(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->get_excel_workbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ExcelWorkbook**](ExcelWorkbook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excel_workbook_allowed_actions**
> ODataAllowedActions get_excel_workbook_allowed_actions(id)

Gets a list of actions allowed in the current session, user permissions and product edition capabilities are considered when querying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a list of actions allowed in the current session, user permissions and product edition capabilities are considered when querying.
    api_response = api_instance.get_excel_workbook_allowed_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->get_excel_workbook_allowed_actions: %s\n" % e)
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

# **get_excel_workbook_comments**
> ODataComments get_excel_workbook_comments(id)

Gets the Comments for a ExcelWorkbook specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the Comments for a ExcelWorkbook specified by the Id.
    api_response = api_instance.get_excel_workbook_comments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->get_excel_workbook_comments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataComments**](ODataComments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excel_workbook_content**
> file get_excel_workbook_content(id)

Gets the content of the specified ExcelWorkbook CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the content of the specified ExcelWorkbook CatalogItem specified by the Id.
    api_response = api_instance.get_excel_workbook_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->get_excel_workbook_content: %s\n" % e)
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

# **get_excel_workbook_policies**
> list[ItemPolicy] get_excel_workbook_policies(id)

Gets policies associated with the specified ExcelWorkbook CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets policies associated with the specified ExcelWorkbook CatalogItem.
    api_response = api_instance.get_excel_workbook_policies(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->get_excel_workbook_policies: %s\n" % e)
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

# **get_excel_workbook_properties**
> ODataProperties get_excel_workbook_properties(id, properties=properties)

Gets ExcelWorkbook properties (takes list of property names to retrieve the values)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = ['properties_example'] # list[str] | Names for the properties to be returned. (optional)

try:
    # Gets ExcelWorkbook properties (takes list of property names to retrieve the values)
    api_response = api_instance.get_excel_workbook_properties(id, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->get_excel_workbook_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **properties** | [**list[str]**](str.md)| Names for the properties to be returned. | [optional] 

### Return type

[**ODataProperties**](ODataProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_excel_workbooks**
> ODataExcelWorkbooks get_excel_workbooks(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)

Gets an array of ExcelWorkbook CatalogItems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)
order_by = 'order_by_example' # str | Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) (optional)
select = 'select_example' # str | Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) (optional)

try:
    # Gets an array of ExcelWorkbook CatalogItems.
    api_response = api_instance.get_excel_workbooks(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->get_excel_workbooks: %s\n" % e)
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

[**ODataExcelWorkbooks**](ODataExcelWorkbooks.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_excel_workbook_policies**
> set_excel_workbook_policies(id, item_policy)

Replaces ItemPolicies associated with the specified ExcelWorkbook item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
item_policy = [swagger_client.ItemPolicy()] # list[ItemPolicy] | The ItemPolicy definitions that will be replaced.

try:
    # Replaces ItemPolicies associated with the specified ExcelWorkbook item.
    api_instance.set_excel_workbook_policies(id, item_policy)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->set_excel_workbook_policies: %s\n" % e)
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

# **update_excel_workbook**
> update_excel_workbook(id, excel_workbook)

Updates the specified ExcelWorkbook CatalogItem using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
excel_workbook = swagger_client.ExcelWorkbook() # ExcelWorkbook | Definition of the ExcelWorkbook item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged.

try:
    # Updates the specified ExcelWorkbook CatalogItem using the provided definition.
    api_instance.update_excel_workbook(id, excel_workbook)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->update_excel_workbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **excel_workbook** | [**ExcelWorkbook**](ExcelWorkbook.md)| Definition of the ExcelWorkbook item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_excel_workbook_comment**
> update_excel_workbook_comment(id, comment_id, comment)

Updates the Comment specified by CommentId in the associated ExcelWorkbook.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment_id = 'comment_id_example' # str | The Id of the Comment.
comment = swagger_client.Comment() # Comment | The Comment to be updated

try:
    # Updates the Comment specified by CommentId in the associated ExcelWorkbook.
    api_instance.update_excel_workbook_comment(id, comment_id, comment)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->update_excel_workbook_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **comment_id** | **str**| The Id of the Comment. | 
 **comment** | [**Comment**](Comment.md)| The Comment to be updated | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_excel_workbook_properties**
> update_excel_workbook_properties(id, properties)

Updates the ExcelWorkbook properties included in the given list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = [swagger_client.ModelProperty()] # list[ModelProperty] | The properties that will be updated.

try:
    # Updates the ExcelWorkbook properties included in the given list.
    api_instance.update_excel_workbook_properties(id, properties)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->update_excel_workbook_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **properties** | [**list[ModelProperty]**](ModelProperty.md)| The properties that will be updated. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_excel_workbook**
> ExcelWorkbook upload_excel_workbook(id, file)

Creates a new ExcelWorkbook CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExcelWorkbooksApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
file = '/path/to/file.txt' # file | The file contents.

try:
    # Creates a new ExcelWorkbook CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.
    api_response = api_instance.upload_excel_workbook(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExcelWorkbooksApi->upload_excel_workbook: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **file** | **file**| The file contents. | 

### Return type

[**ExcelWorkbook**](ExcelWorkbook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

