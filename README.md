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

# Updating the TKBeacon from the Current API Specification

The "gory" details of code regeneration are provided below this section but generally speaking, a Makefile 
is provided which may be conveniently used to trigger regeneration of the client.

There is a `validation` target to check the project OpenAPI specifications, prior to regenerating the code:

```bash
make api-validation
```

The *validation* target calls a local shell script `generate.sh` in the root directory of the project.  This script 
checks for the presence of the OpenAPI Code Generator binary and attempts to install it if it is not yet installed 
on the computer. This installation may be problematic on some platforms (e.g. Microsoft Windows) but you can also 
[manually install the OpenAPI Code Generator](https://openapi-generator.tech/docs/installation). If you do this, 
you may need to override the OPENAPI_GENERATOR_CLI and OPENAPI_GENERATOR_CLI_PATH environment variables used by the 
generator script.  

Note also that the `openapi-generator-cli` script depends on  `mvn`, `jq` and `curl` to run (these dependencies
should be installed first).

Even on Unix-type systems, the `generate.sh` script installation of the OpenAPI Code generator may 
fail if not run as 'sudo' since the binary is being installed under _/usr/local/bin_, thus so you may need to run the 
above *validation* make target as `sudo` the first time, to ensure a successful installation (however, the 
installation processes does fix the execute permissions for general access, so 'sudo' should not be needed afterwards).
 
After installing the `openapi-generator` tool and validating the API's, the code may be (re-)generated:

```bash
make code-generation
```

# The Gory Details...

Ideally, the aforementioned `make` process using the default values in the `generate.sh` script should work but, 
just in case, we provide more details on the whole code generation procedure here below (review also the contents 
of the `generate.sh` script for code generation customisations feasible simply using OS shell environment variables).

##The OpenAPI specifications

Refer to the [Python client](./tkbeacon) for details.  

## (Re-)Generating the Translator Knowledge Beacon (TKBeacon) Client

The *TKBeacon* client is a direct Python web service client implementation of the 
[NCATS Knowledge Beacon OpenAPI specification](knowledge-beacon-api_1-3-0.yaml), 
which is used as a template to generate the code stubs into the `tkbeacon` subfolder, to which some 
additional support code may be added.   

By [installing a local copy of the OpenAPI Code Generator](https://openapi-generator.tech/docs/installation), 
modified OpenAPI 3.0 YAML specifications can be processed to recreate the Python client stubs (Note that running the 
`generate.sh` shell will itself automatically install the OpenAPI code generated if not already present).

Depending on how you install the OpenAPI Code Generator, the manner in which you execute the 
 `openapi-generator` command below will change accordingly (Note that the code generation processes are a bit more 
 streamlined and robust under Linux and OSX than Microsoft Windows).

The code generation commands are generally run from the root project directory directory.  First, one should check 
your new or modified OpenAPI YAML specifications using the _validate_ command:

```bash
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

## Repairing the Generated Code

After generating the code stubs, a developer may need to repair some of the regenerated files where previous 
customised content was overwritten by the new code generation session.

For example, in the *tkbeacon* subfolder, the _README.md_ file is overwritten by the code generation. 
This file should be restored using the \*-master.\* versions of these files in each directory (note that you can 
als update this master file as required to reflect the latest cycle of API code changes).
 
For good measure, after such extensive rebuilding of the libraries, the 'pip' environment dependencies should also 
be updated, as documented for the client , prior to re-testing and using the updated software.
