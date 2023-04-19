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


class FileChanges(object):
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
        'path': 'str',
        'mode': 'float',
        'uid': 'float',
        'gid': 'float'
    }

    attribute_map = {
        'path': 'path',
        'mode': 'mode',
        'uid': 'uid',
        'gid': 'gid'
    }

    def __init__(self, path=None, mode=None, uid=None, gid=None, local_vars_configuration=None):  # noqa: E501
        """FileChanges - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._path = None
        self._mode = None
        self._uid = None
        self._gid = None
        self.discriminator = None

        self.path = path
        self.mode = mode
        self.uid = uid
        self.gid = gid

    @property
    def path(self):
        """Gets the path of this FileChanges.  # noqa: E501

        Optional New path  # noqa: E501

        :return: The path of this FileChanges.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this FileChanges.

        Optional New path  # noqa: E501

        :param path: The path of this FileChanges.  # noqa: E501
        :type path: str
        """

        self._path = path

    @property
    def mode(self):
        """Gets the mode of this FileChanges.  # noqa: E501

        Optional New Mode  # noqa: E501

        :return: The mode of this FileChanges.  # noqa: E501
        :rtype: float
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this FileChanges.

        Optional New Mode  # noqa: E501

        :param mode: The mode of this FileChanges.  # noqa: E501
        :type mode: float
        """

        self._mode = mode

    @property
    def uid(self):
        """Gets the uid of this FileChanges.  # noqa: E501

        Optional New Owner UID  # noqa: E501

        :return: The uid of this FileChanges.  # noqa: E501
        :rtype: float
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this FileChanges.

        Optional New Owner UID  # noqa: E501

        :param uid: The uid of this FileChanges.  # noqa: E501
        :type uid: float
        """

        self._uid = uid

    @property
    def gid(self):
        """Gets the gid of this FileChanges.  # noqa: E501

        Optional New Group GID  # noqa: E501

        :return: The gid of this FileChanges.  # noqa: E501
        :rtype: float
        """
        return self._gid

    @gid.setter
    def gid(self, gid):
        """Sets the gid of this FileChanges.

        Optional New Group GID  # noqa: E501

        :param gid: The gid of this FileChanges.  # noqa: E501
        :type gid: float
        """

        self._gid = gid

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
        if not isinstance(other, FileChanges):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FileChanges):
            return True

        return self.to_dict() != other.to_dict()
