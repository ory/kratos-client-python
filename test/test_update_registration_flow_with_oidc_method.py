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

from ory_kratos_client.models.update_registration_flow_with_oidc_method import UpdateRegistrationFlowWithOidcMethod

class TestUpdateRegistrationFlowWithOidcMethod(unittest.TestCase):
    """UpdateRegistrationFlowWithOidcMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateRegistrationFlowWithOidcMethod:
        """Test UpdateRegistrationFlowWithOidcMethod
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateRegistrationFlowWithOidcMethod`
        """
        model = UpdateRegistrationFlowWithOidcMethod()
        if include_optional:
            return UpdateRegistrationFlowWithOidcMethod(
                csrf_token = '',
                id_token = '',
                id_token_nonce = '',
                method = '',
                provider = '',
                traits = ory_kratos_client.models.traits.traits(),
                transient_payload = ory_kratos_client.models.transient_payload.transient_payload(),
                upstream_parameters = ory_kratos_client.models.upstream_parameters.upstream_parameters()
            )
        else:
            return UpdateRegistrationFlowWithOidcMethod(
                method = '',
                provider = '',
        )
        """

    def testUpdateRegistrationFlowWithOidcMethod(self):
        """Test UpdateRegistrationFlowWithOidcMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
