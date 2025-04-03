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


class Firmware(object):
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
        'version': 'str',
        'buildid': 'str',
        'android_flavor': 'str',
        'api_version': 'str',
        'sha256sum': 'str',
        'sha1sum': 'str',
        'md5sum': 'str',
        'size': 'float',
        'unique_id': 'str',
        'metadata': 'object',
        'releasedate': 'datetime',
        'uploaddate': 'datetime',
        'url': 'str',
        'orig_url': 'str',
        'filename': 'str'
    }

    attribute_map = {
        'version': 'version',
        'buildid': 'buildid',
        'android_flavor': 'AndroidFlavor',
        'api_version': 'APIVersion',
        'sha256sum': 'sha256sum',
        'sha1sum': 'sha1sum',
        'md5sum': 'md5sum',
        'size': 'size',
        'unique_id': 'uniqueId',
        'metadata': 'metadata',
        'releasedate': 'releasedate',
        'uploaddate': 'uploaddate',
        'url': 'url',
        'orig_url': 'orig_url',
        'filename': 'filename'
    }

    def __init__(self, version=None, buildid=None, android_flavor=None, api_version=None, sha256sum=None, sha1sum=None, md5sum=None, size=None, unique_id=None, metadata=None, releasedate=None, uploaddate=None, url=None, orig_url=None, filename=None, local_vars_configuration=None):  # noqa: E501
        """Firmware - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._version = None
        self._buildid = None
        self._android_flavor = None
        self._api_version = None
        self._sha256sum = None
        self._sha1sum = None
        self._md5sum = None
        self._size = None
        self._unique_id = None
        self._metadata = None
        self._releasedate = None
        self._uploaddate = None
        self._url = None
        self._orig_url = None
        self._filename = None
        self.discriminator = None

        self.version = version
        self.buildid = buildid
        self.android_flavor = android_flavor
        self.api_version = api_version
        self.sha256sum = sha256sum
        self.sha1sum = sha1sum
        self.md5sum = md5sum
        self.size = size
        self.unique_id = unique_id
        self.metadata = metadata
        self.releasedate = releasedate
        self.uploaddate = uploaddate
        self.url = url
        self.orig_url = orig_url
        self.filename = filename

    @property
    def version(self):
        """Gets the version of this Firmware.  # noqa: E501

          # noqa: E501

        :return: The version of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Firmware.

          # noqa: E501

        :param version: The version of this Firmware.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def buildid(self):
        """Gets the buildid of this Firmware.  # noqa: E501

          # noqa: E501

        :return: The buildid of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._buildid

    @buildid.setter
    def buildid(self, buildid):
        """Sets the buildid of this Firmware.

          # noqa: E501

        :param buildid: The buildid of this Firmware.  # noqa: E501
        :type buildid: str
        """

        self._buildid = buildid

    @property
    def android_flavor(self):
        """Gets the android_flavor of this Firmware.  # noqa: E501

        Android only flavor  # noqa: E501

        :return: The android_flavor of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._android_flavor

    @android_flavor.setter
    def android_flavor(self, android_flavor):
        """Sets the android_flavor of this Firmware.

        Android only flavor  # noqa: E501

        :param android_flavor: The android_flavor of this Firmware.  # noqa: E501
        :type android_flavor: str
        """

        self._android_flavor = android_flavor

    @property
    def api_version(self):
        """Gets the api_version of this Firmware.  # noqa: E501

        Android only API version  # noqa: E501

        :return: The api_version of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this Firmware.

        Android only API version  # noqa: E501

        :param api_version: The api_version of this Firmware.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def sha256sum(self):
        """Gets the sha256sum of this Firmware.  # noqa: E501

          # noqa: E501

        :return: The sha256sum of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._sha256sum

    @sha256sum.setter
    def sha256sum(self, sha256sum):
        """Sets the sha256sum of this Firmware.

          # noqa: E501

        :param sha256sum: The sha256sum of this Firmware.  # noqa: E501
        :type sha256sum: str
        """

        self._sha256sum = sha256sum

    @property
    def sha1sum(self):
        """Gets the sha1sum of this Firmware.  # noqa: E501

          # noqa: E501

        :return: The sha1sum of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._sha1sum

    @sha1sum.setter
    def sha1sum(self, sha1sum):
        """Sets the sha1sum of this Firmware.

          # noqa: E501

        :param sha1sum: The sha1sum of this Firmware.  # noqa: E501
        :type sha1sum: str
        """

        self._sha1sum = sha1sum

    @property
    def md5sum(self):
        """Gets the md5sum of this Firmware.  # noqa: E501

          # noqa: E501

        :return: The md5sum of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._md5sum

    @md5sum.setter
    def md5sum(self, md5sum):
        """Sets the md5sum of this Firmware.

          # noqa: E501

        :param md5sum: The md5sum of this Firmware.  # noqa: E501
        :type md5sum: str
        """

        self._md5sum = md5sum

    @property
    def size(self):
        """Gets the size of this Firmware.  # noqa: E501

          # noqa: E501

        :return: The size of this Firmware.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Firmware.

          # noqa: E501

        :param size: The size of this Firmware.  # noqa: E501
        :type size: float
        """

        self._size = size

    @property
    def unique_id(self):
        """Gets the unique_id of this Firmware.  # noqa: E501

          # noqa: E501

        :return: The unique_id of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this Firmware.

          # noqa: E501

        :param unique_id: The unique_id of this Firmware.  # noqa: E501
        :type unique_id: str
        """

        self._unique_id = unique_id

    @property
    def metadata(self):
        """Gets the metadata of this Firmware.  # noqa: E501

        Firmware metadata  # noqa: E501

        :return: The metadata of this Firmware.  # noqa: E501
        :rtype: object
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Firmware.

        Firmware metadata  # noqa: E501

        :param metadata: The metadata of this Firmware.  # noqa: E501
        :type metadata: object
        """

        self._metadata = metadata

    @property
    def releasedate(self):
        """Gets the releasedate of this Firmware.  # noqa: E501

        Release Date  # noqa: E501

        :return: The releasedate of this Firmware.  # noqa: E501
        :rtype: datetime
        """
        return self._releasedate

    @releasedate.setter
    def releasedate(self, releasedate):
        """Sets the releasedate of this Firmware.

        Release Date  # noqa: E501

        :param releasedate: The releasedate of this Firmware.  # noqa: E501
        :type releasedate: datetime
        """

        self._releasedate = releasedate

    @property
    def uploaddate(self):
        """Gets the uploaddate of this Firmware.  # noqa: E501

        Date uploaded  # noqa: E501

        :return: The uploaddate of this Firmware.  # noqa: E501
        :rtype: datetime
        """
        return self._uploaddate

    @uploaddate.setter
    def uploaddate(self, uploaddate):
        """Sets the uploaddate of this Firmware.

        Date uploaded  # noqa: E501

        :param uploaddate: The uploaddate of this Firmware.  # noqa: E501
        :type uploaddate: datetime
        """

        self._uploaddate = uploaddate

    @property
    def url(self):
        """Gets the url of this Firmware.  # noqa: E501

        URL firmware is available at  # noqa: E501

        :return: The url of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Firmware.

        URL firmware is available at  # noqa: E501

        :param url: The url of this Firmware.  # noqa: E501
        :type url: str
        """

        self._url = url

    @property
    def orig_url(self):
        """Gets the orig_url of this Firmware.  # noqa: E501

        URL firmware is available at from vendor  # noqa: E501

        :return: The orig_url of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._orig_url

    @orig_url.setter
    def orig_url(self, orig_url):
        """Sets the orig_url of this Firmware.

        URL firmware is available at from vendor  # noqa: E501

        :param orig_url: The orig_url of this Firmware.  # noqa: E501
        :type orig_url: str
        """

        self._orig_url = orig_url

    @property
    def filename(self):
        """Gets the filename of this Firmware.  # noqa: E501

          # noqa: E501

        :return: The filename of this Firmware.  # noqa: E501
        :rtype: str
        """
        return self._filename

    @filename.setter
    def filename(self, filename):
        """Sets the filename of this Firmware.

          # noqa: E501

        :param filename: The filename of this Firmware.  # noqa: E501
        :type filename: str
        """

        self._filename = filename

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
        if not isinstance(other, Firmware):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Firmware):
            return True

        return self.to_dict() != other.to_dict()
