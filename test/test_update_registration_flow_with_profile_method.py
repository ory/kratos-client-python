# coding: utf-8

"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more. 

    The version of the OpenAPI document: v1.2.1
    Contact: office@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ory_kratos_client.models.update_registration_flow_with_profile_method import UpdateRegistrationFlowWithProfileMethod

class TestUpdateRegistrationFlowWithProfileMethod(unittest.TestCase):
    """UpdateRegistrationFlowWithProfileMethod unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateRegistrationFlowWithProfileMethod:
        """Test UpdateRegistrationFlowWithProfileMethod
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateRegistrationFlowWithProfileMethod`
        """
        model = UpdateRegistrationFlowWithProfileMethod()
        if include_optional:
            return UpdateRegistrationFlowWithProfileMethod(
                csrf_token = '',
                method = '',
                screen = '',
                traits = None,
                transient_payload = None
            )
        else:
            return UpdateRegistrationFlowWithProfileMethod(
                method = '',
                traits = None,
        )
        """

    def testUpdateRegistrationFlowWithProfileMethod(self):
        """Test UpdateRegistrationFlowWithProfileMethod"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()