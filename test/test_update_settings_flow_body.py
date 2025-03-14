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

from ory_kratos_client.models.update_settings_flow_body import UpdateSettingsFlowBody

class TestUpdateSettingsFlowBody(unittest.TestCase):
    """UpdateSettingsFlowBody unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateSettingsFlowBody:
        """Test UpdateSettingsFlowBody
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateSettingsFlowBody`
        """
        model = UpdateSettingsFlowBody()
        if include_optional:
            return UpdateSettingsFlowBody(
                csrf_token = '',
                method = '',
                password = '',
                transient_payload = ory_kratos_client.models.transient_payload.transient_payload(),
                traits = ory_kratos_client.models.traits.traits(),
                flow = '',
                link = '',
                unlink = '',
                upstream_parameters = ory_kratos_client.models.upstream_parameters.upstream_parameters(),
                totp_code = '',
                totp_unlink = True,
                webauthn_register = '',
                webauthn_register_displayname = '',
                webauthn_remove = '',
                lookup_secret_confirm = True,
                lookup_secret_disable = True,
                lookup_secret_regenerate = True,
                lookup_secret_reveal = True,
                passkey_remove = '',
                passkey_settings_register = ''
            )
        else:
            return UpdateSettingsFlowBody(
                method = '',
                password = '',
                traits = ory_kratos_client.models.traits.traits(),
        )
        """

    def testUpdateSettingsFlowBody(self):
        """Test UpdateSettingsFlowBody"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
