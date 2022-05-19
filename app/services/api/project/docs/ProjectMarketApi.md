# project.ProjectMarketApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_market**](ProjectMarketApi.md#create_project_market) | **POST** /v1/project-market/ | Create Project Market
[**delete_project_market**](ProjectMarketApi.md#delete_project_market) | **DELETE** /v1/project-market/{id} | Delete Project Market
[**get_project_market**](ProjectMarketApi.md#get_project_market) | **GET** /v1/project-market/{id} | Get Project Market
[**list_project_markets**](ProjectMarketApi.md#list_project_markets) | **GET** /v1/project-market/ | List Project Markets
[**update_project_market**](ProjectMarketApi.md#update_project_market) | **PUT** /v1/project-market/{id} | Update Project Market


# **create_project_market**
> ProjectMarketResponse create_project_market(project_market_create)

Create Project Market

Create new project_market.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectMarketApi()
project_market_create = project.ProjectMarketCreate() # ProjectMarketCreate | 

try:
    # Create Project Market
    api_response = api_instance.create_project_market(project_market_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMarketApi->create_project_market: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_market_create** | [**ProjectMarketCreate**](ProjectMarketCreate.md)|  | 

### Return type

[**ProjectMarketResponse**](ProjectMarketResponse.md)

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

# **delete_project_market**
> ProjectMarketResponse delete_project_market(id)

Delete Project Market

Delete a project market.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectMarketApi()
id = 'id_example' # str | 

try:
    # Delete Project Market
    api_response = api_instance.delete_project_market(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMarketApi->delete_project_market: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectMarketResponse**](ProjectMarketResponse.md)

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

# **get_project_market**
> ProjectMarketResponse get_project_market(id)

Get Project Market

Get project market by ID.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectMarketApi()
id = 'id_example' # str | 

try:
    # Get Project Market
    api_response = api_instance.get_project_market(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMarketApi->get_project_market: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectMarketResponse**](ProjectMarketResponse.md)

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

# **list_project_markets**
> ProjectMarketListResponse list_project_markets()

List Project Markets

Retrieve project markets.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectMarketApi()

try:
    # List Project Markets
    api_response = api_instance.list_project_markets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMarketApi->list_project_markets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectMarketListResponse**](ProjectMarketListResponse.md)

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

# **update_project_market**
> ProjectMarketResponse update_project_market(id, project_market_update)

Update Project Market

Update a project market.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectMarketApi()
id = 'id_example' # str | 
project_market_update = project.ProjectMarketUpdate() # ProjectMarketUpdate | 

try:
    # Update Project Market
    api_response = api_instance.update_project_market(id, project_market_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectMarketApi->update_project_market: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project_market_update** | [**ProjectMarketUpdate**](ProjectMarketUpdate.md)|  | 

### Return type

[**ProjectMarketResponse**](ProjectMarketResponse.md)

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

