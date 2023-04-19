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


class ProjectKey(object):
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
        'kind': 'str',
        'project': 'str',
        'key': 'str',
        'fingerprint': 'str',
        'updated_at': 'datetime',
        'created_at': 'datetime'
    }

    attribute_map = {
        'identifier': 'identifier',
        'kind': 'kind',
        'project': 'project',
        'key': 'key',
        'fingerprint': 'fingerprint',
        'updated_at': 'updatedAt',
        'created_at': 'createdAt'
    }

    def __init__(self, identifier=None, kind=None, project=None, key=None, fingerprint=None, updated_at=None, created_at=None, local_vars_configuration=None):  # noqa: E501
        """ProjectKey - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._identifier = None
        self._kind = None
        self._project = None
        self._key = None
        self._fingerprint = None
        self._updated_at = None
        self._created_at = None
        self.discriminator = None

        self.identifier = identifier
        self.kind = kind
        self.project = project
        self.key = key
        self.fingerprint = fingerprint
        self.updated_at = updated_at
        self.created_at = created_at

    @property
    def identifier(self):
        """Gets the identifier of this ProjectKey.  # noqa: E501

        keyId  # noqa: E501

        :return: The identifier of this ProjectKey.  # noqa: E501
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ProjectKey.

        keyId  # noqa: E501

        :param identifier: The identifier of this ProjectKey.  # noqa: E501
        :type identifier: str
        """

        self._identifier = identifier

    @property
    def kind(self):
        """Gets the kind of this ProjectKey.  # noqa: E501

        kind of key  # noqa: E501

        :return: The kind of this ProjectKey.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ProjectKey.

        kind of key  # noqa: E501

        :param kind: The kind of this ProjectKey.  # noqa: E501
        :type kind: str
        """
        if self.local_vars_configuration.client_side_validation and kind is None:  # noqa: E501
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["ssh", "adb"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and kind not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def project(self):
        """Gets the project of this ProjectKey.  # noqa: E501

        projectId  # noqa: E501

        :return: The project of this ProjectKey.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ProjectKey.

        projectId  # noqa: E501

        :param project: The project of this ProjectKey.  # noqa: E501
        :type project: str
        """

        self._project = project

    @property
    def key(self):
        """Gets the key of this ProjectKey.  # noqa: E501

        The public key  # noqa: E501

        :return: The key of this ProjectKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ProjectKey.

        The public key  # noqa: E501

        :param key: The key of this ProjectKey.  # noqa: E501
        :type key: str
        """
        if self.local_vars_configuration.client_side_validation and key is None:  # noqa: E501
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def fingerprint(self):
        """Gets the fingerprint of this ProjectKey.  # noqa: E501

        Key fingerprint  # noqa: E501

        :return: The fingerprint of this ProjectKey.  # noqa: E501
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this ProjectKey.

        Key fingerprint  # noqa: E501

        :param fingerprint: The fingerprint of this ProjectKey.  # noqa: E501
        :type fingerprint: str
        """

        self._fingerprint = fingerprint

    @property
    def updated_at(self):
        """Gets the updated_at of this ProjectKey.  # noqa: E501

        Time of last update  # noqa: E501

        :return: The updated_at of this ProjectKey.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ProjectKey.

        Time of last update  # noqa: E501

        :param updated_at: The updated_at of this ProjectKey.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def created_at(self):
        """Gets the created_at of this ProjectKey.  # noqa: E501

        Time of creation  # noqa: E501

        :return: The created_at of this ProjectKey.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ProjectKey.

        Time of creation  # noqa: E501

        :param created_at: The created_at of this ProjectKey.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

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
        if not isinstance(other, ProjectKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectKey):
            return True

        return self.to_dict() != other.to_dict()
