# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.11.0-13642
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


class TouchCurveInput(object):
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
        'start': 'object',
        'end': 'object'
    }

    attribute_map = {
        'start': 'start',
        'end': 'end'
    }

    def __init__(self, start=None, end=None, local_vars_configuration=None):  # noqa: E501
        """TouchCurveInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._start = None
        self._end = None
        self.discriminator = None

        if start is not None:
            self.start = start
        if end is not None:
            self.end = end

    @property
    def start(self):
        """Gets the start of this TouchCurveInput.  # noqa: E501

        Finger Positions  # noqa: E501

        :return: The start of this TouchCurveInput.  # noqa: E501
        :rtype: object
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TouchCurveInput.

        Finger Positions  # noqa: E501

        :param start: The start of this TouchCurveInput.  # noqa: E501
        :type start: object
        """

        self._start = start

    @property
    def end(self):
        """Gets the end of this TouchCurveInput.  # noqa: E501

        Finger Positions  # noqa: E501

        :return: The end of this TouchCurveInput.  # noqa: E501
        :rtype: object
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this TouchCurveInput.

        Finger Positions  # noqa: E501

        :param end: The end of this TouchCurveInput.  # noqa: E501
        :type end: object
        """

        self._end = end

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
        if not isinstance(other, TouchCurveInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TouchCurveInput):
            return True

        return self.to_dict() != other.to_dict()