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


class TrialRequestOptions(object):
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
        'address': 'Address',
        'email': 'str',
        'name': 'str',
        'metadata': 'TrialRequestMetadata',
        'enterprise': 'bool',
        'token': 'str'
    }

    attribute_map = {
        'address': 'address',
        'email': 'email',
        'name': 'name',
        'metadata': 'metadata',
        'enterprise': 'enterprise',
        'token': 'token'
    }

    def __init__(self, address=None, email=None, name=None, metadata=None, enterprise=None, token=None, local_vars_configuration=None):  # noqa: E501
        """TrialRequestOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._email = None
        self._name = None
        self._metadata = None
        self._enterprise = None
        self._token = None
        self.discriminator = None

        if address is not None:
            self.address = address
        self.email = email
        self.name = name
        if metadata is not None:
            self.metadata = metadata
        self.enterprise = enterprise
        self.token = token

    @property
    def address(self):
        """Gets the address of this TrialRequestOptions.  # noqa: E501


        :return: The address of this TrialRequestOptions.  # noqa: E501
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this TrialRequestOptions.


        :param address: The address of this TrialRequestOptions.  # noqa: E501
        :type address: Address
        """

        self._address = address

    @property
    def email(self):
        """Gets the email of this TrialRequestOptions.  # noqa: E501

        The user's email address.  # noqa: E501

        :return: The email of this TrialRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this TrialRequestOptions.

        The user's email address.  # noqa: E501

        :param email: The email of this TrialRequestOptions.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def name(self):
        """Gets the name of this TrialRequestOptions.  # noqa: E501

        The user's full name.  # noqa: E501

        :return: The name of this TrialRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrialRequestOptions.

        The user's full name.  # noqa: E501

        :param name: The name of this TrialRequestOptions.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def metadata(self):
        """Gets the metadata of this TrialRequestOptions.  # noqa: E501


        :return: The metadata of this TrialRequestOptions.  # noqa: E501
        :rtype: TrialRequestMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this TrialRequestOptions.


        :param metadata: The metadata of this TrialRequestOptions.  # noqa: E501
        :type metadata: TrialRequestMetadata
        """

        self._metadata = metadata

    @property
    def enterprise(self):
        """Gets the enterprise of this TrialRequestOptions.  # noqa: E501

        If true, create an enterprise domain.  # noqa: E501

        :return: The enterprise of this TrialRequestOptions.  # noqa: E501
        :rtype: bool
        """
        return self._enterprise

    @enterprise.setter
    def enterprise(self, enterprise):
        """Sets the enterprise of this TrialRequestOptions.

        If true, create an enterprise domain.  # noqa: E501

        :param enterprise: The enterprise of this TrialRequestOptions.  # noqa: E501
        :type enterprise: bool
        """

        self._enterprise = enterprise

    @property
    def token(self):
        """Gets the token of this TrialRequestOptions.  # noqa: E501

        Stripe payment token.  # noqa: E501

        :return: The token of this TrialRequestOptions.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TrialRequestOptions.

        Stripe payment token.  # noqa: E501

        :param token: The token of this TrialRequestOptions.  # noqa: E501
        :type token: str
        """

        self._token = token

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
        if not isinstance(other, TrialRequestOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrialRequestOptions):
            return True

        return self.to_dict() != other.to_dict()
