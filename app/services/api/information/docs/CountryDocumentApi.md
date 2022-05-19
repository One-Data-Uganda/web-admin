# information.CountryDocumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_country_document**](CountryDocumentApi.md#create_country_document) | **POST** /v1/country-document/ | Create Country Document
[**delete_country_document**](CountryDocumentApi.md#delete_country_document) | **DELETE** /v1/country-document/{id} | Delete Country Document
[**get_country_document**](CountryDocumentApi.md#get_country_document) | **GET** /v1/country-document/{id} | Get Country Document
[**get_country_document_file**](CountryDocumentApi.md#get_country_document_file) | **GET** /v1/country-document/{id}/file | Get Country Document File
[**list_country_documents**](CountryDocumentApi.md#list_country_documents) | **GET** /v1/country-document/{country_id}/list | List Country Documents
[**update_country_document**](CountryDocumentApi.md#update_country_document) | **PUT** /v1/country-document/{id} | Update Country Document


# **create_country_document**
> CountryDocument create_country_document(country_document_create)

Create Country Document

Create new country_document.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryDocumentApi()
country_document_create = information.CountryDocumentCreate() # CountryDocumentCreate | 

try:
    # Create Country Document
    api_response = api_instance.create_country_document(country_document_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryDocumentApi->create_country_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_document_create** | [**CountryDocumentCreate**](CountryDocumentCreate.md)|  | 

### Return type

[**CountryDocument**](CountryDocument.md)

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

# **delete_country_document**
> CountryDocument delete_country_document(id)

Delete Country Document

Delete an country_document.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryDocumentApi()
id = 'id_example' # str | 

try:
    # Delete Country Document
    api_response = api_instance.delete_country_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryDocumentApi->delete_country_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**CountryDocument**](CountryDocument.md)

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

# **get_country_document**
> CountryDocument get_country_document(id)

Get Country Document

Get country_document by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryDocumentApi()
id = 'id_example' # str | 

try:
    # Get Country Document
    api_response = api_instance.get_country_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryDocumentApi->get_country_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**CountryDocument**](CountryDocument.md)

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

# **get_country_document_file**
> Any get_country_document_file(id)

Get Country Document File

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryDocumentApi()
id = 'id_example' # str | 

try:
    # Get Country Document File
    api_response = api_instance.get_country_document_file(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryDocumentApi->get_country_document_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**Any**](Any.md)

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

# **list_country_documents**
> List[CountryDocument] list_country_documents(country_id)

List Country Documents

Retrieve country_documents.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryDocumentApi()
country_id = 'country_id_example' # str | 

try:
    # List Country Documents
    api_response = api_instance.list_country_documents(country_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryDocumentApi->list_country_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_id** | **str**|  | 

### Return type

[**List[CountryDocument]**](CountryDocument.md)

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

# **update_country_document**
> CountryDocument update_country_document(id, country_document_update)

Update Country Document

Update a country_document.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryDocumentApi()
id = 'id_example' # str | 
country_document_update = information.CountryDocumentUpdate() # CountryDocumentUpdate | 

try:
    # Update Country Document
    api_response = api_instance.update_country_document(id, country_document_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryDocumentApi->update_country_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **country_document_update** | [**CountryDocumentUpdate**](CountryDocumentUpdate.md)|  | 

### Return type

[**CountryDocument**](CountryDocument.md)

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

