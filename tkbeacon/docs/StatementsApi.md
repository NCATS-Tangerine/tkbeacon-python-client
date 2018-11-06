# tkbeacon.StatementsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_statement_details**](StatementsApi.md#get_statement_details) | **GET** /statements/{statement_id} | 
[**get_statements**](StatementsApi.md#get_statements) | **GET** /statements | 


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

# create an instance of the API class
api_instance = tkbeacon.StatementsApi()
statement_id = 'statement_id_example' # str | (url-encoded) CURIE identifier of the concept-relationship statement (\"assertion\", \"claim\") for which associated evidence is sought 
keywords = ['keywords_example'] # list[str] | an array of keywords or substrings against which to  filter annotation names (e.g. publication titles). (optional)
offset = 56 # int | offset (cursor position) to next batch of annotation entries of amount 'size' to return.  (optional)
size = 56 # int | maximum number of evidence citation entries requested by the client; if this  argument is omitted, then the query is expected to returned all of the available annotation for this statement  (optional)

try:
    api_response = api_instance.get_statement_details(statement_id, keywords=keywords, offset=offset, size=size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StatementsApi->get_statement_details: %s\n" % e)
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

# create an instance of the API class
api_instance = tkbeacon.StatementsApi()
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
    print("Exception when calling StatementsApi->get_statements: %s\n" % e)
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

