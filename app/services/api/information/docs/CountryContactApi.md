# information.CountryContactApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_country_contact**](CountryContactApi.md#create_country_contact) | **POST** /v1/country-contact/ | Create Country Contact
[**delete_country_contact**](CountryContactApi.md#delete_country_contact) | **DELETE** /v1/country-contact/{id} | Delete Country Contact
[**get_country_contact**](CountryContactApi.md#get_country_contact) | **GET** /v1/country-contact/{id} | Get Country Contact
[**list_country_contacts**](CountryContactApi.md#list_country_contacts) | **GET** /v1/country-contact/ | List Country Contacts
[**update_country_contact**](CountryContactApi.md#update_country_contact) | **PUT** /v1/country-contact/{id} | Update Country Contact


# **create_country_contact**
> CountryContact create_country_contact(country_contact_create)

Create Country Contact

Create new country_contact.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryContactApi()
country_contact_create = information.CountryContactCreate() # CountryContactCreate | 

try:
    # Create Country Contact
    api_response = api_instance.create_country_contact(country_contact_create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryContactApi->create_country_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **country_contact_create** | [**CountryContactCreate**](CountryContactCreate.md)|  | 

### Return type

[**CountryContact**](CountryContact.md)

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

# **delete_country_contact**
> CountryContact delete_country_contact(id)

Delete Country Contact

Delete an country_contact.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryContactApi()
id = 'id_example' # str | 

try:
    # Delete Country Contact
    api_response = api_instance.delete_country_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryContactApi->delete_country_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CountryContact**](CountryContact.md)

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

# **get_country_contact**
> CountryContact get_country_contact(id)

Get Country Contact

Get country_contact by ID.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryContactApi()
id = 'id_example' # str | 

try:
    # Get Country Contact
    api_response = api_instance.get_country_contact(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryContactApi->get_country_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CountryContact**](CountryContact.md)

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

# **list_country_contacts**
> List[CountryContact] list_country_contacts()

List Country Contacts

Retrieve country_contacts.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryContactApi()

try:
    # List Country Contacts
    api_response = api_instance.list_country_contacts()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryContactApi->list_country_contacts: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[CountryContact]**](CountryContact.md)

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

# **update_country_contact**
> CountryContact update_country_contact(id, country_contact_update)

Update Country Contact

Update a country_contact.

### Example

```python
from __future__ import print_function
import time
import information
from information.rest import ApiException
from pprint import pprint

# Create an instance of the API class
api_instance = information.CountryContactApi()
id = 'id_example' # str | 
country_contact_update = information.CountryContactUpdate() # CountryContactUpdate | 

try:
    # Update Country Contact
    api_response = api_instance.update_country_contact(id, country_contact_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CountryContactApi->update_country_contact: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **country_contact_update** | [**CountryContactUpdate**](CountryContactUpdate.md)|  | 

### Return type

[**CountryContact**](CountryContact.md)

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

