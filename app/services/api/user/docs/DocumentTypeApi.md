# user.DocumentTypeApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_document_type**](DocumentTypeApi.md#create_document_type) | **POST** /v1/document-type/ | Create Document Type
[**delete_document_type**](DocumentTypeApi.md#delete_document_type) | **DELETE** /v1/document-type/{id} | Delete Document Type
[**get_document_type**](DocumentTypeApi.md#get_document_type) | **GET** /v1/document-type/{id} | Get Document Type
[**list_document_types**](DocumentTypeApi.md#list_document_types) | **GET** /v1/document-type/ | List Document Types
[**update_document_type**](DocumentTypeApi.md#update_document_type) | **PUT** /v1/document-type/{id} | Update Document Type


# **create_document_type**
> DocumentTypeResponse create_document_type(document_type_create)

Create Document Type

Create new document_type.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.DocumentTypeApi()
document_type_create = user.DocumentTypeCreate() # DocumentTypeCreate | 

try:
    # Create Document Type
    api_response = api_instance.create_document_type(document_type_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTypeApi->create_document_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_type_create** | [**DocumentTypeCreate**](DocumentTypeCreate.md)|  | 

### Return type

[**DocumentTypeResponse**](DocumentTypeResponse.md)

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

# **delete_document_type**
> DocumentTypeResponse delete_document_type(id)

Delete Document Type

Delete a document_type.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.DocumentTypeApi()
id = 'id_example' # str | 

try:
    # Delete Document Type
    api_response = api_instance.delete_document_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTypeApi->delete_document_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DocumentTypeResponse**](DocumentTypeResponse.md)

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

# **get_document_type**
> DocumentTypeResponse get_document_type(id)

Get Document Type

Get DocumentType

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.DocumentTypeApi()
id = 'id_example' # str | 

try:
    # Get Document Type
    api_response = api_instance.get_document_type(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTypeApi->get_document_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DocumentTypeResponse**](DocumentTypeResponse.md)

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

# **list_document_types**
> DocumentTypeListResponse list_document_types()

List Document Types

Get all document_types

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.DocumentTypeApi()

try:
    # List Document Types
    api_response = api_instance.list_document_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTypeApi->list_document_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DocumentTypeListResponse**](DocumentTypeListResponse.md)

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

# **update_document_type**
> DocumentTypeResponse update_document_type(id, document_type_update)

Update Document Type

Update document_type

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.DocumentTypeApi()
id = 'id_example' # str | 
document_type_update = user.DocumentTypeUpdate() # DocumentTypeUpdate | 

try:
    # Update Document Type
    api_response = api_instance.update_document_type(id, document_type_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DocumentTypeApi->update_document_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **document_type_update** | [**DocumentTypeUpdate**](DocumentTypeUpdate.md)|  | 

### Return type

[**DocumentTypeResponse**](DocumentTypeResponse.md)

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

