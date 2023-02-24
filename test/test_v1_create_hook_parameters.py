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
from corellium_api.models.v1_create_hook_parameters import V1CreateHookParameters  # noqa: E501
from corellium_api.rest import ApiException

class TestV1CreateHookParameters(unittest.TestCase):
    """V1CreateHookParameters unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test V1CreateHookParameters
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.v1_create_hook_parameters.V1CreateHookParameters()  # noqa: E501
        if include_optional :
            return V1CreateHookParameters(
                label = '', 
                address = '', 
                patch = '', 
                patch_type = 'csmfcc'
            )
        else :
            return V1CreateHookParameters(
                label = '',
                address = '',
                patch = '',
                patch_type = 'csmfcc',
        )

    def testV1CreateHookParameters(self):
        """Test V1CreateHookParameters"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()