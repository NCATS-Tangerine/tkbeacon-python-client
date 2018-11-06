# BeaconConceptWithDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | local object CURIE for the concept in the specified knowledge source database  | [optional] 
**uri** | **str** | (optional) equivalent to expansion of the CURIE  | [optional] 
**name** | **str** | canonical human readable name of the concept  | [optional] 
**symbol** | **str** | (optional) symbol, used for genomic data  | [optional] 
**categories** | **list[str]** | concept semantic type &#39;category&#39;. Should be specified from the [Biolink Model](https://biolink.github.io/biolink-model).  | [optional] 
**description** | **str** | (optional) narrative concept definition  | [optional] 
**synonyms** | **list[str]** | list of synonyms for concept  | [optional] 
**exact_matches** | **list[str]** | List of [CURIE](https://www.w3.org/TR/curie/)  identifiers of concepts thought to be exactly matching concepts, [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch). This is generally the same list returned by the /exact_matches endpoint (given the concept &#39;id&#39; as input)  | [optional] 
**details** | [**list[BeaconConceptDetail]**](BeaconConceptDetail.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


