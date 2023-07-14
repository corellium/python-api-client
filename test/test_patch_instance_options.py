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
from corellium_api.models.patch_instance_options import PatchInstanceOptions  # noqa: E501
from corellium_api.rest import ApiException

class TestPatchInstanceOptions(unittest.TestCase):
    """PatchInstanceOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PatchInstanceOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.patch_instance_options.PatchInstanceOptions()  # noqa: E501
        if include_optional :
            return PatchInstanceOptions(
                name = '', 
                state = 'on', 
                boot_options = corellium_api.models.instance_boot_options.InstanceBootOptions(
                    boot_args = '', 
                    restore_boot_args = '', 
                    udid = '', 
                    ecid = '', 
                    random_seed = '', 
                    pac = True, 
                    aprr = True, 
                    additional_tags = [
                        'kalloc'
                        ], ), 
                proxy = [
                    corellium_api.models.proxy_config.ProxyConfig(
                        device_port = 1.337, 
                        first_available = True, 
                        expose = True, 
                        router_port = 1.337, )
                    ]
            )
        else :
            return PatchInstanceOptions(
        )

    def testPatchInstanceOptions(self):
        """Test PatchInstanceOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
