# user.AccountIndustryApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_account_industry**](AccountIndustryApi.md#create_account_industry) | **POST** /v1/account-industry/ | Create Account Industry
[**delete_account_industry**](AccountIndustryApi.md#delete_account_industry) | **DELETE** /v1/account-industry/{id} | Delete Account Industry
[**get_account_industry**](AccountIndustryApi.md#get_account_industry) | **GET** /v1/account-industry/{id} | Get Account Industry
[**list_account_industrys**](AccountIndustryApi.md#list_account_industrys) | **GET** /v1/account-industry/ | List Account Industrys
[**update_account_industry**](AccountIndustryApi.md#update_account_industry) | **PUT** /v1/account-industry/{id} | Update Account Industry


# **create_account_industry**
> AccountIndustryResponse create_account_industry(account_industry_create)

Create Account Industry

Create new account industry.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountIndustryApi()
account_industry_create = user.AccountIndustryCreate() # AccountIndustryCreate | 

try:
    # Create Account Industry
    api_response = api_instance.create_account_industry(account_industry_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountIndustryApi->create_account_industry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_industry_create** | [**AccountIndustryCreate**](AccountIndustryCreate.md)|  | 

### Return type

[**AccountIndustryResponse**](AccountIndustryResponse.md)

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

# **delete_account_industry**
> AccountIndustryResponse delete_account_industry(id)

Delete Account Industry

Delete account_industry

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountIndustryApi()
id = 56 # int | 

try:
    # Delete Account Industry
    api_response = api_instance.delete_account_industry(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountIndustryApi->delete_account_industry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AccountIndustryResponse**](AccountIndustryResponse.md)

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

# **get_account_industry**
> AccountIndustryResponse get_account_industry(id)

Get Account Industry

Get a specific account_industry by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountIndustryApi()
id = 56 # int | 

try:
    # Get Account Industry
    api_response = api_instance.get_account_industry(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountIndustryApi->get_account_industry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**AccountIndustryResponse**](AccountIndustryResponse.md)

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

# **list_account_industrys**
> AccountIndustryListResponse list_account_industrys()

List Account Industrys

Account Industry listing

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountIndustryApi()

try:
    # List Account Industrys
    api_response = api_instance.list_account_industrys()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountIndustryApi->list_account_industrys: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountIndustryListResponse**](AccountIndustryListResponse.md)

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

# **update_account_industry**
> AccountIndustryResponse update_account_industry(id, account_industry_update)

Update Account Industry

Update a account_industry.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AccountIndustryApi()
id = 56 # int | 
account_industry_update = user.AccountIndustryUpdate() # AccountIndustryUpdate | 

try:
    # Update Account Industry
    api_response = api_instance.update_account_industry(id, account_industry_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountIndustryApi->update_account_industry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **account_industry_update** | [**AccountIndustryUpdate**](AccountIndustryUpdate.md)|  | 

### Return type

[**AccountIndustryResponse**](AccountIndustryResponse.md)

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

