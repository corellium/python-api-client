# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 7.3.0
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from corellium_api.configuration import Configuration


class Logging(object):
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
        'development': 'bool',
        'throw_warnings': 'bool'
    }

    attribute_map = {
        'development': 'development',
        'throw_warnings': 'throwWarnings'
    }

    def __init__(self, development=None, throw_warnings=None, local_vars_configuration=None):  # noqa: E501
        """Logging - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._development = None
        self._throw_warnings = None
        self.discriminator = None

        self.development = development
        self.throw_warnings = throw_warnings

    @property
    def development(self):
        """Gets the development of this Logging.  # noqa: E501

        Denotes whether it's in development  # noqa: E501

        :return: The development of this Logging.  # noqa: E501
        :rtype: bool
        """
        return self._development

    @development.setter
    def development(self, development):
        """Sets the development of this Logging.

        Denotes whether it's in development  # noqa: E501

        :param development: The development of this Logging.  # noqa: E501
        :type development: bool
        """

        self._development = development

    @property
    def throw_warnings(self):
        """Gets the throw_warnings of this Logging.  # noqa: E501

        Denotes whether to throw warnings  # noqa: E501

        :return: The throw_warnings of this Logging.  # noqa: E501
        :rtype: bool
        """
        return self._throw_warnings

    @throw_warnings.setter
    def throw_warnings(self, throw_warnings):
        """Sets the throw_warnings of this Logging.

        Denotes whether to throw warnings  # noqa: E501

        :param throw_warnings: The throw_warnings of this Logging.  # noqa: E501
        :type throw_warnings: bool
        """

        self._throw_warnings = throw_warnings

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Logging):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Logging):
            return True

        return self.to_dict() != other.to_dict()
