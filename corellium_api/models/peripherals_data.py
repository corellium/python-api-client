# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.10.0-13354
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


class PeripheralsData(object):
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
        'acceleration': 'list[float]',
        'gyroscope': 'list[float]',
        'magnetic': 'list[float]',
        'orientation': 'list[float]',
        'temperature': 'float',
        'proximity': 'float',
        'light': 'float',
        'pressure': 'float',
        'humidity': 'float'
    }

    attribute_map = {
        'acceleration': 'acceleration',
        'gyroscope': 'gyroscope',
        'magnetic': 'magnetic',
        'orientation': 'orientation',
        'temperature': 'temperature',
        'proximity': 'proximity',
        'light': 'light',
        'pressure': 'pressure',
        'humidity': 'humidity'
    }

    def __init__(self, acceleration=None, gyroscope=None, magnetic=None, orientation=None, temperature=None, proximity=None, light=None, pressure=None, humidity=None, local_vars_configuration=None):  # noqa: E501
        """PeripheralsData - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._acceleration = None
        self._gyroscope = None
        self._magnetic = None
        self._orientation = None
        self._temperature = None
        self._proximity = None
        self._light = None
        self._pressure = None
        self._humidity = None
        self.discriminator = None

        self.acceleration = acceleration
        self.gyroscope = gyroscope
        self.magnetic = magnetic
        self.orientation = orientation
        self.temperature = temperature
        self.proximity = proximity
        self.light = light
        self.pressure = pressure
        self.humidity = humidity

    @property
    def acceleration(self):
        """Gets the acceleration of this PeripheralsData.  # noqa: E501


        :return: The acceleration of this PeripheralsData.  # noqa: E501
        :rtype: list[float]
        """
        return self._acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        """Sets the acceleration of this PeripheralsData.


        :param acceleration: The acceleration of this PeripheralsData.  # noqa: E501
        :type acceleration: list[float]
        """

        self._acceleration = acceleration

    @property
    def gyroscope(self):
        """Gets the gyroscope of this PeripheralsData.  # noqa: E501


        :return: The gyroscope of this PeripheralsData.  # noqa: E501
        :rtype: list[float]
        """
        return self._gyroscope

    @gyroscope.setter
    def gyroscope(self, gyroscope):
        """Sets the gyroscope of this PeripheralsData.


        :param gyroscope: The gyroscope of this PeripheralsData.  # noqa: E501
        :type gyroscope: list[float]
        """

        self._gyroscope = gyroscope

    @property
    def magnetic(self):
        """Gets the magnetic of this PeripheralsData.  # noqa: E501


        :return: The magnetic of this PeripheralsData.  # noqa: E501
        :rtype: list[float]
        """
        return self._magnetic

    @magnetic.setter
    def magnetic(self, magnetic):
        """Sets the magnetic of this PeripheralsData.


        :param magnetic: The magnetic of this PeripheralsData.  # noqa: E501
        :type magnetic: list[float]
        """

        self._magnetic = magnetic

    @property
    def orientation(self):
        """Gets the orientation of this PeripheralsData.  # noqa: E501


        :return: The orientation of this PeripheralsData.  # noqa: E501
        :rtype: list[float]
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this PeripheralsData.


        :param orientation: The orientation of this PeripheralsData.  # noqa: E501
        :type orientation: list[float]
        """

        self._orientation = orientation

    @property
    def temperature(self):
        """Gets the temperature of this PeripheralsData.  # noqa: E501


        :return: The temperature of this PeripheralsData.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this PeripheralsData.


        :param temperature: The temperature of this PeripheralsData.  # noqa: E501
        :type temperature: float
        """

        self._temperature = temperature

    @property
    def proximity(self):
        """Gets the proximity of this PeripheralsData.  # noqa: E501


        :return: The proximity of this PeripheralsData.  # noqa: E501
        :rtype: float
        """
        return self._proximity

    @proximity.setter
    def proximity(self, proximity):
        """Sets the proximity of this PeripheralsData.


        :param proximity: The proximity of this PeripheralsData.  # noqa: E501
        :type proximity: float
        """

        self._proximity = proximity

    @property
    def light(self):
        """Gets the light of this PeripheralsData.  # noqa: E501


        :return: The light of this PeripheralsData.  # noqa: E501
        :rtype: float
        """
        return self._light

    @light.setter
    def light(self, light):
        """Sets the light of this PeripheralsData.


        :param light: The light of this PeripheralsData.  # noqa: E501
        :type light: float
        """

        self._light = light

    @property
    def pressure(self):
        """Gets the pressure of this PeripheralsData.  # noqa: E501


        :return: The pressure of this PeripheralsData.  # noqa: E501
        :rtype: float
        """
        return self._pressure

    @pressure.setter
    def pressure(self, pressure):
        """Sets the pressure of this PeripheralsData.


        :param pressure: The pressure of this PeripheralsData.  # noqa: E501
        :type pressure: float
        """

        self._pressure = pressure

    @property
    def humidity(self):
        """Gets the humidity of this PeripheralsData.  # noqa: E501


        :return: The humidity of this PeripheralsData.  # noqa: E501
        :rtype: float
        """
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        """Sets the humidity of this PeripheralsData.


        :param humidity: The humidity of this PeripheralsData.  # noqa: E501
        :type humidity: float
        """

        self._humidity = humidity

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
        if not isinstance(other, PeripheralsData):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PeripheralsData):
            return True

        return self.to_dict() != other.to_dict()
