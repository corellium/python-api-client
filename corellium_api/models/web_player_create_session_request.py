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


class WebPlayerCreateSessionRequest(object):
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
        'project_id': 'str',
        'instance_id': 'str',
        'expires_in': 'float',
        'features': 'Features',
        'client_id': 'str'
    }

    attribute_map = {
        'project_id': 'projectId',
        'instance_id': 'instanceId',
        'expires_in': 'expiresIn',
        'features': 'features',
        'client_id': 'clientId'
    }

    def __init__(self, project_id=None, instance_id=None, expires_in=None, features=None, client_id=None, local_vars_configuration=None):  # noqa: E501
        """WebPlayerCreateSessionRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._project_id = None
        self._instance_id = None
        self._expires_in = None
        self._features = None
        self._client_id = None
        self.discriminator = None

        self.project_id = project_id
        self.instance_id = instance_id
        self.expires_in = expires_in
        self.features = features
        self.client_id = client_id

    @property
    def project_id(self):
        """Gets the project_id of this WebPlayerCreateSessionRequest.  # noqa: E501

        Project Identifier  # noqa: E501

        :return: The project_id of this WebPlayerCreateSessionRequest.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this WebPlayerCreateSessionRequest.

        Project Identifier  # noqa: E501

        :param project_id: The project_id of this WebPlayerCreateSessionRequest.  # noqa: E501
        :type project_id: str
        """
        if self.local_vars_configuration.client_side_validation and project_id is None:  # noqa: E501
            raise ValueError("Invalid value for `project_id`, must not be `None`")  # noqa: E501

        self._project_id = project_id

    @property
    def instance_id(self):
        """Gets the instance_id of this WebPlayerCreateSessionRequest.  # noqa: E501

        VM Instance Identifier  # noqa: E501

        :return: The instance_id of this WebPlayerCreateSessionRequest.  # noqa: E501
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this WebPlayerCreateSessionRequest.

        VM Instance Identifier  # noqa: E501

        :param instance_id: The instance_id of this WebPlayerCreateSessionRequest.  # noqa: E501
        :type instance_id: str
        """
        if self.local_vars_configuration.client_side_validation and instance_id is None:  # noqa: E501
            raise ValueError("Invalid value for `instance_id`, must not be `None`")  # noqa: E501

        self._instance_id = instance_id

    @property
    def expires_in(self):
        """Gets the expires_in of this WebPlayerCreateSessionRequest.  # noqa: E501

        Number of seconds token remains valid  # noqa: E501

        :return: The expires_in of this WebPlayerCreateSessionRequest.  # noqa: E501
        :rtype: float
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this WebPlayerCreateSessionRequest.

        Number of seconds token remains valid  # noqa: E501

        :param expires_in: The expires_in of this WebPlayerCreateSessionRequest.  # noqa: E501
        :type expires_in: float
        """
        if self.local_vars_configuration.client_side_validation and expires_in is None:  # noqa: E501
            raise ValueError("Invalid value for `expires_in`, must not be `None`")  # noqa: E501

        self._expires_in = expires_in

    @property
    def features(self):
        """Gets the features of this WebPlayerCreateSessionRequest.  # noqa: E501


        :return: The features of this WebPlayerCreateSessionRequest.  # noqa: E501
        :rtype: Features
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this WebPlayerCreateSessionRequest.


        :param features: The features of this WebPlayerCreateSessionRequest.  # noqa: E501
        :type features: Features
        """
        if self.local_vars_configuration.client_side_validation and features is None:  # noqa: E501
            raise ValueError("Invalid value for `features`, must not be `None`")  # noqa: E501

        self._features = features

    @property
    def client_id(self):
        """Gets the client_id of this WebPlayerCreateSessionRequest.  # noqa: E501

        Optional string value supplied by client for tracking purposes  # noqa: E501

        :return: The client_id of this WebPlayerCreateSessionRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this WebPlayerCreateSessionRequest.

        Optional string value supplied by client for tracking purposes  # noqa: E501

        :param client_id: The client_id of this WebPlayerCreateSessionRequest.  # noqa: E501
        :type client_id: str
        """

        self._client_id = client_id

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
        if not isinstance(other, WebPlayerCreateSessionRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WebPlayerCreateSessionRequest):
            return True

        return self.to_dict() != other.to_dict()
