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


class DomainOptions(object):
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
        'totp_required': 'bool',
        'trial_extension': 'TrialExtension',
        'snapshot_sharing_permissions': 'SnapshotSharingPermissions'
    }

    attribute_map = {
        'totp_required': 'totpRequired',
        'trial_extension': 'trialExtension',
        'snapshot_sharing_permissions': 'snapshotSharingPermissions'
    }

    def __init__(self, totp_required=None, trial_extension=None, snapshot_sharing_permissions=None, local_vars_configuration=None):  # noqa: E501
        """DomainOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._totp_required = None
        self._trial_extension = None
        self._snapshot_sharing_permissions = None
        self.discriminator = None

        self.totp_required = totp_required
        if trial_extension is not None:
            self.trial_extension = trial_extension
        if snapshot_sharing_permissions is not None:
            self.snapshot_sharing_permissions = snapshot_sharing_permissions

    @property
    def totp_required(self):
        """Gets the totp_required of this DomainOptions.  # noqa: E501

        if true, totp is required  # noqa: E501

        :return: The totp_required of this DomainOptions.  # noqa: E501
        :rtype: bool
        """
        return self._totp_required

    @totp_required.setter
    def totp_required(self, totp_required):
        """Sets the totp_required of this DomainOptions.

        if true, totp is required  # noqa: E501

        :param totp_required: The totp_required of this DomainOptions.  # noqa: E501
        :type totp_required: bool
        """

        self._totp_required = totp_required

    @property
    def trial_extension(self):
        """Gets the trial_extension of this DomainOptions.  # noqa: E501


        :return: The trial_extension of this DomainOptions.  # noqa: E501
        :rtype: TrialExtension
        """
        return self._trial_extension

    @trial_extension.setter
    def trial_extension(self, trial_extension):
        """Sets the trial_extension of this DomainOptions.


        :param trial_extension: The trial_extension of this DomainOptions.  # noqa: E501
        :type trial_extension: TrialExtension
        """

        self._trial_extension = trial_extension

    @property
    def snapshot_sharing_permissions(self):
        """Gets the snapshot_sharing_permissions of this DomainOptions.  # noqa: E501


        :return: The snapshot_sharing_permissions of this DomainOptions.  # noqa: E501
        :rtype: SnapshotSharingPermissions
        """
        return self._snapshot_sharing_permissions

    @snapshot_sharing_permissions.setter
    def snapshot_sharing_permissions(self, snapshot_sharing_permissions):
        """Sets the snapshot_sharing_permissions of this DomainOptions.


        :param snapshot_sharing_permissions: The snapshot_sharing_permissions of this DomainOptions.  # noqa: E501
        :type snapshot_sharing_permissions: SnapshotSharingPermissions
        """

        self._snapshot_sharing_permissions = snapshot_sharing_permissions

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
        if not isinstance(other, DomainOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DomainOptions):
            return True

        return self.to_dict() != other.to_dict()
