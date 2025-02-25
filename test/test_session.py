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

from ory_kratos_client.models.session import Session

class TestSession(unittest.TestCase):
    """Session unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Session:
        """Test Session
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Session`
        """
        model = Session()
        if include_optional:
            return Session(
                active = True,
                authenticated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                authentication_methods = [
                    ory_kratos_client.models.authentication_method_identifies_an_authentication_method.AuthenticationMethod identifies an authentication method(
                        aal = 'aal0', 
                        completed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        method = 'link_recovery', 
                        organization = '', 
                        provider = '', )
                    ],
                authenticator_assurance_level = 'aal0',
                devices = [
                    ory_kratos_client.models.session_device.sessionDevice(
                        id = '', 
                        ip_address = '', 
                        location = '', 
                        user_agent = '', )
                    ],
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                identity = ory_kratos_client.models.identity_represents_an_ory_kratos_identity.Identity represents an Ory Kratos identity(
                    created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    credentials = {
                        'key' : ory_kratos_client.models.identity_credentials.identityCredentials(
                            config = ory_kratos_client.models.json_raw_message_represents_a_json/raw_message_that_works_well_with_json,_sql,_and_swagger/.JSONRawMessage represents a json.RawMessage that works well with JSON, SQL, and Swagger.(), 
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            identifiers = [
                                ''
                                ], 
                            type = 'password', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            version = 56, )
                        }, 
                    id = '', 
                    metadata_admin = null, 
                    metadata_public = null, 
                    organization_id = '', 
                    recovery_addresses = [
                        ory_kratos_client.models.recovery_identity_address.recoveryIdentityAddress(
                            created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            id = '', 
                            updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            value = '', 
                            via = '', )
                        ], 
                    schema_id = '', 
                    schema_url = '', 
                    state = 'active', 
                    state_changed_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    traits = null, 
                    updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    verifiable_addresses = [
                        ory_kratos_client.models.verifiable_identity_address.verifiableIdentityAddress(
                            created_at = '2014-01-01T23:28:56.782Z', 
                            id = '', 
                            status = '', 
                            updated_at = '2014-01-01T23:28:56.782Z', 
                            value = '', 
                            verified = True, 
                            verified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            via = 'email', )
                        ], ),
                issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                tokenized = ''
            )
        else:
            return Session(
                id = '',
        )
        """

    def testSession(self):
        """Test Session"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
