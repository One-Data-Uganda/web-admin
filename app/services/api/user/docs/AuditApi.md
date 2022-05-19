# user.AuditApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_audit_json**](AuditApi.md#account_audit_json) | **POST** /v1/audit/{account_id}/json | Account Audit Json
[**admin_audit_json**](AuditApi.md#admin_audit_json) | **POST** /v1/audit/json/admin | Admin Audit Json
[**audit_json**](AuditApi.md#audit_json) | **POST** /v1/audit/json | Audit Json


# **account_audit_json**
> Any account_audit_json(account_id, body)

Account Audit Json

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AuditApi()
account_id = 'account_id_example' # str | 
body = user.Any() # Any | 

try:
    # Account Audit Json
    api_response = api_instance.account_audit_json(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->account_audit_json: %s\n" % e)
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

# **admin_audit_json**
> Any admin_audit_json(body)

Admin Audit Json

Get audit records for admins

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AuditApi()
body = user.Any() # Any | 

try:
    # Admin Audit Json
    api_response = api_instance.admin_audit_json(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->admin_audit_json: %s\n" % e)
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

# **audit_json**
> Any audit_json(body)

Audit Json

Get all account audit records

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.AuditApi()
body = user.Any() # Any | 

try:
    # Audit Json
    api_response = api_instance.audit_json(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->audit_json: %s\n" % e)
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

