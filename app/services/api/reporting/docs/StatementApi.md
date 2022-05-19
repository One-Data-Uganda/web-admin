# reporting.StatementApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statement**](StatementApi.md#get_statement) | **POST** /v1/statement/ | Get Statement


# **get_statement**
> FailureResponseModel get_statement(statement_model)

Get Statement

### Example

```python
from __future__ import print_function
import time
import reporting
from reporting.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = reporting.StatementApi()
statement_model = reporting.StatementModel() # StatementModel | 

try:
    # Get Statement
    api_response = api_instance.get_statement(statement_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementApi->get_statement: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_model** | [**StatementModel**](StatementModel.md)|  | 

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

