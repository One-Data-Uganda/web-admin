# user.AccountCountryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_country**](AccountCountryApi.md#create_account_country) | **POST** /v1/account-country/ | Create Account Country
[**delete_account_country**](AccountCountryApi.md#delete_account_country) | **DELETE** /v1/account-country/{id} | Delete Account Country
[**get_account_country**](AccountCountryApi.md#get_account_country) | **GET** /v1/account-country/{id} | Get Account Country
[**list_account_countrys**](AccountCountryApi.md#list_account_countrys) | **GET** /v1/account-country/ | List Account Countrys
[**update_account_country**](AccountCountryApi.md#update_account_country) | **PUT** /v1/account-country/{id} | Update Account Country


# **create_account_country**
> AccountCountryResponse create_account_country(account_country_create)

Create Account Country

Create new account country.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountCountryApi()
account_country_create = user.AccountCountryCreate() # AccountCountryCreate | 

try:
    # Create Account Country
    api_response = api_instance.create_account_country(account_country_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountCountryApi->create_account_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_country_create** | [**AccountCountryCreate**](AccountCountryCreate.md)|  | 

### Return type

[**AccountCountryResponse**](AccountCountryResponse.md)

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

# **delete_account_country**
> AccountCountryResponse delete_account_country(id)

Delete Account Country

Delete account_country

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountCountryApi()
id = 56 # int | 

try:
    # Delete Account Country
    api_response = api_instance.delete_account_country(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountCountryApi->delete_account_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AccountCountryResponse**](AccountCountryResponse.md)

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

# **get_account_country**
> AccountCountryResponse get_account_country(id)

Get Account Country

Get a specific account_country by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountCountryApi()
id = 56 # int | 

try:
    # Get Account Country
    api_response = api_instance.get_account_country(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountCountryApi->get_account_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AccountCountryResponse**](AccountCountryResponse.md)

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

# **list_account_countrys**
> AccountCountryListResponse list_account_countrys()

List Account Countrys

Account Country listing

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountCountryApi()

try:
    # List Account Countrys
    api_response = api_instance.list_account_countrys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountCountryApi->list_account_countrys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountCountryListResponse**](AccountCountryListResponse.md)

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

# **update_account_country**
> AccountCountryResponse update_account_country(id, account_country_update)

Update Account Country

Update a account_country.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountCountryApi()
id = 56 # int | 
account_country_update = user.AccountCountryUpdate() # AccountCountryUpdate | 

try:
    # Update Account Country
    api_response = api_instance.update_account_country(id, account_country_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountCountryApi->update_account_country: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **account_country_update** | [**AccountCountryUpdate**](AccountCountryUpdate.md)|  | 

### Return type

[**AccountCountryResponse**](AccountCountryResponse.md)

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

