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

from ory_kratos_client.models.verifiable_identity_address import VerifiableIdentityAddress

class TestVerifiableIdentityAddress(unittest.TestCase):
    """VerifiableIdentityAddress unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VerifiableIdentityAddress:
        """Test VerifiableIdentityAddress
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VerifiableIdentityAddress`
        """
        model = VerifiableIdentityAddress()
        if include_optional:
            return VerifiableIdentityAddress(
                created_at = '2014-01-01T23:28:56.782Z',
                id = '',
                status = '',
                updated_at = '2014-01-01T23:28:56.782Z',
                value = '',
                verified = True,
                verified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                via = 'email'
            )
        else:
            return VerifiableIdentityAddress(
                status = '',
                value = '',
                verified = True,
                via = 'email',
        )
        """

    def testVerifiableIdentityAddress(self):
        """Test VerifiableIdentityAddress"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
