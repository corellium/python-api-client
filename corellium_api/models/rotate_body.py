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


class RotateBody(object):
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
        'orientation': 'float'
    }

    attribute_map = {
        'orientation': 'orientation'
    }

    def __init__(self, orientation=None, local_vars_configuration=None):  # noqa: E501
        """RotateBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._orientation = None
        self.discriminator = None

        self.orientation = orientation

    @property
    def orientation(self):
        """Gets the orientation of this RotateBody.  # noqa: E501

        Desired orientation  # noqa: E501

        :return: The orientation of this RotateBody.  # noqa: E501
        :rtype: float
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this RotateBody.

        Desired orientation  # noqa: E501

        :param orientation: The orientation of this RotateBody.  # noqa: E501
        :type orientation: float
        """
        if self.local_vars_configuration.client_side_validation and orientation is None:  # noqa: E501
            raise ValueError("Invalid value for `orientation`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2, 3, 4]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and orientation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `orientation` ({0}), must be one of {1}"  # noqa: E501
                .format(orientation, allowed_values)
            )

        self._orientation = orientation

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
        if not isinstance(other, RotateBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RotateBody):
            return True

        return self.to_dict() != other.to_dict()
