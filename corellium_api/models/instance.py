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


class Instance(object):
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
        'key': 'str',
        'flavor': 'str',
        'type': 'str',
        'project': 'str',
        'state': 'InstanceState',
        'state_changed': 'datetime',
        'started_at': 'str',
        'user_task': 'str',
        'task_state': 'str',
        'error': 'str',
        'boot_options': 'InstanceBootOptions',
        'service_ip': 'str',
        'wifi_ip': 'str',
        'secondary_ip': 'str',
        'services': 'InstanceServices',
        'panicked': 'bool',
        'created': 'datetime',
        'model': 'str',
        'fwpackage': 'str',
        'os': 'str',
        'agent': 'InstanceAgentState',
        'netmon': 'InstanceNetmonState',
        'expose_port': 'str',
        'fault': 'bool',
        'patches': 'list[str]',
        'created_by': 'CreatedBy'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'key': 'key',
        'flavor': 'flavor',
        'type': 'type',
        'project': 'project',
        'state': 'state',
        'state_changed': 'stateChanged',
        'started_at': 'startedAt',
        'user_task': 'userTask',
        'task_state': 'taskState',
        'error': 'error',
        'boot_options': 'bootOptions',
        'service_ip': 'serviceIp',
        'wifi_ip': 'wifiIp',
        'secondary_ip': 'secondaryIp',
        'services': 'services',
        'panicked': 'panicked',
        'created': 'created',
        'model': 'model',
        'fwpackage': 'fwpackage',
        'os': 'os',
        'agent': 'agent',
        'netmon': 'netmon',
        'expose_port': 'exposePort',
        'fault': 'fault',
        'patches': 'patches',
        'created_by': 'createdBy'
    }

    def __init__(self, id=None, name=None, key=None, flavor=None, type=None, project=None, state=None, state_changed=None, started_at=None, user_task=None, task_state=None, error=None, boot_options=None, service_ip=None, wifi_ip=None, secondary_ip=None, services=None, panicked=None, created=None, model=None, fwpackage=None, os=None, agent=None, netmon=None, expose_port=None, fault=None, patches=None, created_by=None, local_vars_configuration=None):  # noqa: E501
        """Instance - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._key = None
        self._flavor = None
        self._type = None
        self._project = None
        self._state = None
        self._state_changed = None
        self._started_at = None
        self._user_task = None
        self._task_state = None
        self._error = None
        self._boot_options = None
        self._service_ip = None
        self._wifi_ip = None
        self._secondary_ip = None
        self._services = None
        self._panicked = None
        self._created = None
        self._model = None
        self._fwpackage = None
        self._os = None
        self._agent = None
        self._netmon = None
        self._expose_port = None
        self._fault = None
        self._patches = None
        self._created_by = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.key = key
        self.flavor = flavor
        self.type = type
        self.project = project
        if state is not None:
            self.state = state
        self.state_changed = state_changed
        self.started_at = started_at
        self.user_task = user_task
        self.task_state = task_state
        self.error = error
        if boot_options is not None:
            self.boot_options = boot_options
        self.service_ip = service_ip
        self.wifi_ip = wifi_ip
        self.secondary_ip = secondary_ip
        if services is not None:
            self.services = services
        self.panicked = panicked
        self.created = created
        self.model = model
        self.fwpackage = fwpackage
        self.os = os
        self.agent = agent
        self.netmon = netmon
        self.expose_port = expose_port
        self.fault = fault
        self.patches = patches
        if created_by is not None:
            self.created_by = created_by

    @property
    def id(self):
        """Gets the id of this Instance.  # noqa: E501

        Instance Identifier  # noqa: E501

        :return: The id of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Instance.

        Instance Identifier  # noqa: E501

        :param id: The id of this Instance.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Instance.  # noqa: E501

        Instance Name  # noqa: E501

        :return: The name of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Instance.

        Instance Name  # noqa: E501

        :param name: The name of this Instance.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def key(self):
        """Gets the key of this Instance.  # noqa: E501

        Key used to encrypt the Instance  # noqa: E501

        :return: The key of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Instance.

        Key used to encrypt the Instance  # noqa: E501

        :param key: The key of this Instance.  # noqa: E501
        :type key: str
        """

        self._key = key

    @property
    def flavor(self):
        """Gets the flavor of this Instance.  # noqa: E501

        The type of virtual machine this is  # noqa: E501

        :return: The flavor of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        """Sets the flavor of this Instance.

        The type of virtual machine this is  # noqa: E501

        :param flavor: The flavor of this Instance.  # noqa: E501
        :type flavor: str
        """

        self._flavor = flavor

    @property
    def type(self):
        """Gets the type of this Instance.  # noqa: E501

          # noqa: E501

        :return: The type of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Instance.

          # noqa: E501

        :param type: The type of this Instance.  # noqa: E501
        :type type: str
        """

        self._type = type

    @property
    def project(self):
        """Gets the project of this Instance.  # noqa: E501

        The projectId of the project this instance belongs to  # noqa: E501

        :return: The project of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Instance.

        The projectId of the project this instance belongs to  # noqa: E501

        :param project: The project of this Instance.  # noqa: E501
        :type project: str
        """

        self._project = project

    @property
    def state(self):
        """Gets the state of this Instance.  # noqa: E501


        :return: The state of this Instance.  # noqa: E501
        :rtype: InstanceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Instance.


        :param state: The state of this Instance.  # noqa: E501
        :type state: InstanceState
        """

        self._state = state

    @property
    def state_changed(self):
        """Gets the state_changed of this Instance.  # noqa: E501

        Time the state of the instance last changed  # noqa: E501

        :return: The state_changed of this Instance.  # noqa: E501
        :rtype: datetime
        """
        return self._state_changed

    @state_changed.setter
    def state_changed(self, state_changed):
        """Sets the state_changed of this Instance.

        Time the state of the instance last changed  # noqa: E501

        :param state_changed: The state_changed of this Instance.  # noqa: E501
        :type state_changed: datetime
        """

        self._state_changed = state_changed

    @property
    def started_at(self):
        """Gets the started_at of this Instance.  # noqa: E501

        Time the instance was started  # noqa: E501

        :return: The started_at of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this Instance.

        Time the instance was started  # noqa: E501

        :param started_at: The started_at of this Instance.  # noqa: E501
        :type started_at: str
        """

        self._started_at = started_at

    @property
    def user_task(self):
        """Gets the user_task of this Instance.  # noqa: E501

        Currently executing User Task  # noqa: E501

        :return: The user_task of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._user_task

    @user_task.setter
    def user_task(self, user_task):
        """Sets the user_task of this Instance.

        Currently executing User Task  # noqa: E501

        :param user_task: The user_task of this Instance.  # noqa: E501
        :type user_task: str
        """

        self._user_task = user_task

    @property
    def task_state(self):
        """Gets the task_state of this Instance.  # noqa: E501

        Current task state if any  # noqa: E501

        :return: The task_state of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._task_state

    @task_state.setter
    def task_state(self, task_state):
        """Sets the task_state of this Instance.

        Current task state if any  # noqa: E501

        :param task_state: The task_state of this Instance.  # noqa: E501
        :type task_state: str
        """

        self._task_state = task_state

    @property
    def error(self):
        """Gets the error of this Instance.  # noqa: E501

        Current error state if any  # noqa: E501

        :return: The error of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this Instance.

        Current error state if any  # noqa: E501

        :param error: The error of this Instance.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def boot_options(self):
        """Gets the boot_options of this Instance.  # noqa: E501


        :return: The boot_options of this Instance.  # noqa: E501
        :rtype: InstanceBootOptions
        """
        return self._boot_options

    @boot_options.setter
    def boot_options(self, boot_options):
        """Sets the boot_options of this Instance.


        :param boot_options: The boot_options of this Instance.  # noqa: E501
        :type boot_options: InstanceBootOptions
        """

        self._boot_options = boot_options

    @property
    def service_ip(self):
        """Gets the service_ip of this Instance.  # noqa: E501

        Services IP Address  # noqa: E501

        :return: The service_ip of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._service_ip

    @service_ip.setter
    def service_ip(self, service_ip):
        """Sets the service_ip of this Instance.

        Services IP Address  # noqa: E501

        :param service_ip: The service_ip of this Instance.  # noqa: E501
        :type service_ip: str
        """

        self._service_ip = service_ip

    @property
    def wifi_ip(self):
        """Gets the wifi_ip of this Instance.  # noqa: E501

        LAN IP Address  # noqa: E501

        :return: The wifi_ip of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._wifi_ip

    @wifi_ip.setter
    def wifi_ip(self, wifi_ip):
        """Sets the wifi_ip of this Instance.

        LAN IP Address  # noqa: E501

        :param wifi_ip: The wifi_ip of this Instance.  # noqa: E501
        :type wifi_ip: str
        """

        self._wifi_ip = wifi_ip

    @property
    def secondary_ip(self):
        """Gets the secondary_ip of this Instance.  # noqa: E501

        Secondary Inteface LAN IP Address (if supported)  # noqa: E501

        :return: The secondary_ip of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._secondary_ip

    @secondary_ip.setter
    def secondary_ip(self, secondary_ip):
        """Sets the secondary_ip of this Instance.

        Secondary Inteface LAN IP Address (if supported)  # noqa: E501

        :param secondary_ip: The secondary_ip of this Instance.  # noqa: E501
        :type secondary_ip: str
        """

        self._secondary_ip = secondary_ip

    @property
    def services(self):
        """Gets the services of this Instance.  # noqa: E501


        :return: The services of this Instance.  # noqa: E501
        :rtype: InstanceServices
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Instance.


        :param services: The services of this Instance.  # noqa: E501
        :type services: InstanceServices
        """

        self._services = services

    @property
    def panicked(self):
        """Gets the panicked of this Instance.  # noqa: E501

          # noqa: E501

        :return: The panicked of this Instance.  # noqa: E501
        :rtype: bool
        """
        return self._panicked

    @panicked.setter
    def panicked(self, panicked):
        """Sets the panicked of this Instance.

          # noqa: E501

        :param panicked: The panicked of this Instance.  # noqa: E501
        :type panicked: bool
        """

        self._panicked = panicked

    @property
    def created(self):
        """Gets the created of this Instance.  # noqa: E501

        Time instance was created  # noqa: E501

        :return: The created of this Instance.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this Instance.

        Time instance was created  # noqa: E501

        :param created: The created of this Instance.  # noqa: E501
        :type created: datetime
        """

        self._created = created

    @property
    def model(self):
        """Gets the model of this Instance.  # noqa: E501

        Model of virtual machine device  # noqa: E501

        :return: The model of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this Instance.

        Model of virtual machine device  # noqa: E501

        :param model: The model of this Instance.  # noqa: E501
        :type model: str
        """

        self._model = model

    @property
    def fwpackage(self):
        """Gets the fwpackage of this Instance.  # noqa: E501

        URL that package used to create this instance is available at  # noqa: E501

        :return: The fwpackage of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._fwpackage

    @fwpackage.setter
    def fwpackage(self, fwpackage):
        """Sets the fwpackage of this Instance.

        URL that package used to create this instance is available at  # noqa: E501

        :param fwpackage: The fwpackage of this Instance.  # noqa: E501
        :type fwpackage: str
        """

        self._fwpackage = fwpackage

    @property
    def os(self):
        """Gets the os of this Instance.  # noqa: E501

          # noqa: E501

        :return: The os of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this Instance.

          # noqa: E501

        :param os: The os of this Instance.  # noqa: E501
        :type os: str
        """

        self._os = os

    @property
    def agent(self):
        """Gets the agent of this Instance.  # noqa: E501


        :return: The agent of this Instance.  # noqa: E501
        :rtype: InstanceAgentState
        """
        return self._agent

    @agent.setter
    def agent(self, agent):
        """Sets the agent of this Instance.


        :param agent: The agent of this Instance.  # noqa: E501
        :type agent: InstanceAgentState
        """

        self._agent = agent

    @property
    def netmon(self):
        """Gets the netmon of this Instance.  # noqa: E501


        :return: The netmon of this Instance.  # noqa: E501
        :rtype: InstanceNetmonState
        """
        return self._netmon

    @netmon.setter
    def netmon(self, netmon):
        """Sets the netmon of this Instance.


        :param netmon: The netmon of this Instance.  # noqa: E501
        :type netmon: InstanceNetmonState
        """

        self._netmon = netmon

    @property
    def expose_port(self):
        """Gets the expose_port of this Instance.  # noqa: E501

          # noqa: E501

        :return: The expose_port of this Instance.  # noqa: E501
        :rtype: str
        """
        return self._expose_port

    @expose_port.setter
    def expose_port(self, expose_port):
        """Sets the expose_port of this Instance.

          # noqa: E501

        :param expose_port: The expose_port of this Instance.  # noqa: E501
        :type expose_port: str
        """

        self._expose_port = expose_port

    @property
    def fault(self):
        """Gets the fault of this Instance.  # noqa: E501

          # noqa: E501

        :return: The fault of this Instance.  # noqa: E501
        :rtype: bool
        """
        return self._fault

    @fault.setter
    def fault(self, fault):
        """Sets the fault of this Instance.

          # noqa: E501

        :param fault: The fault of this Instance.  # noqa: E501
        :type fault: bool
        """

        self._fault = fault

    @property
    def patches(self):
        """Gets the patches of this Instance.  # noqa: E501

          # noqa: E501

        :return: The patches of this Instance.  # noqa: E501
        :rtype: list[str]
        """
        return self._patches

    @patches.setter
    def patches(self, patches):
        """Sets the patches of this Instance.

          # noqa: E501

        :param patches: The patches of this Instance.  # noqa: E501
        :type patches: list[str]
        """

        self._patches = patches

    @property
    def created_by(self):
        """Gets the created_by of this Instance.  # noqa: E501


        :return: The created_by of this Instance.  # noqa: E501
        :rtype: CreatedBy
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Instance.


        :param created_by: The created_by of this Instance.  # noqa: E501
        :type created_by: CreatedBy
        """

        self._created_by = created_by

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
        if not isinstance(other, Instance):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Instance):
            return True

        return self.to_dict() != other.to_dict()
