# information.SubRegionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sub_region**](SubRegionApi.md#create_sub_region) | **POST** /v1/sub-region/ | Create Sub Region
[**delete_sub_region**](SubRegionApi.md#delete_sub_region) | **DELETE** /v1/sub-region/{id} | Delete Sub Region
[**get_sub_region**](SubRegionApi.md#get_sub_region) | **GET** /v1/sub-region/{id} | Get Sub Region
[**list_sub_regions**](SubRegionApi.md#list_sub_regions) | **GET** /v1/sub-region/ | List Sub Regions
[**update_sub_region**](SubRegionApi.md#update_sub_region) | **PUT** /v1/sub-region/{id} | Update Sub Region


# **create_sub_region**
> SubRegion create_sub_region(sub_region_create)

Create Sub Region

Create new sub_region.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SubRegionApi()
sub_region_create = information.SubRegionCreate() # SubRegionCreate | 

try:
    # Create Sub Region
    api_response = api_instance.create_sub_region(sub_region_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubRegionApi->create_sub_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_region_create** | [**SubRegionCreate**](SubRegionCreate.md)|  | 

### Return type

[**SubRegion**](SubRegion.md)

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

# **delete_sub_region**
> SubRegion delete_sub_region(id)

Delete Sub Region

Delete an sub_region.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SubRegionApi()
id = 'id_example' # str | 

try:
    # Delete Sub Region
    api_response = api_instance.delete_sub_region(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubRegionApi->delete_sub_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SubRegion**](SubRegion.md)

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

# **get_sub_region**
> SubRegion get_sub_region(id)

Get Sub Region

Get sub_region by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SubRegionApi()
id = 'id_example' # str | 

try:
    # Get Sub Region
    api_response = api_instance.get_sub_region(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubRegionApi->get_sub_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SubRegion**](SubRegion.md)

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

# **list_sub_regions**
> List[SubRegion] list_sub_regions()

List Sub Regions

Retrieve sub_regions.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SubRegionApi()

try:
    # List Sub Regions
    api_response = api_instance.list_sub_regions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubRegionApi->list_sub_regions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SubRegion]**](SubRegion.md)

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

# **update_sub_region**
> SubRegion update_sub_region(id, sub_region_update)

Update Sub Region

Update a sub_region.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SubRegionApi()
id = 'id_example' # str | 
sub_region_update = information.SubRegionUpdate() # SubRegionUpdate | 

try:
    # Update Sub Region
    api_response = api_instance.update_sub_region(id, sub_region_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubRegionApi->update_sub_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sub_region_update** | [**SubRegionUpdate**](SubRegionUpdate.md)|  | 

### Return type

[**SubRegion**](SubRegion.md)

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

