# user.KycApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_kyc_document**](KycApi.md#add_kyc_document) | **POST** /v1/kyc/{kyc_id}/document | Add Kyc Document
[**create_kyc**](KycApi.md#create_kyc) | **POST** /v1/kyc/ | Create Kyc
[**get_by_business_name**](KycApi.md#get_by_business_name) | **POST** /v1/kyc/check-business-name | Get By Business Name
[**get_by_email**](KycApi.md#get_by_email) | **POST** /v1/kyc/check-email | Get By Email
[**get_by_msisdn**](KycApi.md#get_by_msisdn) | **POST** /v1/kyc/check-msisdn | Get By Msisdn
[**get_kyc**](KycApi.md#get_kyc) | **GET** /v1/kyc/{id} | Get Kyc
[**get_kyc_document**](KycApi.md#get_kyc_document) | **GET** /v1/kyc/document/{id} | Get Kyc Document
[**get_kyc_document_file**](KycApi.md#get_kyc_document_file) | **GET** /v1/kyc/{kyc_id}/document/{id}/file | Get Kyc Document File
[**update_kyc**](KycApi.md#update_kyc) | **PUT** /v1/kyc/{id} | Update Kyc
[**update_kyc_document**](KycApi.md#update_kyc_document) | **PUT** /v1/kyc/{id}/document | Update Kyc Document


# **add_kyc_document**
> KYCDocumentResponse add_kyc_document(kyc_id, name, document_type_id, uploaded_file)

Add Kyc Document

Add a KYC document

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
kyc_id = 'kyc_id_example' # str | 
name = 'name_example' # str | 
document_type_id = 'document_type_id_example' # str | 
uploaded_file = user.IO() # IO | 

try:
    # Add Kyc Document
    api_response = api_instance.add_kyc_document(kyc_id, name, document_type_id, uploaded_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->add_kyc_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kyc_id** | [**str**](.md)|  | 
 **name** | **str**|  | 
 **document_type_id** | **str**|  | 
 **uploaded_file** | **IO**|  | 

### Return type

[**KYCDocumentResponse**](KYCDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kyc**
> KYCResponse create_kyc(kyc_create)

Create Kyc

Create new kyc.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
kyc_create = user.KYCCreate() # KYCCreate | 

try:
    # Create Kyc
    api_response = api_instance.create_kyc(kyc_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->create_kyc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kyc_create** | [**KYCCreate**](KYCCreate.md)|  | 

### Return type

[**KYCResponse**](KYCResponse.md)

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

# **get_by_business_name**
> KYCResponse get_by_business_name(business_name)

Get By Business Name

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
business_name = 'business_name_example' # str | 

try:
    # Get By Business Name
    api_response = api_instance.get_by_business_name(business_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->get_by_business_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **business_name** | **str**|  | 

### Return type

[**KYCResponse**](KYCResponse.md)

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

# **get_by_email**
> KYCResponse get_by_email(email)

Get By Email

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
email = 'email_example' # str | 

try:
    # Get By Email
    api_response = api_instance.get_by_email(email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->get_by_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**|  | 

### Return type

[**KYCResponse**](KYCResponse.md)

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

# **get_by_msisdn**
> KYCResponse get_by_msisdn(msisdn)

Get By Msisdn

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
msisdn = 'msisdn_example' # str | 

try:
    # Get By Msisdn
    api_response = api_instance.get_by_msisdn(msisdn)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->get_by_msisdn: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **msisdn** | **str**|  | 

### Return type

[**KYCResponse**](KYCResponse.md)

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

# **get_kyc**
> KYCResponse get_kyc(id)

Get Kyc

Get a specific kyc by id.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
id = 'id_example' # str | 

try:
    # Get Kyc
    api_response = api_instance.get_kyc(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->get_kyc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**KYCResponse**](KYCResponse.md)

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

# **get_kyc_document**
> KYCDocumentResponse get_kyc_document(id)

Get Kyc Document

Retrieve a KYC document

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
id = 'id_example' # str | 

try:
    # Get Kyc Document
    api_response = api_instance.get_kyc_document(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->get_kyc_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**KYCDocumentResponse**](KYCDocumentResponse.md)

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

# **get_kyc_document_file**
> Any get_kyc_document_file(kyc_id, id)

Get Kyc Document File

Retrieve a KYC document

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
kyc_id = 'kyc_id_example' # str | 
id = 'id_example' # str | 

try:
    # Get Kyc Document File
    api_response = api_instance.get_kyc_document_file(kyc_id, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->get_kyc_document_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **kyc_id** | [**str**](.md)|  | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kyc**
> KYCResponse update_kyc(id, kyc_update)

Update Kyc

Update a kyc.

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
id = 'id_example' # str | 
kyc_update = user.KYCUpdate() # KYCUpdate | 

try:
    # Update Kyc
    api_response = api_instance.update_kyc(id, kyc_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->update_kyc: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **kyc_update** | [**KYCUpdate**](KYCUpdate.md)|  | 

### Return type

[**KYCResponse**](KYCResponse.md)

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

# **update_kyc_document**
> KYCDocumentResponse update_kyc_document(id, uploaded_file)

Update Kyc Document

Update a KYC document

### Example

```python
from __future__ import print_function
import time
import user
from user.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = user.KycApi()
id = 'id_example' # str | 
uploaded_file = user.IO() # IO | 

try:
    # Update Kyc Document
    api_response = api_instance.update_kyc_document(id, uploaded_file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling KycApi->update_kyc_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **uploaded_file** | **IO**|  | 

### Return type

[**KYCDocumentResponse**](KYCDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

