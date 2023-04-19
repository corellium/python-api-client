# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 4.5.0-16775
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


class VpnDefinition(object):
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
        'proxy': 'list[object]',
        'listeners': 'list[object]'
    }

    attribute_map = {
        'proxy': 'proxy',
        'listeners': 'listeners'
    }

    def __init__(self, proxy=None, listeners=None, local_vars_configuration=None):  # noqa: E501
        """VpnDefinition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._proxy = None
        self._listeners = None
        self.discriminator = None

        self.proxy = proxy
        self.listeners = listeners

    @property
    def proxy(self):
        """Gets the proxy of this VpnDefinition.  # noqa: E501

          # noqa: E501

        :return: The proxy of this VpnDefinition.  # noqa: E501
        :rtype: list[object]
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this VpnDefinition.

          # noqa: E501

        :param proxy: The proxy of this VpnDefinition.  # noqa: E501
        :type proxy: list[object]
        """

        self._proxy = proxy

    @property
    def listeners(self):
        """Gets the listeners of this VpnDefinition.  # noqa: E501

          # noqa: E501

        :return: The listeners of this VpnDefinition.  # noqa: E501
        :rtype: list[object]
        """
        return self._listeners

    @listeners.setter
    def listeners(self, listeners):
        """Sets the listeners of this VpnDefinition.

          # noqa: E501

        :param listeners: The listeners of this VpnDefinition.  # noqa: E501
        :type listeners: list[object]
        """

        self._listeners = listeners

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
        if not isinstance(other, VpnDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VpnDefinition):
            return True

        return self.to_dict() != other.to_dict()
