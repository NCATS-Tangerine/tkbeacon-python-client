# tkbeacon.ConceptsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concept_details**](ConceptsApi.md#get_concept_details) | **GET** /concepts/{concept_id} | 
[**get_concepts**](ConceptsApi.md#get_concepts) | **GET** /concepts | 
[**get_exact_matches_to_concept_list**](ConceptsApi.md#get_exact_matches_to_concept_list) | **GET** /exactmatches | 


# **get_concept_details**
> BeaconConceptWithDetails get_concept_details(concept_id)



Retrieves details for a specified concepts in the system, as specified by a (url-encoded) CURIE identifier of a concept known the given knowledge source. 

### Example
```python
from __future__ import print_function
import time
import tkbeacon
from tkbeacon.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tkbeacon.ConceptsApi()
concept_id = 'concept_id_example' # str | (url-encoded) CURIE identifier of concept of interest

try:
    api_response = api_instance.get_concept_details(concept_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concept_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **concept_id** | **str**| (url-encoded) CURIE identifier of concept of interest | 

### Return type

[**BeaconConceptWithDetails**](BeaconConceptWithDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_concepts**
> list[BeaconConcept] get_concepts(keywords=keywords, categories=categories, offset=offset, size=size)



Retrieves a list of whose concept in the beacon knowledge base with names and/or synonyms matching a set of keywords or substrings. The results returned should generally be returned in order of the quality of the match, that is, the highest ranked concepts should exactly match the most keywords, in the same order as the keywords were given. Lower quality hits with fewer keyword matches or out-of-order keyword matches, should be returned lower in the list. 

### Example
```python
from __future__ import print_function
import time
import tkbeacon
from tkbeacon.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tkbeacon.ConceptsApi()
keywords = ['keywords_example'] # list[str] | (Optional) array of keywords or substrings against which to match concept names and synonyms (optional)
categories = ['categories_example'] # list[str] | (Optional) array set of concept categories - specified as Biolink name labels codes gene, pathway, etc. - to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of terms)  (optional)
offset = 56 # int | offset (cursor position) to next batch of statements of amount 'size' to return.  (optional)
size = 56 # int | maximum number of concept entries requested by the client; if this argument is omitted, then the query is expected to returned all the available data for the query  (optional)

try:
    api_response = api_instance.get_concepts(keywords=keywords, categories=categories, offset=offset, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_concepts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keywords** | [**list[str]**](str.md)| (Optional) array of keywords or substrings against which to match concept names and synonyms | [optional] 
 **categories** | [**list[str]**](str.md)| (Optional) array set of concept categories - specified as Biolink name labels codes gene, pathway, etc. - to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of terms)  | [optional] 
 **offset** | **int**| offset (cursor position) to next batch of statements of amount &#39;size&#39; to return.  | [optional] 
 **size** | **int**| maximum number of concept entries requested by the client; if this argument is omitted, then the query is expected to returned all the available data for the query  | [optional] 

### Return type

[**list[BeaconConcept]**](BeaconConcept.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_exact_matches_to_concept_list**
> list[ExactMatchResponse] get_exact_matches_to_concept_list(c)



Given an input array of [CURIE](https://www.w3.org/TR/curie/) identifiers of known exactly matched concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch), retrieves the list of [CURIE](https://www.w3.org/TR/curie/) identifiers of additional concepts that are deemed by the given knowledge source to be exact matches to one or more of the input concepts **plus** whichever concept identifiers from the input list were specifically matched to these additional concepts, thus giving the whole known set of equivalent concepts known to this particular knowledge source.  If an empty set is returned, the it can be assumed that the given knowledge source does not know of any new equivalent concepts matching the input set. The caller of this endpoint can then decide whether or not to treat  its input identifiers as its own equivalent set. 

### Example
```python
from __future__ import print_function
import time
import tkbeacon
from tkbeacon.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = tkbeacon.ConceptsApi()
c = ['c_example'] # list[str] | an array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of concepts thought to be exactly matching concepts, to be used in a search for additional exactly matching concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch). 

try:
    api_response = api_instance.get_exact_matches_to_concept_list(c)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConceptsApi->get_exact_matches_to_concept_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **c** | [**list[str]**](str.md)| an array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of concepts thought to be exactly matching concepts, to be used in a search for additional exactly matching concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch).  | 

### Return type

[**list[ExactMatchResponse]**](ExactMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

