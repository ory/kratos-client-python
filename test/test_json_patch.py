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

from ory_kratos_client.models.json_patch import JsonPatch

class TestJsonPatch(unittest.TestCase):
    """JsonPatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> JsonPatch:
        """Test JsonPatch
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `JsonPatch`
        """
        model = JsonPatch()
        if include_optional:
            return JsonPatch(
                var_from = '/name',
                op = 'replace',
                path = '/name',
                value = foobar
            )
        else:
            return JsonPatch(
                op = 'replace',
                path = '/name',
        )
        """

    def testJsonPatch(self):
        """Test JsonPatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
