# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 4.2.0-6a4b86f
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import corellium_api
from corellium_api.models.hook import Hook  # noqa: E501
from corellium_api.rest import ApiException

class TestHook(unittest.TestCase):
    """Hook unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Hook
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.hook.Hook()  # noqa: E501
        if include_optional :
            return Hook(
                identifier = '', 
                label = '', 
                address = '', 
                patch = '', 
                patch_type = 'csmfcc', 
                enabled = True, 
                created_at = '', 
                updated_at = '', 
                instance_id = ''
            )
        else :
            return Hook(
        )

    def testHook(self):
        """Test Hook"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
