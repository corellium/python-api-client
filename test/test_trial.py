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
from corellium_api.models.trial import Trial  # noqa: E501
from corellium_api.rest import ApiException

class TestTrial(unittest.TestCase):
    """Trial unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Trial
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.trial.Trial()  # noqa: E501
        if include_optional :
            return Trial(
                default_duration = 1.337, 
                default_hours = 1.337, 
                default_devices = 1.337, 
                default_cores = 1.337
            )
        else :
            return Trial(
        )

    def testTrial(self):
        """Test Trial"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
