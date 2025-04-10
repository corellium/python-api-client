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


class V1CreateHookParameters(object):
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
        'label': 'str',
        'address': 'str',
        'patch': 'str',
        'patch_type': 'str'
    }

    attribute_map = {
        'label': 'label',
        'address': 'address',
        'patch': 'patch',
        'patch_type': 'patchType'
    }

    def __init__(self, label=None, address=None, patch=None, patch_type=None, local_vars_configuration=None):  # noqa: E501
        """V1CreateHookParameters - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._label = None
        self._address = None
        self._patch = None
        self._patch_type = None
        self.discriminator = None

        self.label = label
        self.address = address
        self.patch = patch
        self.patch_type = patch_type

    @property
    def label(self):
        """Gets the label of this V1CreateHookParameters.  # noqa: E501

        Label  # noqa: E501

        :return: The label of this V1CreateHookParameters.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this V1CreateHookParameters.

        Label  # noqa: E501

        :param label: The label of this V1CreateHookParameters.  # noqa: E501
        :type label: str
        """
        if self.local_vars_configuration.client_side_validation and label is None:  # noqa: E501
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501

        self._label = label

    @property
    def address(self):
        """Gets the address of this V1CreateHookParameters.  # noqa: E501

        Address  # noqa: E501

        :return: The address of this V1CreateHookParameters.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this V1CreateHookParameters.

        Address  # noqa: E501

        :param address: The address of this V1CreateHookParameters.  # noqa: E501
        :type address: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def patch(self):
        """Gets the patch of this V1CreateHookParameters.  # noqa: E501

        Patch  # noqa: E501

        :return: The patch of this V1CreateHookParameters.  # noqa: E501
        :rtype: str
        """
        return self._patch

    @patch.setter
    def patch(self, patch):
        """Sets the patch of this V1CreateHookParameters.

        Patch  # noqa: E501

        :param patch: The patch of this V1CreateHookParameters.  # noqa: E501
        :type patch: str
        """
        if self.local_vars_configuration.client_side_validation and patch is None:  # noqa: E501
            raise ValueError("Invalid value for `patch`, must not be `None`")  # noqa: E501

        self._patch = patch

    @property
    def patch_type(self):
        """Gets the patch_type of this V1CreateHookParameters.  # noqa: E501

        Patch Type  # noqa: E501

        :return: The patch_type of this V1CreateHookParameters.  # noqa: E501
        :rtype: str
        """
        return self._patch_type

    @patch_type.setter
    def patch_type(self, patch_type):
        """Sets the patch_type of this V1CreateHookParameters.

        Patch Type  # noqa: E501

        :param patch_type: The patch_type of this V1CreateHookParameters.  # noqa: E501
        :type patch_type: str
        """
        if self.local_vars_configuration.client_side_validation and patch_type is None:  # noqa: E501
            raise ValueError("Invalid value for `patch_type`, must not be `None`")  # noqa: E501
        allowed_values = ["csmfcc", "csmfvm"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and patch_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `patch_type` ({0}), must be one of {1}"  # noqa: E501
                .format(patch_type, allowed_values)
            )

        self._patch_type = patch_type

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
        if not isinstance(other, V1CreateHookParameters):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1CreateHookParameters):
            return True

        return self.to_dict() != other.to_dict()
