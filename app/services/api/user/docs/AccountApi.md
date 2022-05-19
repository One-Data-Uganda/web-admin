# user.AccountApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_contact_person**](AccountApi.md#add_contact_person) | **POST** /v1/account/contact-person | Add Contact Person
[**add_countries**](AccountApi.md#add_countries) | **POST** /v1/account/country | Add Countries
[**add_industries**](AccountApi.md#add_industries) | **POST** /v1/account/industry | Add Industries
[**create_account**](AccountApi.md#create_account) | **POST** /v1/account/ | Create Account
[**disable_account**](AccountApi.md#disable_account) | **PUT** /v1/account/{id}/disable | Disable Account
[**enable_account**](AccountApi.md#enable_account) | **PUT** /v1/account/{id}/enable | Enable Account
[**get_account**](AccountApi.md#get_account) | **GET** /v1/account/{id} | Get Account
[**list_accounts**](AccountApi.md#list_accounts) | **GET** /v1/account/ | List Accounts
[**search_accounts**](AccountApi.md#search_accounts) | **POST** /v1/account/search | Search Accounts
[**search_individual**](AccountApi.md#search_individual) | **POST** /v1/account/search/individual | Search Individual
[**update_account**](AccountApi.md#update_account) | **PUT** /v1/account/{id} | Update Account


# **add_contact_person**
> ContactPersonResponse add_contact_person(contact_person)

Add Contact Person

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
contact_person = user.ContactPerson() # ContactPerson | 

try:
    # Add Contact Person
    api_response = api_instance.add_contact_person(contact_person)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->add_contact_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_person** | [**ContactPerson**](ContactPerson.md)|  | 

### Return type

[**ContactPersonResponse**](ContactPersonResponse.md)

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

# **add_countries**
> FailureResponseModel add_countries(any)

Add Countries

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
any = [user.Any()] # List[Any] | 

try:
    # Add Countries
    api_response = api_instance.add_countries(any)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->add_countries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **any** | [**List[Any]**](Any.md)|  | 

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

# **add_industries**
> FailureResponseModel add_industries(any)

Add Industries

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
any = [user.Any()] # List[Any] | 

try:
    # Add Industries
    api_response = api_instance.add_industries(any)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->add_industries: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **any** | [**List[Any]**](Any.md)|  | 

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

# **create_account**
> AccountResponse create_account(account_view_create)

Create Account

Create new account.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
account_view_create = user.AccountViewCreate() # AccountViewCreate | 

try:
    # Create Account
    api_response = api_instance.create_account(account_view_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_view_create** | [**AccountViewCreate**](AccountViewCreate.md)|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **disable_account**
> AccountResponse disable_account(id)

Disable Account

Disable an account.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
id = 'id_example' # str | 

try:
    # Disable Account
    api_response = api_instance.disable_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->disable_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **enable_account**
> AccountResponse enable_account(id)

Enable Account

Enable an account.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
id = 'id_example' # str | 

try:
    # Enable Account
    api_response = api_instance.enable_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->enable_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **get_account**
> AccountResponse get_account(id)

Get Account

Get a specific account by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
id = 'id_example' # str | 

try:
    # Get Account
    api_response = api_instance.get_account(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->get_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **list_accounts**
> AccountListResponse list_accounts()

List Accounts

List accounts

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()

try:
    # List Accounts
    api_response = api_instance.list_accounts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->list_accounts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountListResponse**](AccountListResponse.md)

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

# **search_accounts**
> Any search_accounts(body)

Search Accounts

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
body = user.Any() # Any | 

try:
    # Search Accounts
    api_response = api_instance.search_accounts(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->search_accounts: %s\n" % e)
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

# **search_individual**
> Any search_individual(body)

Search Individual

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
body = user.Any() # Any | 

try:
    # Search Individual
    api_response = api_instance.search_individual(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->search_individual: %s\n" % e)
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

# **update_account**
> AccountResponse update_account(id, account_view_update)

Update Account

Update a account.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountApi()
id = 'id_example' # str | 
account_view_update = user.AccountViewUpdate() # AccountViewUpdate | 

try:
    # Update Account
    api_response = api_instance.update_account(id, account_view_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->update_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **account_view_update** | [**AccountViewUpdate**](AccountViewUpdate.md)|  | 

### Return type

[**AccountResponse**](AccountResponse.md)

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

