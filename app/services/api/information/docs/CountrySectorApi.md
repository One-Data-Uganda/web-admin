# information.CountrySectorApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_country_sector**](CountrySectorApi.md#create_country_sector) | **POST** /v1/country-sector/ | Create Country Sector
[**delete_country_sector**](CountrySectorApi.md#delete_country_sector) | **DELETE** /v1/country-sector/{id} | Delete Country Sector
[**get_country_sector**](CountrySectorApi.md#get_country_sector) | **GET** /v1/country-sector/{id} | Get Country Sector
[**list_country_sectors**](CountrySectorApi.md#list_country_sectors) | **GET** /v1/country-sector/ | List Country Sectors
[**update_country_sector**](CountrySectorApi.md#update_country_sector) | **PUT** /v1/country-sector/{id} | Update Country Sector


# **create_country_sector**
> CountrySector create_country_sector(country_sector_create)

Create Country Sector

Create new country_sector.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountrySectorApi()
country_sector_create = information.CountrySectorCreate() # CountrySectorCreate | 

try:
    # Create Country Sector
    api_response = api_instance.create_country_sector(country_sector_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountrySectorApi->create_country_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_sector_create** | [**CountrySectorCreate**](CountrySectorCreate.md)|  | 

### Return type

[**CountrySector**](CountrySector.md)

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

# **delete_country_sector**
> CountrySector delete_country_sector(id)

Delete Country Sector

Delete an country_sector.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountrySectorApi()
id = 'id_example' # str | 

try:
    # Delete Country Sector
    api_response = api_instance.delete_country_sector(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountrySectorApi->delete_country_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CountrySector**](CountrySector.md)

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

# **get_country_sector**
> CountrySector get_country_sector(id)

Get Country Sector

Get country_sector by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountrySectorApi()
id = 'id_example' # str | 

try:
    # Get Country Sector
    api_response = api_instance.get_country_sector(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountrySectorApi->get_country_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CountrySector**](CountrySector.md)

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

# **list_country_sectors**
> List[CountrySector] list_country_sectors()

List Country Sectors

Retrieve country_sectors.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountrySectorApi()

try:
    # List Country Sectors
    api_response = api_instance.list_country_sectors()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountrySectorApi->list_country_sectors: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[CountrySector]**](CountrySector.md)

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

# **update_country_sector**
> CountrySector update_country_sector(id, country_sector_update)

Update Country Sector

Update a country_sector.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountrySectorApi()
id = 'id_example' # str | 
country_sector_update = information.CountrySectorUpdate() # CountrySectorUpdate | 

try:
    # Update Country Sector
    api_response = api_instance.update_country_sector(id, country_sector_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountrySectorApi->update_country_sector: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **country_sector_update** | [**CountrySectorUpdate**](CountrySectorUpdate.md)|  | 

### Return type

[**CountrySector**](CountrySector.md)

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

