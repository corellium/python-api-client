# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 4.2.0-6a4b86f
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


class AgentApp(object):
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
        'tags': 'list[str]',
        'running': 'bool',
        'disk_usage': 'int',
        'date': 'int',
        'application_type': 'str',
        'name': 'str',
        'bundle_id': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'running': 'running',
        'disk_usage': 'diskUsage',
        'date': 'Date',
        'application_type': 'applicationType',
        'name': 'name',
        'bundle_id': 'bundleID'
    }

    def __init__(self, tags=None, running=None, disk_usage=None, date=None, application_type=None, name=None, bundle_id=None, local_vars_configuration=None):  # noqa: E501
        """AgentApp - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._tags = None
        self._running = None
        self._disk_usage = None
        self._date = None
        self._application_type = None
        self._name = None
        self._bundle_id = None
        self.discriminator = None

        self.tags = tags
        self.running = running
        self.disk_usage = disk_usage
        self.date = date
        self.application_type = application_type
        self.name = name
        self.bundle_id = bundle_id

    @property
    def tags(self):
        """Gets the tags of this AgentApp.  # noqa: E501

          # noqa: E501

        :return: The tags of this AgentApp.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this AgentApp.

          # noqa: E501

        :param tags: The tags of this AgentApp.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def running(self):
        """Gets the running of this AgentApp.  # noqa: E501

          # noqa: E501

        :return: The running of this AgentApp.  # noqa: E501
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this AgentApp.

          # noqa: E501

        :param running: The running of this AgentApp.  # noqa: E501
        :type running: bool
        """

        self._running = running

    @property
    def disk_usage(self):
        """Gets the disk_usage of this AgentApp.  # noqa: E501

          # noqa: E501

        :return: The disk_usage of this AgentApp.  # noqa: E501
        :rtype: int
        """
        return self._disk_usage

    @disk_usage.setter
    def disk_usage(self, disk_usage):
        """Sets the disk_usage of this AgentApp.

          # noqa: E501

        :param disk_usage: The disk_usage of this AgentApp.  # noqa: E501
        :type disk_usage: int
        """

        self._disk_usage = disk_usage

    @property
    def date(self):
        """Gets the date of this AgentApp.  # noqa: E501

          # noqa: E501

        :return: The date of this AgentApp.  # noqa: E501
        :rtype: int
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this AgentApp.

          # noqa: E501

        :param date: The date of this AgentApp.  # noqa: E501
        :type date: int
        """

        self._date = date

    @property
    def application_type(self):
        """Gets the application_type of this AgentApp.  # noqa: E501

          # noqa: E501

        :return: The application_type of this AgentApp.  # noqa: E501
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        """Sets the application_type of this AgentApp.

          # noqa: E501

        :param application_type: The application_type of this AgentApp.  # noqa: E501
        :type application_type: str
        """

        self._application_type = application_type

    @property
    def name(self):
        """Gets the name of this AgentApp.  # noqa: E501

          # noqa: E501

        :return: The name of this AgentApp.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AgentApp.

          # noqa: E501

        :param name: The name of this AgentApp.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def bundle_id(self):
        """Gets the bundle_id of this AgentApp.  # noqa: E501

          # noqa: E501

        :return: The bundle_id of this AgentApp.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this AgentApp.

          # noqa: E501

        :param bundle_id: The bundle_id of this AgentApp.  # noqa: E501
        :type bundle_id: str
        """

        self._bundle_id = bundle_id

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
        if not isinstance(other, AgentApp):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AgentApp):
            return True

        return self.to_dict() != other.to_dict()
