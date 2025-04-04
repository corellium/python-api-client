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


class ProjectQuota(object):
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
        'cores': 'float',
        'instances': 'float',
        'ram': 'float'
    }

    attribute_map = {
        'cores': 'cores',
        'instances': 'instances',
        'ram': 'ram'
    }

    def __init__(self, cores=None, instances=None, ram=None, local_vars_configuration=None):  # noqa: E501
        """ProjectQuota - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._cores = None
        self._instances = None
        self._ram = None
        self.discriminator = None

        self.cores = cores
        self.instances = instances
        self.ram = ram

    @property
    def cores(self):
        """Gets the cores of this ProjectQuota.  # noqa: E501

          # noqa: E501

        :return: The cores of this ProjectQuota.  # noqa: E501
        :rtype: float
        """
        return self._cores

    @cores.setter
    def cores(self, cores):
        """Sets the cores of this ProjectQuota.

          # noqa: E501

        :param cores: The cores of this ProjectQuota.  # noqa: E501
        :type cores: float
        """

        self._cores = cores

    @property
    def instances(self):
        """Gets the instances of this ProjectQuota.  # noqa: E501

          # noqa: E501

        :return: The instances of this ProjectQuota.  # noqa: E501
        :rtype: float
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this ProjectQuota.

          # noqa: E501

        :param instances: The instances of this ProjectQuota.  # noqa: E501
        :type instances: float
        """

        self._instances = instances

    @property
    def ram(self):
        """Gets the ram of this ProjectQuota.  # noqa: E501

          # noqa: E501

        :return: The ram of this ProjectQuota.  # noqa: E501
        :rtype: float
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this ProjectQuota.

          # noqa: E501

        :param ram: The ram of this ProjectQuota.  # noqa: E501
        :type ram: float
        """

        self._ram = ram

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
        if not isinstance(other, ProjectQuota):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ProjectQuota):
            return True

        return self.to_dict() != other.to_dict()
