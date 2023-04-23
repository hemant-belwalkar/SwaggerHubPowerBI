# swagger_client.SubscriptionsApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_subscription**](SubscriptionsApi.md#add_subscription) | **POST** /Subscriptions | Creates new Subscription item
[**delete_subscription**](SubscriptionsApi.md#delete_subscription) | **DELETE** /Subscriptions({Id}) | Deletes the specified Subscription.
[**disable_subscription**](SubscriptionsApi.md#disable_subscription) | **POST** /Subscriptions({Id})/Model.Disable | Disables the Subscription specified by the Id.
[**enable_subscription**](SubscriptionsApi.md#enable_subscription) | **POST** /Subscriptions({Id})/Model.Enable | Enables a Subscription specified by the Id.
[**execute_subscription**](SubscriptionsApi.md#execute_subscription) | **POST** /Subscriptions({Id})/Model.Execute | Executes the Subscription specified by the Id.
[**get_subscription**](SubscriptionsApi.md#get_subscription) | **GET** /Subscriptions({Id}) | Get the specified Subscription.
[**get_subscriptions**](SubscriptionsApi.md#get_subscriptions) | **GET** /Subscriptions | Gets an array of Subscriptions.
[**set_subscription**](SubscriptionsApi.md#set_subscription) | **PUT** /Subscriptions({Id}) | Replaces the Subscription item using Id property as key.
[**update_subscription**](SubscriptionsApi.md#update_subscription) | **PATCH** /Subscriptions({Id}) | Updates the Subscription item using Id property as key.


# **add_subscription**
> Subscription add_subscription(subscription)

Creates new Subscription item

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
subscription = swagger_client.Subscription() # Subscription | The definition of the new Subscription item. Id field given in the Example is not required.

try:
    # Creates new Subscription item
    api_response = api_instance.add_subscription(subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->add_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription** | [**Subscription**](Subscription.md)| The definition of the new Subscription item. Id field given in the Example is not required. | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_subscription**
> delete_subscription(id)

Deletes the specified Subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Deletes the specified Subscription.
    api_instance.delete_subscription(id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_subscription**
> disable_subscription(id)

Disables the Subscription specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Disables the Subscription specified by the Id.
    api_instance.disable_subscription(id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->disable_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_subscription**
> enable_subscription(id)

Enables a Subscription specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Enables a Subscription specified by the Id.
    api_instance.enable_subscription(id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->enable_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **execute_subscription**
> execute_subscription(id)

Executes the Subscription specified by the Id.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Executes the Subscription specified by the Id.
    api_instance.execute_subscription(id)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->execute_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription**
> Subscription get_subscription(id)

Get the specified Subscription.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef

try:
    # Get the specified Subscription.
    api_response = api_instance.get_subscription(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 

### Return type

[**Subscription**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscriptions**
> list[Subscription] get_subscriptions(top=top, skip=skip, filter=filter, count=count, order_by=order_by, expand=expand, select=select)

Gets an array of Subscriptions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)
order_by = 'order_by_example' # str | Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) (optional)
expand = 'expand_example' # str | Expand related entities, see [OData Expand](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374621) (optional)
select = 'select_example' # str | Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) (optional)

try:
    # Gets an array of Subscriptions.
    api_response = api_instance.get_subscriptions(top=top, skip=skip, filter=filter, count=count, order_by=order_by, expand=expand, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->get_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top** | **int**| Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) | [optional] 
 **skip** | **int**| Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) | [optional] 
 **filter** | **str**| Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) | [optional] 
 **count** | **str**| Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) | [optional] 
 **order_by** | **str**| Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) | [optional] 
 **expand** | **str**| Expand related entities, see [OData Expand](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374621) | [optional] 
 **select** | **str**| Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) | [optional] 

### Return type

[**list[Subscription]**](Subscription.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_subscription**
> set_subscription(id, subscription)

Replaces the Subscription item using Id property as key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef
subscription = swagger_client.Subscription() # Subscription | Subscription item to update.

try:
    # Replaces the Subscription item using Id property as key.
    api_instance.set_subscription(id, subscription)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->set_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 
 **subscription** | [**Subscription**](Subscription.md)| Subscription item to update. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_subscription**
> update_subscription(id, subscription)

Updates the Subscription item using Id property as key.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SubscriptionsApi()
id = 'id_example' # str | The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef
subscription = swagger_client.Subscription() # Subscription | Definition of the Subscription that updates the current item on the server. It is only necessary to include properties to be updated. All other property values will be left unchanged.

try:
    # Updates the Subscription item using Id property as key.
    api_instance.update_subscription(id, subscription)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->update_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The key (GUID) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef | 
 **subscription** | [**Subscription**](Subscription.md)| Definition of the Subscription that updates the current item on the server. It is only necessary to include properties to be updated. All other property values will be left unchanged. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

