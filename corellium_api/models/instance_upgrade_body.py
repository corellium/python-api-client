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


class InstanceUpgradeBody(object):
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
        'os': 'str',
        'osbuild': 'str'
    }

    attribute_map = {
        'os': 'os',
        'osbuild': 'osbuild'
    }

    def __init__(self, os=None, osbuild=None, local_vars_configuration=None):  # noqa: E501
        """InstanceUpgradeBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._os = None
        self._osbuild = None
        self.discriminator = None

        self.os = os
        self.osbuild = osbuild

    @property
    def os(self):
        """Gets the os of this InstanceUpgradeBody.  # noqa: E501

        iOS version  # noqa: E501

        :return: The os of this InstanceUpgradeBody.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this InstanceUpgradeBody.

        iOS version  # noqa: E501

        :param os: The os of this InstanceUpgradeBody.  # noqa: E501
        :type os: str
        """
        if self.local_vars_configuration.client_side_validation and os is None:  # noqa: E501
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def osbuild(self):
        """Gets the osbuild of this InstanceUpgradeBody.  # noqa: E501

        (optional) iOS build ID  # noqa: E501

        :return: The osbuild of this InstanceUpgradeBody.  # noqa: E501
        :rtype: str
        """
        return self._osbuild

    @osbuild.setter
    def osbuild(self, osbuild):
        """Sets the osbuild of this InstanceUpgradeBody.

        (optional) iOS build ID  # noqa: E501

        :param osbuild: The osbuild of this InstanceUpgradeBody.  # noqa: E501
        :type osbuild: str
        """

        self._osbuild = osbuild

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
        if not isinstance(other, InstanceUpgradeBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceUpgradeBody):
            return True

        return self.to_dict() != other.to_dict()
