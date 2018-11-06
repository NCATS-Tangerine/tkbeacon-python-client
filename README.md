# tkbeacon
This is the Translator Knowledge Beacon web service application programming interface (API).

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.3.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [http://starinformatics.com](http://starinformatics.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

```sh
pip install tkbeacon
```

Alternatively you can install the latest version directly from Github

```sh
pip install git+https://github.com/NCATS-Tangerine/tkbeacon-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/NCATS-Tangerine/tkbeacon-python-client.git`)

Then import the package:
```python
import tkbeacon
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tkbeacon
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
from tkbeacon import build, KnowledgeSource
from tkbeacon.rest import ApiException

# create an instance of the BeaconApi class pointing at the remote SMPDB beacon
b = build(KnowledgeSource.SMPDB)

try:
  concepts = b.get_concepts(categories=['protein'], size=10)

  for concept in concepts:
    print(concept.id, concept.name)

  print('All results are proteins:', all('protein' in concept.categories for concept in concepts))

except ApiException as e:
  print("Exception when calling BeaconApi->get_concepts: %s\n" % e)
```

Note that the model objects are represented as dictionaries when being printed, but they are not actually dictionaries.

## Documentation for API Endpoints

All URIs are relative to the given source url

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BeaconApi* | [**get_concept_categories**](docs/BeaconApi.md#get_concept_categories) | **GET** /categories |
*BeaconApi* | [**get_concept_details**](docs/BeaconApi.md#get_concept_details) | **GET** /concepts/{concept_id} |
*BeaconApi* | [**get_concepts**](docs/BeaconApi.md#get_concepts) | **GET** /concepts |
*BeaconApi* | [**get_exact_matches_to_concept_list**](docs/BeaconApi.md#get_exact_matches_to_concept_list) | **GET** /exactmatches |
*BeaconApi* | [**get_knowledge_map**](docs/BeaconApi.md#get_knowledge_map) | **GET** /kmap |
*BeaconApi* | [**get_predicates**](docs/BeaconApi.md#get_predicates) | **GET** /predicates |
*BeaconApi* | [**get_statement_details**](docs/BeaconApi.md#get_statement_details) | **GET** /statements/{statement_id} |
*BeaconApi* | [**get_statements**](docs/BeaconApi.md#get_statements) | **GET** /statements |


## Documentation For Models

 - [BeaconConcept](docs/BeaconConcept.md)
 - [BeaconConceptCategory](docs/BeaconConceptCategory.md)
 - [BeaconConceptDetail](docs/BeaconConceptDetail.md)
 - [BeaconConceptWithDetails](docs/BeaconConceptWithDetails.md)
 - [BeaconKnowledgeMapObject](docs/BeaconKnowledgeMapObject.md)
 - [BeaconKnowledgeMapPredicate](docs/BeaconKnowledgeMapPredicate.md)
 - [BeaconKnowledgeMapStatement](docs/BeaconKnowledgeMapStatement.md)
 - [BeaconKnowledgeMapSubject](docs/BeaconKnowledgeMapSubject.md)
 - [BeaconPredicate](docs/BeaconPredicate.md)
 - [BeaconStatement](docs/BeaconStatement.md)
 - [BeaconStatementAnnotation](docs/BeaconStatementAnnotation.md)
 - [BeaconStatementCitation](docs/BeaconStatementCitation.md)
 - [BeaconStatementObject](docs/BeaconStatementObject.md)
 - [BeaconStatementPredicate](docs/BeaconStatementPredicate.md)
 - [BeaconStatementSubject](docs/BeaconStatementSubject.md)
 - [BeaconStatementWithDetails](docs/BeaconStatementWithDetails.md)
 - [ExactMatchResponse](docs/ExactMatchResponse.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

richard@starinformatics.com
