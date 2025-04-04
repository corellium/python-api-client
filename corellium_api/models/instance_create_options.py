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


class InstanceCreateOptions(object):
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
        'shared_snapshot': 'str',
        'shared_snapshot_password': 'str',
        'name': 'str',
        'key': 'str',
        'flavor': 'str',
        'project': 'str',
        'os': 'str',
        'osbuild': 'str',
        'patches': 'list[str]',
        'fwpackage': 'str',
        'orig_fw_package_url': 'str',
        'encrypt': 'bool',
        'wifi_mac': 'str',
        'volume': 'VolumeOptions',
        'snapshot': 'str',
        'boot_options': 'InstanceBootOptions',
        'device': 'Model'
    }

    attribute_map = {
        'shared_snapshot': 'sharedSnapshot',
        'shared_snapshot_password': 'sharedSnapshotPassword',
        'name': 'name',
        'key': 'key',
        'flavor': 'flavor',
        'project': 'project',
        'os': 'os',
        'osbuild': 'osbuild',
        'patches': 'patches',
        'fwpackage': 'fwpackage',
        'orig_fw_package_url': 'origFwPackageUrl',
        'encrypt': 'encrypt',
        'wifi_mac': 'wifiMac',
        'volume': 'volume',
        'snapshot': 'snapshot',
        'boot_options': 'bootOptions',
        'device': 'device'
    }

    def __init__(self, shared_snapshot=None, shared_snapshot_password=None, name=None, key=None, flavor=None, project=None, os=None, osbuild=None, patches=None, fwpackage=None, orig_fw_package_url=None, encrypt=None, wifi_mac=None, volume=None, snapshot=None, boot_options=None, device=None, local_vars_configuration=None):  # noqa: E501
        """InstanceCreateOptions - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._shared_snapshot = None
        self._shared_snapshot_password = None
        self._name = None
        self._key = None
        self._flavor = None
        self._project = None
        self._os = None
        self._osbuild = None
        self._patches = None
        self._fwpackage = None
        self._orig_fw_package_url = None
        self._encrypt = None
        self._wifi_mac = None
        self._volume = None
        self._snapshot = None
        self._boot_options = None
        self._device = None
        self.discriminator = None

        self.shared_snapshot = shared_snapshot
        self.shared_snapshot_password = shared_snapshot_password
        self.name = name
        self.key = key
        self.flavor = flavor
        self.project = project
        self.os = os
        self.osbuild = osbuild
        self.patches = patches
        self.fwpackage = fwpackage
        self.orig_fw_package_url = orig_fw_package_url
        self.encrypt = encrypt
        self.wifi_mac = wifi_mac
        if volume is not None:
            self.volume = volume
        self.snapshot = snapshot
        if boot_options is not None:
            self.boot_options = boot_options
        if device is not None:
            self.device = device

    @property
    def shared_snapshot(self):
        """Gets the shared_snapshot of this InstanceCreateOptions.  # noqa: E501

        identifier of the snapshot that was shared.  # noqa: E501

        :return: The shared_snapshot of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._shared_snapshot

    @shared_snapshot.setter
    def shared_snapshot(self, shared_snapshot):
        """Sets the shared_snapshot of this InstanceCreateOptions.

        identifier of the snapshot that was shared.  # noqa: E501

        :param shared_snapshot: The shared_snapshot of this InstanceCreateOptions.  # noqa: E501
        :type shared_snapshot: str
        """

        self._shared_snapshot = shared_snapshot

    @property
    def shared_snapshot_password(self):
        """Gets the shared_snapshot_password of this InstanceCreateOptions.  # noqa: E501

        optional password if the shared snapshot requires a password.  # noqa: E501

        :return: The shared_snapshot_password of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._shared_snapshot_password

    @shared_snapshot_password.setter
    def shared_snapshot_password(self, shared_snapshot_password):
        """Sets the shared_snapshot_password of this InstanceCreateOptions.

        optional password if the shared snapshot requires a password.  # noqa: E501

        :param shared_snapshot_password: The shared_snapshot_password of this InstanceCreateOptions.  # noqa: E501
        :type shared_snapshot_password: str
        """

        self._shared_snapshot_password = shared_snapshot_password

    @property
    def name(self):
        """Gets the name of this InstanceCreateOptions.  # noqa: E501

        the name of the device  # noqa: E501

        :return: The name of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceCreateOptions.

        the name of the device  # noqa: E501

        :param name: The name of this InstanceCreateOptions.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this InstanceCreateOptions.  # noqa: E501

        Key used to encrypt the Instance  # noqa: E501

        :return: The key of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this InstanceCreateOptions.

        Key used to encrypt the Instance  # noqa: E501

        :param key: The key of this InstanceCreateOptions.  # noqa: E501
        :type key: str
        """

        self._key = key

    @property
    def flavor(self):
        """Gets the flavor of this InstanceCreateOptions.  # noqa: E501

        the flavor id  # noqa: E501

        :return: The flavor of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this InstanceCreateOptions.

        the flavor id  # noqa: E501

        :param flavor: The flavor of this InstanceCreateOptions.  # noqa: E501
        :type flavor: str
        """
        if self.local_vars_configuration.client_side_validation and flavor is None:  # noqa: E501
            raise ValueError("Invalid value for `flavor`, must not be `None`")  # noqa: E501

        self._flavor = flavor

    @property
    def project(self):
        """Gets the project of this InstanceCreateOptions.  # noqa: E501

        project UUID  # noqa: E501

        :return: The project of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this InstanceCreateOptions.

        project UUID  # noqa: E501

        :param project: The project of this InstanceCreateOptions.  # noqa: E501
        :type project: str
        """
        if self.local_vars_configuration.client_side_validation and project is None:  # noqa: E501
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def os(self):
        """Gets the os of this InstanceCreateOptions.  # noqa: E501

        OS Version  # noqa: E501

        :return: The os of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this InstanceCreateOptions.

        OS Version  # noqa: E501

        :param os: The os of this InstanceCreateOptions.  # noqa: E501
        :type os: str
        """
        if self.local_vars_configuration.client_side_validation and os is None:  # noqa: E501
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def osbuild(self):
        """Gets the osbuild of this InstanceCreateOptions.  # noqa: E501

        OS Build  # noqa: E501

        :return: The osbuild of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._osbuild

    @osbuild.setter
    def osbuild(self, osbuild):
        """Sets the osbuild of this InstanceCreateOptions.

        OS Build  # noqa: E501

        :param osbuild: The osbuild of this InstanceCreateOptions.  # noqa: E501
        :type osbuild: str
        """

        self._osbuild = osbuild

    @property
    def patches(self):
        """Gets the patches of this InstanceCreateOptions.  # noqa: E501

        list of patches to apply  # noqa: E501

        :return: The patches of this InstanceCreateOptions.  # noqa: E501
        :rtype: list[str]
        """
        return self._patches

    @patches.setter
    def patches(self, patches):
        """Sets the patches of this InstanceCreateOptions.

        list of patches to apply  # noqa: E501

        :param patches: The patches of this InstanceCreateOptions.  # noqa: E501
        :type patches: list[str]
        """

        self._patches = patches

    @property
    def fwpackage(self):
        """Gets the fwpackage of this InstanceCreateOptions.  # noqa: E501

        URL or image id  # noqa: E501

        :return: The fwpackage of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._fwpackage

    @fwpackage.setter
    def fwpackage(self, fwpackage):
        """Sets the fwpackage of this InstanceCreateOptions.

        URL or image id  # noqa: E501

        :param fwpackage: The fwpackage of this InstanceCreateOptions.  # noqa: E501
        :type fwpackage: str
        """

        self._fwpackage = fwpackage

    @property
    def orig_fw_package_url(self):
        """Gets the orig_fw_package_url of this InstanceCreateOptions.  # noqa: E501

        URL that firmware package used to create this instance is available at  # noqa: E501

        :return: The orig_fw_package_url of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._orig_fw_package_url

    @orig_fw_package_url.setter
    def orig_fw_package_url(self, orig_fw_package_url):
        """Sets the orig_fw_package_url of this InstanceCreateOptions.

        URL that firmware package used to create this instance is available at  # noqa: E501

        :param orig_fw_package_url: The orig_fw_package_url of this InstanceCreateOptions.  # noqa: E501
        :type orig_fw_package_url: str
        """

        self._orig_fw_package_url = orig_fw_package_url

    @property
    def encrypt(self):
        """Gets the encrypt of this InstanceCreateOptions.  # noqa: E501

          # noqa: E501

        :return: The encrypt of this InstanceCreateOptions.  # noqa: E501
        :rtype: bool
        """
        return self._encrypt

    @encrypt.setter
    def encrypt(self, encrypt):
        """Sets the encrypt of this InstanceCreateOptions.

          # noqa: E501

        :param encrypt: The encrypt of this InstanceCreateOptions.  # noqa: E501
        :type encrypt: bool
        """

        self._encrypt = encrypt

    @property
    def wifi_mac(self):
        """Gets the wifi_mac of this InstanceCreateOptions.  # noqa: E501

          # noqa: E501

        :return: The wifi_mac of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._wifi_mac

    @wifi_mac.setter
    def wifi_mac(self, wifi_mac):
        """Sets the wifi_mac of this InstanceCreateOptions.

          # noqa: E501

        :param wifi_mac: The wifi_mac of this InstanceCreateOptions.  # noqa: E501
        :type wifi_mac: str
        """

        self._wifi_mac = wifi_mac

    @property
    def volume(self):
        """Gets the volume of this InstanceCreateOptions.  # noqa: E501


        :return: The volume of this InstanceCreateOptions.  # noqa: E501
        :rtype: VolumeOptions
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this InstanceCreateOptions.


        :param volume: The volume of this InstanceCreateOptions.  # noqa: E501
        :type volume: VolumeOptions
        """

        self._volume = volume

    @property
    def snapshot(self):
        """Gets the snapshot of this InstanceCreateOptions.  # noqa: E501

        Snapshot ID for this instance to be cloned from if defined  # noqa: E501

        :return: The snapshot of this InstanceCreateOptions.  # noqa: E501
        :rtype: str
        """
        return self._snapshot

    @snapshot.setter
    def snapshot(self, snapshot):
        """Sets the snapshot of this InstanceCreateOptions.

        Snapshot ID for this instance to be cloned from if defined  # noqa: E501

        :param snapshot: The snapshot of this InstanceCreateOptions.  # noqa: E501
        :type snapshot: str
        """

        self._snapshot = snapshot

    @property
    def boot_options(self):
        """Gets the boot_options of this InstanceCreateOptions.  # noqa: E501


        :return: The boot_options of this InstanceCreateOptions.  # noqa: E501
        :rtype: InstanceBootOptions
        """
        return self._boot_options

    @boot_options.setter
    def boot_options(self, boot_options):
        """Sets the boot_options of this InstanceCreateOptions.


        :param boot_options: The boot_options of this InstanceCreateOptions.  # noqa: E501
        :type boot_options: InstanceBootOptions
        """

        self._boot_options = boot_options

    @property
    def device(self):
        """Gets the device of this InstanceCreateOptions.  # noqa: E501


        :return: The device of this InstanceCreateOptions.  # noqa: E501
        :rtype: Model
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this InstanceCreateOptions.


        :param device: The device of this InstanceCreateOptions.  # noqa: E501
        :type device: Model
        """

        self._device = device

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
        if not isinstance(other, InstanceCreateOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, InstanceCreateOptions):
            return True

        return self.to_dict() != other.to_dict()
