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


class CreatedBy(object):
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
        'id': 'str',
        'username': 'str',
        'label': 'str',
        'deleted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'label': 'label',
        'deleted': 'deleted'
    }

    def __init__(self, id=None, username=None, label=None, deleted=None, local_vars_configuration=None):  # noqa: E501
        """CreatedBy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._username = None
        self._label = None
        self._deleted = None
        self.discriminator = None

        self.id = id
        self.username = username
        self.label = label
        self.deleted = deleted

    @property
    def id(self):
        """Gets the id of this CreatedBy.  # noqa: E501

        User Identifier  # noqa: E501

        :return: The id of this CreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreatedBy.

        User Identifier  # noqa: E501

        :param id: The id of this CreatedBy.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this CreatedBy.  # noqa: E501

        Username  # noqa: E501

        :return: The username of this CreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this CreatedBy.

        Username  # noqa: E501

        :param username: The username of this CreatedBy.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def label(self):
        """Gets the label of this CreatedBy.  # noqa: E501

        User Label  # noqa: E501

        :return: The label of this CreatedBy.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this CreatedBy.

        User Label  # noqa: E501

        :param label: The label of this CreatedBy.  # noqa: E501
        :type label: str
        """

        self._label = label

    @property
    def deleted(self):
        """Gets the deleted of this CreatedBy.  # noqa: E501

        Indicates if user was deleted  # noqa: E501

        :return: The deleted of this CreatedBy.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this CreatedBy.

        Indicates if user was deleted  # noqa: E501

        :param deleted: The deleted of this CreatedBy.  # noqa: E501
        :type deleted: bool
        """

        self._deleted = deleted

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
        if not isinstance(other, CreatedBy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CreatedBy):
            return True

        return self.to_dict() != other.to_dict()
