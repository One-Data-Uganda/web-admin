# user.ApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_api**](ApiApi.md#auth_api) | **POST** /v1/api/auth | Auth Api
[**create_api**](ApiApi.md#create_api) | **POST** /v1/api/ | Create Api
[**delete_api**](ApiApi.md#delete_api) | **DELETE** /v1/api/{id} | Delete Api
[**disable_api**](ApiApi.md#disable_api) | **PUT** /v1/api/{id}/disable | Disable Api
[**enable_api**](ApiApi.md#enable_api) | **PUT** /v1/api/{id}/enable | Enable Api
[**get_api**](ApiApi.md#get_api) | **GET** /v1/api/{id} | Get Api
[**get_api_count**](ApiApi.md#get_api_count) | **GET** /v1/api/{account_id}/count | Get Api Count
[**list_by_account_id**](ApiApi.md#list_by_account_id) | **GET** /v1/api/{account_id}/list | List By Account Id


# **auth_api**
> APIAuthResponse auth_api(api_login)

Auth Api

Authenticate API

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ApiApi()
api_login = user.APILogin() # APILogin | 

try:
    # Auth Api
    api_response = api_instance.auth_api(api_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->auth_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_login** | [**APILogin**](APILogin.md)|  | 

### Return type

[**APIAuthResponse**](APIAuthResponse.md)

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

# **create_api**
> APIResponse create_api(api_new)

Create Api

Create new api.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ApiApi()
api_new = user.APINew() # APINew | 

try:
    # Create Api
    api_response = api_instance.create_api(api_new)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->create_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_new** | [**APINew**](APINew.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

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

# **delete_api**
> APIResponse delete_api(id)

Delete Api

Delete an api.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ApiApi()
id = 'id_example' # str | 

try:
    # Delete Api
    api_response = api_instance.delete_api(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->delete_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

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

# **disable_api**
> APIResponse disable_api(id)

Disable Api

Disable api

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ApiApi()
id = 'id_example' # str | 

try:
    # Disable Api
    api_response = api_instance.disable_api(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->disable_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

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

# **enable_api**
> APIResponse enable_api(id)

Enable Api

Enable api

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ApiApi()
id = 'id_example' # str | 

try:
    # Enable Api
    api_response = api_instance.enable_api(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->enable_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

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

# **get_api**
> APIResponse get_api(id)

Get Api

Get an api.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ApiApi()
id = 'id_example' # str | 

try:
    # Get Api
    api_response = api_instance.get_api(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_api: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**APIResponse**](APIResponse.md)

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

# **get_api_count**
> APICountResponse get_api_count(account_id)

Get Api Count

Count API Keys

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ApiApi()
account_id = 'account_id_example' # str | 

try:
    # Get Api Count
    api_response = api_instance.get_api_count(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->get_api_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 

### Return type

[**APICountResponse**](APICountResponse.md)

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

# **list_by_account_id**
> APIListResponse list_by_account_id(account_id)

List By Account Id

List API Keys

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ApiApi()
account_id = 'account_id_example' # str | 

try:
    # List By Account Id
    api_response = api_instance.list_by_account_id(account_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ApiApi->list_by_account_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 

### Return type

[**APIListResponse**](APIListResponse.md)

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

