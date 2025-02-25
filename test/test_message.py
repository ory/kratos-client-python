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

from ory_kratos_client.models.message import Message

class TestMessage(unittest.TestCase):
    """Message unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Message:
        """Test Message
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Message`
        """
        model = Message()
        if include_optional:
            return Message(
                body = '',
                channel = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dispatches = [
                    ory_kratos_client.models.message_dispatch.messageDispatch(
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        error = ory_kratos_client.models.json_raw_message_represents_a_json/raw_message_that_works_well_with_json,_sql,_and_swagger/.JSONRawMessage represents a json.RawMessage that works well with JSON, SQL, and Swagger.(), 
                        id = '', 
                        message_id = '', 
                        status = 'failed', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ],
                id = '',
                recipient = '',
                send_count = 56,
                status = 'queued',
                subject = '',
                template_type = 'recovery_invalid',
                type = 'email',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Message(
                body = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                recipient = '',
                send_count = 56,
                status = 'queued',
                subject = '',
                template_type = 'recovery_invalid',
                type = 'email',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testMessage(self):
        """Test Message"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
