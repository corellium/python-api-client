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


class Model(object):
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
        'type': 'str',
        'name': 'str',
        'flavor': 'str',
        'description': 'str',
        'model': 'str',
        'board_config': 'str',
        'platform': 'str',
        'cpid': 'float',
        'bdid': 'float',
        'peripherals': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'flavor': 'flavor',
        'description': 'description',
        'model': 'model',
        'board_config': 'boardConfig',
        'platform': 'platform',
        'cpid': 'cpid',
        'bdid': 'bdid',
        'peripherals': 'peripherals'
    }

    def __init__(self, type=None, name=None, flavor=None, description=None, model=None, board_config=None, platform=None, cpid=None, bdid=None, peripherals=None, local_vars_configuration=None):  # noqa: E501
        """Model - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._flavor = None
        self._description = None
        self._model = None
        self._board_config = None
        self._platform = None
        self._cpid = None
        self._bdid = None
        self._peripherals = None
        self.discriminator = None

        self.type = type
        self.name = name
        self.flavor = flavor
        self.description = description
        self.model = model
        self.board_config = board_config
        self.platform = platform
        self.cpid = cpid
        self.bdid = bdid
        self.peripherals = peripherals

    @property
    def type(self):
        """Gets the type of this Model.  # noqa: E501


        :return: The type of this Model.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Model.


        :param type: The type of this Model.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this Model.  # noqa: E501


        :return: The name of this Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Model.


        :param name: The name of this Model.  # noqa: E501
        :type name: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def flavor(self):
        """Gets the flavor of this Model.  # noqa: E501


        :return: The flavor of this Model.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this Model.


        :param flavor: The flavor of this Model.  # noqa: E501
        :type flavor: str
        """
        if self.local_vars_configuration.client_side_validation and flavor is None:  # noqa: E501
            raise ValueError("Invalid value for `flavor`, must not be `None`")  # noqa: E501

        self._flavor = flavor

    @property
    def description(self):
        """Gets the description of this Model.  # noqa: E501


        :return: The description of this Model.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Model.


        :param description: The description of this Model.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def model(self):
        """Gets the model of this Model.  # noqa: E501


        :return: The model of this Model.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Model.


        :param model: The model of this Model.  # noqa: E501
        :type model: str
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def board_config(self):
        """Gets the board_config of this Model.  # noqa: E501


        :return: The board_config of this Model.  # noqa: E501
        :rtype: str
        """
        return self._board_config

    @board_config.setter
    def board_config(self, board_config):
        """Sets the board_config of this Model.


        :param board_config: The board_config of this Model.  # noqa: E501
        :type board_config: str
        """

        self._board_config = board_config

    @property
    def platform(self):
        """Gets the platform of this Model.  # noqa: E501


        :return: The platform of this Model.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Model.


        :param platform: The platform of this Model.  # noqa: E501
        :type platform: str
        """

        self._platform = platform

    @property
    def cpid(self):
        """Gets the cpid of this Model.  # noqa: E501


        :return: The cpid of this Model.  # noqa: E501
        :rtype: float
        """
        return self._cpid

    @cpid.setter
    def cpid(self, cpid):
        """Sets the cpid of this Model.


        :param cpid: The cpid of this Model.  # noqa: E501
        :type cpid: float
        """

        self._cpid = cpid

    @property
    def bdid(self):
        """Gets the bdid of this Model.  # noqa: E501


        :return: The bdid of this Model.  # noqa: E501
        :rtype: float
        """
        return self._bdid

    @bdid.setter
    def bdid(self, bdid):
        """Sets the bdid of this Model.


        :param bdid: The bdid of this Model.  # noqa: E501
        :type bdid: float
        """

        self._bdid = bdid

    @property
    def peripherals(self):
        """Gets the peripherals of this Model.  # noqa: E501


        :return: The peripherals of this Model.  # noqa: E501
        :rtype: bool
        """
        return self._peripherals

    @peripherals.setter
    def peripherals(self, peripherals):
        """Sets the peripherals of this Model.


        :param peripherals: The peripherals of this Model.  # noqa: E501
        :type peripherals: bool
        """

        self._peripherals = peripherals

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
        if not isinstance(other, Model):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Model):
            return True

        return self.to_dict() != other.to_dict()
