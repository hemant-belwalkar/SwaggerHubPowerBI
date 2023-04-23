# swagger_client.CacheRefreshPlansApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_cache_refresh_plan**](CacheRefreshPlansApi.md#add_cache_refresh_plan) | **POST** /CacheRefreshPlans | Creates a new CacheRefreshPlan item.
[**delete_cache_refresh_plan**](CacheRefreshPlansApi.md#delete_cache_refresh_plan) | **DELETE** /CacheRefreshPlans({Id}) | Deletes the specified CacheRefreshPlan.
[**execute_cache_refresh_plan**](CacheRefreshPlansApi.md#execute_cache_refresh_plan) | **POST** /CacheRefreshPlans({Id})/Model.Execute | Executes given CacheRefreshPlan immediately.
[**get_cache_refresh_plan**](CacheRefreshPlansApi.md#get_cache_refresh_plan) | **GET** /CacheRefreshPlans({Id}) | Gets a CacheRefreshPlan item specified by the Id.
[**get_cache_refresh_plan_history**](CacheRefreshPlansApi.md#get_cache_refresh_plan_history) | **GET** /CacheRefreshPlans({Id})/History | Gets an array of history or execution records for the specified cache refresh plan.
[**set_cache_refresh_plan**](CacheRefreshPlansApi.md#set_cache_refresh_plan) | **PUT** /CacheRefreshPlans({Id}) | Replaces the specified CacheRefreshPlan item using the provided definition.


# **add_cache_refresh_plan**
> CacheRefreshPlan add_cache_refresh_plan(cache_refresh_plan)

Creates a new CacheRefreshPlan item.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CacheRefreshPlansApi()
cache_refresh_plan = swagger_client.CacheRefreshPlan() # CacheRefreshPlan | The definition of the new CacheRefreshPlan item.

try:
    # Creates a new CacheRefreshPlan item.
    api_response = api_instance.add_cache_refresh_plan(cache_refresh_plan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheRefreshPlansApi->add_cache_refresh_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cache_refresh_plan** | [**CacheRefreshPlan**](CacheRefreshPlan.md)| The definition of the new CacheRefreshPlan item. | 

### Return type

[**CacheRefreshPlan**](CacheRefreshPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_cache_refresh_plan**
> delete_cache_refresh_plan(id)

Deletes the specified CacheRefreshPlan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CacheRefreshPlansApi()
id = 'id_example' # str | The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Deletes the specified CacheRefreshPlan.
    api_instance.delete_cache_refresh_plan(id)
except ApiException as e:
    print("Exception when calling CacheRefreshPlansApi->delete_cache_refresh_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_cache_refresh_plan**
> execute_cache_refresh_plan(id)

Executes given CacheRefreshPlan immediately.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CacheRefreshPlansApi()
id = 'id_example' # str | The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Executes given CacheRefreshPlan immediately.
    api_instance.execute_cache_refresh_plan(id)
except ApiException as e:
    print("Exception when calling CacheRefreshPlansApi->execute_cache_refresh_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cache_refresh_plan**
> CacheRefreshPlan get_cache_refresh_plan(id)

Gets a CacheRefreshPlan item specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CacheRefreshPlansApi()
id = 'id_example' # str | The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Gets a CacheRefreshPlan item specified by the Id.
    api_response = api_instance.get_cache_refresh_plan(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheRefreshPlansApi->get_cache_refresh_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

[**CacheRefreshPlan**](CacheRefreshPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cache_refresh_plan_history**
> ODataSubscriptionHistory get_cache_refresh_plan_history(id)

Gets an array of history or execution records for the specified cache refresh plan.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CacheRefreshPlansApi()
id = 'id_example' # str | The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Gets an array of history or execution records for the specified cache refresh plan.
    api_response = api_instance.get_cache_refresh_plan_history(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheRefreshPlansApi->get_cache_refresh_plan_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

[**ODataSubscriptionHistory**](ODataSubscriptionHistory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_cache_refresh_plan**
> CacheRefreshPlan set_cache_refresh_plan(id, cache_refresh_plan)

Replaces the specified CacheRefreshPlan item using the provided definition.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CacheRefreshPlansApi()
id = 'id_example' # str | The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef
cache_refresh_plan = swagger_client.CacheRefreshPlan() # CacheRefreshPlan | Definition of the CacheRefreshPlan item that updates the current item on the server.

try:
    # Replaces the specified CacheRefreshPlan item using the provided definition.
    api_response = api_instance.set_cache_refresh_plan(id, cache_refresh_plan)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CacheRefreshPlansApi->set_cache_refresh_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The GUID that uniquely identifies the CacheRefreshPlan. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 
 **cache_refresh_plan** | [**CacheRefreshPlan**](CacheRefreshPlan.md)| Definition of the CacheRefreshPlan item that updates the current item on the server. | 

### Return type

[**CacheRefreshPlan**](CacheRefreshPlan.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

