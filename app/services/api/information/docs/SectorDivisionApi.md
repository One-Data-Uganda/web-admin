# information.SectorDivisionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sector_division**](SectorDivisionApi.md#create_sector_division) | **POST** /v1/sector-division/ | Create Sector Division
[**delete_sector_division**](SectorDivisionApi.md#delete_sector_division) | **DELETE** /v1/sector-division/{id} | Delete Sector Division
[**get_sector_division**](SectorDivisionApi.md#get_sector_division) | **GET** /v1/sector-division/{id} | Get Sector Division
[**list_sector_divisions**](SectorDivisionApi.md#list_sector_divisions) | **GET** /v1/sector-division/ | List Sector Divisions
[**update_sector_division**](SectorDivisionApi.md#update_sector_division) | **PUT** /v1/sector-division/{id} | Update Sector Division


# **create_sector_division**
> SectorDivisionResponse create_sector_division(sector_division_create)

Create Sector Division

Create new sector_division.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorDivisionApi()
sector_division_create = information.SectorDivisionCreate() # SectorDivisionCreate | 

try:
    # Create Sector Division
    api_response = api_instance.create_sector_division(sector_division_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorDivisionApi->create_sector_division: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sector_division_create** | [**SectorDivisionCreate**](SectorDivisionCreate.md)|  | 

### Return type

[**SectorDivisionResponse**](SectorDivisionResponse.md)

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

# **delete_sector_division**
> SectorDivisionResponse delete_sector_division(id)

Delete Sector Division

Delete an sector_division.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorDivisionApi()
id = 'id_example' # str | 

try:
    # Delete Sector Division
    api_response = api_instance.delete_sector_division(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorDivisionApi->delete_sector_division: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectorDivisionResponse**](SectorDivisionResponse.md)

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

# **get_sector_division**
> SectorDivisionResponse get_sector_division(id)

Get Sector Division

Get sector_division by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorDivisionApi()
id = 'id_example' # str | 

try:
    # Get Sector Division
    api_response = api_instance.get_sector_division(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorDivisionApi->get_sector_division: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectorDivisionResponse**](SectorDivisionResponse.md)

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

# **list_sector_divisions**
> SectorDivisionListResponse list_sector_divisions()

List Sector Divisions

Retrieve sector_divisions.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorDivisionApi()

try:
    # List Sector Divisions
    api_response = api_instance.list_sector_divisions()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorDivisionApi->list_sector_divisions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SectorDivisionListResponse**](SectorDivisionListResponse.md)

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

# **update_sector_division**
> SectorDivisionResponse update_sector_division(id, sector_division_update)

Update Sector Division

Update a sector_division.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorDivisionApi()
id = 'id_example' # str | 
sector_division_update = information.SectorDivisionUpdate() # SectorDivisionUpdate | 

try:
    # Update Sector Division
    api_response = api_instance.update_sector_division(id, sector_division_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorDivisionApi->update_sector_division: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sector_division_update** | [**SectorDivisionUpdate**](SectorDivisionUpdate.md)|  | 

### Return type

[**SectorDivisionResponse**](SectorDivisionResponse.md)

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

