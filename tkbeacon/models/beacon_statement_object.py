# coding: utf-8

"""
    Translator Knowledge Beacon API

    This is the Translator Knowledge Beacon web service application programming interface (API).   # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class BeaconStatementObject(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'str',
        'name': 'str',
        'categories': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'categories': 'categories'
    }

    def __init__(self, id=None, name=None, categories=None):  # noqa: E501
        """BeaconStatementObject - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._name = None
        self._categories = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if categories is not None:
            self.categories = categories

    @property
    def id(self):
        """Gets the id of this BeaconStatementObject.  # noqa: E501

        CURIE-encoded identifier of object concept   # noqa: E501

        :return: The id of this BeaconStatementObject.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BeaconStatementObject.

        CURIE-encoded identifier of object concept   # noqa: E501

        :param id: The id of this BeaconStatementObject.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this BeaconStatementObject.  # noqa: E501

        human readable label of object concept  # noqa: E501

        :return: The name of this BeaconStatementObject.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BeaconStatementObject.

        human readable label of object concept  # noqa: E501

        :param name: The name of this BeaconStatementObject.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def categories(self):
        """Gets the categories of this BeaconStatementObject.  # noqa: E501

        a semantic group for the object concept (specified as a code gene, pathway, disease, etc. - see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of categories)   # noqa: E501

        :return: The categories of this BeaconStatementObject.  # noqa: E501
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this BeaconStatementObject.

        a semantic group for the object concept (specified as a code gene, pathway, disease, etc. - see [Biolink Model](https://biolink.github.io/biolink-model) for the full list of categories)   # noqa: E501

        :param categories: The categories of this BeaconStatementObject.  # noqa: E501
        :type: list[str]
        """

        self._categories = categories

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if not isinstance(other, BeaconStatementObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
