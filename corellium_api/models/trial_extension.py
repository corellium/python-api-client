# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.11.0-13738
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


class TrialExtension(object):
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
        'duration': 'float',
        'reason': 'str',
        'denied': 'list[object]',
        'denied_reason': 'str'
    }

    attribute_map = {
        'duration': 'duration',
        'reason': 'reason',
        'denied': 'denied',
        'denied_reason': 'deniedReason'
    }

    def __init__(self, duration=None, reason=None, denied=None, denied_reason=None, local_vars_configuration=None):  # noqa: E501
        """TrialExtension - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._duration = None
        self._reason = None
        self._denied = None
        self._denied_reason = None
        self.discriminator = None

        self.duration = duration
        self.reason = reason
        self.denied = denied
        self.denied_reason = denied_reason

    @property
    def duration(self):
        """Gets the duration of this TrialExtension.  # noqa: E501

        how many additional days?  # noqa: E501

        :return: The duration of this TrialExtension.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this TrialExtension.

        how many additional days?  # noqa: E501

        :param duration: The duration of this TrialExtension.  # noqa: E501
        :type duration: float
        """

        self._duration = duration

    @property
    def reason(self):
        """Gets the reason of this TrialExtension.  # noqa: E501

        why does the user want more time?  # noqa: E501

        :return: The reason of this TrialExtension.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this TrialExtension.

        why does the user want more time?  # noqa: E501

        :param reason: The reason of this TrialExtension.  # noqa: E501
        :type reason: str
        """

        self._reason = reason

    @property
    def denied(self):
        """Gets the denied of this TrialExtension.  # noqa: E501


        :return: The denied of this TrialExtension.  # noqa: E501
        :rtype: list[object]
        """
        return self._denied

    @denied.setter
    def denied(self, denied):
        """Sets the denied of this TrialExtension.


        :param denied: The denied of this TrialExtension.  # noqa: E501
        :type denied: list[object]
        """

        self._denied = denied

    @property
    def denied_reason(self):
        """Gets the denied_reason of this TrialExtension.  # noqa: E501

        explanation for why the request was denied  # noqa: E501

        :return: The denied_reason of this TrialExtension.  # noqa: E501
        :rtype: str
        """
        return self._denied_reason

    @denied_reason.setter
    def denied_reason(self, denied_reason):
        """Sets the denied_reason of this TrialExtension.

        explanation for why the request was denied  # noqa: E501

        :param denied_reason: The denied_reason of this TrialExtension.  # noqa: E501
        :type denied_reason: str
        """

        self._denied_reason = denied_reason

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
        if not isinstance(other, TrialExtension):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrialExtension):
            return True

        return self.to_dict() != other.to_dict()
