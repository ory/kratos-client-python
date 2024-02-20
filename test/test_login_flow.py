"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more.   # noqa: E501

    The version of the OpenAPI document: v1.1.0
    Contact: office@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_kratos_client
from ory_kratos_client.model.authenticator_assurance_level import AuthenticatorAssuranceLevel
from ory_kratos_client.model.o_auth2_login_request import OAuth2LoginRequest
from ory_kratos_client.model.ui_container import UiContainer
globals()['AuthenticatorAssuranceLevel'] = AuthenticatorAssuranceLevel
globals()['OAuth2LoginRequest'] = OAuth2LoginRequest
globals()['UiContainer'] = UiContainer
from ory_kratos_client.model.login_flow import LoginFlow


class TestLoginFlow(unittest.TestCase):
    """LoginFlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testLoginFlow(self):
        """Test LoginFlow"""
        # FIXME: construct object with mandatory attributes with example values
        # model = LoginFlow()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
