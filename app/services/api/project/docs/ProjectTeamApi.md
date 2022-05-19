# project.ProjectTeamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_project_team**](ProjectTeamApi.md#create_project_team) | **POST** /v1/project-team/ | Create Project Team
[**delete_project_team**](ProjectTeamApi.md#delete_project_team) | **DELETE** /v1/project-team/{id} | Delete Project Team
[**get_project_team**](ProjectTeamApi.md#get_project_team) | **GET** /v1/project-team/{id} | Get Project Team
[**list_project_teams**](ProjectTeamApi.md#list_project_teams) | **GET** /v1/project-team/ | List Project Teams
[**update_project_team**](ProjectTeamApi.md#update_project_team) | **PUT** /v1/project-team/{id} | Update Project Team


# **create_project_team**
> ProjectTeamResponse create_project_team(project_team_create)

Create Project Team

Create new project_team.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectTeamApi()
project_team_create = project.ProjectTeamCreate() # ProjectTeamCreate | 

try:
    # Create Project Team
    api_response = api_instance.create_project_team(project_team_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTeamApi->create_project_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_team_create** | [**ProjectTeamCreate**](ProjectTeamCreate.md)|  | 

### Return type

[**ProjectTeamResponse**](ProjectTeamResponse.md)

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

# **delete_project_team**
> ProjectTeamResponse delete_project_team(id)

Delete Project Team

Delete a project team.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectTeamApi()
id = 'id_example' # str | 

try:
    # Delete Project Team
    api_response = api_instance.delete_project_team(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTeamApi->delete_project_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectTeamResponse**](ProjectTeamResponse.md)

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

# **get_project_team**
> ProjectTeamResponse get_project_team(id)

Get Project Team

Get project team by ID.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectTeamApi()
id = 'id_example' # str | 

try:
    # Get Project Team
    api_response = api_instance.get_project_team(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTeamApi->get_project_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ProjectTeamResponse**](ProjectTeamResponse.md)

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

# **list_project_teams**
> ProjectTeamListResponse list_project_teams()

List Project Teams

Retrieve project teams.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectTeamApi()

try:
    # List Project Teams
    api_response = api_instance.list_project_teams()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTeamApi->list_project_teams: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ProjectTeamListResponse**](ProjectTeamListResponse.md)

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

# **update_project_team**
> ProjectTeamResponse update_project_team(id, project_team_update)

Update Project Team

Update a project team.

### Example

```python
from __future__ import print_function
import time
import project
from project.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = project.ProjectTeamApi()
id = 'id_example' # str | 
project_team_update = project.ProjectTeamUpdate() # ProjectTeamUpdate | 

try:
    # Update Project Team
    api_response = api_instance.update_project_team(id, project_team_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectTeamApi->update_project_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **project_team_update** | [**ProjectTeamUpdate**](ProjectTeamUpdate.md)|  | 

### Return type

[**ProjectTeamResponse**](ProjectTeamResponse.md)

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

