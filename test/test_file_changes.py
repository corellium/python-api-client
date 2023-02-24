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
from corellium_api.models.file_changes import FileChanges  # noqa: E501
from corellium_api.rest import ApiException

class TestFileChanges(unittest.TestCase):
    """FileChanges unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test FileChanges
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.file_changes.FileChanges()  # noqa: E501
        if include_optional :
            return FileChanges(
                path = '', 
                mode = 1.337, 
                uid = 1.337, 
                gid = 1.337
            )
        else :
            return FileChanges(
        )

    def testFileChanges(self):
        """Test FileChanges"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
