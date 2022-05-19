# information.SectorGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sector_group**](SectorGroupApi.md#create_sector_group) | **POST** /v1/sector-group/ | Create Sector Group
[**delete_sector_group**](SectorGroupApi.md#delete_sector_group) | **DELETE** /v1/sector-group/{id} | Delete Sector Group
[**get_sector_group**](SectorGroupApi.md#get_sector_group) | **GET** /v1/sector-group/{id} | Get Sector Group
[**list_sector_groups**](SectorGroupApi.md#list_sector_groups) | **GET** /v1/sector-group/ | List Sector Groups
[**update_sector_group**](SectorGroupApi.md#update_sector_group) | **PUT** /v1/sector-group/{id} | Update Sector Group


# **create_sector_group**
> SectorGroupResponse create_sector_group(sector_group_create)

Create Sector Group

Create new sector_group.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorGroupApi()
sector_group_create = information.SectorGroupCreate() # SectorGroupCreate | 

try:
    # Create Sector Group
    api_response = api_instance.create_sector_group(sector_group_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorGroupApi->create_sector_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sector_group_create** | [**SectorGroupCreate**](SectorGroupCreate.md)|  | 

### Return type

[**SectorGroupResponse**](SectorGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sector_group**
> SectorGroupResponse delete_sector_group(id)

Delete Sector Group

Delete an sector_group.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorGroupApi()
id = 'id_example' # str | 

try:
    # Delete Sector Group
    api_response = api_instance.delete_sector_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorGroupApi->delete_sector_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectorGroupResponse**](SectorGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sector_group**
> SectorGroupResponse get_sector_group(id)

Get Sector Group

Get sector_group by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorGroupApi()
id = 'id_example' # str | 

try:
    # Get Sector Group
    api_response = api_instance.get_sector_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorGroupApi->get_sector_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectorGroupResponse**](SectorGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sector_groups**
> SectorGroupListResponse list_sector_groups()

List Sector Groups

Retrieve sector_groups.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorGroupApi()

try:
    # List Sector Groups
    api_response = api_instance.list_sector_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorGroupApi->list_sector_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SectorGroupListResponse**](SectorGroupListResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sector_group**
> SectorGroupResponse update_sector_group(id, sector_group_update)

Update Sector Group

Update a sector_group.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorGroupApi()
id = 'id_example' # str | 
sector_group_update = information.SectorGroupUpdate() # SectorGroupUpdate | 

try:
    # Update Sector Group
    api_response = api_instance.update_sector_group(id, sector_group_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorGroupApi->update_sector_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sector_group_update** | [**SectorGroupUpdate**](SectorGroupUpdate.md)|  | 

### Return type

[**SectorGroupResponse**](SectorGroupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

