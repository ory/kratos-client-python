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

from ory_kratos_client.models.identity_with_credentials_oidc_config import IdentityWithCredentialsOidcConfig

class TestIdentityWithCredentialsOidcConfig(unittest.TestCase):
    """IdentityWithCredentialsOidcConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IdentityWithCredentialsOidcConfig:
        """Test IdentityWithCredentialsOidcConfig
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IdentityWithCredentialsOidcConfig`
        """
        model = IdentityWithCredentialsOidcConfig()
        if include_optional:
            return IdentityWithCredentialsOidcConfig(
                config = ory_kratos_client.models.identity_with_credentials_password_config.identityWithCredentialsPasswordConfig(
                    hashed_password = '', 
                    password = '', 
                    use_password_migration_hook = True, ),
                providers = [
                    ory_kratos_client.models.identity_with_credentials_oidc_config_provider.identityWithCredentialsOidcConfigProvider(
                        provider = '', 
                        subject = '', 
                        use_auto_link = True, )
                    ]
            )
        else:
            return IdentityWithCredentialsOidcConfig(
        )
        """

    def testIdentityWithCredentialsOidcConfig(self):
        """Test IdentityWithCredentialsOidcConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
