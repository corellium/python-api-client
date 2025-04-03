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
from corellium_api.models.shared_snapshots_info import SharedSnapshotsInfo  # noqa: E501
from corellium_api.rest import ApiException

class TestSharedSnapshotsInfo(unittest.TestCase):
    """SharedSnapshotsInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SharedSnapshotsInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.shared_snapshots_info.SharedSnapshotsInfo()  # noqa: E501
        if include_optional :
            return SharedSnapshotsInfo(
                id = '', 
                name = '', 
                model = '', 
                shared_on = 1.337, 
                shared_with_member = '', 
                shared_by = corellium_api.models.snapshot_owner.SnapshotOwner(
                    name = '', 
                    email = '', )
            )
        else :
            return SharedSnapshotsInfo(
                id = '',
                name = '',
                model = '',
                shared_on = 1.337,
        )

    def testSharedSnapshotsInfo(self):
        """Test SharedSnapshotsInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
