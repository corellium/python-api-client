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


class GpioStateDefinition(object):
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
        'bit_count': 'float',
        'banks': 'list[list[Bit]]'
    }

    attribute_map = {
        'bit_count': 'bitCount',
        'banks': 'banks'
    }

    def __init__(self, bit_count=None, banks=None, local_vars_configuration=None):  # noqa: E501
        """GpioStateDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._bit_count = None
        self._banks = None
        self.discriminator = None

        self.bit_count = bit_count
        self.banks = banks

    @property
    def bit_count(self):
        """Gets the bit_count of this GpioStateDefinition.  # noqa: E501

        count of bits in members of this bank  # noqa: E501

        :return: The bit_count of this GpioStateDefinition.  # noqa: E501
        :rtype: float
        """
        return self._bit_count

    @bit_count.setter
    def bit_count(self, bit_count):
        """Sets the bit_count of this GpioStateDefinition.

        count of bits in members of this bank  # noqa: E501

        :param bit_count: The bit_count of this GpioStateDefinition.  # noqa: E501
        :type bit_count: float
        """
        if self.local_vars_configuration.client_side_validation and bit_count is None:  # noqa: E501
            raise ValueError("Invalid value for `bit_count`, must not be `None`")  # noqa: E501

        self._bit_count = bit_count

    @property
    def banks(self):
        """Gets the banks of this GpioStateDefinition.  # noqa: E501

        bits for each bank of this name as an array of arrays  # noqa: E501

        :return: The banks of this GpioStateDefinition.  # noqa: E501
        :rtype: list[list[Bit]]
        """
        return self._banks

    @banks.setter
    def banks(self, banks):
        """Sets the banks of this GpioStateDefinition.

        bits for each bank of this name as an array of arrays  # noqa: E501

        :param banks: The banks of this GpioStateDefinition.  # noqa: E501
        :type banks: list[list[Bit]]
        """
        if self.local_vars_configuration.client_side_validation and banks is None:  # noqa: E501
            raise ValueError("Invalid value for `banks`, must not be `None`")  # noqa: E501

        self._banks = banks

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
        if not isinstance(other, GpioStateDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GpioStateDefinition):
            return True

        return self.to_dict() != other.to_dict()
