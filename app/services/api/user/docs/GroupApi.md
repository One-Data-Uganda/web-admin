# user.GroupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_group**](GroupApi.md#create_account_group) | **POST** /v1/group/ | Create Account Group
[**delete_account_group**](GroupApi.md#delete_account_group) | **DELETE** /v1/group/{id} | Delete Account Group
[**get_account_group**](GroupApi.md#get_account_group) | **GET** /v1/group/{id} | Get Account Group
[**list_account_groups**](GroupApi.md#list_account_groups) | **GET** /v1/group/account/{account_id} | List Account Groups
[**update_account_group**](GroupApi.md#update_account_group) | **PUT** /v1/group/{id} | Update Account Group


# **create_account_group**
> AccountGroupResponse create_account_group(account_group_create)

Create Account Group

Create new account group.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.GroupApi()
account_group_create = user.AccountGroupCreate() # AccountGroupCreate | 

try:
    # Create Account Group
    api_response = api_instance.create_account_group(account_group_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->create_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_group_create** | [**AccountGroupCreate**](AccountGroupCreate.md)|  | 

### Return type

[**AccountGroupResponse**](AccountGroupResponse.md)

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

# **delete_account_group**
> AccountGroupResponse delete_account_group(id)

Delete Account Group

Delete account_group

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.GroupApi()
id = 56 # int | 

try:
    # Delete Account Group
    api_response = api_instance.delete_account_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->delete_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AccountGroupResponse**](AccountGroupResponse.md)

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

# **get_account_group**
> AccountGroupResponse get_account_group(id)

Get Account Group

Get a specific account_group by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.GroupApi()
id = 56 # int | 

try:
    # Get Account Group
    api_response = api_instance.get_account_group(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->get_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AccountGroupResponse**](AccountGroupResponse.md)

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

# **list_account_groups**
> AccountGroupListResponse list_account_groups(account_id)

List Account Groups

Account Group listing

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.GroupApi()
account_id = 'account_id_example' # str | 

try:
    # List Account Groups
    api_response = api_instance.list_account_groups(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->list_account_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 

### Return type

[**AccountGroupListResponse**](AccountGroupListResponse.md)

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

# **update_account_group**
> AccountGroupResponse update_account_group(id, account_group_update)

Update Account Group

Update a account_group.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.GroupApi()
id = 56 # int | 
account_group_update = user.AccountGroupUpdate() # AccountGroupUpdate | 

try:
    # Update Account Group
    api_response = api_instance.update_account_group(id, account_group_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupApi->update_account_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **account_group_update** | [**AccountGroupUpdate**](AccountGroupUpdate.md)|  | 

### Return type

[**AccountGroupResponse**](AccountGroupResponse.md)

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

