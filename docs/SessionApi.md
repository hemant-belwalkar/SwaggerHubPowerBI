# swagger_client.SessionApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_session**](SessionApi.md#create_session) | **POST** /Session | Creates a new session
[**delete_session**](SessionApi.md#delete_session) | **DELETE** /Session | Deletes the currently active session


# **create_session**
> create_session(user_credentials)

Creates a new session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()
user_credentials = swagger_client.UserCredentials() # UserCredentials | The credentials of the user to logon as

try:
    # Creates a new session
    api_instance.create_session(user_credentials)
except ApiException as e:
    print("Exception when calling SessionApi->create_session: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_credentials** | [**UserCredentials**](UserCredentials.md)| The credentials of the user to logon as | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_session**
> delete_session()

Deletes the currently active session

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SessionApi()

try:
    # Deletes the currently active session
    api_instance.delete_session()
except ApiException as e:
    print("Exception when calling SessionApi->delete_session: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

