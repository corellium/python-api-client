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
from corellium_api.models.agent_app import AgentApp  # noqa: E501
from corellium_api.rest import ApiException

class TestAgentApp(unittest.TestCase):
    """AgentApp unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AgentApp
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.agent_app.AgentApp()  # noqa: E501
        if include_optional :
            return AgentApp(
                tags = [
                    ''
                    ], 
                running = True, 
                disk_usage = 56, 
                date = 56, 
                application_type = '', 
                name = '', 
                bundle_id = ''
            )
        else :
            return AgentApp(
        )

    def testAgentApp(self):
        """Test AgentApp"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
