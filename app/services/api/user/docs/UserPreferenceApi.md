# user.UserPreferenceApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_preference**](UserPreferenceApi.md#delete_preference) | **DELETE** /v1/user-preference/{user_id}/{name} | Delete Preference
[**get_preference**](UserPreferenceApi.md#get_preference) | **GET** /v1/user-preference/{user_id}/{name} | Get Preference
[**list_preferences**](UserPreferenceApi.md#list_preferences) | **GET** /v1/user-preference/{user_id} | List Preferences
[**set_user_preference**](UserPreferenceApi.md#set_user_preference) | **POST** /v1/user-preference/ | Set User Preference


# **delete_preference**
> UserPreferenceResponse delete_preference(user_id, name)

Delete Preference

Delete user_preference

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserPreferenceApi()
user_id = 'user_id_example' # str | 
name = 'name_example' # str | 

try:
    # Delete Preference
    api_response = api_instance.delete_preference(user_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPreferenceApi->delete_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)|  | 
 **name** | **str**|  | 

### Return type

[**UserPreferenceResponse**](UserPreferenceResponse.md)

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

# **get_preference**
> UserPreferenceResponse get_preference(user_id, name)

Get Preference

Get a specific user_preference by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserPreferenceApi()
user_id = 'user_id_example' # str | 
name = 'name_example' # str | 

try:
    # Get Preference
    api_response = api_instance.get_preference(user_id, name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPreferenceApi->get_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)|  | 
 **name** | **str**|  | 

### Return type

[**UserPreferenceResponse**](UserPreferenceResponse.md)

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

# **list_preferences**
> UserPreferenceListResponse list_preferences(user_id)

List Preferences

Get a specific user_preference by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserPreferenceApi()
user_id = 'user_id_example' # str | 

try:
    # List Preferences
    api_response = api_instance.list_preferences(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPreferenceApi->list_preferences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**str**](.md)|  | 

### Return type

[**UserPreferenceListResponse**](UserPreferenceListResponse.md)

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

# **set_user_preference**
> UserPreferenceResponse set_user_preference(user_preference_create)

Set User Preference

Create new user preference.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserPreferenceApi()
user_preference_create = user.UserPreferenceCreate() # UserPreferenceCreate | 

try:
    # Set User Preference
    api_response = api_instance.set_user_preference(user_preference_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserPreferenceApi->set_user_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_preference_create** | [**UserPreferenceCreate**](UserPreferenceCreate.md)|  | 

### Return type

[**UserPreferenceResponse**](UserPreferenceResponse.md)

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

