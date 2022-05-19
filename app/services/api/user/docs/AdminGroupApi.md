# user.AdminGroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_admin_group**](AdminGroupApi.md#create_admin_group) | **POST** /v1/admin-group/ | Create Admin Group
[**delete_admin_group**](AdminGroupApi.md#delete_admin_group) | **DELETE** /v1/admin-group/{id} | Delete Admin Group
[**get_admin_group**](AdminGroupApi.md#get_admin_group) | **GET** /v1/admin-group/{id} | Get Admin Group
[**list_admin_groups**](AdminGroupApi.md#list_admin_groups) | **GET** /v1/admin-group/ | List Admin Groups
[**update_admin_group**](AdminGroupApi.md#update_admin_group) | **PUT** /v1/admin-group/{id} | Update Admin Group


# **create_admin_group**
> AdminGroupResponse create_admin_group(admin_group_create)

Create Admin Group

Create new admin group.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminGroupApi()
admin_group_create = user.AdminGroupCreate() # AdminGroupCreate | 

try:
    # Create Admin Group
    api_response = api_instance.create_admin_group(admin_group_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminGroupApi->create_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_group_create** | [**AdminGroupCreate**](AdminGroupCreate.md)|  | 

### Return type

[**AdminGroupResponse**](AdminGroupResponse.md)

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

# **delete_admin_group**
> AdminGroupResponse delete_admin_group(id)

Delete Admin Group

Delete admin_group

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminGroupApi()
id = 56 # int | 

try:
    # Delete Admin Group
    api_response = api_instance.delete_admin_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminGroupApi->delete_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AdminGroupResponse**](AdminGroupResponse.md)

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

# **get_admin_group**
> AdminGroupResponse get_admin_group(id)

Get Admin Group

Get a specific admin_group by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminGroupApi()
id = 56 # int | 

try:
    # Get Admin Group
    api_response = api_instance.get_admin_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminGroupApi->get_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AdminGroupResponse**](AdminGroupResponse.md)

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

# **list_admin_groups**
> AdminGroupListResponse list_admin_groups()

List Admin Groups

Admin Group listing

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminGroupApi()

try:
    # List Admin Groups
    api_response = api_instance.list_admin_groups()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminGroupApi->list_admin_groups: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminGroupListResponse**](AdminGroupListResponse.md)

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

# **update_admin_group**
> AdminGroupResponse update_admin_group(id, admin_group_update)

Update Admin Group

Update a admin_group.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminGroupApi()
id = 56 # int | 
admin_group_update = user.AdminGroupUpdate() # AdminGroupUpdate | 

try:
    # Update Admin Group
    api_response = api_instance.update_admin_group(id, admin_group_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminGroupApi->update_admin_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **admin_group_update** | [**AdminGroupUpdate**](AdminGroupUpdate.md)|  | 

### Return type

[**AdminGroupResponse**](AdminGroupResponse.md)

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

