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
from corellium_api.models.subscriber_invite import SubscriberInvite  # noqa: E501
from corellium_api.rest import ApiException

class TestSubscriberInvite(unittest.TestCase):
    """SubscriberInvite unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SubscriberInvite
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = corellium_api.models.subscriber_invite.SubscriberInvite()  # noqa: E501
        if include_optional :
            return SubscriberInvite(
                coupon_options = corellium_api.models.coupon_options.coupon_options(
                    type = 'percent', 
                    amount = 1.337, 
                    used = True, ), 
                plan = corellium_api.models.plan.plan(
                    license_type = 'premium', 
                    cores = 56, ), 
                trial = corellium_api.models.trial.trial(
                    duration = 1.337, ), 
                name = '', 
                email = '', 
                coupon_code = '', 
                domain = '', 
                aggregate = '', 
                use_by = '', 
                active = True, 
                reusable = True, 
                created_at = '', 
                updated_at = ''
            )
        else :
            return SubscriberInvite(
                coupon_code = '',
                aggregate = '',
                active = True,
                reusable = True,
                created_at = '',
                updated_at = '',
        )

    def testSubscriberInvite(self):
        """Test SubscriberInvite"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
