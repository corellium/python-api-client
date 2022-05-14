# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.10.0-13354
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import corellium_api
from corellium_api.models.instance_return import InstanceReturn  # noqa: E501
from corellium_api.rest import ApiException

class TestInstanceReturn(unittest.TestCase):
    """InstanceReturn unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InstanceReturn
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.instance_return.InstanceReturn()  # noqa: E501
        if include_optional :
            return InstanceReturn(
                id = '', 
                state = 'on'
            )
        else :
            return InstanceReturn(
                id = '',
                state = 'on',
        )

    def testInstanceReturn(self):
        """Test InstanceReturn"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
