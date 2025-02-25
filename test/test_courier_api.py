# coding: utf-8

"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more. 

    The version of the OpenAPI document: v1.3.8
    Contact: office@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_kratos_client.api.courier_api import CourierApi


class TestCourierApi(unittest.TestCase):
    """CourierApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CourierApi()

    def tearDown(self) -> None:
        pass

    def test_get_courier_message(self) -> None:
        """Test case for get_courier_message

        Get a Message
        """
        pass

    def test_list_courier_messages(self) -> None:
        """Test case for list_courier_messages

        List Messages
        """
        pass


if __name__ == '__main__':
    unittest.main()
