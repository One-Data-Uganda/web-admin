# reporting.MtApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**mt_graph**](MtApi.md#mt_graph) | **POST** /v1/mt/graph | Mt Graph
[**mt_network_admin**](MtApi.md#mt_network_admin) | **POST** /v1/mt/network | Mt Network Admin
[**mt_report**](MtApi.md#mt_report) | **POST** /v1/mt/report/{account_id} | Mt Report
[**mt_report_admin**](MtApi.md#mt_report_admin) | **POST** /v1/mt/report | Mt Report Admin
[**mt_report_light**](MtApi.md#mt_report_light) | **POST** /v1/mt/light | Mt Report Light
[**mt_simple_report**](MtApi.md#mt_simple_report) | **POST** /v1/mt/simple/{account_id} | Mt Simple Report
[**mt_summary**](MtApi.md#mt_summary) | **POST** /v1/mt/summary/{account_id} | Mt Summary
[**mt_summary_admin**](MtApi.md#mt_summary_admin) | **POST** /v1/mt/summary | Mt Summary Admin


# **mt_graph**
> Any mt_graph(body)

Mt Graph

MT Graph JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MtApi()
body = reporting.Any() # Any | 

try:
    # Mt Graph
    api_response = api_instance.mt_graph(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtApi->mt_graph: %s\n" % e)
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

# **mt_network_admin**
> Any mt_network_admin(body)

Mt Network Admin

MT Network JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MtApi()
body = reporting.Any() # Any | 

try:
    # Mt Network Admin
    api_response = api_instance.mt_network_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtApi->mt_network_admin: %s\n" % e)
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

# **mt_report**
> Any mt_report(account_id, body)

Mt Report

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MtApi()
account_id = 'account_id_example' # str | 
body = reporting.Any() # Any | 

try:
    # Mt Report
    api_response = api_instance.mt_report(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtApi->mt_report: %s\n" % e)
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

# **mt_report_admin**
> Any mt_report_admin(body)

Mt Report Admin

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MtApi()
body = reporting.Any() # Any | 

try:
    # Mt Report Admin
    api_response = api_instance.mt_report_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtApi->mt_report_admin: %s\n" % e)
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

# **mt_report_light**
> Any mt_report_light(body)

Mt Report Light

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MtApi()
body = reporting.Any() # Any | 

try:
    # Mt Report Light
    api_response = api_instance.mt_report_light(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtApi->mt_report_light: %s\n" % e)
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

# **mt_simple_report**
> Any mt_simple_report(account_id, body)

Mt Simple Report

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MtApi()
account_id = 'account_id_example' # str | 
body = reporting.Any() # Any | 

try:
    # Mt Simple Report
    api_response = api_instance.mt_simple_report(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtApi->mt_simple_report: %s\n" % e)
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

# **mt_summary**
> Any mt_summary(account_id, body)

Mt Summary

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MtApi()
account_id = 'account_id_example' # str | 
body = reporting.Any() # Any | 

try:
    # Mt Summary
    api_response = api_instance.mt_summary(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtApi->mt_summary: %s\n" % e)
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

# **mt_summary_admin**
> Any mt_summary_admin(body)

Mt Summary Admin

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.MtApi()
body = reporting.Any() # Any | 

try:
    # Mt Summary Admin
    api_response = api_instance.mt_summary_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MtApi->mt_summary_admin: %s\n" % e)
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

