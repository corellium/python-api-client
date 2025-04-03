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


class AuthProvider(object):
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
        'identifier': 'str',
        'provider_type': 'str',
        'default': 'bool',
        'label': 'str',
        'enabled': 'bool',
        'authorization_url': 'str',
        'id': 'str',
        'provider': 'str'
    }

    attribute_map = {
        'name': 'name',
        'identifier': 'identifier',
        'provider_type': 'providerType',
        'default': 'default',
        'label': 'label',
        'enabled': 'enabled',
        'authorization_url': 'authorizationUrl',
        'id': 'id',
        'provider': 'provider'
    }

    def __init__(self, name=None, identifier=None, provider_type=None, default=None, label=None, enabled=None, authorization_url=None, id=None, provider=None, local_vars_configuration=None):  # noqa: E501
        """AuthProvider - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._identifier = None
        self._provider_type = None
        self._default = None
        self._label = None
        self._enabled = None
        self._authorization_url = None
        self._id = None
        self._provider = None
        self.discriminator = None

        self.name = name
        self.identifier = identifier
        self.provider_type = provider_type
        self.default = default
        self.label = label
        self.enabled = enabled
        self.authorization_url = authorization_url
        self.id = id
        self.provider = provider

    @property
    def name(self):
        """Gets the name of this AuthProvider.  # noqa: E501

        Provider name for a given provider type  # noqa: E501

        :return: The name of this AuthProvider.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AuthProvider.

        Provider name for a given provider type  # noqa: E501

        :param name: The name of this AuthProvider.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def identifier(self):
        """Gets the identifier of this AuthProvider.  # noqa: E501

        The identifier for the provider  # noqa: E501

        :return: The identifier of this AuthProvider.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this AuthProvider.

        The identifier for the provider  # noqa: E501

        :param identifier: The identifier of this AuthProvider.  # noqa: E501
        :type identifier: str
        """

        self._identifier = identifier

    @property
    def provider_type(self):
        """Gets the provider_type of this AuthProvider.  # noqa: E501

        Provider type  # noqa: E501

        :return: The provider_type of this AuthProvider.  # noqa: E501
        :rtype: str
        """
        return self._provider_type

    @provider_type.setter
    def provider_type(self, provider_type):
        """Sets the provider_type of this AuthProvider.

        Provider type  # noqa: E501

        :param provider_type: The provider_type of this AuthProvider.  # noqa: E501
        :type provider_type: str
        """

        self._provider_type = provider_type

    @property
    def default(self):
        """Gets the default of this AuthProvider.  # noqa: E501

        Denotes whether it's the default  # noqa: E501

        :return: The default of this AuthProvider.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this AuthProvider.

        Denotes whether it's the default  # noqa: E501

        :param default: The default of this AuthProvider.  # noqa: E501
        :type default: bool
        """

        self._default = default

    @property
    def label(self):
        """Gets the label of this AuthProvider.  # noqa: E501

        Provider label  # noqa: E501

        :return: The label of this AuthProvider.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this AuthProvider.

        Provider label  # noqa: E501

        :param label: The label of this AuthProvider.  # noqa: E501
        :type label: str
        """

        self._label = label

    @property
    def enabled(self):
        """Gets the enabled of this AuthProvider.  # noqa: E501

        Denotes whether they're enabled or not  # noqa: E501

        :return: The enabled of this AuthProvider.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AuthProvider.

        Denotes whether they're enabled or not  # noqa: E501

        :param enabled: The enabled of this AuthProvider.  # noqa: E501
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def authorization_url(self):
        """Gets the authorization_url of this AuthProvider.  # noqa: E501

        URL for provider auth  # noqa: E501

        :return: The authorization_url of this AuthProvider.  # noqa: E501
        :rtype: str
        """
        return self._authorization_url

    @authorization_url.setter
    def authorization_url(self, authorization_url):
        """Sets the authorization_url of this AuthProvider.

        URL for provider auth  # noqa: E501

        :param authorization_url: The authorization_url of this AuthProvider.  # noqa: E501
        :type authorization_url: str
        """

        self._authorization_url = authorization_url

    @property
    def id(self):
        """Gets the id of this AuthProvider.  # noqa: E501

        The identifier for the provider  # noqa: E501

        :return: The id of this AuthProvider.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AuthProvider.

        The identifier for the provider  # noqa: E501

        :param id: The id of this AuthProvider.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def provider(self):
        """Gets the provider of this AuthProvider.  # noqa: E501

        Auth provider  # noqa: E501

        :return: The provider of this AuthProvider.  # noqa: E501
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this AuthProvider.

        Auth provider  # noqa: E501

        :param provider: The provider of this AuthProvider.  # noqa: E501
        :type provider: str
        """

        self._provider = provider

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
        if not isinstance(other, AuthProvider):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AuthProvider):
            return True

        return self.to_dict() != other.to_dict()
