# user.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_json**](AdminApi.md#admin_json) | **POST** /v1/admin/json | Admin Json
[**check_admin_email**](AdminApi.md#check_admin_email) | **POST** /v1/admin/check-email | Check Admin Email
[**check_admin_msisdn**](AdminApi.md#check_admin_msisdn) | **POST** /v1/admin/check-msisdn | Check Admin Msisdn
[**create_admin**](AdminApi.md#create_admin) | **POST** /v1/admin/ | Create Admin
[**disable_admin**](AdminApi.md#disable_admin) | **PUT** /v1/admin/{id}/disable | Disable Admin
[**enable_admin**](AdminApi.md#enable_admin) | **PUT** /v1/admin/{id}/enable | Enable Admin
[**get_admin**](AdminApi.md#get_admin) | **GET** /v1/admin/{id} | Get Admin
[**list_admins**](AdminApi.md#list_admins) | **GET** /v1/admin/ | List Admins
[**login_admin**](AdminApi.md#login_admin) | **POST** /v1/admin/login | Login Admin
[**set_admin_password**](AdminApi.md#set_admin_password) | **PUT** /v1/admin/{id}/password | Set Admin Password
[**update_admin**](AdminApi.md#update_admin) | **PUT** /v1/admin/{id} | Update Admin


# **admin_json**
> Any admin_json(body)

Admin Json

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
body = user.Any() # Any | 

try:
    # Admin Json
    api_response = api_instance.admin_json(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_json: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **check_admin_email**
> AdminResponse check_admin_email(email_model)

Check Admin Email

Check email uniqueness

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
email_model = user.EmailModel() # EmailModel | 

try:
    # Check Admin Email
    api_response = api_instance.check_admin_email(email_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->check_admin_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_model** | [**EmailModel**](EmailModel.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

# **check_admin_msisdn**
> AdminResponse check_admin_msisdn(msisdn_model)

Check Admin Msisdn

Check msisdn uniqueness

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
msisdn_model = user.MSISDNModel() # MSISDNModel | 

try:
    # Check Admin Msisdn
    api_response = api_instance.check_admin_msisdn(msisdn_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->check_admin_msisdn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msisdn_model** | [**MSISDNModel**](MSISDNModel.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

# **create_admin**
> AdminResponse create_admin(admin_create)

Create Admin

Create new admin.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
admin_create = user.AdminCreate() # AdminCreate | 

try:
    # Create Admin
    api_response = api_instance.create_admin(admin_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_create** | [**AdminCreate**](AdminCreate.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

# **disable_admin**
> AdminResponse disable_admin(id)

Disable Admin

Disable admin

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
id = 'id_example' # str | 

try:
    # Disable Admin
    api_response = api_instance.disable_admin(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->disable_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

# **enable_admin**
> AdminResponse enable_admin(id)

Enable Admin

Enable admin

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
id = 'id_example' # str | 

try:
    # Enable Admin
    api_response = api_instance.enable_admin(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->enable_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

# **get_admin**
> AdminResponse get_admin(id)

Get Admin

Get a specific admin by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
id = 'id_example' # str | 

try:
    # Get Admin
    api_response = api_instance.get_admin(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

# **list_admins**
> AdminListResponse list_admins()

List Admins

List admins

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()

try:
    # List Admins
    api_response = api_instance.list_admins()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->list_admins: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AdminListResponse**](AdminListResponse.md)

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

# **login_admin**
> AdminResponse login_admin(admin_login)

Login Admin

Admin login

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
admin_login = user.AdminLogin() # AdminLogin | 

try:
    # Login Admin
    api_response = api_instance.login_admin(admin_login)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->login_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_login** | [**AdminLogin**](AdminLogin.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

# **set_admin_password**
> AdminResponse set_admin_password(id, password_model)

Set Admin Password

Set admin password

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
id = 'id_example' # str | 
password_model = user.PasswordModel() # PasswordModel | 

try:
    # Set Admin Password
    api_response = api_instance.set_admin_password(id, password_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->set_admin_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **password_model** | [**PasswordModel**](PasswordModel.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

# **update_admin**
> AdminResponse update_admin(id, admin_update)

Update Admin

Update an admin.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AdminApi()
id = 'id_example' # str | 
admin_update = user.AdminUpdate() # AdminUpdate | 

try:
    # Update Admin
    api_response = api_instance.update_admin(id, admin_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_admin: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **admin_update** | [**AdminUpdate**](AdminUpdate.md)|  | 

### Return type

[**AdminResponse**](AdminResponse.md)

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

