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


class KernelThread(object):
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
        'kernel_id': 'str',
        'tid': 'int',
        'stack': 'list[str]'
    }

    attribute_map = {
        'kernel_id': 'kernelId',
        'tid': 'tid',
        'stack': 'stack'
    }

    def __init__(self, kernel_id=None, tid=None, stack=None, local_vars_configuration=None):  # noqa: E501
        """KernelThread - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._kernel_id = None
        self._tid = None
        self._stack = None
        self.discriminator = None

        self.kernel_id = kernel_id
        self.tid = tid
        self.stack = stack

    @property
    def kernel_id(self):
        """Gets the kernel_id of this KernelThread.  # noqa: E501

        Kernel Thread ID  # noqa: E501

        :return: The kernel_id of this KernelThread.  # noqa: E501
        :rtype: str
        """
        return self._kernel_id

    @kernel_id.setter
    def kernel_id(self, kernel_id):
        """Sets the kernel_id of this KernelThread.

        Kernel Thread ID  # noqa: E501

        :param kernel_id: The kernel_id of this KernelThread.  # noqa: E501
        :type kernel_id: str
        """

        self._kernel_id = kernel_id

    @property
    def tid(self):
        """Gets the tid of this KernelThread.  # noqa: E501

        Task ID  # noqa: E501

        :return: The tid of this KernelThread.  # noqa: E501
        :rtype: int
        """
        return self._tid

    @tid.setter
    def tid(self, tid):
        """Sets the tid of this KernelThread.

        Task ID  # noqa: E501

        :param tid: The tid of this KernelThread.  # noqa: E501
        :type tid: int
        """

        self._tid = tid

    @property
    def stack(self):
        """Gets the stack of this KernelThread.  # noqa: E501

        Array of stack addresses  # noqa: E501

        :return: The stack of this KernelThread.  # noqa: E501
        :rtype: list[str]
        """
        return self._stack

    @stack.setter
    def stack(self, stack):
        """Sets the stack of this KernelThread.

        Array of stack addresses  # noqa: E501

        :param stack: The stack of this KernelThread.  # noqa: E501
        :type stack: list[str]
        """

        self._stack = stack

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
        if not isinstance(other, KernelThread):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, KernelThread):
            return True

        return self.to_dict() != other.to_dict()
