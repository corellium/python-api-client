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


class PasswordChangeBody(object):
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
        'user': 'str',
        'old_password': 'str',
        'new_password': 'str'
    }

    attribute_map = {
        'user': 'user',
        'old_password': 'old-password',
        'new_password': 'new-password'
    }

    def __init__(self, user=None, old_password=None, new_password=None, local_vars_configuration=None):  # noqa: E501
        """PasswordChangeBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._user = None
        self._old_password = None
        self._new_password = None
        self.discriminator = None

        self.user = user
        self.old_password = old_password
        self.new_password = new_password

    @property
    def user(self):
        """Gets the user of this PasswordChangeBody.  # noqa: E501

        userId  # noqa: E501

        :return: The user of this PasswordChangeBody.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this PasswordChangeBody.

        userId  # noqa: E501

        :param user: The user of this PasswordChangeBody.  # noqa: E501
        :type user: str
        """
        if self.local_vars_configuration.client_side_validation and user is None:  # noqa: E501
            raise ValueError("Invalid value for `user`, must not be `None`")  # noqa: E501

        self._user = user

    @property
    def old_password(self):
        """Gets the old_password of this PasswordChangeBody.  # noqa: E501

        old password  # noqa: E501

        :return: The old_password of this PasswordChangeBody.  # noqa: E501
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this PasswordChangeBody.

        old password  # noqa: E501

        :param old_password: The old_password of this PasswordChangeBody.  # noqa: E501
        :type old_password: str
        """
        if self.local_vars_configuration.client_side_validation and old_password is None:  # noqa: E501
            raise ValueError("Invalid value for `old_password`, must not be `None`")  # noqa: E501

        self._old_password = old_password

    @property
    def new_password(self):
        """Gets the new_password of this PasswordChangeBody.  # noqa: E501

        new password  # noqa: E501

        :return: The new_password of this PasswordChangeBody.  # noqa: E501
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this PasswordChangeBody.

        new password  # noqa: E501

        :param new_password: The new_password of this PasswordChangeBody.  # noqa: E501
        :type new_password: str
        """
        if self.local_vars_configuration.client_side_validation and new_password is None:  # noqa: E501
            raise ValueError("Invalid value for `new_password`, must not be `None`")  # noqa: E501

        self._new_password = new_password

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
        if not isinstance(other, PasswordChangeBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PasswordChangeBody):
            return True

        return self.to_dict() != other.to_dict()
