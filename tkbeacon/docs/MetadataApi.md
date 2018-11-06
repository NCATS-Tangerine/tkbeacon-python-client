# tkbeacon.MetadataApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concept_categories**](MetadataApi.md#get_concept_categories) | **GET** /categories | 
[**get_knowledge_map**](MetadataApi.md#get_knowledge_map) | **GET** /kmap | 
[**get_predicates**](MetadataApi.md#get_predicates) | **GET** /predicates | 


# **get_concept_categories**
> list[BeaconConceptCategory] get_concept_categories()



Get a list of concept categories and number of their concept instances documented by the knowledge source. These types should be mapped onto the Translator-endorsed Biolink Model concept type classes with local types, explicitly added as mappings to the Biolink Model YAML file. A frequency of -1 indicates the category can exist, but the count is unknown. 

### Example
```python
from __future__ import print_function
import time
import tkbeacon
from tkbeacon.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tkbeacon.MetadataApi()

try:
    api_response = api_instance.get_concept_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_concept_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BeaconConceptCategory]**](BeaconConceptCategory.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_knowledge_map**
> list[BeaconKnowledgeMapStatement] get_knowledge_map()



Get a high level knowledge map of the all the beacons by subject semantic type, predicate and semantic object type 

### Example
```python
from __future__ import print_function
import time
import tkbeacon
from tkbeacon.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tkbeacon.MetadataApi()

try:
    api_response = api_instance.get_knowledge_map()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_knowledge_map: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BeaconKnowledgeMapStatement]**](BeaconKnowledgeMapStatement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_predicates**
> list[BeaconPredicate] get_predicates()



Get a list of predicates used in statements issued by the knowledge source 

### Example
```python
from __future__ import print_function
import time
import tkbeacon
from tkbeacon.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tkbeacon.MetadataApi()

try:
    api_response = api_instance.get_predicates()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetadataApi->get_predicates: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[BeaconPredicate]**](BeaconPredicate.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

