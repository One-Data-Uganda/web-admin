# project.ProjectInvestmentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_investment**](ProjectInvestmentApi.md#create_project_investment) | **POST** /v1/project-investment/ | Create Project Investment
[**delete_project_investment**](ProjectInvestmentApi.md#delete_project_investment) | **DELETE** /v1/project-investment/{id} | Delete Project Investment
[**get_project_investment**](ProjectInvestmentApi.md#get_project_investment) | **GET** /v1/project-investment/{id} | Get Project Investment
[**list_project_investments**](ProjectInvestmentApi.md#list_project_investments) | **GET** /v1/project-investment/ | List Project Investments
[**update_project_investment**](ProjectInvestmentApi.md#update_project_investment) | **PUT** /v1/project-investment/{id} | Update Project Investment


# **create_project_investment**
> ProjectInvestmentResponse create_project_investment(project_investment_create)

Create Project Investment

Create new project_investment.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectInvestmentApi()
project_investment_create = project.ProjectInvestmentCreate() # ProjectInvestmentCreate | 

try:
    # Create Project Investment
    api_response = api_instance.create_project_investment(project_investment_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectInvestmentApi->create_project_investment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_investment_create** | [**ProjectInvestmentCreate**](ProjectInvestmentCreate.md)|  | 

### Return type

[**ProjectInvestmentResponse**](ProjectInvestmentResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project_investment**
> ProjectInvestmentResponse delete_project_investment(id)

Delete Project Investment

Delete a project investment.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectInvestmentApi()
id = 'id_example' # str | 

try:
    # Delete Project Investment
    api_response = api_instance.delete_project_investment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectInvestmentApi->delete_project_investment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectInvestmentResponse**](ProjectInvestmentResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_investment**
> ProjectInvestmentResponse get_project_investment(id)

Get Project Investment

Get project investment by ID.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectInvestmentApi()
id = 'id_example' # str | 

try:
    # Get Project Investment
    api_response = api_instance.get_project_investment(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectInvestmentApi->get_project_investment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectInvestmentResponse**](ProjectInvestmentResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_investments**
> ProjectInvestmentListResponse list_project_investments()

List Project Investments

Retrieve project investments.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectInvestmentApi()

try:
    # List Project Investments
    api_response = api_instance.list_project_investments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectInvestmentApi->list_project_investments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectInvestmentListResponse**](ProjectInvestmentListResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_investment**
> ProjectInvestmentResponse update_project_investment(id, project_investment_update)

Update Project Investment

Update a project investment.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectInvestmentApi()
id = 'id_example' # str | 
project_investment_update = project.ProjectInvestmentUpdate() # ProjectInvestmentUpdate | 

try:
    # Update Project Investment
    api_response = api_instance.update_project_investment(id, project_investment_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectInvestmentApi->update_project_investment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project_investment_update** | [**ProjectInvestmentUpdate**](ProjectInvestmentUpdate.md)|  | 

### Return type

[**ProjectInvestmentResponse**](ProjectInvestmentResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

