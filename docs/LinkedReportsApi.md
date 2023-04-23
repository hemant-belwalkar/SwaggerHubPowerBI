# swagger_client.LinkedReportsApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_linked_report**](LinkedReportsApi.md#add_linked_report) | **POST** /LinkedReports | Creates a new LinkedReport CatalogItem.
[**add_linked_report_comment**](LinkedReportsApi.md#add_linked_report_comment) | **POST** /LinkedReports({Id})/Comments | Creates a new Comment associated to the specified LinkedReport.
[**add_linked_report_history_snapshot**](LinkedReportsApi.md#add_linked_report_history_snapshot) | **POST** /LinkedReports({Id})/HistorySnapshots | Creates new HistorySnapshot
[**delete_linked_report**](LinkedReportsApi.md#delete_linked_report) | **DELETE** /LinkedReports({Id}) | Deletes the specified LinkedReport.
[**delete_linked_report_comment**](LinkedReportsApi.md#delete_linked_report_comment) | **DELETE** /LinkedReports({Id})/Comments({CommentId}) | Deletes the specified Comment associated to the LinkedReport.
[**delete_linked_report_history_snapshot**](LinkedReportsApi.md#delete_linked_report_history_snapshot) | **DELETE** /LinkedReports({Id})/HistorySnapshots({HistoryId}) | Deletes a HistorySnapshot specified by HistoryId from the LinkedReport specified by Id.
[**get_linked_report**](LinkedReportsApi.md#get_linked_report) | **GET** /LinkedReports({Id}) | Gets a LinkedReport CatalogItem specified by the Id.
[**get_linked_report_allowed_actions**](LinkedReportsApi.md#get_linked_report_allowed_actions) | **GET** /LinkedReports({Id})/AllowedActions | Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
[**get_linked_report_cache_options**](LinkedReportsApi.md#get_linked_report_cache_options) | **GET** /LinkedReports({Id})/CacheOptions | Gets the content of CacheOptions for the LinkedReport specified by the Id.
[**get_linked_report_cache_refresh_plans**](LinkedReportsApi.md#get_linked_report_cache_refresh_plans) | **GET** /LinkedReports({Id})/CacheRefreshPlans | Gets the CacheRefreshPlans for a LinkedReport specified by the Id.
[**get_linked_report_comments**](LinkedReportsApi.md#get_linked_report_comments) | **GET** /LinkedReports({Id})/Comments | Gets the Comments for a LinkedReport specified by the Id.
[**get_linked_report_history_snapshot**](LinkedReportsApi.md#get_linked_report_history_snapshot) | **GET** /LinkedReports({Id})/HistorySnapshots({HistoryId}) | Gets requested HistorySnapshot item specified by HistoryId of the LinkedReport specified by Id.
[**get_linked_report_history_snapshot_options**](LinkedReportsApi.md#get_linked_report_history_snapshot_options) | **GET** /LinkedReports({Id})/HistorySnapshotOptions | Gets HistorySnapshotOptions for the specified LinkedReport.
[**get_linked_report_history_snapshots**](LinkedReportsApi.md#get_linked_report_history_snapshots) | **GET** /LinkedReports({Id})/HistorySnapshots | Get a list of HistorySnapshots of the LinkedReport specified by Id.
[**get_linked_report_parameter_definitions**](LinkedReportsApi.md#get_linked_report_parameter_definitions) | **GET** /LinkedReports({Id})/ParameterDefinitions | Gets the ParameterDefinitions associated with the LinkedReport specified by the Id.
[**get_linked_report_policies**](LinkedReportsApi.md#get_linked_report_policies) | **GET** /LinkedReports({Id})/Policies | Gets ItemPolicies associated with the specified LinkedReport CatalogItem.
[**get_linked_report_properties**](LinkedReportsApi.md#get_linked_report_properties) | **GET** /LinkedReports({Id})/Properties | Gets LinkedReport Properties (takes list of Property names to retrieve the values)
[**get_linked_reports**](LinkedReportsApi.md#get_linked_reports) | **GET** /LinkedReports | Gets an array of LinkedReport CatalogItems.
[**set_linked_report_cache_options**](LinkedReportsApi.md#set_linked_report_cache_options) | **PUT** /LinkedReports({Id})/CacheOptions | Replaces the CacheOption&#39;s content for a given LinkedReport using the provided definition.
[**set_linked_report_history_snapshot_options**](LinkedReportsApi.md#set_linked_report_history_snapshot_options) | **PUT** /LinkedReports({Id})/HistorySnapshotOptions | Updates HistorySnapshotOptions property.
[**set_linked_report_policies**](LinkedReportsApi.md#set_linked_report_policies) | **PUT** /LinkedReports({Id})/Policies | Replaces ItemPolicies associated with the specified LinkedReport item.
[**update_linked_report**](LinkedReportsApi.md#update_linked_report) | **PATCH** /LinkedReports({Id}) | Updates the specified LinkedReport CatalogItem using the provided definition.
[**update_linked_report_comment**](LinkedReportsApi.md#update_linked_report_comment) | **PUT** /LinkedReports({Id})/Comments({CommentId}) | Updates the Comment specified by CommentId in the associated LinkedReport.
[**update_linked_report_parameter_definitions**](LinkedReportsApi.md#update_linked_report_parameter_definitions) | **PATCH** /LinkedReports({Id})/ParameterDefinitions | Updates the ParameterDefinitions associated with the specified LinkedReport by the Id.
[**update_linked_report_properties**](LinkedReportsApi.md#update_linked_report_properties) | **PUT** /LinkedReports({Id})/Properties | Updates the LinkedReport Properties included in the given list.


# **add_linked_report**
> LinkedReport add_linked_report(linked_report)

Creates a new LinkedReport CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
linked_report = swagger_client.LinkedReport() # LinkedReport | The definition of the new LinkedReport CatalogItem.

try:
    # Creates a new LinkedReport CatalogItem.
    api_response = api_instance.add_linked_report(linked_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->add_linked_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **linked_report** | [**LinkedReport**](LinkedReport.md)| The definition of the new LinkedReport CatalogItem. | 

### Return type

[**LinkedReport**](LinkedReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_linked_report_comment**
> add_linked_report_comment(id, comment)

Creates a new Comment associated to the specified LinkedReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment = swagger_client.Comment() # Comment | The Comment to be created

try:
    # Creates a new Comment associated to the specified LinkedReport.
    api_instance.add_linked_report_comment(id, comment)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->add_linked_report_comment: %s\n" % e)
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

# **add_linked_report_history_snapshot**
> bool add_linked_report_history_snapshot(id)

Creates new HistorySnapshot

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Creates new HistorySnapshot
    api_response = api_instance.add_linked_report_history_snapshot(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->add_linked_report_history_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_linked_report**
> delete_linked_report(id)

Deletes the specified LinkedReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Deletes the specified LinkedReport.
    api_instance.delete_linked_report(id)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->delete_linked_report: %s\n" % e)
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

# **delete_linked_report_comment**
> delete_linked_report_comment(id, comment_id)

Deletes the specified Comment associated to the LinkedReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment_id = 'comment_id_example' # str | The Id of the Comment.

try:
    # Deletes the specified Comment associated to the LinkedReport.
    api_instance.delete_linked_report_comment(id, comment_id)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->delete_linked_report_comment: %s\n" % e)
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

# **delete_linked_report_history_snapshot**
> bool delete_linked_report_history_snapshot(id, history_id)

Deletes a HistorySnapshot specified by HistoryId from the LinkedReport specified by Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
history_id = 'history_id_example' # str | The Id property of the HistorySnapshot

try:
    # Deletes a HistorySnapshot specified by HistoryId from the LinkedReport specified by Id.
    api_response = api_instance.delete_linked_report_history_snapshot(id, history_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->delete_linked_report_history_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **history_id** | **str**| The Id property of the HistorySnapshot | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_report**
> LinkedReport get_linked_report(id)

Gets a LinkedReport CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a LinkedReport CatalogItem specified by the Id.
    api_response = api_instance.get_linked_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**LinkedReport**](LinkedReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_report_allowed_actions**
> ODataAllowedActions get_linked_report_allowed_actions(id)

Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
    api_response = api_instance.get_linked_report_allowed_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_allowed_actions: %s\n" % e)
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

# **get_linked_report_cache_options**
> CacheOptions get_linked_report_cache_options(id)

Gets the content of CacheOptions for the LinkedReport specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the content of CacheOptions for the LinkedReport specified by the Id.
    api_response = api_instance.get_linked_report_cache_options(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_cache_options: %s\n" % e)
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

# **get_linked_report_cache_refresh_plans**
> ODataCacheRefreshPlans get_linked_report_cache_refresh_plans(id)

Gets the CacheRefreshPlans for a LinkedReport specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the CacheRefreshPlans for a LinkedReport specified by the Id.
    api_response = api_instance.get_linked_report_cache_refresh_plans(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_cache_refresh_plans: %s\n" % e)
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

# **get_linked_report_comments**
> ODataComments get_linked_report_comments(id)

Gets the Comments for a LinkedReport specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the Comments for a LinkedReport specified by the Id.
    api_response = api_instance.get_linked_report_comments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_comments: %s\n" % e)
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

# **get_linked_report_history_snapshot**
> HistorySnapshot get_linked_report_history_snapshot(id, history_id)

Gets requested HistorySnapshot item specified by HistoryId of the LinkedReport specified by Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
history_id = 'history_id_example' # str | The Id property of the HistorySnapshot

try:
    # Gets requested HistorySnapshot item specified by HistoryId of the LinkedReport specified by Id.
    api_response = api_instance.get_linked_report_history_snapshot(id, history_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_history_snapshot: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **history_id** | **str**| The Id property of the HistorySnapshot | 

### Return type

[**HistorySnapshot**](HistorySnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_report_history_snapshot_options**
> HistorySnapshotOptions get_linked_report_history_snapshot_options(id)

Gets HistorySnapshotOptions for the specified LinkedReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets HistorySnapshotOptions for the specified LinkedReport.
    api_response = api_instance.get_linked_report_history_snapshot_options(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_history_snapshot_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**HistorySnapshotOptions**](HistorySnapshotOptions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_report_history_snapshots**
> list[HistorySnapshot] get_linked_report_history_snapshots(id)

Get a list of HistorySnapshots of the LinkedReport specified by Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Get a list of HistorySnapshots of the LinkedReport specified by Id.
    api_response = api_instance.get_linked_report_history_snapshots(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_history_snapshots: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**list[HistorySnapshot]**](HistorySnapshot.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_linked_report_parameter_definitions**
> ODataReportParameterDefinitions get_linked_report_parameter_definitions(id)

Gets the ParameterDefinitions associated with the LinkedReport specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the ParameterDefinitions associated with the LinkedReport specified by the Id.
    api_response = api_instance.get_linked_report_parameter_definitions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_parameter_definitions: %s\n" % e)
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

# **get_linked_report_policies**
> list[ItemPolicy] get_linked_report_policies(id)

Gets ItemPolicies associated with the specified LinkedReport CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets ItemPolicies associated with the specified LinkedReport CatalogItem.
    api_response = api_instance.get_linked_report_policies(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_policies: %s\n" % e)
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

# **get_linked_report_properties**
> ODataProperties get_linked_report_properties(id, properties=properties)

Gets LinkedReport Properties (takes list of Property names to retrieve the values)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = ['properties_example'] # list[str] | Names for the Properties to be returned. (optional)

try:
    # Gets LinkedReport Properties (takes list of Property names to retrieve the values)
    api_response = api_instance.get_linked_report_properties(id, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_report_properties: %s\n" % e)
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

# **get_linked_reports**
> ODataLinkedReports get_linked_reports(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)

Gets an array of LinkedReport CatalogItems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)
order_by = 'order_by_example' # str | Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) (optional)
select = 'select_example' # str | Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) (optional)

try:
    # Gets an array of LinkedReport CatalogItems.
    api_response = api_instance.get_linked_reports(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->get_linked_reports: %s\n" % e)
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

[**ODataLinkedReports**](ODataLinkedReports.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_linked_report_cache_options**
> set_linked_report_cache_options(id, cache_options)

Replaces the CacheOption's content for a given LinkedReport using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
cache_options = swagger_client.CacheOptions() # CacheOptions | Updated definition for the CacheOption's content associated with the LinkedReport specified by the Id.

try:
    # Replaces the CacheOption's content for a given LinkedReport using the provided definition.
    api_instance.set_linked_report_cache_options(id, cache_options)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->set_linked_report_cache_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **cache_options** | [**CacheOptions**](CacheOptions.md)| Updated definition for the CacheOption&#39;s content associated with the LinkedReport specified by the Id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_linked_report_history_snapshot_options**
> set_linked_report_history_snapshot_options(id, history_snapshot_options)

Updates HistorySnapshotOptions property.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
history_snapshot_options = swagger_client.HistorySnapshotOptions() # HistorySnapshotOptions | Modified HistorySnapshotOptions object.

try:
    # Updates HistorySnapshotOptions property.
    api_instance.set_linked_report_history_snapshot_options(id, history_snapshot_options)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->set_linked_report_history_snapshot_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **history_snapshot_options** | [**HistorySnapshotOptions**](HistorySnapshotOptions.md)| Modified HistorySnapshotOptions object. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_linked_report_policies**
> set_linked_report_policies(id, item_policy)

Replaces ItemPolicies associated with the specified LinkedReport item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
item_policy = [swagger_client.ItemPolicy()] # list[ItemPolicy] | The ItemPolicy definitions that will be replaced.

try:
    # Replaces ItemPolicies associated with the specified LinkedReport item.
    api_instance.set_linked_report_policies(id, item_policy)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->set_linked_report_policies: %s\n" % e)
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

# **update_linked_report**
> update_linked_report(id, linked_report)

Updates the specified LinkedReport CatalogItem using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
linked_report = swagger_client.LinkedReport() # LinkedReport | Definition of the LinkedReport item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged.

try:
    # Updates the specified LinkedReport CatalogItem using the provided definition.
    api_instance.update_linked_report(id, linked_report)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->update_linked_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **linked_report** | [**LinkedReport**](LinkedReport.md)| Definition of the LinkedReport item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_linked_report_comment**
> update_linked_report_comment(id, comment_id, comment)

Updates the Comment specified by CommentId in the associated LinkedReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment_id = 'comment_id_example' # str | The Id of the Comment.
comment = swagger_client.Comment() # Comment | The Comment to be updated

try:
    # Updates the Comment specified by CommentId in the associated LinkedReport.
    api_instance.update_linked_report_comment(id, comment_id, comment)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->update_linked_report_comment: %s\n" % e)
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

# **update_linked_report_parameter_definitions**
> update_linked_report_parameter_definitions(id, parameter_definitions)

Updates the ParameterDefinitions associated with the specified LinkedReport by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
parameter_definitions = [swagger_client.ReportParameterDefinitionPatch()] # list[ReportParameterDefinitionPatch] | Updated definitions for the ParameterDefinitions associated with the LinkedReport, represented as ParameterDefinitionsPatch objects. It is only necessary to include properties to be updated. All other property values will be left unchanged.

try:
    # Updates the ParameterDefinitions associated with the specified LinkedReport by the Id.
    api_instance.update_linked_report_parameter_definitions(id, parameter_definitions)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->update_linked_report_parameter_definitions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **parameter_definitions** | [**list[ReportParameterDefinitionPatch]**](ReportParameterDefinitionPatch.md)| Updated definitions for the ParameterDefinitions associated with the LinkedReport, represented as ParameterDefinitionsPatch objects. It is only necessary to include properties to be updated. All other property values will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_linked_report_properties**
> update_linked_report_properties(id, properties)

Updates the LinkedReport Properties included in the given list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.LinkedReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = [swagger_client.ModelProperty()] # list[ModelProperty] | The Properties that will be updated.

try:
    # Updates the LinkedReport Properties included in the given list.
    api_instance.update_linked_report_properties(id, properties)
except ApiException as e:
    print("Exception when calling LinkedReportsApi->update_linked_report_properties: %s\n" % e)
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

