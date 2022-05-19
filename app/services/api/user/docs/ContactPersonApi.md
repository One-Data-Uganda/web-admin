# user.ContactPersonApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_person**](ContactPersonApi.md#create_contact_person) | **POST** /v1/contact-person/ | Create Contact Person
[**delete_contact_person**](ContactPersonApi.md#delete_contact_person) | **DELETE** /v1/contact-person/{id} | Delete Contact Person
[**get_contact_person**](ContactPersonApi.md#get_contact_person) | **GET** /v1/contact-person/{id} | Get Contact Person
[**list_contact_persons**](ContactPersonApi.md#list_contact_persons) | **GET** /v1/contact-person/ | List Contact Persons
[**update_contact_person**](ContactPersonApi.md#update_contact_person) | **PUT** /v1/contact-person/{id} | Update Contact Person


# **create_contact_person**
> ContactPersonResponse create_contact_person(contact_person_create)

Create Contact Person

Create new contact person.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ContactPersonApi()
contact_person_create = user.ContactPersonCreate() # ContactPersonCreate | 

try:
    # Create Contact Person
    api_response = api_instance.create_contact_person(contact_person_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactPersonApi->create_contact_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **contact_person_create** | [**ContactPersonCreate**](ContactPersonCreate.md)|  | 

### Return type

[**ContactPersonResponse**](ContactPersonResponse.md)

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

# **delete_contact_person**
> ContactPersonResponse delete_contact_person(id)

Delete Contact Person

Delete contact_person

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ContactPersonApi()
id = 56 # int | 

try:
    # Delete Contact Person
    api_response = api_instance.delete_contact_person(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactPersonApi->delete_contact_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ContactPersonResponse**](ContactPersonResponse.md)

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

# **get_contact_person**
> ContactPersonResponse get_contact_person(id)

Get Contact Person

Get a specific contact_person by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ContactPersonApi()
id = 56 # int | 

try:
    # Get Contact Person
    api_response = api_instance.get_contact_person(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactPersonApi->get_contact_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**ContactPersonResponse**](ContactPersonResponse.md)

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

# **list_contact_persons**
> ContactPersonListResponse list_contact_persons()

List Contact Persons

Contact Person listing

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ContactPersonApi()

try:
    # List Contact Persons
    api_response = api_instance.list_contact_persons()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactPersonApi->list_contact_persons: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContactPersonListResponse**](ContactPersonListResponse.md)

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

# **update_contact_person**
> ContactPersonResponse update_contact_person(id, contact_person_update)

Update Contact Person

Update a contact_person.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.ContactPersonApi()
id = 56 # int | 
contact_person_update = user.ContactPersonUpdate() # ContactPersonUpdate | 

try:
    # Update Contact Person
    api_response = api_instance.update_contact_person(id, contact_person_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ContactPersonApi->update_contact_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **contact_person_update** | [**ContactPersonUpdate**](ContactPersonUpdate.md)|  | 

### Return type

[**ContactPersonResponse**](ContactPersonResponse.md)

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

