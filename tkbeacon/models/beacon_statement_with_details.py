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


class BeaconStatementWithDetails(object):
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
        'is_defined_by': 'str',
        'provided_by': 'str',
        'qualifiers': 'list[str]',
        'annotation': 'list[BeaconStatementAnnotation]',
        'evidence': 'list[BeaconStatementCitation]'
    }

    attribute_map = {
        'id': 'id',
        'is_defined_by': 'is_defined_by',
        'provided_by': 'provided_by',
        'qualifiers': 'qualifiers',
        'annotation': 'annotation',
        'evidence': 'evidence'
    }

    def __init__(self, id=None, is_defined_by=None, provided_by=None, qualifiers=None, annotation=None, evidence=None, local_vars_configuration=None):  # noqa: E501
        """BeaconStatementWithDetails - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._is_defined_by = None
        self._provided_by = None
        self._qualifiers = None
        self._annotation = None
        self._evidence = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if is_defined_by is not None:
            self.is_defined_by = is_defined_by
        if provided_by is not None:
            self.provided_by = provided_by
        if qualifiers is not None:
            self.qualifiers = qualifiers
        if annotation is not None:
            self.annotation = annotation
        if evidence is not None:
            self.evidence = evidence

    @property
    def id(self):
        """Gets the id of this BeaconStatementWithDetails.  # noqa: E501

        Statement identifier of the statement made in an edge (echoed back)   # noqa: E501

        :return: The id of this BeaconStatementWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BeaconStatementWithDetails.

        Statement identifier of the statement made in an edge (echoed back)   # noqa: E501

        :param id: The id of this BeaconStatementWithDetails.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_defined_by(self):
        """Gets the is_defined_by of this BeaconStatementWithDetails.  # noqa: E501

        A CURIE/URI for the translator group that wrapped this knowledge source ('beacon') that publishes the statement made in an edge.   # noqa: E501

        :return: The is_defined_by of this BeaconStatementWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._is_defined_by

    @is_defined_by.setter
    def is_defined_by(self, is_defined_by):
        """Sets the is_defined_by of this BeaconStatementWithDetails.

        A CURIE/URI for the translator group that wrapped this knowledge source ('beacon') that publishes the statement made in an edge.   # noqa: E501

        :param is_defined_by: The is_defined_by of this BeaconStatementWithDetails.  # noqa: E501
        :type: str
        """

        self._is_defined_by = is_defined_by

    @property
    def provided_by(self):
        """Gets the provided_by of this BeaconStatementWithDetails.  # noqa: E501

        A CURIE prefix, e.g. Pharos, MGI, Monarch. The group that curated/asserted the statement made in an edge.   # noqa: E501

        :return: The provided_by of this BeaconStatementWithDetails.  # noqa: E501
        :rtype: str
        """
        return self._provided_by

    @provided_by.setter
    def provided_by(self, provided_by):
        """Sets the provided_by of this BeaconStatementWithDetails.

        A CURIE prefix, e.g. Pharos, MGI, Monarch. The group that curated/asserted the statement made in an edge.   # noqa: E501

        :param provided_by: The provided_by of this BeaconStatementWithDetails.  # noqa: E501
        :type: str
        """

        self._provided_by = provided_by

    @property
    def qualifiers(self):
        """Gets the qualifiers of this BeaconStatementWithDetails.  # noqa: E501

        (Optional) terms representing qualifiers that modify or qualify the meaning of the statement made in an edge.   # noqa: E501

        :return: The qualifiers of this BeaconStatementWithDetails.  # noqa: E501
        :rtype: list[str]
        """
        return self._qualifiers

    @qualifiers.setter
    def qualifiers(self, qualifiers):
        """Sets the qualifiers of this BeaconStatementWithDetails.

        (Optional) terms representing qualifiers that modify or qualify the meaning of the statement made in an edge.   # noqa: E501

        :param qualifiers: The qualifiers of this BeaconStatementWithDetails.  # noqa: E501
        :type: list[str]
        """

        self._qualifiers = qualifiers

    @property
    def annotation(self):
        """Gets the annotation of this BeaconStatementWithDetails.  # noqa: E501

        Extra edge properties, generally compliant with Translator Knowledge Graph Standard Specification   # noqa: E501

        :return: The annotation of this BeaconStatementWithDetails.  # noqa: E501
        :rtype: list[BeaconStatementAnnotation]
        """
        return self._annotation

    @annotation.setter
    def annotation(self, annotation):
        """Sets the annotation of this BeaconStatementWithDetails.

        Extra edge properties, generally compliant with Translator Knowledge Graph Standard Specification   # noqa: E501

        :param annotation: The annotation of this BeaconStatementWithDetails.  # noqa: E501
        :type: list[BeaconStatementAnnotation]
        """

        self._annotation = annotation

    @property
    def evidence(self):
        """Gets the evidence of this BeaconStatementWithDetails.  # noqa: E501

        Array of research citations serving as supporting evidence for this knowledge statement.   # noqa: E501

        :return: The evidence of this BeaconStatementWithDetails.  # noqa: E501
        :rtype: list[BeaconStatementCitation]
        """
        return self._evidence

    @evidence.setter
    def evidence(self, evidence):
        """Sets the evidence of this BeaconStatementWithDetails.

        Array of research citations serving as supporting evidence for this knowledge statement.   # noqa: E501

        :param evidence: The evidence of this BeaconStatementWithDetails.  # noqa: E501
        :type: list[BeaconStatementCitation]
        """

        self._evidence = evidence

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
        if not isinstance(other, BeaconStatementWithDetails):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BeaconStatementWithDetails):
            return True

        return self.to_dict() != other.to_dict()
