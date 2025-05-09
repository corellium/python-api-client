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
from corellium_api.models.domain_options import DomainOptions  # noqa: E501
from corellium_api.rest import ApiException

class TestDomainOptions(unittest.TestCase):
    """DomainOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test DomainOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.domain_options.DomainOptions()  # noqa: E501
        if include_optional :
            return DomainOptions(
                totp_required = True, 
                trial_extension = corellium_api.models.trial_extension.TrialExtension(
                    duration = 1.337, 
                    reason = '', 
                    denied = True, 
                    denied_reason = '', ), 
                snapshot_sharing_permissions = corellium_api.models.snapshot_sharing_permissions.SnapshotSharingPermissions(
                    cloud_enabled = True, 
                    domain_enabled = True, 
                    public_link = True, 
                    domain_restricted_link = True, 
                    password_public_link = True, 
                    email_invite = True, )
            )
        else :
            return DomainOptions(
        )

    def testDomainOptions(self):
        """Test DomainOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
