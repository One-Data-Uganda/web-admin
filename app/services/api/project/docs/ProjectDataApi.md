# project.ProjectDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_data**](ProjectDataApi.md#create_project_data) | **POST** /v1/project-data/ | Create Project Data
[**delete_project_data**](ProjectDataApi.md#delete_project_data) | **DELETE** /v1/project-data/{id} | Delete Project Data
[**get_project_data**](ProjectDataApi.md#get_project_data) | **GET** /v1/project-data/{id} | Get Project Data
[**list_project_datas**](ProjectDataApi.md#list_project_datas) | **GET** /v1/project-data/ | List Project Datas
[**update_project_data**](ProjectDataApi.md#update_project_data) | **PUT** /v1/project-data/{id} | Update Project Data


# **create_project_data**
> ProjectDataResponse create_project_data(project_data_create)

Create Project Data

Create new project_data.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectDataApi()
project_data_create = project.ProjectDataCreate() # ProjectDataCreate | 

try:
    # Create Project Data
    api_response = api_instance.create_project_data(project_data_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectDataApi->create_project_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_data_create** | [**ProjectDataCreate**](ProjectDataCreate.md)|  | 

### Return type

[**ProjectDataResponse**](ProjectDataResponse.md)

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

# **delete_project_data**
> ProjectDataResponse delete_project_data(id)

Delete Project Data

Delete a project data.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectDataApi()
id = 'id_example' # str | 

try:
    # Delete Project Data
    api_response = api_instance.delete_project_data(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectDataApi->delete_project_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectDataResponse**](ProjectDataResponse.md)

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

# **get_project_data**
> ProjectDataResponse get_project_data(id)

Get Project Data

Get project data by ID.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectDataApi()
id = 'id_example' # str | 

try:
    # Get Project Data
    api_response = api_instance.get_project_data(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectDataApi->get_project_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectDataResponse**](ProjectDataResponse.md)

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

# **list_project_datas**
> ProjectDataListResponse list_project_datas()

List Project Datas

Retrieve project datas.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectDataApi()

try:
    # List Project Datas
    api_response = api_instance.list_project_datas()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectDataApi->list_project_datas: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectDataListResponse**](ProjectDataListResponse.md)

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

# **update_project_data**
> ProjectDataResponse update_project_data(id, project_data_update)

Update Project Data

Update a project data.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectDataApi()
id = 'id_example' # str | 
project_data_update = project.ProjectDataUpdate() # ProjectDataUpdate | 

try:
    # Update Project Data
    api_response = api_instance.update_project_data(id, project_data_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectDataApi->update_project_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project_data_update** | [**ProjectDataUpdate**](ProjectDataUpdate.md)|  | 

### Return type

[**ProjectDataResponse**](ProjectDataResponse.md)

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

