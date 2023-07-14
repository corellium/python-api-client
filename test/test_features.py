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
from corellium_api.models.features import Features  # noqa: E501
from corellium_api.rest import ApiException

class TestFeatures(unittest.TestCase):
    """Features unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Features
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.features.Features()  # noqa: E501
        if include_optional :
            return Features(
                apps = True, 
                connect = True, 
                console = True, 
                coretrace = True, 
                device_control = True, 
                device_delete = True, 
                files = True, 
                frida = True, 
                images = True, 
                messaging = True, 
                netmon = True, 
                network = True, 
                port_forwarding = True, 
                power_management = True, 
                profile = True, 
                sensors = True, 
                settings = True, 
                snapshots = True, 
                strace = True, 
                system = True
            )
        else :
            return Features(
        )

    def testFeatures(self):
        """Test Features"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
