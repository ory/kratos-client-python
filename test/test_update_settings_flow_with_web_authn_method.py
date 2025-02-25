# coding: utf-8

"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more. 

    The version of the OpenAPI document: v1.3.6-alpha.2
    Contact: office@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_kratos_client.models.update_settings_flow_with_web_authn_method import UpdateSettingsFlowWithWebAuthnMethod

class TestUpdateSettingsFlowWithWebAuthnMethod(unittest.TestCase):
    """UpdateSettingsFlowWithWebAuthnMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSettingsFlowWithWebAuthnMethod:
        """Test UpdateSettingsFlowWithWebAuthnMethod
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSettingsFlowWithWebAuthnMethod`
        """
        model = UpdateSettingsFlowWithWebAuthnMethod()
        if include_optional:
            return UpdateSettingsFlowWithWebAuthnMethod(
                csrf_token = '',
                method = '',
                transient_payload = ory_kratos_client.models.transient_payload.transient_payload(),
                webauthn_register = '',
                webauthn_register_displayname = '',
                webauthn_remove = ''
            )
        else:
            return UpdateSettingsFlowWithWebAuthnMethod(
                method = '',
        )
        """

    def testUpdateSettingsFlowWithWebAuthnMethod(self):
        """Test UpdateSettingsFlowWithWebAuthnMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
