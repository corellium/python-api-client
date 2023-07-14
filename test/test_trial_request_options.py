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
from corellium_api.models.trial_request_options import TrialRequestOptions  # noqa: E501
from corellium_api.rest import ApiException

class TestTrialRequestOptions(unittest.TestCase):
    """TrialRequestOptions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test TrialRequestOptions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.trial_request_options.TrialRequestOptions()  # noqa: E501
        if include_optional :
            return TrialRequestOptions(
                address = corellium_api.models.address.Address(
                    address1 = '', 
                    address2 = '', 
                    city = '', 
                    country = '', 
                    postal_code = '', 
                    state = '', ), 
                email = '', 
                name = '', 
                metadata = corellium_api.models.trial_request_metadata.TrialRequestMetadata(
                    name = '', 
                    company = '', 
                    malware = True, 
                    research = True, 
                    pentest = True, 
                    other = '', ), 
                enterprise = True, 
                token = ''
            )
        else :
            return TrialRequestOptions(
        )

    def testTrialRequestOptions(self):
        """Test TrialRequestOptions"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
