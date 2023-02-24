# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 4.2.0-6a4b86f
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


class Invitation(object):
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
        'identifier': 'str',
        'email': 'str',
        'settings': 'object'
    }

    attribute_map = {
        'identifier': 'identifier',
        'email': 'email',
        'settings': 'settings'
    }

    def __init__(self, identifier=None, email=None, settings=None, local_vars_configuration=None):  # noqa: E501
        """Invitation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._identifier = None
        self._email = None
        self._settings = None
        self.discriminator = None

        self.identifier = identifier
        self.email = email
        self.settings = settings

    @property
    def identifier(self):
        """Gets the identifier of this Invitation.  # noqa: E501

        Invite ID  # noqa: E501

        :return: The identifier of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this Invitation.

        Invite ID  # noqa: E501

        :param identifier: The identifier of this Invitation.  # noqa: E501
        :type identifier: str
        """

        self._identifier = identifier

    @property
    def email(self):
        """Gets the email of this Invitation.  # noqa: E501

        Invited email  # noqa: E501

        :return: The email of this Invitation.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this Invitation.

        Invited email  # noqa: E501

        :param email: The email of this Invitation.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def settings(self):
        """Gets the settings of this Invitation.  # noqa: E501

          # noqa: E501

        :return: The settings of this Invitation.  # noqa: E501
        :rtype: object
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Invitation.

          # noqa: E501

        :param settings: The settings of this Invitation.  # noqa: E501
        :type settings: object
        """

        self._settings = settings

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
        if not isinstance(other, Invitation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Invitation):
            return True

        return self.to_dict() != other.to_dict()
