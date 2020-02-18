# Translator Knowledge Beacon Client

This is a Python client for programmatic access to the Translator Knowledge Beacon web service 
application programming interface (API).

- API version: 1.3.0
- Package version: 1.3.0.R3

For more information, please visit 
[the project web site](https://github.com/NCATS-Tangerine/tkbeacon-python-client.git)

## Requirements.

Python 3.7+

## Installation & Usage

The quick way to use the stable version of the client is to use the Pypi published module of the latest release
(described here below). Note that if your default python binary is not 3.7+, you may wish or need to run the module 
within a Python virtual environment running Python 3.7 or better.

### Default Installation and Use

For installation of the latest published TKBeacon client in Pypi, type:

```sh
python3.7 -m pip install tkbeacon
```

Alternatively you can install the latest version directly from Github

```sh
python3.7 -m pip install git+https://github.com/NCATS-Tangerine/tkbeacon-python-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/NCATS-Tangerine/tkbeacon-python-client.git`)

Then import the package:
```python
import tkbeacon
```

### Installation using Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python3.7 setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import tkbeacon
```

# Using the Module

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
#!/usr/bin/env python
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

This sample snippet of code is available in the project as `beacon-sample-script.py`.

Note that the model objects are represented as dictionaries when being printed, but they are not actually dictionaries.

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

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

## Authors

richard@starinformatics.com
lance.hannestad@gmail.com

# Working Directly with the latest project code

To play more directly with the code, first clone this repo using git.

```
git clone https://github.com/ncats/translator-modules.git

# ... then  enter  into your cloned project repository
cd translator-modules
```

## Setting up your environment

The code is now validated to work only with Python 3.7 only. We recommend using a virtualenv to enforce this.

```
virtualenv -p python3.7 venv
source venv/bin/activate
```

or, alternately, use python venv to manage packages and the development environment:

```
python3.7 -m venv venv
source venv/bin/activate
```

To exit the environment, type:

```deactivate```

To reenter, source the `activate` command again.

Alternately, you can also use use conda env to manage packages and the development environment:

```
conda create -n translator-modules python=3.7
conda activate translator-modules
```
Some IDE's (e.g. PyCharm) may also have provisions for directly creating such a virtualenv. This should work fine.

## (Re-)Generating the Translator Knowledge Beacon (TKBeacon) Client from its API Specification

A Makefile is provided which may be used to regenerate the code.

First, there is a `validation` target to check the project OpenAPI specifications, prior to regenerating the code:

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

After generating the module, it may be installed:


```bash
make installation
```

then tested. The tests use Python `nosetests` application, which needs to be installed. For example, for Ubuntu Linux:
 
```
sudo apt install python-nose
```

will do this. After the `nosetests` application is installed, then the tests may be run:

```bash
make tests
```

After installation, the module should be available as noted in the [Using the Module](#using-the-module) section above.

## The Gory Details...

The *client* is a direct Python web service client implementation. Refer to the [Python client](./tkbeacon).  

The implementation of the *TKBeacon* client uses code generation from the 
[OpenAPI NCATS Knowledge Beacon specification](knowledge-beacon-OA3-api_1-3-0.yaml), 
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
openapi-generator validate (-i | --input-spec=)knowledge-beacon-OA3-api_1-3-0.yaml
```

If the specifications pass muster, then to recreate the Python Flask *client* Python access stubs, 
something along the lines of the following command is typed:

```bash
openapi-generator generate  --input-spec=knowledge-beacon-OA3-api_1-3-0.yaml \
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

After generating the code stubs, a developer likely needs to repair the regenerated code a bit.

the *tkbeacon* subdirectory _README.md_ and `.gitignore` files are overwritten by the code generation. 
These should be merge/restored from the \*-master.\* versions of these files in each directory.
 
For good measure, after such extensive rebuilding of the libraries, the 'pip' environment dependencies should also 
be updated, as documented for the client , prior to re-testing and using the updated software.
