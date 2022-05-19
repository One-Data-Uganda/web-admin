# project.PowerScheduleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_power_schedule**](PowerScheduleApi.md#create_power_schedule) | **POST** /v1/power-schedule/ | Create Power Schedule
[**delete_power_schedule**](PowerScheduleApi.md#delete_power_schedule) | **DELETE** /v1/power-schedule/{id} | Delete Power Schedule
[**get_power_schedule**](PowerScheduleApi.md#get_power_schedule) | **GET** /v1/power-schedule/{id} | Get Power Schedule
[**list_power_schedules**](PowerScheduleApi.md#list_power_schedules) | **GET** /v1/power-schedule/ | List Power Schedules
[**update_power_schedule**](PowerScheduleApi.md#update_power_schedule) | **PUT** /v1/power-schedule/{id} | Update Power Schedule


# **create_power_schedule**
> PowerScheduleResponse create_power_schedule(power_schedule_create)

Create Power Schedule

Create new power_schedule.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerScheduleApi()
power_schedule_create = project.PowerScheduleCreate() # PowerScheduleCreate | 

try:
    # Create Power Schedule
    api_response = api_instance.create_power_schedule(power_schedule_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerScheduleApi->create_power_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **power_schedule_create** | [**PowerScheduleCreate**](PowerScheduleCreate.md)|  | 

### Return type

[**PowerScheduleResponse**](PowerScheduleResponse.md)

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

# **delete_power_schedule**
> PowerScheduleResponse delete_power_schedule(id)

Delete Power Schedule

Delete a power schedule.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerScheduleApi()
id = 'id_example' # str | 

try:
    # Delete Power Schedule
    api_response = api_instance.delete_power_schedule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerScheduleApi->delete_power_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PowerScheduleResponse**](PowerScheduleResponse.md)

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

# **get_power_schedule**
> PowerScheduleResponse get_power_schedule(id)

Get Power Schedule

Get power schedule by ID.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerScheduleApi()
id = 'id_example' # str | 

try:
    # Get Power Schedule
    api_response = api_instance.get_power_schedule(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerScheduleApi->get_power_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PowerScheduleResponse**](PowerScheduleResponse.md)

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

# **list_power_schedules**
> PowerScheduleListResponse list_power_schedules()

List Power Schedules

Retrieve power schedules.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerScheduleApi()

try:
    # List Power Schedules
    api_response = api_instance.list_power_schedules()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerScheduleApi->list_power_schedules: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**PowerScheduleListResponse**](PowerScheduleListResponse.md)

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

# **update_power_schedule**
> PowerScheduleResponse update_power_schedule(id, power_schedule_update)

Update Power Schedule

Update a power schedule.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.PowerScheduleApi()
id = 'id_example' # str | 
power_schedule_update = project.PowerScheduleUpdate() # PowerScheduleUpdate | 

try:
    # Update Power Schedule
    api_response = api_instance.update_power_schedule(id, power_schedule_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PowerScheduleApi->update_power_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **power_schedule_update** | [**PowerScheduleUpdate**](PowerScheduleUpdate.md)|  | 

### Return type

[**PowerScheduleResponse**](PowerScheduleResponse.md)

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

