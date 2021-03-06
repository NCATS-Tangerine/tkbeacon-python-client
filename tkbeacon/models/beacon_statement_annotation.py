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


class BeaconStatementAnnotation(object):
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
        'tag': 'str',
        'value': 'str'
    }

    attribute_map = {
        'tag': 'tag',
        'value': 'value'
    }

    def __init__(self, tag=None, value=None, local_vars_configuration=None):  # noqa: E501
        """BeaconStatementAnnotation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._tag = None
        self._value = None
        self.discriminator = None

        if tag is not None:
            self.tag = tag
        if value is not None:
            self.value = value

    @property
    def tag(self):
        """Gets the tag of this BeaconStatementAnnotation.  # noqa: E501

        property name   # noqa: E501

        :return: The tag of this BeaconStatementAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this BeaconStatementAnnotation.

        property name   # noqa: E501

        :param tag: The tag of this BeaconStatementAnnotation.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def value(self):
        """Gets the value of this BeaconStatementAnnotation.  # noqa: E501

        property value   # noqa: E501

        :return: The value of this BeaconStatementAnnotation.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this BeaconStatementAnnotation.

        property value   # noqa: E501

        :param value: The value of this BeaconStatementAnnotation.  # noqa: E501
        :type: str
        """

        self._value = value

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
        if not isinstance(other, BeaconStatementAnnotation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BeaconStatementAnnotation):
            return True

        return self.to_dict() != other.to_dict()
