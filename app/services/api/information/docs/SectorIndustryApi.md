# information.SectorIndustryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sector_industry**](SectorIndustryApi.md#create_sector_industry) | **POST** /v1/sector-industry/ | Create Sector Industry
[**delete_sector_industry**](SectorIndustryApi.md#delete_sector_industry) | **DELETE** /v1/sector-industry/{id} | Delete Sector Industry
[**get_sector_industry**](SectorIndustryApi.md#get_sector_industry) | **GET** /v1/sector-industry/{id} | Get Sector Industry
[**list_sector_industries**](SectorIndustryApi.md#list_sector_industries) | **GET** /v1/sector-industry/ | List Sector Industries
[**update_sector_industry**](SectorIndustryApi.md#update_sector_industry) | **PUT** /v1/sector-industry/{id} | Update Sector Industry


# **create_sector_industry**
> SectorIndustryResponse create_sector_industry(sector_industry_create)

Create Sector Industry

Create new sector_industry.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorIndustryApi()
sector_industry_create = information.SectorIndustryCreate() # SectorIndustryCreate | 

try:
    # Create Sector Industry
    api_response = api_instance.create_sector_industry(sector_industry_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorIndustryApi->create_sector_industry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sector_industry_create** | [**SectorIndustryCreate**](SectorIndustryCreate.md)|  | 

### Return type

[**SectorIndustryResponse**](SectorIndustryResponse.md)

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

# **delete_sector_industry**
> SectorIndustryResponse delete_sector_industry(id)

Delete Sector Industry

Delete an sector_industry.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorIndustryApi()
id = 'id_example' # str | 

try:
    # Delete Sector Industry
    api_response = api_instance.delete_sector_industry(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorIndustryApi->delete_sector_industry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectorIndustryResponse**](SectorIndustryResponse.md)

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

# **get_sector_industry**
> SectorIndustryResponse get_sector_industry(id)

Get Sector Industry

Get sector_industry by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorIndustryApi()
id = 'id_example' # str | 

try:
    # Get Sector Industry
    api_response = api_instance.get_sector_industry(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorIndustryApi->get_sector_industry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**SectorIndustryResponse**](SectorIndustryResponse.md)

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

# **list_sector_industries**
> SectorIndustryListResponse list_sector_industries()

List Sector Industries

Retrieve sector_industrys.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorIndustryApi()

try:
    # List Sector Industries
    api_response = api_instance.list_sector_industries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorIndustryApi->list_sector_industries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SectorIndustryListResponse**](SectorIndustryListResponse.md)

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

# **update_sector_industry**
> SectorIndustryResponse update_sector_industry(id, sector_industry_update)

Update Sector Industry

Update a sector_industry.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.SectorIndustryApi()
id = 'id_example' # str | 
sector_industry_update = information.SectorIndustryUpdate() # SectorIndustryUpdate | 

try:
    # Update Sector Industry
    api_response = api_instance.update_sector_industry(id, sector_industry_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SectorIndustryApi->update_sector_industry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sector_industry_update** | [**SectorIndustryUpdate**](SectorIndustryUpdate.md)|  | 

### Return type

[**SectorIndustryResponse**](SectorIndustryResponse.md)

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

