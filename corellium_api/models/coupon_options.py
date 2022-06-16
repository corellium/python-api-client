# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.11.0-13738
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


class CouponOptions(object):
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
        'type': 'str',
        'amount': 'float',
        'used': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'amount': 'amount',
        'used': 'used'
    }

    def __init__(self, type=None, amount=None, used=None, local_vars_configuration=None):  # noqa: E501
        """CouponOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._amount = None
        self._used = None
        self.discriminator = None

        self.type = type
        self.amount = amount
        self.used = used

    @property
    def type(self):
        """Gets the type of this CouponOptions.  # noqa: E501


        :return: The type of this CouponOptions.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CouponOptions.


        :param type: The type of this CouponOptions.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["percent", "discount", "absolute"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def amount(self):
        """Gets the amount of this CouponOptions.  # noqa: E501

        Amount  # noqa: E501

        :return: The amount of this CouponOptions.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this CouponOptions.

        Amount  # noqa: E501

        :param amount: The amount of this CouponOptions.  # noqa: E501
        :type amount: float
        """
        if self.local_vars_configuration.client_side_validation and amount is None:  # noqa: E501
            raise ValueError("Invalid value for `amount`, must not be `None`")  # noqa: E501

        self._amount = amount

    @property
    def used(self):
        """Gets the used of this CouponOptions.  # noqa: E501

        Is Used. If true, this coupon has been used and cannot be used again  # noqa: E501

        :return: The used of this CouponOptions.  # noqa: E501
        :rtype: bool
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this CouponOptions.

        Is Used. If true, this coupon has been used and cannot be used again  # noqa: E501

        :param used: The used of this CouponOptions.  # noqa: E501
        :type used: bool
        """
        if self.local_vars_configuration.client_side_validation and used is None:  # noqa: E501
            raise ValueError("Invalid value for `used`, must not be `None`")  # noqa: E501

        self._used = used

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
        if not isinstance(other, CouponOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CouponOptions):
            return True

        return self.to_dict() != other.to_dict()
