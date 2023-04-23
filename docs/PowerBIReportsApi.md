# swagger_client.PowerBIReportsApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_power_bi_report**](PowerBIReportsApi.md#add_power_bi_report) | **POST** /PowerBIReports | Creates a new PowerBIReport CatalogItem.
[**add_power_bi_report_comment**](PowerBIReportsApi.md#add_power_bi_report_comment) | **POST** /PowerBIReports({Id})/Comments | Creates a new Comment associated to the specified PowerBIReport.
[**check_power_bi_report_data_source_connection**](PowerBIReportsApi.md#check_power_bi_report_data_source_connection) | **POST** /PowerBIReports({Id})/Model.CheckDataSourceConnection | Checks the status of the specified DataSource connection.
[**delete_power_bi_report**](PowerBIReportsApi.md#delete_power_bi_report) | **DELETE** /PowerBIReports({Id}) | Deletes the specified PowerBIReport.
[**delete_power_bi_report_comment**](PowerBIReportsApi.md#delete_power_bi_report_comment) | **DELETE** /PowerBIReports({Id})/Comments({CommentId}) | Deletes the specified Comment associated to the PowerBIReport.
[**get_power_bi_cache_refresh_plans**](PowerBIReportsApi.md#get_power_bi_cache_refresh_plans) | **GET** /PowerBIReports({Id})/CacheRefreshPlans | Gets the CacheRefreshPlans for a given Power BI Report.
[**get_power_bi_report**](PowerBIReportsApi.md#get_power_bi_report) | **GET** /PowerBIReports({Id}) | Gets a PowerBIReport CatalogItem specified by the Id.
[**get_power_bi_report_allowed_actions**](PowerBIReportsApi.md#get_power_bi_report_allowed_actions) | **GET** /PowerBIReports({Id})/AllowedActions | Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
[**get_power_bi_report_comments**](PowerBIReportsApi.md#get_power_bi_report_comments) | **GET** /PowerBIReports({Id})/Comments | Gets the Comments for a PowerBIReport specified by the Id.
[**get_power_bi_report_content**](PowerBIReportsApi.md#get_power_bi_report_content) | **GET** /PowerBIReports({Id})/Content/$value | Gets the content of the specified PowerBIReport CatalogItem.
[**get_power_bi_report_data_model_parameters**](PowerBIReportsApi.md#get_power_bi_report_data_model_parameters) | **GET** /PowerBIReports({Id})/DataModelParameters | Gets the data model parameters that are associated with the specified PowerBIReport.
[**get_power_bi_report_data_model_role_assignments**](PowerBIReportsApi.md#get_power_bi_report_data_model_role_assignments) | **GET** /PowerBIReports({Id})/DataModelRoleAssignments | Gets the data model role assignments that are associated with the specified PowerBIReport.
[**get_power_bi_report_data_model_roles**](PowerBIReportsApi.md#get_power_bi_report_data_model_roles) | **GET** /PowerBIReports({Id})/DataModelRoles | Gets the data model roles that are associated with the specified PowerBIReport.
[**get_power_bi_report_data_sources**](PowerBIReportsApi.md#get_power_bi_report_data_sources) | **GET** /PowerBIReports({Id})/DataSources | Gets the DataSources that are associated with the specified PowerBIReport.
[**get_power_bi_report_policies**](PowerBIReportsApi.md#get_power_bi_report_policies) | **GET** /PowerBIReports({Id})/Policies | Gets ItemPolicies associated with the specified PowerBIReport CatalogItem.
[**get_power_bi_report_properties**](PowerBIReportsApi.md#get_power_bi_report_properties) | **GET** /PowerBIReports({Id})/Properties | Gets PowerBIReports Properties (takes list of Property names to retrieve the values)
[**get_power_bi_reports**](PowerBIReportsApi.md#get_power_bi_reports) | **GET** /PowerBIReports | Gets an array of PowerBIReport CatalogItems.
[**replace_power_bi_report_data_model_role_assignments**](PowerBIReportsApi.md#replace_power_bi_report_data_model_role_assignments) | **PUT** /PowerBIReports({Id})/DataModelRoleAssignments | Replaces the data model role assignments that are associated with the specified PowerBIReport.
[**set_power_bi_report_policies**](PowerBIReportsApi.md#set_power_bi_report_policies) | **PUT** /PowerBIReports({Id})/Policies | Replaces ItemPolicies associated with the specified PowerBIReport item.
[**update_power_bi_report**](PowerBIReportsApi.md#update_power_bi_report) | **PATCH** /PowerBIReports({Id}) | Updates the specified PowerBIReport CatalogItem using the provided definition.
[**update_power_bi_report_comment**](PowerBIReportsApi.md#update_power_bi_report_comment) | **PUT** /PowerBIReports({Id})/Comments({CommentId}) | Updates the Comment specified by CommentId in the associated PowerBIReport.
[**update_power_bi_report_data_model_parameters**](PowerBIReportsApi.md#update_power_bi_report_data_model_parameters) | **POST** /PowerBIReports({Id})/DataModelParameters | Updates the data model parameters that are associated with the specified PowerBIReport. If any datasources are updated based on parameters, they can be fetched with DataSources api.
[**update_power_bi_report_data_source**](PowerBIReportsApi.md#update_power_bi_report_data_source) | **PATCH** /PowerBIReports({Id})/DataSources | Updates the DataSource definition associated with the PowerBIReport specified by the Id.
[**update_power_bi_report_properties**](PowerBIReportsApi.md#update_power_bi_report_properties) | **PUT** /PowerBIReports({Id})/Properties | Updates the PowerBIReport Properties included in the given list.
[**upload_power_bi_report**](PowerBIReportsApi.md#upload_power_bi_report) | **POST** /PowerBIReports({Id})/Model.Upload | Does an efficient binary upload of a new or existing PowerBIReport CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.


# **add_power_bi_report**
> PowerBIReport add_power_bi_report(power_bi_report)

Creates a new PowerBIReport CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
power_bi_report = swagger_client.PowerBIReport() # PowerBIReport | The definition of the new PowerBIReport CatalogItem.

try:
    # Creates a new PowerBIReport CatalogItem.
    api_response = api_instance.add_power_bi_report(power_bi_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->add_power_bi_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **power_bi_report** | [**PowerBIReport**](PowerBIReport.md)| The definition of the new PowerBIReport CatalogItem. | 

### Return type

[**PowerBIReport**](PowerBIReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_power_bi_report_comment**
> add_power_bi_report_comment(id, comment)

Creates a new Comment associated to the specified PowerBIReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment = swagger_client.Comment() # Comment | The Comment to be created

try:
    # Creates a new Comment associated to the specified PowerBIReport.
    api_instance.add_power_bi_report_comment(id, comment)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->add_power_bi_report_comment: %s\n" % e)
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

# **check_power_bi_report_data_source_connection**
> DataSourceCheckResult check_power_bi_report_data_source_connection(id, data_source_name)

Checks the status of the specified DataSource connection.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_source_name = 'data_source_name_example' # str | The name of the DataSource to check.

try:
    # Checks the status of the specified DataSource connection.
    api_response = api_instance.check_power_bi_report_data_source_connection(id, data_source_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->check_power_bi_report_data_source_connection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_source_name** | **str**| The name of the DataSource to check. | 

### Return type

[**DataSourceCheckResult**](DataSourceCheckResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_power_bi_report**
> delete_power_bi_report(id)

Deletes the specified PowerBIReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Deletes the specified PowerBIReport.
    api_instance.delete_power_bi_report(id)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->delete_power_bi_report: %s\n" % e)
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

# **delete_power_bi_report_comment**
> delete_power_bi_report_comment(id, comment_id)

Deletes the specified Comment associated to the PowerBIReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment_id = 'comment_id_example' # str | The Id of the Comment.

try:
    # Deletes the specified Comment associated to the PowerBIReport.
    api_instance.delete_power_bi_report_comment(id, comment_id)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->delete_power_bi_report_comment: %s\n" % e)
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

# **get_power_bi_cache_refresh_plans**
> ODataCacheRefreshPlans get_power_bi_cache_refresh_plans(id)

Gets the CacheRefreshPlans for a given Power BI Report.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the CacheRefreshPlans for a given Power BI Report.
    api_response = api_instance.get_power_bi_cache_refresh_plans(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_cache_refresh_plans: %s\n" % e)
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

# **get_power_bi_report**
> PowerBIReport get_power_bi_report(id)

Gets a PowerBIReport CatalogItem specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a PowerBIReport CatalogItem specified by the Id.
    api_response = api_instance.get_power_bi_report(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**PowerBIReport**](PowerBIReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_bi_report_allowed_actions**
> ODataAllowedActions get_power_bi_report_allowed_actions(id)

Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets a list of actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
    api_response = api_instance.get_power_bi_report_allowed_actions(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_allowed_actions: %s\n" % e)
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

# **get_power_bi_report_comments**
> ODataComments get_power_bi_report_comments(id)

Gets the Comments for a PowerBIReport specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the Comments for a PowerBIReport specified by the Id.
    api_response = api_instance.get_power_bi_report_comments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_comments: %s\n" % e)
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

# **get_power_bi_report_content**
> file get_power_bi_report_content(id)

Gets the content of the specified PowerBIReport CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the content of the specified PowerBIReport CatalogItem.
    api_response = api_instance.get_power_bi_report_content(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_content: %s\n" % e)
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

# **get_power_bi_report_data_model_parameters**
> ODataDataModelParameters get_power_bi_report_data_model_parameters(id)

Gets the data model parameters that are associated with the specified PowerBIReport.

Added in October 2020 Release

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the data model parameters that are associated with the specified PowerBIReport.
    api_response = api_instance.get_power_bi_report_data_model_parameters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_data_model_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataDataModelParameters**](ODataDataModelParameters.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_bi_report_data_model_role_assignments**
> ODataDataModelRoleAssignments get_power_bi_report_data_model_role_assignments(id)

Gets the data model role assignments that are associated with the specified PowerBIReport.

Added in January 2019 Release

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the data model role assignments that are associated with the specified PowerBIReport.
    api_response = api_instance.get_power_bi_report_data_model_role_assignments(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_data_model_role_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataDataModelRoleAssignments**](ODataDataModelRoleAssignments.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_bi_report_data_model_roles**
> ODataDataModelRoles get_power_bi_report_data_model_roles(id)

Gets the data model roles that are associated with the specified PowerBIReport.

Added in January 2019 Release

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the data model roles that are associated with the specified PowerBIReport.
    api_response = api_instance.get_power_bi_report_data_model_roles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_data_model_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataDataModelRoles**](ODataDataModelRoles.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_bi_report_data_sources**
> ODataDataSources get_power_bi_report_data_sources(id)

Gets the DataSources that are associated with the specified PowerBIReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets the DataSources that are associated with the specified PowerBIReport.
    api_response = api_instance.get_power_bi_report_data_sources(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_data_sources: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**ODataDataSources**](ODataDataSources.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_power_bi_report_policies**
> list[ItemPolicy] get_power_bi_report_policies(id)

Gets ItemPolicies associated with the specified PowerBIReport CatalogItem.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Gets ItemPolicies associated with the specified PowerBIReport CatalogItem.
    api_response = api_instance.get_power_bi_report_policies(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_policies: %s\n" % e)
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

# **get_power_bi_report_properties**
> ODataProperties get_power_bi_report_properties(id, properties=properties)

Gets PowerBIReports Properties (takes list of Property names to retrieve the values)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = ['properties_example'] # list[str] | Names for the Properties to be returned. (optional)

try:
    # Gets PowerBIReports Properties (takes list of Property names to retrieve the values)
    api_response = api_instance.get_power_bi_report_properties(id, properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_report_properties: %s\n" % e)
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

# **get_power_bi_reports**
> ODataPowerBIReports get_power_bi_reports(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)

Gets an array of PowerBIReport CatalogItems.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)
order_by = 'order_by_example' # str | Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) (optional)
select = 'select_example' # str | Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) (optional)

try:
    # Gets an array of PowerBIReport CatalogItems.
    api_response = api_instance.get_power_bi_reports(top=top, skip=skip, filter=filter, count=count, order_by=order_by, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->get_power_bi_reports: %s\n" % e)
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

[**ODataPowerBIReports**](ODataPowerBIReports.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_power_bi_report_data_model_role_assignments**
> replace_power_bi_report_data_model_role_assignments(id, data_model_role_assignments)

Replaces the data model role assignments that are associated with the specified PowerBIReport.

Added in January 2019 Release

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_model_role_assignments = [swagger_client.DataModelRoleAssignment()] # list[DataModelRoleAssignment] | Updated data model role assignments associated with the specified PowerBIReport.

try:
    # Replaces the data model role assignments that are associated with the specified PowerBIReport.
    api_instance.replace_power_bi_report_data_model_role_assignments(id, data_model_role_assignments)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->replace_power_bi_report_data_model_role_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_model_role_assignments** | [**list[DataModelRoleAssignment]**](DataModelRoleAssignment.md)| Updated data model role assignments associated with the specified PowerBIReport. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_power_bi_report_policies**
> set_power_bi_report_policies(id, item_policies)

Replaces ItemPolicies associated with the specified PowerBIReport item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
item_policies = [swagger_client.ItemPolicy()] # list[ItemPolicy] | The ItemPolicy definitions that will be replaced.

try:
    # Replaces ItemPolicies associated with the specified PowerBIReport item.
    api_instance.set_power_bi_report_policies(id, item_policies)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->set_power_bi_report_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **item_policies** | [**list[ItemPolicy]**](ItemPolicy.md)| The ItemPolicy definitions that will be replaced. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_power_bi_report**
> PowerBIReport update_power_bi_report(id, power_bi_report)

Updates the specified PowerBIReport CatalogItem using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
power_bi_report = swagger_client.PowerBIReport() # PowerBIReport | Definition of the PowerBIReport item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged.

try:
    # Updates the specified PowerBIReport CatalogItem using the provided definition.
    api_response = api_instance.update_power_bi_report(id, power_bi_report)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->update_power_bi_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **power_bi_report** | [**PowerBIReport**](PowerBIReport.md)| Definition of the PowerBIReport item that updates the current item on the server. It is only necessary to include properties to be updated. All other property values on the CatalogItem will be left unchanged. | 

### Return type

[**PowerBIReport**](PowerBIReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_power_bi_report_comment**
> update_power_bi_report_comment(id, comment_id, comment)

Updates the Comment specified by CommentId in the associated PowerBIReport.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
comment_id = 'comment_id_example' # str | The Id of the Comment.
comment = swagger_client.Comment() # Comment | The Comment to be updated

try:
    # Updates the Comment specified by CommentId in the associated PowerBIReport.
    api_instance.update_power_bi_report_comment(id, comment_id, comment)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->update_power_bi_report_comment: %s\n" % e)
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

# **update_power_bi_report_data_model_parameters**
> update_power_bi_report_data_model_parameters(id, data_model_parameters)

Updates the data model parameters that are associated with the specified PowerBIReport. If any datasources are updated based on parameters, they can be fetched with DataSources api.

Added in October 2020 Release

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_model_parameters = [swagger_client.DataModelParameter()] # list[DataModelParameter] | Updated data model parameters associated with the specified PowerBIReport.

try:
    # Updates the data model parameters that are associated with the specified PowerBIReport. If any datasources are updated based on parameters, they can be fetched with DataSources api.
    api_instance.update_power_bi_report_data_model_parameters(id, data_model_parameters)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->update_power_bi_report_data_model_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_model_parameters** | [**list[DataModelParameter]**](DataModelParameter.md)| Updated data model parameters associated with the specified PowerBIReport. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_power_bi_report_data_source**
> update_power_bi_report_data_source(id, data_sources)

Updates the DataSource definition associated with the PowerBIReport specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
data_sources = [swagger_client.DataSource()] # list[DataSource] | Updated definition for the DataSource associated with the PowerBIReport specified by the Id.

try:
    # Updates the DataSource definition associated with the PowerBIReport specified by the Id.
    api_instance.update_power_bi_report_data_source(id, data_sources)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->update_power_bi_report_data_source: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **data_sources** | [**list[DataSource]**](DataSource.md)| Updated definition for the DataSource associated with the PowerBIReport specified by the Id. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_power_bi_report_properties**
> update_power_bi_report_properties(id, properties)

Updates the PowerBIReport Properties included in the given list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
properties = [swagger_client.ModelProperty()] # list[ModelProperty] | The Properties that will be updated.

try:
    # Updates the PowerBIReport Properties included in the given list.
    api_instance.update_power_bi_report_properties(id, properties)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->update_power_bi_report_properties: %s\n" % e)
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

# **upload_power_bi_report**
> PowerBIReport upload_power_bi_report(id, file)

Does an efficient binary upload of a new or existing PowerBIReport CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PowerBIReportsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.
file = '/path/to/file.txt' # file | The file contents.

try:
    # Does an efficient binary upload of a new or existing PowerBIReport CatalogItem from a multipart/form-data request. Use of this API is recommended for files larger than 25 MB in size.
    api_response = api_instance.upload_power_bi_report(id, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerBIReportsApi->upload_power_bi_report: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 
 **file** | **file**| The file contents. | 

### Return type

[**PowerBIReport**](PowerBIReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

