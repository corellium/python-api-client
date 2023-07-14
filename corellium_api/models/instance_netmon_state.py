# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 5.2.0-17368
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


class InstanceNetmonState(object):
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
        'hash': 'str',
        'info': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'hash': 'hash',
        'info': 'info',
        'enabled': 'enabled'
    }

    def __init__(self, hash=None, info=None, enabled=None, local_vars_configuration=None):  # noqa: E501
        """InstanceNetmonState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._hash = None
        self._info = None
        self._enabled = None
        self.discriminator = None

        self.hash = hash
        self.info = info
        self.enabled = enabled

    @property
    def hash(self):
        """Gets the hash of this InstanceNetmonState.  # noqa: E501

          # noqa: E501

        :return: The hash of this InstanceNetmonState.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this InstanceNetmonState.

          # noqa: E501

        :param hash: The hash of this InstanceNetmonState.  # noqa: E501
        :type hash: str
        """

        self._hash = hash

    @property
    def info(self):
        """Gets the info of this InstanceNetmonState.  # noqa: E501

          # noqa: E501

        :return: The info of this InstanceNetmonState.  # noqa: E501
        :rtype: str
        """
        return self._info

    @info.setter
    def info(self, info):
        """Sets the info of this InstanceNetmonState.

          # noqa: E501

        :param info: The info of this InstanceNetmonState.  # noqa: E501
        :type info: str
        """

        self._info = info

    @property
    def enabled(self):
        """Gets the enabled of this InstanceNetmonState.  # noqa: E501

          # noqa: E501

        :return: The enabled of this InstanceNetmonState.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InstanceNetmonState.

          # noqa: E501

        :param enabled: The enabled of this InstanceNetmonState.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

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
        if not isinstance(other, InstanceNetmonState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceNetmonState):
            return True

        return self.to_dict() != other.to_dict()
