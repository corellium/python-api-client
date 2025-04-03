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


class NetworkConnectionProviderOffsetPaginationResult(object):
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
        'total': 'float',
        'count': 'float',
        'limit': 'float',
        'offset': 'float',
        'results': 'list[NetworkConnectionProvider]'
    }

    attribute_map = {
        'total': 'total',
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset',
        'results': 'results'
    }

    def __init__(self, total=None, count=None, limit=None, offset=None, results=None, local_vars_configuration=None):  # noqa: E501
        """NetworkConnectionProviderOffsetPaginationResult - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._total = None
        self._count = None
        self._limit = None
        self._offset = None
        self._results = None
        self.discriminator = None

        self.total = total
        self.count = count
        self.limit = limit
        self.offset = offset
        self.results = results

    @property
    def total(self):
        """Gets the total of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501

        Total number of items.  # noqa: E501

        :return: The total of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this NetworkConnectionProviderOffsetPaginationResult.

        Total number of items.  # noqa: E501

        :param total: The total of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :type total: float
        """
        if self.local_vars_configuration.client_side_validation and total is None:  # noqa: E501
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

    @property
    def count(self):
        """Gets the count of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501

        The number of items returned in this result.  # noqa: E501

        :return: The count of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this NetworkConnectionProviderOffsetPaginationResult.

        The number of items returned in this result.  # noqa: E501

        :param count: The count of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :type count: float
        """
        if self.local_vars_configuration.client_side_validation and count is None:  # noqa: E501
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def limit(self):
        """Gets the limit of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501

        The maximum number of items that could be returned for this result.  # noqa: E501

        :return: The limit of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :rtype: float
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this NetworkConnectionProviderOffsetPaginationResult.

        The maximum number of items that could be returned for this result.  # noqa: E501

        :param limit: The limit of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :type limit: float
        """
        if self.local_vars_configuration.client_side_validation and limit is None:  # noqa: E501
            raise ValueError("Invalid value for `limit`, must not be `None`")  # noqa: E501

        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501

        That starting item 0-indexed.  # noqa: E501

        :return: The offset of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :rtype: float
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this NetworkConnectionProviderOffsetPaginationResult.

        That starting item 0-indexed.  # noqa: E501

        :param offset: The offset of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :type offset: float
        """
        if self.local_vars_configuration.client_side_validation and offset is None:  # noqa: E501
            raise ValueError("Invalid value for `offset`, must not be `None`")  # noqa: E501

        self._offset = offset

    @property
    def results(self):
        """Gets the results of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501

        Array of network connection providers.  # noqa: E501

        :return: The results of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :rtype: list[NetworkConnectionProvider]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this NetworkConnectionProviderOffsetPaginationResult.

        Array of network connection providers.  # noqa: E501

        :param results: The results of this NetworkConnectionProviderOffsetPaginationResult.  # noqa: E501
        :type results: list[NetworkConnectionProvider]
        """
        if self.local_vars_configuration.client_side_validation and results is None:  # noqa: E501
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results

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
        if not isinstance(other, NetworkConnectionProviderOffsetPaginationResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NetworkConnectionProviderOffsetPaginationResult):
            return True

        return self.to_dict() != other.to_dict()
