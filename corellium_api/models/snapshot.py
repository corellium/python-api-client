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


class Snapshot(object):
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
        'id': 'str',
        'name': 'str',
        'instance': 'str',
        'status': 'SnapshotStatus',
        'date': 'float',
        'fresh': 'bool',
        'live': 'bool',
        'local': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'instance': 'instance',
        'status': 'status',
        'date': 'date',
        'fresh': 'fresh',
        'live': 'live',
        'local': 'local'
    }

    def __init__(self, id=None, name=None, instance=None, status=None, date=None, fresh=None, live=None, local=None, local_vars_configuration=None):  # noqa: E501
        """Snapshot - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._instance = None
        self._status = None
        self._date = None
        self._fresh = None
        self._live = None
        self._local = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.instance = instance
        if status is not None:
            self.status = status
        self.date = date
        self.fresh = fresh
        self.live = live
        self.local = local

    @property
    def id(self):
        """Gets the id of this Snapshot.  # noqa: E501

        Snapshot ID  # noqa: E501

        :return: The id of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Snapshot.

        Snapshot ID  # noqa: E501

        :param id: The id of this Snapshot.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Snapshot.  # noqa: E501

        Snapshot name  # noqa: E501

        :return: The name of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Snapshot.

        Snapshot name  # noqa: E501

        :param name: The name of this Snapshot.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def instance(self):
        """Gets the instance of this Snapshot.  # noqa: E501

        Instance that this snapshot is of  # noqa: E501

        :return: The instance of this Snapshot.  # noqa: E501
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this Snapshot.

        Instance that this snapshot is of  # noqa: E501

        :param instance: The instance of this Snapshot.  # noqa: E501
        :type instance: str
        """

        self._instance = instance

    @property
    def status(self):
        """Gets the status of this Snapshot.  # noqa: E501


        :return: The status of this Snapshot.  # noqa: E501
        :rtype: SnapshotStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Snapshot.


        :param status: The status of this Snapshot.  # noqa: E501
        :type status: SnapshotStatus
        """

        self._status = status

    @property
    def date(self):
        """Gets the date of this Snapshot.  # noqa: E501

        UNIX Date that the snapshot was created  # noqa: E501

        :return: The date of this Snapshot.  # noqa: E501
        :rtype: float
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Snapshot.

        UNIX Date that the snapshot was created  # noqa: E501

        :param date: The date of this Snapshot.  # noqa: E501
        :type date: float
        """

        self._date = date

    @property
    def fresh(self):
        """Gets the fresh of this Snapshot.  # noqa: E501


        :return: The fresh of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._fresh

    @fresh.setter
    def fresh(self, fresh):
        """Sets the fresh of this Snapshot.


        :param fresh: The fresh of this Snapshot.  # noqa: E501
        :type fresh: bool
        """

        self._fresh = fresh

    @property
    def live(self):
        """Gets the live of this Snapshot.  # noqa: E501

        Live snapshot (included state and memory)  # noqa: E501

        :return: The live of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._live

    @live.setter
    def live(self, live):
        """Sets the live of this Snapshot.

        Live snapshot (included state and memory)  # noqa: E501

        :param live: The live of this Snapshot.  # noqa: E501
        :type live: bool
        """

        self._live = live

    @property
    def local(self):
        """Gets the local of this Snapshot.  # noqa: E501


        :return: The local of this Snapshot.  # noqa: E501
        :rtype: bool
        """
        return self._local

    @local.setter
    def local(self, local):
        """Sets the local of this Snapshot.


        :param local: The local of this Snapshot.  # noqa: E501
        :type local: bool
        """

        self._local = local

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
        if not isinstance(other, Snapshot):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Snapshot):
            return True

        return self.to_dict() != other.to_dict()
