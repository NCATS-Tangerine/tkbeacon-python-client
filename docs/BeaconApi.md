# tkbeacon.BeaconApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_concept_categories**](BeaconApi.md#get_concept_categories) | **GET** /categories | 
[**get_concept_details**](BeaconApi.md#get_concept_details) | **GET** /concepts/{concept_id} | 
[**get_concepts**](BeaconApi.md#get_concepts) | **GET** /concepts | 
[**get_exact_matches_to_concept_list**](BeaconApi.md#get_exact_matches_to_concept_list) | **GET** /exactmatches | 
[**get_knowledge_map**](BeaconApi.md#get_knowledge_map) | **GET** /kmap | 
[**get_predicates**](BeaconApi.md#get_predicates) | **GET** /predicates | 
[**get_statement_details**](BeaconApi.md#get_statement_details) | **GET** /statements/{statement_id} | 
[**get_statements**](BeaconApi.md#get_statements) | **GET** /statements | 


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

# Enter a context with an instance of the API client
with tkbeacon.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tkbeacon.BeaconApi(api_client)
    
    try:
        api_response = api_instance.get_concept_categories()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BeaconApi->get_concept_categories: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with categories and frequency returned  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# Enter a context with an instance of the API client
with tkbeacon.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tkbeacon.BeaconApi(api_client)
    concept_id = 'concept_id_example' # str | (url-encoded) CURIE identifier of concept of interest

    try:
        api_response = api_instance.get_concept_details(concept_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BeaconApi->get_concept_details: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with concept details returned  |  -  |

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

# Enter a context with an instance of the API client
with tkbeacon.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tkbeacon.BeaconApi(api_client)
    keywords = ['keywords_example'] # list[str] | (Optional) array of keywords or substrings against which to match concept names and synonyms (optional)
categories = ['categories_example'] # list[str] | (Optional) array set of concept categories - specified as Biolink name labels codes gene, pathway, etc. - to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of terms)  (optional)
offset = 56 # int | offset (cursor position) to next batch of statements of amount 'size' to return.  (optional)
size = 56 # int | maximum number of concept entries requested by the client; if this argument is omitted, then the query is expected to returned all the available data for the query  (optional)

    try:
        api_response = api_instance.get_concepts(keywords=keywords, categories=categories, offset=offset, size=size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BeaconApi->get_concepts: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with list of core concept data returned  |  -  |

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

# Enter a context with an instance of the API client
with tkbeacon.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tkbeacon.BeaconApi(api_client)
    c = ['c_example'] # list[str] | an array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of concepts thought to be exactly matching concepts, to be used in a search for additional exactly matching concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch). 

    try:
        api_response = api_instance.get_exact_matches_to_concept_list(c)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BeaconApi->get_exact_matches_to_concept_list: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returns a set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of concepts (with supporting evidence code and reference) matching at least one identifier in the input list of known exactly matched concepts [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch). Each concept identifier is returned with  the full list of any additional associated [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of exact match concepts known to the given Knowledge Source.  |  -  |

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

# Enter a context with an instance of the API client
with tkbeacon.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tkbeacon.BeaconApi(api_client)
    
    try:
        api_response = api_instance.get_knowledge_map()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BeaconApi->get_knowledge_map: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with categories and frequency returned  |  -  |

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

# Enter a context with an instance of the API client
with tkbeacon.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tkbeacon.BeaconApi(api_client)
    
    try:
        api_response = api_instance.get_predicates()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BeaconApi->get_predicates: %s\n" % e)
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

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with predicates with CURIE and definitions indexed by beacons which support the relation  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statement_details**
> BeaconStatementWithDetails get_statement_details(statement_id, keywords=keywords, offset=offset, size=size)



Retrieves a details relating to a specified concept-relationship statement include 'is_defined_by and 'provided_by' provenance; extended edge properties exported as tag = value; and any associated annotations (publications, etc.)  cited as evidence for the given statement. 

### Example

```python
from __future__ import print_function
import time
import tkbeacon
from tkbeacon.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with tkbeacon.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tkbeacon.BeaconApi(api_client)
    statement_id = 'statement_id_example' # str | (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought 
keywords = ['keywords_example'] # list[str] | an array of keywords or substrings against which to  filter annotation names (e.g. publication titles). (optional)
offset = 56 # int | offset (cursor position) to next batch of annotation entries of amount 'size' to return.  (optional)
size = 56 # int | maximum number of evidence citation entries requested by the client; if this  argument is omitted, then the query is expected to returned all of the available annotation for this statement  (optional)

    try:
        api_response = api_instance.get_statement_details(statement_id, keywords=keywords, offset=offset, size=size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BeaconApi->get_statement_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **statement_id** | **str**| (url-encoded) CURIE identifier of the concept-relationship statement (\&quot;assertion\&quot;, \&quot;claim\&quot;) for which associated evidence is sought  | 
 **keywords** | [**list[str]**](str.md)| an array of keywords or substrings against which to  filter annotation names (e.g. publication titles). | [optional] 
 **offset** | **int**| offset (cursor position) to next batch of annotation entries of amount &#39;size&#39; to return.  | [optional] 
 **size** | **int**| maximum number of evidence citation entries requested by the client; if this  argument is omitted, then the query is expected to returned all of the available annotation for this statement  | [optional] 

### Return type

[**BeaconStatementWithDetails**](BeaconStatementWithDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful call with statement details returned  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_statements**
> list[BeaconStatement] get_statements(s=s, s_keywords=s_keywords, s_categories=s_categories, edge_label=edge_label, relation=relation, t=t, t_keywords=t_keywords, t_categories=t_categories, offset=offset, size=size)



Given a constrained set of some [CURIE-encoded](https://www.w3.org/TR/curie/) 's' ('source') concept identifiers, categories and/or keywords (to match in the concept name or description), retrieves a list of relationship statements where either the subject or the object concept matches any of the input source concepts provided.  Optionally, a set of some 't' ('target') concept identifiers, categories and/or keywords (to match in the concept name or description) may also be given, in which case a member of the 't' concept set should matchthe concept opposite an 's' concept in the statement. That is, if the 's' concept matches a subject, then the 't' concept should match the object of a given statement (or vice versa). 

### Example

```python
from __future__ import print_function
import time
import tkbeacon
from tkbeacon.rest import ApiException
from pprint import pprint

# Enter a context with an instance of the API client
with tkbeacon.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = tkbeacon.BeaconApi(api_client)
    s = ['s_example'] # list[str] | An (optional) array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of 'source' ('start') concepts possibly known to the beacon. Unknown CURIES should simply be ignored (silent match failure).  (optional)
s_keywords = ['s_keywords_example'] # list[str] | An (optional) array of keywords or substrings against which to filter 'source' concept names and synonyms (optional)
s_categories = ['s_categories_example'] # list[str] | An (optional) array set of 'source' concept categories (specified as Biolink name labels codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  (optional)
edge_label = 'edge_label_example' # str | (Optional) predicate edge label against which to constrain the search for statements ('edges') associated with the given query seed concept. The predicate edge_names for this parameter should be as published by the /predicates API endpoint and must be taken from the minimal predicate ('slot') list of the [Biolink Model](https://biolink.github.io/biolink-model).  (optional)
relation = 'relation_example' # str | (Optional) predicate relation against which to constrain the search for statements ('edges') associated with the given query seed concept. The predicate relations for this parameter should be as published by the /predicates API endpoint and the preferred format is a CURIE  where one exists, but strings/labels acceptable. This relation may be equivalent to the edge_label (e.g. edge_label: has_phenotype, relation: RO:0002200), or a more specific relation in cases where the source provides more granularity (e.g. edge_label: molecularly_interacts_with, relation: RO:0002447)  (optional)
t = ['t_example'] # list[str] | An (optional) array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of 'target' ('opposite' or 'end') concepts possibly known to the beacon. Unknown CURIEs should simply be ignored (silent match failure).  (optional)
t_keywords = ['t_keywords_example'] # list[str] | An (optional) array of keywords or substrings against which to filter 'target' concept names and synonyms (optional)
t_categories = ['t_categories_example'] # list[str] | An (optional) array set of 'target' concept categories (specified as Biolink name labels codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  (optional)
offset = 56 # int | offset (cursor position) to next batch of statements of amount 'size' to return.  (optional)
size = 56 # int | maximum number of concept entries requested by the client; if this argument is omitted, then the query is expected to returned all  the available data for the query  (optional)

    try:
        api_response = api_instance.get_statements(s=s, s_keywords=s_keywords, s_categories=s_categories, edge_label=edge_label, relation=relation, t=t, t_keywords=t_keywords, t_categories=t_categories, offset=offset, size=size)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BeaconApi->get_statements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **s** | [**list[str]**](str.md)| An (optional) array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of &#39;source&#39; (&#39;start&#39;) concepts possibly known to the beacon. Unknown CURIES should simply be ignored (silent match failure).  | [optional] 
 **s_keywords** | [**list[str]**](str.md)| An (optional) array of keywords or substrings against which to filter &#39;source&#39; concept names and synonyms | [optional] 
 **s_categories** | [**list[str]**](str.md)| An (optional) array set of &#39;source&#39; concept categories (specified as Biolink name labels codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  | [optional] 
 **edge_label** | **str**| (Optional) predicate edge label against which to constrain the search for statements (&#39;edges&#39;) associated with the given query seed concept. The predicate edge_names for this parameter should be as published by the /predicates API endpoint and must be taken from the minimal predicate (&#39;slot&#39;) list of the [Biolink Model](https://biolink.github.io/biolink-model).  | [optional] 
 **relation** | **str**| (Optional) predicate relation against which to constrain the search for statements (&#39;edges&#39;) associated with the given query seed concept. The predicate relations for this parameter should be as published by the /predicates API endpoint and the preferred format is a CURIE  where one exists, but strings/labels acceptable. This relation may be equivalent to the edge_label (e.g. edge_label: has_phenotype, relation: RO:0002200), or a more specific relation in cases where the source provides more granularity (e.g. edge_label: molecularly_interacts_with, relation: RO:0002447)  | [optional] 
 **t** | [**list[str]**](str.md)| An (optional) array set of [CURIE-encoded](https://www.w3.org/TR/curie/) identifiers of &#39;target&#39; (&#39;opposite&#39; or &#39;end&#39;) concepts possibly known to the beacon. Unknown CURIEs should simply be ignored (silent match failure).  | [optional] 
 **t_keywords** | [**list[str]**](str.md)| An (optional) array of keywords or substrings against which to filter &#39;target&#39; concept names and synonyms | [optional] 
 **t_categories** | [**list[str]**](str.md)| An (optional) array set of &#39;target&#39; concept categories (specified as Biolink name labels codes gene, pathway, etc.) to which to constrain concepts matched by the main keyword search (see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of codes)  | [optional] 
 **offset** | **int**| offset (cursor position) to next batch of statements of amount &#39;size&#39; to return.  | [optional] 
 **size** | **int**| maximum number of concept entries requested by the client; if this argument is omitted, then the query is expected to returned all  the available data for the query  | [optional] 

### Return type

[**list[BeaconStatement]**](BeaconStatement.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response returns a list of concept-relations where there is an exact match of an input concept identifier either to the subject or object concepts  of the statement  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

