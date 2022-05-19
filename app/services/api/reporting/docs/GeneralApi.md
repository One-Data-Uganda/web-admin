# reporting.GeneralApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**dummy**](GeneralApi.md#dummy) | **POST** /v1/general/dummy | Dummy
[**keyword_json**](GeneralApi.md#keyword_json) | **POST** /v1/general/keyword | Keyword Json
[**keyword_performance_json**](GeneralApi.md#keyword_performance_json) | **POST** /v1/general/keyword-performance/{account_id} | Keyword Performance Json
[**keyword_performance_json_admin**](GeneralApi.md#keyword_performance_json_admin) | **POST** /v1/general/keyword-performance | Keyword Performance Json Admin
[**outbox_json**](GeneralApi.md#outbox_json) | **POST** /v1/general/outbox/{account_id} | Outbox Json
[**sender_json**](GeneralApi.md#sender_json) | **POST** /v1/general/sender | Sender Json


# **dummy**
> FailureResponseModel dummy()

Dummy

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.GeneralApi()

try:
    # Dummy
    api_response = api_instance.dummy()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralApi->dummy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**FailureResponseModel**](FailureResponseModel.md)

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

# **keyword_json**
> Any keyword_json(body)

Keyword Json

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.GeneralApi()
body = reporting.Any() # Any | 

try:
    # Keyword Json
    api_response = api_instance.keyword_json(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralApi->keyword_json: %s\n" % e)
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

# **keyword_performance_json**
> Any keyword_performance_json(account_id, body)

Keyword Performance Json

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.GeneralApi()
account_id = 'account_id_example' # str | 
body = reporting.Any() # Any | 

try:
    # Keyword Performance Json
    api_response = api_instance.keyword_performance_json(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralApi->keyword_performance_json: %s\n" % e)
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

# **keyword_performance_json_admin**
> Any keyword_performance_json_admin(body)

Keyword Performance Json Admin

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.GeneralApi()
body = reporting.Any() # Any | 

try:
    # Keyword Performance Json Admin
    api_response = api_instance.keyword_performance_json_admin(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralApi->keyword_performance_json_admin: %s\n" % e)
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

# **outbox_json**
> Any outbox_json(account_id, body)

Outbox Json

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.GeneralApi()
account_id = 'account_id_example' # str | 
body = reporting.Any() # Any | 

try:
    # Outbox Json
    api_response = api_instance.outbox_json(account_id, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralApi->outbox_json: %s\n" % e)
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

# **sender_json**
> Any sender_json(body)

Sender Json

MT JSON

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.GeneralApi()
body = reporting.Any() # Any | 

try:
    # Sender Json
    api_response = api_instance.sender_json(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GeneralApi->sender_json: %s\n" % e)
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

