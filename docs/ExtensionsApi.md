# swagger_client.ExtensionsApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_extension_parameters**](ExtensionsApi.md#get_extension_parameters) | **GET** /Extensions({Id})/Parameters | Retrieves the ExtensionParameter list for given extension.
[**get_extensions**](ExtensionsApi.md#get_extensions) | **GET** /Extensions | Retreives all Extension items.
[**validate_extension_parameters**](ExtensionsApi.md#validate_extension_parameters) | **POST** /Extensions/Model.ValidateExtensionSettings | Validates extension parameters and returns collection of ExtensionParameter.


# **get_extension_parameters**
> list[ExtensionParameter] get_extension_parameters(id)

Retrieves the ExtensionParameter list for given extension.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtensionsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Retrieves the ExtensionParameter list for given extension.
    api_response = api_instance.get_extension_parameters(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->get_extension_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path&#x3D;&#39;/folder1/folder2/item&#39; If the path itself contains single quote, it should be escaped - add another single quote. | 

### Return type

[**list[ExtensionParameter]**](ExtensionParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_extensions**
> list[Extension] get_extensions()

Retreives all Extension items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtensionsApi()

try:
    # Retreives all Extension items.
    api_response = api_instance.get_extensions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->get_extensions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Extension]**](Extension.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_extension_parameters**
> list[ExtensionParameter] validate_extension_parameters(extension_settings=extension_settings)

Validates extension parameters and returns collection of ExtensionParameter.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ExtensionsApi()
extension_settings = swagger_client.ExtensionSettings() # ExtensionSettings |  (optional)

try:
    # Validates extension parameters and returns collection of ExtensionParameter.
    api_response = api_instance.validate_extension_parameters(extension_settings=extension_settings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtensionsApi->validate_extension_parameters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **extension_settings** | [**ExtensionSettings**](ExtensionSettings.md)|  | [optional] 

### Return type

[**list[ExtensionParameter]**](ExtensionParameter.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

