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


class SubscriberInvite(object):
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
        'coupon_options': 'CouponOptions',
        'plan': 'Plan',
        'trial': 'Trial',
        'name': 'str',
        'email': 'str',
        'coupon_code': 'str',
        'domain': 'str',
        'aggregate': 'str',
        'use_by': 'str',
        'active': 'bool',
        'reusable': 'bool',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'coupon_options': 'coupon_options',
        'plan': 'plan',
        'trial': 'trial',
        'name': 'name',
        'email': 'email',
        'coupon_code': 'coupon_code',
        'domain': 'domain',
        'aggregate': 'aggregate',
        'use_by': 'use_by',
        'active': 'active',
        'reusable': 'reusable',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt'
    }

    def __init__(self, coupon_options=None, plan=None, trial=None, name=None, email=None, coupon_code=None, domain=None, aggregate=None, use_by=None, active=None, reusable=None, created_at=None, updated_at=None, local_vars_configuration=None):  # noqa: E501
        """SubscriberInvite - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._coupon_options = None
        self._plan = None
        self._trial = None
        self._name = None
        self._email = None
        self._coupon_code = None
        self._domain = None
        self._aggregate = None
        self._use_by = None
        self._active = None
        self._reusable = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if coupon_options is not None:
            self.coupon_options = coupon_options
        if plan is not None:
            self.plan = plan
        if trial is not None:
            self.trial = trial
        self.name = name
        self.email = email
        self.coupon_code = coupon_code
        self.domain = domain
        self.aggregate = aggregate
        self.use_by = use_by
        self.active = active
        self.reusable = reusable
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def coupon_options(self):
        """Gets the coupon_options of this SubscriberInvite.  # noqa: E501


        :return: The coupon_options of this SubscriberInvite.  # noqa: E501
        :rtype: CouponOptions
        """
        return self._coupon_options

    @coupon_options.setter
    def coupon_options(self, coupon_options):
        """Sets the coupon_options of this SubscriberInvite.


        :param coupon_options: The coupon_options of this SubscriberInvite.  # noqa: E501
        :type coupon_options: CouponOptions
        """

        self._coupon_options = coupon_options

    @property
    def plan(self):
        """Gets the plan of this SubscriberInvite.  # noqa: E501


        :return: The plan of this SubscriberInvite.  # noqa: E501
        :rtype: Plan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this SubscriberInvite.


        :param plan: The plan of this SubscriberInvite.  # noqa: E501
        :type plan: Plan
        """

        self._plan = plan

    @property
    def trial(self):
        """Gets the trial of this SubscriberInvite.  # noqa: E501


        :return: The trial of this SubscriberInvite.  # noqa: E501
        :rtype: Trial
        """
        return self._trial

    @trial.setter
    def trial(self, trial):
        """Sets the trial of this SubscriberInvite.


        :param trial: The trial of this SubscriberInvite.  # noqa: E501
        :type trial: Trial
        """

        self._trial = trial

    @property
    def name(self):
        """Gets the name of this SubscriberInvite.  # noqa: E501

        Name  # noqa: E501

        :return: The name of this SubscriberInvite.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriberInvite.

        Name  # noqa: E501

        :param name: The name of this SubscriberInvite.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def email(self):
        """Gets the email of this SubscriberInvite.  # noqa: E501

        Email  # noqa: E501

        :return: The email of this SubscriberInvite.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this SubscriberInvite.

        Email  # noqa: E501

        :param email: The email of this SubscriberInvite.  # noqa: E501
        :type email: str
        """

        self._email = email

    @property
    def coupon_code(self):
        """Gets the coupon_code of this SubscriberInvite.  # noqa: E501

        Coupon code  # noqa: E501

        :return: The coupon_code of this SubscriberInvite.  # noqa: E501
        :rtype: str
        """
        return self._coupon_code

    @coupon_code.setter
    def coupon_code(self, coupon_code):
        """Sets the coupon_code of this SubscriberInvite.

        Coupon code  # noqa: E501

        :param coupon_code: The coupon_code of this SubscriberInvite.  # noqa: E501
        :type coupon_code: str
        """
        if self.local_vars_configuration.client_side_validation and coupon_code is None:  # noqa: E501
            raise ValueError("Invalid value for `coupon_code`, must not be `None`")  # noqa: E501

        self._coupon_code = coupon_code

    @property
    def domain(self):
        """Gets the domain of this SubscriberInvite.  # noqa: E501

        Domain  # noqa: E501

        :return: The domain of this SubscriberInvite.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this SubscriberInvite.

        Domain  # noqa: E501

        :param domain: The domain of this SubscriberInvite.  # noqa: E501
        :type domain: str
        """

        self._domain = domain

    @property
    def aggregate(self):
        """Gets the aggregate of this SubscriberInvite.  # noqa: E501

        Aggregate  # noqa: E501

        :return: The aggregate of this SubscriberInvite.  # noqa: E501
        :rtype: str
        """
        return self._aggregate

    @aggregate.setter
    def aggregate(self, aggregate):
        """Sets the aggregate of this SubscriberInvite.

        Aggregate  # noqa: E501

        :param aggregate: The aggregate of this SubscriberInvite.  # noqa: E501
        :type aggregate: str
        """
        if self.local_vars_configuration.client_side_validation and aggregate is None:  # noqa: E501
            raise ValueError("Invalid value for `aggregate`, must not be `None`")  # noqa: E501

        self._aggregate = aggregate

    @property
    def use_by(self):
        """Gets the use_by of this SubscriberInvite.  # noqa: E501

        Used By  # noqa: E501

        :return: The use_by of this SubscriberInvite.  # noqa: E501
        :rtype: str
        """
        return self._use_by

    @use_by.setter
    def use_by(self, use_by):
        """Sets the use_by of this SubscriberInvite.

        Used By  # noqa: E501

        :param use_by: The use_by of this SubscriberInvite.  # noqa: E501
        :type use_by: str
        """

        self._use_by = use_by

    @property
    def active(self):
        """Gets the active of this SubscriberInvite.  # noqa: E501

        Is Active flag  # noqa: E501

        :return: The active of this SubscriberInvite.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this SubscriberInvite.

        Is Active flag  # noqa: E501

        :param active: The active of this SubscriberInvite.  # noqa: E501
        :type active: bool
        """
        if self.local_vars_configuration.client_side_validation and active is None:  # noqa: E501
            raise ValueError("Invalid value for `active`, must not be `None`")  # noqa: E501

        self._active = active

    @property
    def reusable(self):
        """Gets the reusable of this SubscriberInvite.  # noqa: E501

        Is reusable flag  # noqa: E501

        :return: The reusable of this SubscriberInvite.  # noqa: E501
        :rtype: bool
        """
        return self._reusable

    @reusable.setter
    def reusable(self, reusable):
        """Sets the reusable of this SubscriberInvite.

        Is reusable flag  # noqa: E501

        :param reusable: The reusable of this SubscriberInvite.  # noqa: E501
        :type reusable: bool
        """
        if self.local_vars_configuration.client_side_validation and reusable is None:  # noqa: E501
            raise ValueError("Invalid value for `reusable`, must not be `None`")  # noqa: E501

        self._reusable = reusable

    @property
    def created_at(self):
        """Gets the created_at of this SubscriberInvite.  # noqa: E501

        Created Date in ISO-8601 format e.g. 2022-05-06T02:39:23.000Z  # noqa: E501

        :return: The created_at of this SubscriberInvite.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SubscriberInvite.

        Created Date in ISO-8601 format e.g. 2022-05-06T02:39:23.000Z  # noqa: E501

        :param created_at: The created_at of this SubscriberInvite.  # noqa: E501
        :type created_at: str
        """
        if self.local_vars_configuration.client_side_validation and created_at is None:  # noqa: E501
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this SubscriberInvite.  # noqa: E501

        Updated Date in ISO-8601 format e.g. 2022-05-06T02:39:23.000Z  # noqa: E501

        :return: The updated_at of this SubscriberInvite.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SubscriberInvite.

        Updated Date in ISO-8601 format e.g. 2022-05-06T02:39:23.000Z  # noqa: E501

        :param updated_at: The updated_at of this SubscriberInvite.  # noqa: E501
        :type updated_at: str
        """
        if self.local_vars_configuration.client_side_validation and updated_at is None:  # noqa: E501
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if not isinstance(other, SubscriberInvite):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SubscriberInvite):
            return True

        return self.to_dict() != other.to_dict()
