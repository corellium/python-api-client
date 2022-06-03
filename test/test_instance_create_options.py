# coding: utf-8

"""
    Corellium API

    REST API to manage your virtual devices.  # noqa: E501

    The version of the OpenAPI document: 3.11.0-13642
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import corellium_api
from corellium_api.models.instance_create_options import InstanceCreateOptions  # noqa: E501
from corellium_api.rest import ApiException

class TestInstanceCreateOptions(unittest.TestCase):
    """InstanceCreateOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test InstanceCreateOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.instance_create_options.InstanceCreateOptions()  # noqa: E501
        if include_optional :
            return InstanceCreateOptions(
                name = '', 
                key = '', 
                flavor = '', 
                project = '', 
                os = '', 
                osbuild = '', 
                patches = [
                    ''
                    ], 
                fwpackage = '', 
                orig_fw_package_url = '', 
                encrypt = True, 
                override_wifi_mac = '', 
                volume = corellium_api.models.volume_options.VolumeOptions(
                    allocate = 1.337, 
                    partitions = [
                        None
                        ], 
                    compute_node = '', ), 
                snapshot = '', 
                boot_options = corellium_api.models.instance_boot_options.InstanceBootOptions(
                    boot_args = '', 
                    restore_boot_args = '', 
                    udid = '', 
                    ecid = '', 
                    random_seed = '', 
                    pac = True, 
                    aprr = True, ), 
                device = corellium_api.models.model.Model(
                    type = '', 
                    name = '', 
                    flavor = '', 
                    description = '', 
                    model = '', 
                    board_config = '', 
                    platform = '', 
                    cpid = 1.337, 
                    bdid = 1.337, 
                    peripherals = True, )
            )
        else :
            return InstanceCreateOptions(
                flavor = '',
                project = '',
                os = '',
        )

    def testInstanceCreateOptions(self):
        """Test InstanceCreateOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
