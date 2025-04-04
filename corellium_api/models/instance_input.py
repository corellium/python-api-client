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


class InstanceInput(object):
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
        'position': 'object',
        'buttons': 'list[TouchInputButtonsInner]',
        'normalized': 'bool',
        'wait': 'float',
        'start': 'object',
        'end': 'object',
        'bezier_points': 'list[object]',
        'start_buttons': 'list[TouchInputButtonsInner]',
        'end_buttons': 'list[TouchInputButtonsInner]',
        'duration': 'float',
        'required': 'str',
        'key_duration': 'float'
    }

    attribute_map = {
        'position': 'position',
        'buttons': 'buttons',
        'normalized': 'normalized',
        'wait': 'wait',
        'start': 'start',
        'end': 'end',
        'bezier_points': 'bezierPoints',
        'start_buttons': 'startButtons',
        'end_buttons': 'endButtons',
        'duration': 'duration',
        'required': 'required',
        'key_duration': 'keyDuration'
    }

    def __init__(self, position=None, buttons=None, normalized=None, wait=None, start=None, end=None, bezier_points=None, start_buttons=None, end_buttons=None, duration=None, required=None, key_duration=None, local_vars_configuration=None):  # noqa: E501
        """InstanceInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._position = None
        self._buttons = None
        self._normalized = None
        self._wait = None
        self._start = None
        self._end = None
        self._bezier_points = None
        self._start_buttons = None
        self._end_buttons = None
        self._duration = None
        self._required = None
        self._key_duration = None
        self.discriminator = None

        self.position = position
        self.buttons = buttons
        self.normalized = normalized
        self.wait = wait
        self.start = start
        self.end = end
        self.bezier_points = bezier_points
        self.start_buttons = start_buttons
        self.end_buttons = end_buttons
        self.duration = duration
        self.required = required
        self.key_duration = key_duration

    @property
    def position(self):
        """Gets the position of this InstanceInput.  # noqa: E501

        Finger Positions  # noqa: E501

        :return: The position of this InstanceInput.  # noqa: E501
        :rtype: object
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this InstanceInput.

        Finger Positions  # noqa: E501

        :param position: The position of this InstanceInput.  # noqa: E501
        :type position: object
        """
        if self.local_vars_configuration.client_side_validation and position is None:  # noqa: E501
            raise ValueError("Invalid value for `position`, must not be `None`")  # noqa: E501

        self._position = position

    @property
    def buttons(self):
        """Gets the buttons of this InstanceInput.  # noqa: E501

        Buttons to be held when this position is reached. Either a Button enum object or an ASCII character. No change if not defined.  # noqa: E501

        :return: The buttons of this InstanceInput.  # noqa: E501
        :rtype: list[TouchInputButtonsInner]
        """
        return self._buttons

    @buttons.setter
    def buttons(self, buttons):
        """Sets the buttons of this InstanceInput.

        Buttons to be held when this position is reached. Either a Button enum object or an ASCII character. No change if not defined.  # noqa: E501

        :param buttons: The buttons of this InstanceInput.  # noqa: E501
        :type buttons: list[TouchInputButtonsInner]
        """

        self._buttons = buttons

    @property
    def normalized(self):
        """Gets the normalized of this InstanceInput.  # noqa: E501

        true if you want to use normalized x,y coordinates from 0-10000 (eg 5000,5000 is always center of screen)  # noqa: E501

        :return: The normalized of this InstanceInput.  # noqa: E501
        :rtype: bool
        """
        return self._normalized

    @normalized.setter
    def normalized(self, normalized):
        """Sets the normalized of this InstanceInput.

        true if you want to use normalized x,y coordinates from 0-10000 (eg 5000,5000 is always center of screen)  # noqa: E501

        :param normalized: The normalized of this InstanceInput.  # noqa: E501
        :type normalized: bool
        """

        self._normalized = normalized

    @property
    def wait(self):
        """Gets the wait of this InstanceInput.  # noqa: E501

        Duration to wait before this input is executed.  Instant if not defined.  # noqa: E501

        :return: The wait of this InstanceInput.  # noqa: E501
        :rtype: float
        """
        return self._wait

    @wait.setter
    def wait(self, wait):
        """Sets the wait of this InstanceInput.

        Duration to wait before this input is executed.  Instant if not defined.  # noqa: E501

        :param wait: The wait of this InstanceInput.  # noqa: E501
        :type wait: float
        """

        self._wait = wait

    @property
    def start(self):
        """Gets the start of this InstanceInput.  # noqa: E501

        Finger Positions  # noqa: E501

        :return: The start of this InstanceInput.  # noqa: E501
        :rtype: object
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this InstanceInput.

        Finger Positions  # noqa: E501

        :param start: The start of this InstanceInput.  # noqa: E501
        :type start: object
        """
        if self.local_vars_configuration.client_side_validation and start is None:  # noqa: E501
            raise ValueError("Invalid value for `start`, must not be `None`")  # noqa: E501

        self._start = start

    @property
    def end(self):
        """Gets the end of this InstanceInput.  # noqa: E501

        Finger Positions  # noqa: E501

        :return: The end of this InstanceInput.  # noqa: E501
        :rtype: object
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this InstanceInput.

        Finger Positions  # noqa: E501

        :param end: The end of this InstanceInput.  # noqa: E501
        :type end: object
        """
        if self.local_vars_configuration.client_side_validation and end is None:  # noqa: E501
            raise ValueError("Invalid value for `end`, must not be `None`")  # noqa: E501

        self._end = end

    @property
    def bezier_points(self):
        """Gets the bezier_points of this InstanceInput.  # noqa: E501

        array of per-finger intermediate touch positions, up to 10 depending on model.  Straight line if not defined.  # noqa: E501

        :return: The bezier_points of this InstanceInput.  # noqa: E501
        :rtype: list[object]
        """
        return self._bezier_points

    @bezier_points.setter
    def bezier_points(self, bezier_points):
        """Sets the bezier_points of this InstanceInput.

        array of per-finger intermediate touch positions, up to 10 depending on model.  Straight line if not defined.  # noqa: E501

        :param bezier_points: The bezier_points of this InstanceInput.  # noqa: E501
        :type bezier_points: list[object]
        """

        self._bezier_points = bezier_points

    @property
    def start_buttons(self):
        """Gets the start_buttons of this InstanceInput.  # noqa: E501

        Buttons to be held during this curve.  # noqa: E501

        :return: The start_buttons of this InstanceInput.  # noqa: E501
        :rtype: list[TouchInputButtonsInner]
        """
        return self._start_buttons

    @start_buttons.setter
    def start_buttons(self, start_buttons):
        """Sets the start_buttons of this InstanceInput.

        Buttons to be held during this curve.  # noqa: E501

        :param start_buttons: The start_buttons of this InstanceInput.  # noqa: E501
        :type start_buttons: list[TouchInputButtonsInner]
        """
        if self.local_vars_configuration.client_side_validation and start_buttons is None:  # noqa: E501
            raise ValueError("Invalid value for `start_buttons`, must not be `None`")  # noqa: E501

        self._start_buttons = start_buttons

    @property
    def end_buttons(self):
        """Gets the end_buttons of this InstanceInput.  # noqa: E501

        Buttons to be left held after this curve.  Same as startButtons if not defined.  # noqa: E501

        :return: The end_buttons of this InstanceInput.  # noqa: E501
        :rtype: list[TouchInputButtonsInner]
        """
        return self._end_buttons

    @end_buttons.setter
    def end_buttons(self, end_buttons):
        """Sets the end_buttons of this InstanceInput.

        Buttons to be left held after this curve.  Same as startButtons if not defined.  # noqa: E501

        :param end_buttons: The end_buttons of this InstanceInput.  # noqa: E501
        :type end_buttons: list[TouchInputButtonsInner]
        """

        self._end_buttons = end_buttons

    @property
    def duration(self):
        """Gets the duration of this InstanceInput.  # noqa: E501

        Duration to execute this curve over.  # noqa: E501

        :return: The duration of this InstanceInput.  # noqa: E501
        :rtype: float
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this InstanceInput.

        Duration to execute this curve over.  # noqa: E501

        :param duration: The duration of this InstanceInput.  # noqa: E501
        :type duration: float
        """
        if self.local_vars_configuration.client_side_validation and duration is None:  # noqa: E501
            raise ValueError("Invalid value for `duration`, must not be `None`")  # noqa: E501

        self._duration = duration

    @property
    def required(self):
        """Gets the required of this InstanceInput.  # noqa: E501

        text to type  # noqa: E501

        :return: The required of this InstanceInput.  # noqa: E501
        :rtype: str
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this InstanceInput.

        text to type  # noqa: E501

        :param required: The required of this InstanceInput.  # noqa: E501
        :type required: str
        """
        if self.local_vars_configuration.client_side_validation and required is None:  # noqa: E501
            raise ValueError("Invalid value for `required`, must not be `None`")  # noqa: E501

        self._required = required

    @property
    def key_duration(self):
        """Gets the key_duration of this InstanceInput.  # noqa: E501

        How long to take to type each key.  150ms if not defined.  # noqa: E501

        :return: The key_duration of this InstanceInput.  # noqa: E501
        :rtype: float
        """
        return self._key_duration

    @key_duration.setter
    def key_duration(self, key_duration):
        """Sets the key_duration of this InstanceInput.

        How long to take to type each key.  150ms if not defined.  # noqa: E501

        :param key_duration: The key_duration of this InstanceInput.  # noqa: E501
        :type key_duration: float
        """

        self._key_duration = key_duration

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
        if not isinstance(other, InstanceInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceInput):
            return True

        return self.to_dict() != other.to_dict()
