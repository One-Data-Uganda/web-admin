# project.PowerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_power**](PowerApi.md#create_power) | **POST** /v1/power/ | Create Power
[**delete_power**](PowerApi.md#delete_power) | **DELETE** /v1/power/{id} | Delete Power
[**get_power**](PowerApi.md#get_power) | **GET** /v1/power/{id} | Get Power
[**list_powers**](PowerApi.md#list_powers) | **GET** /v1/power/ | List Powers
[**update_power**](PowerApi.md#update_power) | **PUT** /v1/power/{id} | Update Power


# **create_power**
> PowerResponse create_power(power_create)

Create Power

Create new power.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerApi()
power_create = project.PowerCreate() # PowerCreate | 

try:
    # Create Power
    api_response = api_instance.create_power(power_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerApi->create_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **power_create** | [**PowerCreate**](PowerCreate.md)|  | 

### Return type

[**PowerResponse**](PowerResponse.md)

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

# **delete_power**
> PowerResponse delete_power(id)

Delete Power

Delete a power.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerApi()
id = 'id_example' # str | 

try:
    # Delete Power
    api_response = api_instance.delete_power(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerApi->delete_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PowerResponse**](PowerResponse.md)

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

# **get_power**
> PowerResponse get_power(id)

Get Power

Get power by ID.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerApi()
id = 'id_example' # str | 

try:
    # Get Power
    api_response = api_instance.get_power(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerApi->get_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PowerResponse**](PowerResponse.md)

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

# **list_powers**
> PowerListResponse list_powers()

List Powers

Retrieve powers.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerApi()

try:
    # List Powers
    api_response = api_instance.list_powers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerApi->list_powers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PowerListResponse**](PowerListResponse.md)

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

# **update_power**
> PowerResponse update_power(id, power_update)

Update Power

Update a power.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerApi()
id = 'id_example' # str | 
power_update = project.PowerUpdate() # PowerUpdate | 

try:
    # Update Power
    api_response = api_instance.update_power(id, power_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerApi->update_power: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **power_update** | [**PowerUpdate**](PowerUpdate.md)|  | 

### Return type

[**PowerResponse**](PowerResponse.md)

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

