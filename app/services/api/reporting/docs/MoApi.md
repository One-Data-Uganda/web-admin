# reporting.MoApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mo_graph**](MoApi.md#mo_graph) | **POST** /v1/mo/graph | Mo Graph
[**mo_report**](MoApi.md#mo_report) | **POST** /v1/mo/report/{account_id} | Mo Report
[**mo_report_admin**](MoApi.md#mo_report_admin) | **POST** /v1/mo/report | Mo Report Admin
[**mo_summary**](MoApi.md#mo_summary) | **POST** /v1/mo/summary/{account_id} | Mo Summary
[**mo_summary_admin**](MoApi.md#mo_summary_admin) | **POST** /v1/mo/summary | Mo Summary Admin


# **mo_graph**
> Any mo_graph(body)

Mo Graph

MO Graph JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MoApi()
body = reporting.Any() # Any | 

try:
    # Mo Graph
    api_response = api_instance.mo_graph(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoApi->mo_graph: %s\n" % e)
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

# **mo_report**
> Any mo_report(account_id, body)

Mo Report

MO JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MoApi()
account_id = 'account_id_example' # str | 
body = reporting.Any() # Any | 

try:
    # Mo Report
    api_response = api_instance.mo_report(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoApi->mo_report: %s\n" % e)
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

# **mo_report_admin**
> Any mo_report_admin(body)

Mo Report Admin

MO JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MoApi()
body = reporting.Any() # Any | 

try:
    # Mo Report Admin
    api_response = api_instance.mo_report_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoApi->mo_report_admin: %s\n" % e)
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

# **mo_summary**
> Any mo_summary(account_id, body)

Mo Summary

MO Summary

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MoApi()
account_id = 'account_id_example' # str | 
body = reporting.Any() # Any | 

try:
    # Mo Summary
    api_response = api_instance.mo_summary(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoApi->mo_summary: %s\n" % e)
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

# **mo_summary_admin**
> Any mo_summary_admin(body)

Mo Summary Admin

MO Summary

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MoApi()
body = reporting.Any() # Any | 

try:
    # Mo Summary Admin
    api_response = api_instance.mo_summary_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MoApi->mo_summary_admin: %s\n" % e)
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

