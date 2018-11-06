# BeaconStatementWithDetails

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Statement identifier of the statement made in an edge (echoed back)  | [optional] 
**is_defined_by** | **str** | A CURIE/URI for the translator group that wrapped this knowledge source (&#39;beacon&#39;) that publishes the statement made in an edge.  | [optional] 
**provided_by** | **str** | A CURIE prefix, e.g. Pharos, MGI, Monarch. The group that curated/asserted the statement made in an edge.  | [optional] 
**qualifiers** | **list[str]** | (Optional) terms representing qualifiers that modify or qualify the meaning of the statement made in an edge.  | [optional] 
**annotation** | [**list[BeaconStatementAnnotation]**](BeaconStatementAnnotation.md) | Extra edge properties, generally compliant with Translator Knowledge Graph Standard Specification  | [optional] 
**evidence** | [**list[BeaconStatementCitation]**](BeaconStatementCitation.md) | Array of research citations serving as supporting evidence for this knowledge statement.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


