# user.RoleApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_role**](RoleApi.md#create_role) | **POST** /v1/role/ | Create Role
[**delete_role**](RoleApi.md#delete_role) | **DELETE** /v1/role/{role_id} | Delete Role
[**list_roles**](RoleApi.md#list_roles) | **GET** /v1/role/ | List Roles
[**update_role**](RoleApi.md#update_role) | **PUT** /v1/role/{id} | Update Role


# **create_role**
> RoleResponse create_role(role_create)

Create Role

Create new role.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.RoleApi()
role_create = user.RoleCreate() # RoleCreate | 

try:
    # Create Role
    api_response = api_instance.create_role(role_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_create** | [**RoleCreate**](RoleCreate.md)|  | 

### Return type

[**RoleResponse**](RoleResponse.md)

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

# **delete_role**
> RoleResponse delete_role(role_id)

Delete Role

Delete a role.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.RoleApi()
role_id = 'role_id_example' # str | 

try:
    # Delete Role
    api_response = api_instance.delete_role(role_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**|  | 

### Return type

[**RoleResponse**](RoleResponse.md)

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

# **list_roles**
> RoleListResponse list_roles()

List Roles

Get all roles

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.RoleApi()

try:
    # List Roles
    api_response = api_instance.list_roles()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->list_roles: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RoleListResponse**](RoleListResponse.md)

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

# **update_role**
> RoleResponse update_role(id, role_update)

Update Role

Update role

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.RoleApi()
id = 'id_example' # str | 
role_update = user.RoleUpdate() # RoleUpdate | 

try:
    # Update Role
    api_response = api_instance.update_role(id, role_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RoleApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **role_update** | [**RoleUpdate**](RoleUpdate.md)|  | 

### Return type

[**RoleResponse**](RoleResponse.md)

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

