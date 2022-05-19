# project.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project**](ProjectApi.md#create_project) | **POST** /v1/project/ | Create Project
[**delete_project**](ProjectApi.md#delete_project) | **DELETE** /v1/project/{id} | Delete Project
[**get_project**](ProjectApi.md#get_project) | **GET** /v1/project/{id} | Get Project
[**list_projects**](ProjectApi.md#list_projects) | **GET** /v1/project/ | List Projects
[**update_project**](ProjectApi.md#update_project) | **PUT** /v1/project/{id} | Update Project


# **create_project**
> ProjectResponse create_project(project_create)

Create Project

Create new project.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectApi()
project_create = project.ProjectCreate() # ProjectCreate | 

try:
    # Create Project
    api_response = api_instance.create_project(project_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_create** | [**ProjectCreate**](ProjectCreate.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

# **delete_project**
> ProjectResponse delete_project(id)

Delete Project

Delete a project.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectApi()
id = 'id_example' # str | 

try:
    # Delete Project
    api_response = api_instance.delete_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

# **get_project**
> ProjectResponse get_project(id)

Get Project

Get project by ID.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectApi()
id = 'id_example' # str | 

try:
    # Get Project
    api_response = api_instance.get_project(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->get_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

# **list_projects**
> ProjectListResponse list_projects()

List Projects

Retrieve projects.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectApi()

try:
    # List Projects
    api_response = api_instance.list_projects()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->list_projects: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectListResponse**](ProjectListResponse.md)

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

# **update_project**
> ProjectResponse update_project(id, project_update)

Update Project

Update a project.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectApi()
id = 'id_example' # str | 
project_update = project.ProjectUpdate() # ProjectUpdate | 

try:
    # Update Project
    api_response = api_instance.update_project(id, project_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **project_update** | [**ProjectUpdate**](ProjectUpdate.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

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

