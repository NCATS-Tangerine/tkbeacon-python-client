# tkbeacon

This is the Translator Knowledge Beacon web service application programming interface (API).

- API version: 1.3.0
- Package version: 1.3.0

For more information, please visit [http://starinformatics.com](http://starinformatics.com)

## Requirements.

Python 3.7+

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

#### The OpenAPI specifications

Refer to the [Python client](./tkbeacon).  

#### (Re-)Generating the Translator Knowledge Beacon (TKBeacon) Client

The *client* is a direct Python web service client implementation.

The implementation of the *TKBeacon* client uses code generation from the 
[OpenAPI NCATS Knowledge Beacon specification](knowledge-beacon-api_1-3-0.yaml), 
which is used as a template to generate the code base, which is then wired up by delegation to additional handler code.   
 
The generated and other client/server code is found in the *TKBeacon* subfolder.

By [installing a local copy of the OpenAPI Code Generator](https://openapi-generator.tech/docs/installation), 
modified OpenAPI 3.0 YAML specifications can be processed to recreate the Python client stubs.
Note that depending on how you install the OpenAPI Code Generator, the manner in which you execute the 
 `openapi-generator` command below will change accordingly (Note that the code generation processes are a bit more 
 streamlined and robust under Linux and OSX than Microsoft Windows).

The code generation commands are generally run from the root project directory directory.  First, one should check 
your new or modified OpenAPI YAML specifications using the _validate_ command:

```
openapi-generator validate (-i | --input-spec=)knowledge-beacon-api-1-3-0.yaml
```

If the specifications pass muster, then to recreate the Python Flask *client* Python access stubs, 
something along the lines of the following command is typed:

```bash
openapi-generator generate  --input-spec=knowledge-beacon-api-1-3-0.yaml \
                    --output=client \
                    --generator-name=python \
                    --package-name=ara_client \
	                --model-package=models \
	                --artifact-version=1.3.0 \
	                --additional-properties=\
"projectName=tkbeacon,packageName=tkbeacon,packageVersion=1.3.0,packageUrl=https://github.com/NCATS-Tangerine/tkbeacon-python-client.git"
```

The [OpenAPI 3.0 'generate' command usage](https://openapi-generator.tech/docs/usage#generate) may be consulted
for more specific details on available code generation options and for acceptable program flag abbreviations (here we
used the long form of the flags).

The above commands are also wrapped inside of a `generate.sh` shell script in the root project directory and 
may also be invoked using the provide Makefile targets.

#### Repairing the Generated Code

After generating the code stubs, a developer likely needs to repair the regenerated code a bit.

the *tkbeacon* subdirectory _README.md_ file are overwritten by the code generation. 
These should be restored from the \*-master.\* versions of these files in each directory.
 
For good measure, after such extensive rebuilding of the libraries, the 'pip' environment dependencies should also 
be updated, as documented for the client , prior to re-testing and using the updated software.
