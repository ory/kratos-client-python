# coding: utf-8

"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more. 

    The version of the OpenAPI document: v1.2.0
    Contact: office@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_kratos_client.api.metadata_api import MetadataApi


class TestMetadataApi(unittest.TestCase):
    """MetadataApi unit test stubs"""

    def setUp(self) -> None:
        self.api = MetadataApi()

    def tearDown(self) -> None:
        pass

    def test_get_version(self) -> None:
        """Test case for get_version

        Return Running Software Version.
        """
        pass

    def test_is_alive(self) -> None:
        """Test case for is_alive

        Check HTTP Server Status
        """
        pass

    def test_is_ready(self) -> None:
        """Test case for is_ready

        Check HTTP Server and Database Status
        """
        pass


if __name__ == '__main__':
    unittest.main()
