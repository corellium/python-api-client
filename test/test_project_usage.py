# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 7.3.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import corellium_api
from corellium_api.models.project_usage import ProjectUsage  # noqa: E501
from corellium_api.rest import ApiException

class TestProjectUsage(unittest.TestCase):
    """ProjectUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test ProjectUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.project_usage.ProjectUsage()  # noqa: E501
        if include_optional :
            return ProjectUsage(
                cores = 1.337, 
                instances = 1.337, 
                ram = 1.337, 
                gpu = 1.337
            )
        else :
            return ProjectUsage(
        )

    def testProjectUsage(self):
        """Test ProjectUsage"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
