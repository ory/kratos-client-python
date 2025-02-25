# coding: utf-8

"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more. 

    The version of the OpenAPI document: v1.3.4
    Contact: office@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_kratos_client.models.update_login_flow_body import UpdateLoginFlowBody

class TestUpdateLoginFlowBody(unittest.TestCase):
    """UpdateLoginFlowBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateLoginFlowBody:
        """Test UpdateLoginFlowBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateLoginFlowBody`
        """
        model = UpdateLoginFlowBody()
        if include_optional:
            return UpdateLoginFlowBody(
                csrf_token = '',
                identifier = '',
                method = '',
                password = '',
                password_identifier = '',
                transient_payload = ory_kratos_client.models.transient_payload.transient_payload(),
                id_token = '',
                id_token_nonce = '',
                provider = '',
                traits = ory_kratos_client.models.traits.traits(),
                upstream_parameters = ory_kratos_client.models.upstream_parameters.upstream_parameters(),
                totp_code = '',
                webauthn_login = '',
                lookup_secret = '',
                address = '',
                code = '',
                resend = '',
                passkey_login = ''
            )
        else:
            return UpdateLoginFlowBody(
                csrf_token = '',
                identifier = '',
                method = '',
                password = '',
                provider = '',
                totp_code = '',
                lookup_secret = '',
        )
        """

    def testUpdateLoginFlowBody(self):
        """Test UpdateLoginFlowBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
