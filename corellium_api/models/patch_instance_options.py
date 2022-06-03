# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.11.0-13642
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


class PatchInstanceOptions(object):
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
        'name': 'str',
        'state': 'str',
        'boot_options': 'str',
        'proxy': 'str'
    }

    attribute_map = {
        'name': 'name',
        'state': 'state',
        'boot_options': 'bootOptions',
        'proxy': 'proxy'
    }

    def __init__(self, name=None, state=None, boot_options=None, proxy=None, local_vars_configuration=None):  # noqa: E501
        """PatchInstanceOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._state = None
        self._boot_options = None
        self._proxy = None
        self.discriminator = None

        self.name = name
        self.state = state
        self.boot_options = boot_options
        self.proxy = proxy

    @property
    def name(self):
        """Gets the name of this PatchInstanceOptions.  # noqa: E501

        the name of the device  # noqa: E501

        :return: The name of this PatchInstanceOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PatchInstanceOptions.

        the name of the device  # noqa: E501

        :param name: The name of this PatchInstanceOptions.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def state(self):
        """Gets the state of this PatchInstanceOptions.  # noqa: E501

        the desired state of the device  # noqa: E501

        :return: The state of this PatchInstanceOptions.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PatchInstanceOptions.

        the desired state of the device  # noqa: E501

        :param state: The state of this PatchInstanceOptions.  # noqa: E501
        :type state: str
        """
        allowed_values = [None,"on", "off", "paused", "deleting"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and state not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def boot_options(self):
        """Gets the boot_options of this PatchInstanceOptions.  # noqa: E501

        the desired Boot Options  # noqa: E501

        :return: The boot_options of this PatchInstanceOptions.  # noqa: E501
        :rtype: str
        """
        return self._boot_options

    @boot_options.setter
    def boot_options(self, boot_options):
        """Sets the boot_options of this PatchInstanceOptions.

        the desired Boot Options  # noqa: E501

        :param boot_options: The boot_options of this PatchInstanceOptions.  # noqa: E501
        :type boot_options: str
        """

        self._boot_options = boot_options

    @property
    def proxy(self):
        """Gets the proxy of this PatchInstanceOptions.  # noqa: E501


        :return: The proxy of this PatchInstanceOptions.  # noqa: E501
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this PatchInstanceOptions.


        :param proxy: The proxy of this PatchInstanceOptions.  # noqa: E501
        :type proxy: str
        """

        self._proxy = proxy

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
        if not isinstance(other, PatchInstanceOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PatchInstanceOptions):
            return True

        return self.to_dict() != other.to_dict()
