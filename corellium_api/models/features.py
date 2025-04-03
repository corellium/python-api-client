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


class Features(object):
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
        'apps': 'bool',
        'connect': 'bool',
        'console': 'bool',
        'coretrace': 'bool',
        'device_control': 'bool',
        'device_delete': 'bool',
        'files': 'bool',
        'frida': 'bool',
        'images': 'bool',
        'messaging': 'bool',
        'netmon': 'bool',
        'network': 'bool',
        'port_forwarding': 'bool',
        'power_management': 'bool',
        'profile': 'bool',
        'sensors': 'bool',
        'settings': 'bool',
        'snapshots': 'bool',
        'strace': 'bool',
        'system': 'bool'
    }

    attribute_map = {
        'apps': 'apps',
        'connect': 'connect',
        'console': 'console',
        'coretrace': 'coretrace',
        'device_control': 'deviceControl',
        'device_delete': 'deviceDelete',
        'files': 'files',
        'frida': 'frida',
        'images': 'images',
        'messaging': 'messaging',
        'netmon': 'netmon',
        'network': 'network',
        'port_forwarding': 'portForwarding',
        'power_management': 'powerManagement',
        'profile': 'profile',
        'sensors': 'sensors',
        'settings': 'settings',
        'snapshots': 'snapshots',
        'strace': 'strace',
        'system': 'system'
    }

    def __init__(self, apps=None, connect=None, console=None, coretrace=None, device_control=None, device_delete=None, files=None, frida=None, images=None, messaging=None, netmon=None, network=None, port_forwarding=None, power_management=None, profile=None, sensors=None, settings=None, snapshots=None, strace=None, system=None, local_vars_configuration=None):  # noqa: E501
        """Features - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._apps = None
        self._connect = None
        self._console = None
        self._coretrace = None
        self._device_control = None
        self._device_delete = None
        self._files = None
        self._frida = None
        self._images = None
        self._messaging = None
        self._netmon = None
        self._network = None
        self._port_forwarding = None
        self._power_management = None
        self._profile = None
        self._sensors = None
        self._settings = None
        self._snapshots = None
        self._strace = None
        self._system = None
        self.discriminator = None

        self.apps = apps
        self.connect = connect
        self.console = console
        self.coretrace = coretrace
        self.device_control = device_control
        self.device_delete = device_delete
        self.files = files
        self.frida = frida
        self.images = images
        self.messaging = messaging
        self.netmon = netmon
        self.network = network
        self.port_forwarding = port_forwarding
        self.power_management = power_management
        self.profile = profile
        self.sensors = sensors
        self.settings = settings
        self.snapshots = snapshots
        self.strace = strace
        self.system = system

    @property
    def apps(self):
        """Gets the apps of this Features.  # noqa: E501

          # noqa: E501

        :return: The apps of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this Features.

          # noqa: E501

        :param apps: The apps of this Features.  # noqa: E501
        :type apps: bool
        """

        self._apps = apps

    @property
    def connect(self):
        """Gets the connect of this Features.  # noqa: E501

          # noqa: E501

        :return: The connect of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._connect

    @connect.setter
    def connect(self, connect):
        """Sets the connect of this Features.

          # noqa: E501

        :param connect: The connect of this Features.  # noqa: E501
        :type connect: bool
        """

        self._connect = connect

    @property
    def console(self):
        """Gets the console of this Features.  # noqa: E501

          # noqa: E501

        :return: The console of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._console

    @console.setter
    def console(self, console):
        """Sets the console of this Features.

          # noqa: E501

        :param console: The console of this Features.  # noqa: E501
        :type console: bool
        """

        self._console = console

    @property
    def coretrace(self):
        """Gets the coretrace of this Features.  # noqa: E501

          # noqa: E501

        :return: The coretrace of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._coretrace

    @coretrace.setter
    def coretrace(self, coretrace):
        """Sets the coretrace of this Features.

          # noqa: E501

        :param coretrace: The coretrace of this Features.  # noqa: E501
        :type coretrace: bool
        """

        self._coretrace = coretrace

    @property
    def device_control(self):
        """Gets the device_control of this Features.  # noqa: E501

          # noqa: E501

        :return: The device_control of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._device_control

    @device_control.setter
    def device_control(self, device_control):
        """Sets the device_control of this Features.

          # noqa: E501

        :param device_control: The device_control of this Features.  # noqa: E501
        :type device_control: bool
        """

        self._device_control = device_control

    @property
    def device_delete(self):
        """Gets the device_delete of this Features.  # noqa: E501

          # noqa: E501

        :return: The device_delete of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._device_delete

    @device_delete.setter
    def device_delete(self, device_delete):
        """Sets the device_delete of this Features.

          # noqa: E501

        :param device_delete: The device_delete of this Features.  # noqa: E501
        :type device_delete: bool
        """

        self._device_delete = device_delete

    @property
    def files(self):
        """Gets the files of this Features.  # noqa: E501

          # noqa: E501

        :return: The files of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this Features.

          # noqa: E501

        :param files: The files of this Features.  # noqa: E501
        :type files: bool
        """

        self._files = files

    @property
    def frida(self):
        """Gets the frida of this Features.  # noqa: E501

          # noqa: E501

        :return: The frida of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._frida

    @frida.setter
    def frida(self, frida):
        """Sets the frida of this Features.

          # noqa: E501

        :param frida: The frida of this Features.  # noqa: E501
        :type frida: bool
        """

        self._frida = frida

    @property
    def images(self):
        """Gets the images of this Features.  # noqa: E501

          # noqa: E501

        :return: The images of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Features.

          # noqa: E501

        :param images: The images of this Features.  # noqa: E501
        :type images: bool
        """

        self._images = images

    @property
    def messaging(self):
        """Gets the messaging of this Features.  # noqa: E501

          # noqa: E501

        :return: The messaging of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._messaging

    @messaging.setter
    def messaging(self, messaging):
        """Sets the messaging of this Features.

          # noqa: E501

        :param messaging: The messaging of this Features.  # noqa: E501
        :type messaging: bool
        """

        self._messaging = messaging

    @property
    def netmon(self):
        """Gets the netmon of this Features.  # noqa: E501

          # noqa: E501

        :return: The netmon of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._netmon

    @netmon.setter
    def netmon(self, netmon):
        """Sets the netmon of this Features.

          # noqa: E501

        :param netmon: The netmon of this Features.  # noqa: E501
        :type netmon: bool
        """

        self._netmon = netmon

    @property
    def network(self):
        """Gets the network of this Features.  # noqa: E501

          # noqa: E501

        :return: The network of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this Features.

          # noqa: E501

        :param network: The network of this Features.  # noqa: E501
        :type network: bool
        """

        self._network = network

    @property
    def port_forwarding(self):
        """Gets the port_forwarding of this Features.  # noqa: E501

          # noqa: E501

        :return: The port_forwarding of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._port_forwarding

    @port_forwarding.setter
    def port_forwarding(self, port_forwarding):
        """Sets the port_forwarding of this Features.

          # noqa: E501

        :param port_forwarding: The port_forwarding of this Features.  # noqa: E501
        :type port_forwarding: bool
        """

        self._port_forwarding = port_forwarding

    @property
    def power_management(self):
        """Gets the power_management of this Features.  # noqa: E501

          # noqa: E501

        :return: The power_management of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._power_management

    @power_management.setter
    def power_management(self, power_management):
        """Sets the power_management of this Features.

          # noqa: E501

        :param power_management: The power_management of this Features.  # noqa: E501
        :type power_management: bool
        """

        self._power_management = power_management

    @property
    def profile(self):
        """Gets the profile of this Features.  # noqa: E501

          # noqa: E501

        :return: The profile of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Features.

          # noqa: E501

        :param profile: The profile of this Features.  # noqa: E501
        :type profile: bool
        """

        self._profile = profile

    @property
    def sensors(self):
        """Gets the sensors of this Features.  # noqa: E501

          # noqa: E501

        :return: The sensors of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._sensors

    @sensors.setter
    def sensors(self, sensors):
        """Sets the sensors of this Features.

          # noqa: E501

        :param sensors: The sensors of this Features.  # noqa: E501
        :type sensors: bool
        """

        self._sensors = sensors

    @property
    def settings(self):
        """Gets the settings of this Features.  # noqa: E501

          # noqa: E501

        :return: The settings of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Features.

          # noqa: E501

        :param settings: The settings of this Features.  # noqa: E501
        :type settings: bool
        """

        self._settings = settings

    @property
    def snapshots(self):
        """Gets the snapshots of this Features.  # noqa: E501

          # noqa: E501

        :return: The snapshots of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._snapshots

    @snapshots.setter
    def snapshots(self, snapshots):
        """Sets the snapshots of this Features.

          # noqa: E501

        :param snapshots: The snapshots of this Features.  # noqa: E501
        :type snapshots: bool
        """

        self._snapshots = snapshots

    @property
    def strace(self):
        """Gets the strace of this Features.  # noqa: E501

          # noqa: E501

        :return: The strace of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._strace

    @strace.setter
    def strace(self, strace):
        """Sets the strace of this Features.

          # noqa: E501

        :param strace: The strace of this Features.  # noqa: E501
        :type strace: bool
        """

        self._strace = strace

    @property
    def system(self):
        """Gets the system of this Features.  # noqa: E501

          # noqa: E501

        :return: The system of this Features.  # noqa: E501
        :rtype: bool
        """
        return self._system

    @system.setter
    def system(self, system):
        """Sets the system of this Features.

          # noqa: E501

        :param system: The system of this Features.  # noqa: E501
        :type system: bool
        """

        self._system = system

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
        if not isinstance(other, Features):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Features):
            return True

        return self.to_dict() != other.to_dict()
