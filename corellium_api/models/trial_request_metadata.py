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


class TrialRequestMetadata(object):
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
        'name': 'str',
        'company': 'str',
        'malware': 'bool',
        'research': 'bool',
        'pentest': 'bool',
        'other': 'str'
    }

    attribute_map = {
        'name': 'name',
        'company': 'company',
        'malware': 'malware',
        'research': 'research',
        'pentest': 'pentest',
        'other': 'other'
    }

    def __init__(self, name=None, company=None, malware=None, research=None, pentest=None, other=None, local_vars_configuration=None):  # noqa: E501
        """TrialRequestMetadata - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._company = None
        self._malware = None
        self._research = None
        self._pentest = None
        self._other = None
        self.discriminator = None

        self.name = name
        self.company = company
        self.malware = malware
        self.research = research
        self.pentest = pentest
        self.other = other

    @property
    def name(self):
        """Gets the name of this TrialRequestMetadata.  # noqa: E501


        :return: The name of this TrialRequestMetadata.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TrialRequestMetadata.


        :param name: The name of this TrialRequestMetadata.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def company(self):
        """Gets the company of this TrialRequestMetadata.  # noqa: E501

        provided company name  # noqa: E501

        :return: The company of this TrialRequestMetadata.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this TrialRequestMetadata.

        provided company name  # noqa: E501

        :param company: The company of this TrialRequestMetadata.  # noqa: E501
        :type company: str
        """

        self._company = company

    @property
    def malware(self):
        """Gets the malware of this TrialRequestMetadata.  # noqa: E501

        option from sign up form, interesting using for malware  # noqa: E501

        :return: The malware of this TrialRequestMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._malware

    @malware.setter
    def malware(self, malware):
        """Sets the malware of this TrialRequestMetadata.

        option from sign up form, interesting using for malware  # noqa: E501

        :param malware: The malware of this TrialRequestMetadata.  # noqa: E501
        :type malware: bool
        """

        self._malware = malware

    @property
    def research(self):
        """Gets the research of this TrialRequestMetadata.  # noqa: E501

        option from sign up form, interesting using for research  # noqa: E501

        :return: The research of this TrialRequestMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._research

    @research.setter
    def research(self, research):
        """Sets the research of this TrialRequestMetadata.

        option from sign up form, interesting using for research  # noqa: E501

        :param research: The research of this TrialRequestMetadata.  # noqa: E501
        :type research: bool
        """

        self._research = research

    @property
    def pentest(self):
        """Gets the pentest of this TrialRequestMetadata.  # noqa: E501

        option from sign up form, interesting using for pentesting  # noqa: E501

        :return: The pentest of this TrialRequestMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._pentest

    @pentest.setter
    def pentest(self, pentest):
        """Sets the pentest of this TrialRequestMetadata.

        option from sign up form, interesting using for pentesting  # noqa: E501

        :param pentest: The pentest of this TrialRequestMetadata.  # noqa: E501
        :type pentest: bool
        """

        self._pentest = pentest

    @property
    def other(self):
        """Gets the other of this TrialRequestMetadata.  # noqa: E501

        option from sign up form, interesting using for other area added here  # noqa: E501

        :return: The other of this TrialRequestMetadata.  # noqa: E501
        :rtype: str
        """
        return self._other

    @other.setter
    def other(self, other):
        """Sets the other of this TrialRequestMetadata.

        option from sign up form, interesting using for other area added here  # noqa: E501

        :param other: The other of this TrialRequestMetadata.  # noqa: E501
        :type other: str
        """

        self._other = other

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
        if not isinstance(other, TrialRequestMetadata):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TrialRequestMetadata):
            return True

        return self.to_dict() != other.to_dict()
