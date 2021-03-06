# coding: utf-8

"""
    Translator Knowledge Beacon API

    This is the Translator Knowledge Beacon web service application programming interface (API).   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from tkbeacon.configuration import Configuration


class BeaconConceptWithDetails(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'uri': 'str',
        'name': 'str',
        'symbol': 'str',
        'categories': 'list[str]',
        'description': 'str',
        'synonyms': 'list[str]',
        'exact_matches': 'list[str]',
        'details': 'list[BeaconConceptDetail]'
    }

    attribute_map = {
        'id': 'id',
        'uri': 'uri',
        'name': 'name',
        'symbol': 'symbol',
        'categories': 'categories',
        'description': 'description',
        'synonyms': 'synonyms',
        'exact_matches': 'exact_matches',
        'details': 'details'
    }

    def __init__(self, id=None, uri=None, name=None, symbol=None, categories=None, description=None, synonyms=None, exact_matches=None, details=None, local_vars_configuration=None):  # noqa: E501
        """BeaconConceptWithDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._uri = None
        self._name = None
        self._symbol = None
        self._categories = None
        self._description = None
        self._synonyms = None
        self._exact_matches = None
        self._details = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if uri is not None:
            self.uri = uri
        if name is not None:
            self.name = name
        if symbol is not None:
            self.symbol = symbol
        if categories is not None:
            self.categories = categories
        if description is not None:
            self.description = description
        if synonyms is not None:
            self.synonyms = synonyms
        if exact_matches is not None:
            self.exact_matches = exact_matches
        if details is not None:
            self.details = details

    @property
    def id(self):
        """Gets the id of this BeaconConceptWithDetails.  # noqa: E501

        local object CURIE for the concept in the specified knowledge source database   # noqa: E501

        :return: The id of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BeaconConceptWithDetails.

        local object CURIE for the concept in the specified knowledge source database   # noqa: E501

        :param id: The id of this BeaconConceptWithDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def uri(self):
        """Gets the uri of this BeaconConceptWithDetails.  # noqa: E501

        (optional) equivalent to expansion of the CURIE   # noqa: E501

        :return: The uri of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this BeaconConceptWithDetails.

        (optional) equivalent to expansion of the CURIE   # noqa: E501

        :param uri: The uri of this BeaconConceptWithDetails.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def name(self):
        """Gets the name of this BeaconConceptWithDetails.  # noqa: E501

        canonical human readable name of the concept   # noqa: E501

        :return: The name of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BeaconConceptWithDetails.

        canonical human readable name of the concept   # noqa: E501

        :param name: The name of this BeaconConceptWithDetails.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def symbol(self):
        """Gets the symbol of this BeaconConceptWithDetails.  # noqa: E501

        (optional) symbol, used for genomic data   # noqa: E501

        :return: The symbol of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol):
        """Sets the symbol of this BeaconConceptWithDetails.

        (optional) symbol, used for genomic data   # noqa: E501

        :param symbol: The symbol of this BeaconConceptWithDetails.  # noqa: E501
        :type: str
        """

        self._symbol = symbol

    @property
    def categories(self):
        """Gets the categories of this BeaconConceptWithDetails.  # noqa: E501

        concept semantic type 'category'. Should be specified from the [Biolink Model](https://biolink.github.io/biolink-model).   # noqa: E501

        :return: The categories of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this BeaconConceptWithDetails.

        concept semantic type 'category'. Should be specified from the [Biolink Model](https://biolink.github.io/biolink-model).   # noqa: E501

        :param categories: The categories of this BeaconConceptWithDetails.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    @property
    def description(self):
        """Gets the description of this BeaconConceptWithDetails.  # noqa: E501

        (optional) narrative concept definition   # noqa: E501

        :return: The description of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BeaconConceptWithDetails.

        (optional) narrative concept definition   # noqa: E501

        :param description: The description of this BeaconConceptWithDetails.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def synonyms(self):
        """Gets the synonyms of this BeaconConceptWithDetails.  # noqa: E501

        list of synonyms for concept   # noqa: E501

        :return: The synonyms of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this BeaconConceptWithDetails.

        list of synonyms for concept   # noqa: E501

        :param synonyms: The synonyms of this BeaconConceptWithDetails.  # noqa: E501
        :type: list[str]
        """

        self._synonyms = synonyms

    @property
    def exact_matches(self):
        """Gets the exact_matches of this BeaconConceptWithDetails.  # noqa: E501

        List of [CURIE](https://www.w3.org/TR/curie/)  identifiers of concepts thought to be exactly matching concepts, [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch). This is generally the same list returned by the /exact_matches endpoint (given the concept 'id' as input)   # noqa: E501

        :return: The exact_matches of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._exact_matches

    @exact_matches.setter
    def exact_matches(self, exact_matches):
        """Sets the exact_matches of this BeaconConceptWithDetails.

        List of [CURIE](https://www.w3.org/TR/curie/)  identifiers of concepts thought to be exactly matching concepts, [*sensa*-SKOS](http://www.w3.org/2004/02/skos/core#exactMatch). This is generally the same list returned by the /exact_matches endpoint (given the concept 'id' as input)   # noqa: E501

        :param exact_matches: The exact_matches of this BeaconConceptWithDetails.  # noqa: E501
        :type: list[str]
        """

        self._exact_matches = exact_matches

    @property
    def details(self):
        """Gets the details of this BeaconConceptWithDetails.  # noqa: E501


        :return: The details of this BeaconConceptWithDetails.  # noqa: E501
        :rtype: list[BeaconConceptDetail]
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this BeaconConceptWithDetails.


        :param details: The details of this BeaconConceptWithDetails.  # noqa: E501
        :type: list[BeaconConceptDetail]
        """

        self._details = details

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BeaconConceptWithDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BeaconConceptWithDetails):
            return True

        return self.to_dict() != other.to_dict()
