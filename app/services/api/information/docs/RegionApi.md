# information.RegionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_region**](RegionApi.md#create_region) | **POST** /v1/region/ | Create Region
[**delete_region**](RegionApi.md#delete_region) | **DELETE** /v1/region/{id} | Delete Region
[**get_region**](RegionApi.md#get_region) | **GET** /v1/region/{id} | Get Region
[**list_regions**](RegionApi.md#list_regions) | **GET** /v1/region/ | List Regions
[**update_region**](RegionApi.md#update_region) | **PUT** /v1/region/{id} | Update Region


# **create_region**
> Region create_region(region_create)

Create Region

Create new region.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.RegionApi()
region_create = information.RegionCreate() # RegionCreate | 

try:
    # Create Region
    api_response = api_instance.create_region(region_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->create_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_create** | [**RegionCreate**](RegionCreate.md)|  | 

### Return type

[**Region**](Region.md)

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

# **delete_region**
> Region delete_region(id)

Delete Region

Delete an region.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.RegionApi()
id = 'id_example' # str | 

try:
    # Delete Region
    api_response = api_instance.delete_region(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->delete_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Region**](Region.md)

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

# **get_region**
> Region get_region(id)

Get Region

Get region by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.RegionApi()
id = 'id_example' # str | 

try:
    # Get Region
    api_response = api_instance.get_region(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->get_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**Region**](Region.md)

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

# **list_regions**
> List[Region] list_regions()

List Regions

Retrieve countries.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.RegionApi()

try:
    # List Regions
    api_response = api_instance.list_regions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->list_regions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[Region]**](Region.md)

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

# **update_region**
> Region update_region(id, region_update)

Update Region

Update a region.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.RegionApi()
id = 'id_example' # str | 
region_update = information.RegionUpdate() # RegionUpdate | 

try:
    # Update Region
    api_response = api_instance.update_region(id, region_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionApi->update_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **region_update** | [**RegionUpdate**](RegionUpdate.md)|  | 

### Return type

[**Region**](Region.md)

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

