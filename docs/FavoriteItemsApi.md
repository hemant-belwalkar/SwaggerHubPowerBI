# swagger_client.FavoriteItemsApi

All URIs are relative to *http://localhost/reports/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_favorite_items**](FavoriteItemsApi.md#get_favorite_items) | **GET** /FavoriteItems | Retrieves a collection of items of type CatalogItem which have been designated as favorites. Use the OData $expand option to also get the referenced items.
[**remove_favorite_item**](FavoriteItemsApi.md#remove_favorite_item) | **DELETE** /FavoriteItems({Id}) | Removes a CatalogItem from the list of favorite items.
[**set_favorite_item**](FavoriteItemsApi.md#set_favorite_item) | **POST** /FavoriteItems | Designate a CatalogItem as a favorite.


# **get_favorite_items**
> list[FavoriteItem] get_favorite_items(top=top, skip=skip, filter=filter, count=count, order_by=order_by, expand=expand, select=select)

Retrieves a collection of items of type CatalogItem which have been designated as favorites. Use the OData $expand option to also get the referenced items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FavoriteItemsApi()
top = 56 # int | Show only the first n items, see [OData Paging - Top](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374630) (optional)
skip = 56 # int | Skip the first n items, see [OData Paging - Skip](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374631) (optional)
filter = 'filter_example' # str | Filter items by property values, see [OData Filtering](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374625) (optional)
count = 'count_example' # str | Include count of items, see [OData Count](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374632) (optional)
order_by = 'order_by_example' # str | Order items by property values, see [OData Sorting](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374629) (optional)
expand = 'expand_example' # str | Expand related entities, see [OData Expand](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374621) (optional)
select = 'select_example' # str | Select properties to be returned, see [OData Select](http://docs.oasis-open.org/odata/odata/v4.0/odata-v4.0-part1-protocol.html#_Toc445374620) (optional)

try:
    # Retrieves a collection of items of type CatalogItem which have been designated as favorites. Use the OData $expand option to also get the referenced items.
    api_response = api_instance.get_favorite_items(top=top, skip=skip, filter=filter, count=count, order_by=order_by, expand=expand, select=select)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoriteItemsApi->get_favorite_items: %s\n" % e)
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

[**list[FavoriteItem]**](FavoriteItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_favorite_item**
> remove_favorite_item(id)

Removes a CatalogItem from the list of favorite items.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FavoriteItemsApi()
id = 'id_example' # str | The key (GUID or path) that uniquely identifies the object. GUID example: 01234567-89ab-cdef-0123-456789abcdef path example: path='/folder1/folder2/item' If the path itself contains single quote, it should be escaped - add another single quote.

try:
    # Removes a CatalogItem from the list of favorite items.
    api_instance.remove_favorite_item(id)
except ApiException as e:
    print("Exception when calling FavoriteItemsApi->remove_favorite_item: %s\n" % e)
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

# **set_favorite_item**
> FavoriteItem set_favorite_item(favorite_item)

Designate a CatalogItem as a favorite.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FavoriteItemsApi()
favorite_item = swagger_client.FavoriteItem() # FavoriteItem | The reference to the CatalogItem to be designated as a favorite. It only needs the Id property. Thus, it is not necessary to provide Item property in the payload.

try:
    # Designate a CatalogItem as a favorite.
    api_response = api_instance.set_favorite_item(favorite_item)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FavoriteItemsApi->set_favorite_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **favorite_item** | [**FavoriteItem**](FavoriteItem.md)| The reference to the CatalogItem to be designated as a favorite. It only needs the Id property. Thus, it is not necessary to provide Item property in the payload. | 

### Return type

[**FavoriteItem**](FavoriteItem.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

