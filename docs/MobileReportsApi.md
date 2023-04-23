# swagger_client.MobileReportsApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_mobile_report**](MobileReportsApi.md#add_mobile_report) | **POST** /MobileReports | Creates new MobileReport item
[**add_mobile_report_comment**](MobileReportsApi.md#add_mobile_report_comment) | **POST** /MobileReports({Id})/Comments | Creates a new Comment associated to the specified MobileReport.
[**delete_mobile_report**](MobileReportsApi.md#delete_mobile_report) | **DELETE** /MobileReports({Id}) | Delete the specified MobileReport.
[**delete_mobile_report_comment**](MobileReportsApi.md#delete_mobile_report_comment) | **DELETE** /MobileReports({Id})/Comments({CommentId}) | Deletes the specified Comment associated to the MobileReport.
[**get_mobile_report**](MobileReportsApi.md#get_mobile_report) | **GET** /MobileReports({Id}) | Fetch MobileReport item by Id or path property.
[**get_mobile_report_allowed_actions**](MobileReportsApi.md#get_mobile_report_allowed_actions) | **GET** /MobileReports({Id})/AllowedActions | Gets a list of actions allowed in the current session; considering user permissions and product edition capabilities.
[**get_mobile_report_comments**](MobileReportsApi.md#get_mobile_report_comments) | **GET** /MobileReports({Id})/Comments | Gets the Comments for a MobileReport specified by the Id.
[**get_mobile_report_content**](MobileReportsApi.md#get_mobile_report_content) | **GET** /MobileReports({Id})/Content/$value | Gets the content of the specified MobileReport CatalogItem.
[**get_mobile_report_policies**](MobileReportsApi.md#get_mobile_report_policies) | **GET** /MobileReports({Id})/Policies | Gets ItemPolicies associated with the MobileReport catalog item.
[**get_mobile_report_properties**](MobileReportsApi.md#get_mobile_report_properties) | **GET** /MobileReports({Id})/Properties | Gets MobileReport Properties (takes list of Property names to retrieve the values)
[**get_mobile_reports**](MobileReportsApi.md#get_mobile_reports) | **GET** /MobileReports | Retrieve array of MobileReport catalog items.
[**set_mobile_report_policies**](MobileReportsApi.md#set_mobile_report_policies) | **PUT** /MobileReports({Id})/Policies | Sets ItemPolicies on the MobileReport item.
[**update_mobile_report**](MobileReportsApi.md#update_mobile_report) | **PATCH** /MobileReports({Id}) | Updates the specified MobileReport CatalogItem using the provided definition.
[**update_mobile_report_comment**](MobileReportsApi.md#update_mobile_report_comment) | **PUT** /MobileReports({Id})/Comments({CommentId}) | Updates the Comment specified by CommentId in the associated MobileReport.
[**update_mobile_report_properties**](MobileReportsApi.md#update_mobile_report_properties) | **PUT** /MobileReports({Id})/Properties | Updates the MobileReport properties included in the given list.
[**upload_mobile_report**](MobileReportsApi.md#upload_mobile_report) | **POST** /MobileReports({Id})/Model.Upload | Does an efficient binary upload of a new or existing MobileReport CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.


# **add_mobile_report**
> MobileReport add_mobile_report(body)

Creates new MobileReport item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
body = swagger_client.MobileReport() # MobileReport | The definition of the new MobileReport item.

try:
    # Creates new MobileReport item
    api_response = api_instance.add_mobile_report(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->add_mobile_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MobileReport**](MobileReport.md)| The definition of the new MobileReport item. | 

### Return type

[**MobileReport**](MobileReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_mobile_report_comment**
> add_mobile_report_comment(id, comment)

Creates a new Comment associated to the specified MobileReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment = swagger_client.Comment() # Comment | The Comment to be created

try:
    # Creates a new Comment associated to the specified MobileReport.
    api_instance.add_mobile_report_comment(id, comment)
except ApiException as e:
    print("Exception when calling MobileReportsApi->add_mobile_report_comment: %s\n" % e)
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

# **delete_mobile_report**
> delete_mobile_report(id)

Delete the specified MobileReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Delete the specified MobileReport.
    api_instance.delete_mobile_report(id)
except ApiException as e:
    print("Exception when calling MobileReportsApi->delete_mobile_report: %s\n" % e)
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

# **delete_mobile_report_comment**
> delete_mobile_report_comment(id, comment_id)

Deletes the specified Comment associated to the MobileReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment_id = 'comment_id_example' # str | The Id of the Comment.

try:
    # Deletes the specified Comment associated to the MobileReport.
    api_instance.delete_mobile_report_comment(id, comment_id)
except ApiException as e:
    print("Exception when calling MobileReportsApi->delete_mobile_report_comment: %s\n" % e)
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

# **get_mobile_report**
> MobileReport get_mobile_report(id)

Fetch MobileReport item by Id or path property.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Fetch MobileReport item by Id or path property.
    api_response = api_instance.get_mobile_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->get_mobile_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**MobileReport**](MobileReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mobile_report_allowed_actions**
> ODataAllowedActions get_mobile_report_allowed_actions(id)

Gets a list of actions allowed in the current session; considering user permissions and product edition capabilities.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a list of actions allowed in the current session; considering user permissions and product edition capabilities.
    api_response = api_instance.get_mobile_report_allowed_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->get_mobile_report_allowed_actions: %s\n" % e)
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

# **get_mobile_report_comments**
> ODataComments get_mobile_report_comments(id)

Gets the Comments for a MobileReport specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the Comments for a MobileReport specified by the Id.
    api_response = api_instance.get_mobile_report_comments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->get_mobile_report_comments: %s\n" % e)
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

# **get_mobile_report_content**
> file get_mobile_report_content(id)

Gets the content of the specified MobileReport CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the content of the specified MobileReport CatalogItem.
    api_response = api_instance.get_mobile_report_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->get_mobile_report_content: %s\n" % e)
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

# **get_mobile_report_policies**
> list[ItemPolicy] get_mobile_report_policies(id)

Gets ItemPolicies associated with the MobileReport catalog item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets ItemPolicies associated with the MobileReport catalog item.
    api_response = api_instance.get_mobile_report_policies(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->get_mobile_report_policies: %s\n" % e)
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

# **get_mobile_report_properties**
> ODataProperties get_mobile_report_properties(id, properties=properties)

Gets MobileReport Properties (takes list of Property names to retrieve the values)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = ['properties_example'] # list[str] | Names for the Properties to be returned. (optional)

try:
    # Gets MobileReport Properties (takes list of Property names to retrieve the values)
    api_response = api_instance.get_mobile_report_properties(id, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->get_mobile_report_properties: %s\n" % e)
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

# **get_mobile_reports**
> ODataMobileReport get_mobile_reports(top=top, skip=skip, filter=filter, count=count)

Retrieve array of MobileReport catalog items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)

try:
    # Retrieve array of MobileReport catalog items.
    api_response = api_instance.get_mobile_reports(top=top, skip=skip, filter=filter, count=count)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->get_mobile_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top** | **int**| Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) | [optional] 
 **skip** | **int**| Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) | [optional] 
 **filter** | **str**| Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) | [optional] 
 **count** | **str**| Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) | [optional] 

### Return type

[**ODataMobileReport**](ODataMobileReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_mobile_report_policies**
> set_mobile_report_policies(id, mobile_reports)

Sets ItemPolicies on the MobileReport item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
mobile_reports = [swagger_client.ItemPolicy()] # list[ItemPolicy] | Array of ItemPolicies to set on the MobileReport CatalogItem.

try:
    # Sets ItemPolicies on the MobileReport item.
    api_instance.set_mobile_report_policies(id, mobile_reports)
except ApiException as e:
    print("Exception when calling MobileReportsApi->set_mobile_report_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **mobile_reports** | [**list[ItemPolicy]**](ItemPolicy.md)| Array of ItemPolicies to set on the MobileReport CatalogItem. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mobile_report**
> MobileReport update_mobile_report(id, body)

Updates the specified MobileReport CatalogItem using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
body = swagger_client.MobileReport() # MobileReport | Definition of the MobileReport item that replaces the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged.

try:
    # Updates the specified MobileReport CatalogItem using the provided definition.
    api_response = api_instance.update_mobile_report(id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->update_mobile_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **body** | [**MobileReport**](MobileReport.md)| Definition of the MobileReport item that replaces the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged. | 

### Return type

[**MobileReport**](MobileReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mobile_report_comment**
> update_mobile_report_comment(id, comment_id, comment)

Updates the Comment specified by CommentId in the associated MobileReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment_id = 'comment_id_example' # str | The Id of the Comment.
comment = swagger_client.Comment() # Comment | The Comment to be updated

try:
    # Updates the Comment specified by CommentId in the associated MobileReport.
    api_instance.update_mobile_report_comment(id, comment_id, comment)
except ApiException as e:
    print("Exception when calling MobileReportsApi->update_mobile_report_comment: %s\n" % e)
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

# **update_mobile_report_properties**
> update_mobile_report_properties(id, properties)

Updates the MobileReport properties included in the given list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = [swagger_client.ModelProperty()] # list[ModelProperty] | The Properties that will be updated.

try:
    # Updates the MobileReport properties included in the given list.
    api_instance.update_mobile_report_properties(id, properties)
except ApiException as e:
    print("Exception when calling MobileReportsApi->update_mobile_report_properties: %s\n" % e)
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

# **upload_mobile_report**
> MobileReport upload_mobile_report(id, file)

Does an efficient binary upload of a new or existing MobileReport CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MobileReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
file = '/path/to/file.txt' # file | The file contents.

try:
    # Does an efficient binary upload of a new or existing MobileReport CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.
    api_response = api_instance.upload_mobile_report(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MobileReportsApi->upload_mobile_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **file** | **file**| The file contents. | 

### Return type

[**MobileReport**](MobileReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

