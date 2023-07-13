# coding: utf-8

"""
    BVNK API Endpoints

    The BVNK API is designed to facilitate seamless and secure transactions including payments, channels, anddigital wallet transactions.  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.payments_api import PaymentsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPaymentsApi(unittest.TestCase):
    """PaymentsApi unit test stubs"""

    def setUp(self):
        self.api = PaymentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_v1_pay_summary_get(self):
        """Test case for api_v1_pay_summary_get

        List Payments  # noqa: E501
        """
        pass

    def test_api_v1_pay_summary_post(self):
        """Test case for api_v1_pay_summary_post

        Create payment  # noqa: E501
        """
        pass

    def test_api_v1_pay_uuid_summary_get(self):
        """Test case for api_v1_pay_uuid_summary_get

        Get Payment  # noqa: E501
        """
        pass

    def test_api_v1_pay_validate_put(self):
        """Test case for api_v1_pay_validate_put

        Validate Address  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()