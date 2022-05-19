# user.CountryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_country**](CountryApi.md#create_country) | **POST** /v1/country/ | Create Country
[**delete_country**](CountryApi.md#delete_country) | **DELETE** /v1/country/{country_id} | Delete Country
[**get_country**](CountryApi.md#get_country) | **GET** /v1/country/{id} | Get Country
[**list_countries**](CountryApi.md#list_countries) | **GET** /v1/country/ | List Countries
[**update_country**](CountryApi.md#update_country) | **PUT** /v1/country/{id} | Update Country


# **create_country**
> CountryResponse create_country(country_create)

Create Country

Create new country.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.CountryApi()
country_create = user.CountryCreate() # CountryCreate | 

try:
    # Create Country
    api_response = api_instance.create_country(country_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryApi->create_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_create** | [**CountryCreate**](CountryCreate.md)|  | 

### Return type

[**CountryResponse**](CountryResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_country**
> CountryResponse delete_country(country_id)

Delete Country

Delete a country.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.CountryApi()
country_id = 'country_id_example' # str | 

try:
    # Delete Country
    api_response = api_instance.delete_country(country_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryApi->delete_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 

### Return type

[**CountryResponse**](CountryResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_country**
> CountryResponse get_country(id)

Get Country

Get Country

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.CountryApi()
id = 'id_example' # str | 

try:
    # Get Country
    api_response = api_instance.get_country(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryApi->get_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CountryResponse**](CountryResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_countries**
> CountryListResponse list_countries()

List Countries

Get all countries

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.CountryApi()

try:
    # List Countries
    api_response = api_instance.list_countries()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryApi->list_countries: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CountryListResponse**](CountryListResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_country**
> CountryResponse update_country(id, country_update)

Update Country

Update country

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.CountryApi()
id = 'id_example' # str | 
country_update = user.CountryUpdate() # CountryUpdate | 

try:
    # Update Country
    api_response = api_instance.update_country(id, country_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryApi->update_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **country_update** | [**CountryUpdate**](CountryUpdate.md)|  | 

### Return type

[**CountryResponse**](CountryResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

