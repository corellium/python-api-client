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


class InstanceBootOptions(object):
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
        'boot_args': 'str',
        'restore_boot_args': 'str',
        'udid': 'str',
        'ecid': 'str',
        'random_seed': 'str',
        'pac': 'bool',
        'aprr': 'bool'
    }

    attribute_map = {
        'boot_args': 'bootArgs',
        'restore_boot_args': 'restoreBootArgs',
        'udid': 'udid',
        'ecid': 'ecid',
        'random_seed': 'randomSeed',
        'pac': 'pac',
        'aprr': 'aprr'
    }

    def __init__(self, boot_args=None, restore_boot_args=None, udid=None, ecid=None, random_seed=None, pac=None, aprr=None, local_vars_configuration=None):  # noqa: E501
        """InstanceBootOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._boot_args = None
        self._restore_boot_args = None
        self._udid = None
        self._ecid = None
        self._random_seed = None
        self._pac = None
        self._aprr = None
        self.discriminator = None

        self.boot_args = boot_args
        self.restore_boot_args = restore_boot_args
        self.udid = udid
        self.ecid = ecid
        self.random_seed = random_seed
        self.pac = pac
        self.aprr = aprr

    @property
    def boot_args(self):
        """Gets the boot_args of this InstanceBootOptions.  # noqa: E501


        :return: The boot_args of this InstanceBootOptions.  # noqa: E501
        :rtype: str
        """
        return self._boot_args

    @boot_args.setter
    def boot_args(self, boot_args):
        """Sets the boot_args of this InstanceBootOptions.


        :param boot_args: The boot_args of this InstanceBootOptions.  # noqa: E501
        :type boot_args: str
        """

        self._boot_args = boot_args

    @property
    def restore_boot_args(self):
        """Gets the restore_boot_args of this InstanceBootOptions.  # noqa: E501


        :return: The restore_boot_args of this InstanceBootOptions.  # noqa: E501
        :rtype: str
        """
        return self._restore_boot_args

    @restore_boot_args.setter
    def restore_boot_args(self, restore_boot_args):
        """Sets the restore_boot_args of this InstanceBootOptions.


        :param restore_boot_args: The restore_boot_args of this InstanceBootOptions.  # noqa: E501
        :type restore_boot_args: str
        """

        self._restore_boot_args = restore_boot_args

    @property
    def udid(self):
        """Gets the udid of this InstanceBootOptions.  # noqa: E501

        Boot udid  # noqa: E501

        :return: The udid of this InstanceBootOptions.  # noqa: E501
        :rtype: str
        """
        return self._udid

    @udid.setter
    def udid(self, udid):
        """Sets the udid of this InstanceBootOptions.

        Boot udid  # noqa: E501

        :param udid: The udid of this InstanceBootOptions.  # noqa: E501
        :type udid: str
        """

        self._udid = udid

    @property
    def ecid(self):
        """Gets the ecid of this InstanceBootOptions.  # noqa: E501

        Assigned ECID  # noqa: E501

        :return: The ecid of this InstanceBootOptions.  # noqa: E501
        :rtype: str
        """
        return self._ecid

    @ecid.setter
    def ecid(self, ecid):
        """Sets the ecid of this InstanceBootOptions.

        Assigned ECID  # noqa: E501

        :param ecid: The ecid of this InstanceBootOptions.  # noqa: E501
        :type ecid: str
        """

        self._ecid = ecid

    @property
    def random_seed(self):
        """Gets the random_seed of this InstanceBootOptions.  # noqa: E501

        Random seed to provide to boot if any  # noqa: E501

        :return: The random_seed of this InstanceBootOptions.  # noqa: E501
        :rtype: str
        """
        return self._random_seed

    @random_seed.setter
    def random_seed(self, random_seed):
        """Sets the random_seed of this InstanceBootOptions.

        Random seed to provide to boot if any  # noqa: E501

        :param random_seed: The random_seed of this InstanceBootOptions.  # noqa: E501
        :type random_seed: str
        """

        self._random_seed = random_seed

    @property
    def pac(self):
        """Gets the pac of this InstanceBootOptions.  # noqa: E501

        Enable PAC  # noqa: E501

        :return: The pac of this InstanceBootOptions.  # noqa: E501
        :rtype: bool
        """
        return self._pac

    @pac.setter
    def pac(self, pac):
        """Sets the pac of this InstanceBootOptions.

        Enable PAC  # noqa: E501

        :param pac: The pac of this InstanceBootOptions.  # noqa: E501
        :type pac: bool
        """

        self._pac = pac

    @property
    def aprr(self):
        """Gets the aprr of this InstanceBootOptions.  # noqa: E501

        Enable APRR  # noqa: E501

        :return: The aprr of this InstanceBootOptions.  # noqa: E501
        :rtype: bool
        """
        return self._aprr

    @aprr.setter
    def aprr(self, aprr):
        """Sets the aprr of this InstanceBootOptions.

        Enable APRR  # noqa: E501

        :param aprr: The aprr of this InstanceBootOptions.  # noqa: E501
        :type aprr: bool
        """

        self._aprr = aprr

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
        if not isinstance(other, InstanceBootOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceBootOptions):
            return True

        return self.to_dict() != other.to_dict()
