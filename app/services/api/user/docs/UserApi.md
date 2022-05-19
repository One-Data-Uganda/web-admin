# user.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_password**](UserApi.md#check_password) | **POST** /v1/user/check-password | Check Password
[**check_user_email**](UserApi.md#check_user_email) | **POST** /v1/user/check-email | Check User Email
[**check_user_msisdn**](UserApi.md#check_user_msisdn) | **POST** /v1/user/check-msisdn | Check User Msisdn
[**create_user**](UserApi.md#create_user) | **POST** /v1/user/ | Create User
[**create_user_with_kyc**](UserApi.md#create_user_with_kyc) | **POST** /v1/user/with-kyc | Create User With Kyc
[**disable_user**](UserApi.md#disable_user) | **PUT** /v1/user/{id}/disable | Disable User
[**enable_user**](UserApi.md#enable_user) | **PUT** /v1/user/{id}/enable | Enable User
[**get_user**](UserApi.md#get_user) | **GET** /v1/user/{id} | Get User
[**login_user**](UserApi.md#login_user) | **POST** /v1/user/login | Login User
[**set_password**](UserApi.md#set_password) | **PUT** /v1/user/{id}/password | Set Password
[**update_user**](UserApi.md#update_user) | **PUT** /v1/user/{id} | Update User
[**user_account_json**](UserApi.md#user_account_json) | **POST** /v1/user/{account_id}/json | User Account Json


# **check_password**
> FailureResponseModel check_password(password_model)

Check Password

Check password Complexity

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
password_model = user.PasswordModel() # PasswordModel | 

try:
    # Check Password
    api_response = api_instance.check_password(password_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->check_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_model** | [**PasswordModel**](PasswordModel.md)|  | 

### Return type

[**FailureResponseModel**](FailureResponseModel.md)

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

# **check_user_email**
> UserResponse check_user_email(email_model)

Check User Email

Check email uniqueness

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
email_model = user.EmailModel() # EmailModel | 

try:
    # Check User Email
    api_response = api_instance.check_user_email(email_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->check_user_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_model** | [**EmailModel**](EmailModel.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **check_user_msisdn**
> UserResponse check_user_msisdn(msisdn_model)

Check User Msisdn

Check msisdn uniqueness

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
msisdn_model = user.MSISDNModel() # MSISDNModel | 

try:
    # Check User Msisdn
    api_response = api_instance.check_user_msisdn(msisdn_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->check_user_msisdn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msisdn_model** | [**MSISDNModel**](MSISDNModel.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **create_user**
> UserResponse create_user(user_view_create)

Create User

Create new user.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
user_view_create = user.UserViewCreate() # UserViewCreate | 

try:
    # Create User
    api_response = api_instance.create_user(user_view_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_view_create** | [**UserViewCreate**](UserViewCreate.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **create_user_with_kyc**
> UserResponse create_user_with_kyc(user_create)

Create User With Kyc

Create new user (with KYC).

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
user_create = user.UserCreate() # UserCreate | 

try:
    # Create User With Kyc
    api_response = api_instance.create_user_with_kyc(user_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->create_user_with_kyc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_create** | [**UserCreate**](UserCreate.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **disable_user**
> UserResponse disable_user(id)

Disable User

Disable user

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
id = 'id_example' # str | 

try:
    # Disable User
    api_response = api_instance.disable_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->disable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **enable_user**
> UserResponse enable_user(id)

Enable User

Enable user

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
id = 'id_example' # str | 

try:
    # Enable User
    api_response = api_instance.enable_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->enable_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user**
> UserResponse get_user(id)

Get User

Get a specific user by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
id = 'id_example' # str | 

try:
    # Get User
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **login_user**
> UserResponse login_user(user_login)

Login User

User login

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
user_login = user.UserLogin() # UserLogin | 

try:
    # Login User
    api_response = api_instance.login_user(user_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->login_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_login** | [**UserLogin**](UserLogin.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **set_password**
> UserResponse set_password(id, password_model)

Set Password

Set user password

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
id = 'id_example' # str | 
password_model = user.PasswordModel() # PasswordModel | 

try:
    # Set Password
    api_response = api_instance.set_password(id, password_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->set_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **password_model** | [**PasswordModel**](PasswordModel.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **update_user**
> UserResponse update_user(id, user_view_update)

Update User

Update a user.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
id = 'id_example' # str | 
user_view_update = user.UserViewUpdate() # UserViewUpdate | 

try:
    # Update User
    api_response = api_instance.update_user(id, user_view_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **user_view_update** | [**UserViewUpdate**](UserViewUpdate.md)|  | 

### Return type

[**UserResponse**](UserResponse.md)

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

# **user_account_json**
> Any user_account_json(account_id, body)

User Account Json

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.UserApi()
account_id = 'account_id_example' # str | 
body = user.Any() # Any | 

try:
    # User Account Json
    api_response = api_instance.user_account_json(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserApi->user_account_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | [**str**](.md)|  | 
 **body** | **Any**|  | 

### Return type

[**Any**](Any.md)

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

