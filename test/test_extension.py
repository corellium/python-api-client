# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 5.2.0-17368
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import corellium_api
from corellium_api.models.extension import Extension  # noqa: E501
from corellium_api.rest import ApiException

class TestExtension(unittest.TestCase):
    """Extension unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Extension
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.extension.Extension()  # noqa: E501
        if include_optional :
            return Extension(
                identifier = '', 
                enabled = True, 
                created_at = '', 
                updated_at = '', 
                image_id = '', 
                state = '', 
                flavors = [
                    None
                    ]
            )
        else :
            return Extension(
        )

    def testExtension(self):
        """Test Extension"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
