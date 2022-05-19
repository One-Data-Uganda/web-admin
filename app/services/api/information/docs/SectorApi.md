# information.SectorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sector**](SectorApi.md#create_sector) | **POST** /v1/sector/ | Create Sector
[**delete_sector**](SectorApi.md#delete_sector) | **DELETE** /v1/sector/{id} | Delete Sector
[**get_sector**](SectorApi.md#get_sector) | **GET** /v1/sector/{id} | Get Sector
[**list_sectors**](SectorApi.md#list_sectors) | **GET** /v1/sector/ | List Sectors
[**update_sector**](SectorApi.md#update_sector) | **PUT** /v1/sector/{id} | Update Sector


# **create_sector**
> SectorResponse create_sector(sector_create)

Create Sector

Create new sector.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorApi()
sector_create = information.SectorCreate() # SectorCreate | 

try:
    # Create Sector
    api_response = api_instance.create_sector(sector_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorApi->create_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sector_create** | [**SectorCreate**](SectorCreate.md)|  | 

### Return type

[**SectorResponse**](SectorResponse.md)

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

# **delete_sector**
> SectorResponse delete_sector(id)

Delete Sector

Delete an sector.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorApi()
id = 'id_example' # str | 

try:
    # Delete Sector
    api_response = api_instance.delete_sector(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorApi->delete_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectorResponse**](SectorResponse.md)

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

# **get_sector**
> SectorResponse get_sector(id)

Get Sector

Get sector by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorApi()
id = 'id_example' # str | 

try:
    # Get Sector
    api_response = api_instance.get_sector(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorApi->get_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectorResponse**](SectorResponse.md)

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

# **list_sectors**
> SectorListResponse list_sectors()

List Sectors

Retrieve sectors.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorApi()

try:
    # List Sectors
    api_response = api_instance.list_sectors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorApi->list_sectors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SectorListResponse**](SectorListResponse.md)

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

# **update_sector**
> SectorResponse update_sector(id, sector_update)

Update Sector

Update a sector.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorApi()
id = 'id_example' # str | 
sector_update = information.SectorUpdate() # SectorUpdate | 

try:
    # Update Sector
    api_response = api_instance.update_sector(id, sector_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorApi->update_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sector_update** | [**SectorUpdate**](SectorUpdate.md)|  | 

### Return type

[**SectorResponse**](SectorResponse.md)

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

