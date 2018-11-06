# BeaconPredicate

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edge_label** | **str** | A predicate edge label which must be taken from the minimal predicate (&#39;slot&#39;) list of the [Biolink Model](https://biolink.github.io/biolink-model).  | [optional] 
**relation** | **str** | The predicate relation, with the preferred format being a CURIE where one exists, but strings/labels acceptable. This relation  may be equivalent to the edge_label (e.g. edge_label: has_phenotype, relation: RO:0002200), or a more specific relation in cases where the source provides more granularity  (e.g. edge_label: molecularly_interacts_with, relation: RO:0002447)  | [optional] 
**description** | **str** | human readable definition of predicate relation  provided by this beacon  | [optional] 
**frequency** | **int** | the number of statement entries using the specified predicate in the given beacon knowledge base | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


