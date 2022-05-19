# project.PowerImpactApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_power_impact**](PowerImpactApi.md#create_power_impact) | **POST** /v1/power-impact/ | Create Power Impact
[**delete_power_impact**](PowerImpactApi.md#delete_power_impact) | **DELETE** /v1/power-impact/{id} | Delete Power Impact
[**get_power_impact**](PowerImpactApi.md#get_power_impact) | **GET** /v1/power-impact/{id} | Get Power Impact
[**list_power_impacts**](PowerImpactApi.md#list_power_impacts) | **GET** /v1/power-impact/ | List Power Impacts
[**update_power_impact**](PowerImpactApi.md#update_power_impact) | **PUT** /v1/power-impact/{id} | Update Power Impact


# **create_power_impact**
> PowerImpactResponse create_power_impact(power_impact_create)

Create Power Impact

Create new power_impact.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerImpactApi()
power_impact_create = project.PowerImpactCreate() # PowerImpactCreate | 

try:
    # Create Power Impact
    api_response = api_instance.create_power_impact(power_impact_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerImpactApi->create_power_impact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **power_impact_create** | [**PowerImpactCreate**](PowerImpactCreate.md)|  | 

### Return type

[**PowerImpactResponse**](PowerImpactResponse.md)

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

# **delete_power_impact**
> PowerImpactResponse delete_power_impact(id)

Delete Power Impact

Delete a power impact.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerImpactApi()
id = 'id_example' # str | 

try:
    # Delete Power Impact
    api_response = api_instance.delete_power_impact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerImpactApi->delete_power_impact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PowerImpactResponse**](PowerImpactResponse.md)

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

# **get_power_impact**
> PowerImpactResponse get_power_impact(id)

Get Power Impact

Get power impact by ID.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerImpactApi()
id = 'id_example' # str | 

try:
    # Get Power Impact
    api_response = api_instance.get_power_impact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerImpactApi->get_power_impact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PowerImpactResponse**](PowerImpactResponse.md)

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

# **list_power_impacts**
> PowerImpactListResponse list_power_impacts()

List Power Impacts

Retrieve power impacts.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerImpactApi()

try:
    # List Power Impacts
    api_response = api_instance.list_power_impacts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerImpactApi->list_power_impacts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PowerImpactListResponse**](PowerImpactListResponse.md)

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

# **update_power_impact**
> PowerImpactResponse update_power_impact(id, power_impact_update)

Update Power Impact

Update a power impact.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerImpactApi()
id = 'id_example' # str | 
power_impact_update = project.PowerImpactUpdate() # PowerImpactUpdate | 

try:
    # Update Power Impact
    api_response = api_instance.update_power_impact(id, power_impact_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerImpactApi->update_power_impact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **power_impact_update** | [**PowerImpactUpdate**](PowerImpactUpdate.md)|  | 

### Return type

[**PowerImpactResponse**](PowerImpactResponse.md)

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

