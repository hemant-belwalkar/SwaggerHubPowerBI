# swagger_client.MeApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_details**](MeApi.md#get_user_details) | **GET** /Me | Gets the User object for the current user.


# **get_user_details**
> User get_user_details()

Gets the User object for the current user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MeApi()

try:
    # Gets the User object for the current user.
    api_response = api_instance.get_user_details()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MeApi->get_user_details: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

