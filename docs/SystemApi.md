# swagger_client.SystemApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_system_allowed_actions**](SystemApi.md#get_system_allowed_actions) | **GET** /System/AllowedActions | Gets a list of system level actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
[**get_system_info**](SystemApi.md#get_system_info) | **GET** /System | Get SystemInformation
[**get_system_policies**](SystemApi.md#get_system_policies) | **GET** /System/Policies | Gets the System Policies.
[**get_system_properties**](SystemApi.md#get_system_properties) | **GET** /System/Properties | Gets the Systems Properties (takes list of Property names to retrieve the values)
[**set_system_policies**](SystemApi.md#set_system_policies) | **PUT** /System/Policies | Updates the System&#39;s Policies.
[**update_system_properties**](SystemApi.md#update_system_properties) | **PATCH** /System/Properties | Updates the System Properties with the given property list.


# **get_system_allowed_actions**
> ODataAllowedActions get_system_allowed_actions()

Gets a list of system level actions allowed in the current session; user permissions and product edition capabilities are considered when querying.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # Gets a list of system level actions allowed in the current session; user permissions and product edition capabilities are considered when querying.
    api_response = api_instance.get_system_allowed_actions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_allowed_actions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ODataAllowedActions**](ODataAllowedActions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_info**
> SystemInfo get_system_info()

Get SystemInformation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # Get SystemInformation
    api_response = api_instance.get_system_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemInfo**](SystemInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_policies**
> list[Policy] get_system_policies()

Gets the System Policies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()

try:
    # Gets the System Policies.
    api_response = api_instance.get_system_policies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_policies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Policy]**](Policy.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_properties**
> ODataProperties get_system_properties(properties=properties)

Gets the Systems Properties (takes list of Property names to retrieve the values)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
properties = ['properties_example'] # list[str] | Names for the Properties to be returned. (optional)

try:
    # Gets the Systems Properties (takes list of Property names to retrieve the values)
    api_response = api_instance.get_system_properties(properties=properties)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemApi->get_system_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **properties** | [**list[str]**](str.md)| Names for the Properties to be returned. | [optional] 

### Return type

[**ODataProperties**](ODataProperties.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_system_policies**
> set_system_policies(system_policy)

Updates the System's Policies.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
system_policy = swagger_client.SystemPolicy() # SystemPolicy | The SystemPolicy object that contains settings to apply.

try:
    # Updates the System's Policies.
    api_instance.set_system_policies(system_policy)
except ApiException as e:
    print("Exception when calling SystemApi->set_system_policies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_policy** | [**SystemPolicy**](SystemPolicy.md)| The SystemPolicy object that contains settings to apply. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_system_properties**
> update_system_properties(properties)

Updates the System Properties with the given property list.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemApi()
properties = [swagger_client.ModelProperty()] # list[ModelProperty] | Definition of the SystemProperties that updates the current item on the server. It is only necessary to include properties to be updated. All other property values will be left unchanged.

try:
    # Updates the System Properties with the given property list.
    api_instance.update_system_properties(properties)
except ApiException as e:
    print("Exception when calling SystemApi->update_system_properties: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **properties** | [**list[ModelProperty]**](ModelProperty.md)| Definition of the SystemProperties that updates the current item on the server. It is only necessary to include properties to be updated. All other property values will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

