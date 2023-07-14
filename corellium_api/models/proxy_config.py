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


class ProxyConfig(object):
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
        'device_port': 'float',
        'first_available': 'bool',
        'expose': 'bool',
        'router_port': 'float'
    }

    attribute_map = {
        'device_port': 'devicePort',
        'first_available': 'firstAvailable',
        'expose': 'expose',
        'router_port': 'routerPort'
    }

    def __init__(self, device_port=None, first_available=None, expose=None, router_port=None, local_vars_configuration=None):  # noqa: E501
        """ProxyConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._device_port = None
        self._first_available = None
        self._expose = None
        self._router_port = None
        self.discriminator = None

        self.device_port = device_port
        self.first_available = first_available
        self.expose = expose
        self.router_port = router_port

    @property
    def device_port(self):
        """Gets the device_port of this ProxyConfig.  # noqa: E501

        The device port to use for proxying.  # noqa: E501

        :return: The device_port of this ProxyConfig.  # noqa: E501
        :rtype: float
        """
        return self._device_port

    @device_port.setter
    def device_port(self, device_port):
        """Sets the device_port of this ProxyConfig.

        The device port to use for proxying.  # noqa: E501

        :param device_port: The device_port of this ProxyConfig.  # noqa: E501
        :type device_port: float
        """

        self._device_port = device_port

    @property
    def first_available(self):
        """Gets the first_available of this ProxyConfig.  # noqa: E501

        If `true`, the first available port will be used if `devicePort` is not available.  # noqa: E501

        :return: The first_available of this ProxyConfig.  # noqa: E501
        :rtype: bool
        """
        return self._first_available

    @first_available.setter
    def first_available(self, first_available):
        """Sets the first_available of this ProxyConfig.

        If `true`, the first available port will be used if `devicePort` is not available.  # noqa: E501

        :param first_available: The first_available of this ProxyConfig.  # noqa: E501
        :type first_available: bool
        """

        self._first_available = first_available

    @property
    def expose(self):
        """Gets the expose of this ProxyConfig.  # noqa: E501

        If `true`, the proxy will be exposed to the external interface.  # noqa: E501

        :return: The expose of this ProxyConfig.  # noqa: E501
        :rtype: bool
        """
        return self._expose

    @expose.setter
    def expose(self, expose):
        """Sets the expose of this ProxyConfig.

        If `true`, the proxy will be exposed to the external interface.  # noqa: E501

        :param expose: The expose of this ProxyConfig.  # noqa: E501
        :type expose: bool
        """

        self._expose = expose

    @property
    def router_port(self):
        """Gets the router_port of this ProxyConfig.  # noqa: E501

        The router port to use for proxying.  # noqa: E501

        :return: The router_port of this ProxyConfig.  # noqa: E501
        :rtype: float
        """
        return self._router_port

    @router_port.setter
    def router_port(self, router_port):
        """Sets the router_port of this ProxyConfig.

        The router port to use for proxying.  # noqa: E501

        :param router_port: The router_port of this ProxyConfig.  # noqa: E501
        :type router_port: float
        """

        self._router_port = router_port

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
        if not isinstance(other, ProxyConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProxyConfig):
            return True

        return self.to_dict() != other.to_dict()
