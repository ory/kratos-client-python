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

from ory_kratos_client.models.login_flow import LoginFlow

class TestLoginFlow(unittest.TestCase):
    """LoginFlow unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoginFlow:
        """Test LoginFlow
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoginFlow`
        """
        model = LoginFlow()
        if include_optional:
            return LoginFlow(
                active = 'password',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                oauth2_login_challenge = '',
                oauth2_login_request = ory_kratos_client.models.o_auth2_login_request.OAuth2LoginRequest(
                    challenge = '', 
                    client = ory_kratos_client.models.o_auth2_client_o_auth_2/0_clients_are_used_to_perform_o_auth_2/0_and_open_id_connect_flows/_usually,_o_auth_2/0_clients_are_generated_for_applications_which_want_to_consume_your_o_auth_2/0_or_open_id_connect_capabilities/.OAuth2Client OAuth 2.0 Clients are used to perform OAuth 2.0 and OpenID Connect flows. Usually, OAuth 2.0 clients are generated for applications which want to consume your OAuth 2.0 or OpenID Connect capabilities.(
                        access_token_strategy = '', 
                        allowed_cors_origins = [
                            ''
                            ], 
                        audience = [
                            ''
                            ], 
                        authorization_code_grant_access_token_lifespan = '', 
                        authorization_code_grant_id_token_lifespan = '', 
                        authorization_code_grant_refresh_token_lifespan = '', 
                        backchannel_logout_session_required = True, 
                        backchannel_logout_uri = '', 
                        client_credentials_grant_access_token_lifespan = '', 
                        client_id = '', 
                        client_name = '', 
                        client_secret = '', 
                        client_secret_expires_at = 56, 
                        client_uri = '', 
                        contacts = [
                            ''
                            ], 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        frontchannel_logout_session_required = True, 
                        frontchannel_logout_uri = '', 
                        grant_types = [
                            ''
                            ], 
                        implicit_grant_access_token_lifespan = '', 
                        implicit_grant_id_token_lifespan = '', 
                        jwks = null, 
                        jwks_uri = '', 
                        jwt_bearer_grant_access_token_lifespan = '', 
                        logo_uri = '', 
                        metadata = null, 
                        owner = '', 
                        policy_uri = '', 
                        post_logout_redirect_uris = [
                            ''
                            ], 
                        redirect_uris = [
                            ''
                            ], 
                        refresh_token_grant_access_token_lifespan = '', 
                        refresh_token_grant_id_token_lifespan = '', 
                        refresh_token_grant_refresh_token_lifespan = '', 
                        registration_access_token = '', 
                        registration_client_uri = '', 
                        request_object_signing_alg = '', 
                        request_uris = [
                            ''
                            ], 
                        response_types = [
                            ''
                            ], 
                        scope = '', 
                        sector_identifier_uri = '', 
                        skip_consent = True, 
                        skip_logout_consent = True, 
                        subject_type = '', 
                        token_endpoint_auth_method = '', 
                        token_endpoint_auth_signing_alg = '', 
                        tos_uri = '', 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        userinfo_signed_response_alg = '', ), 
                    oidc_context = ory_kratos_client.models.o_auth2_consent_request_open_id_connect_context.OAuth2ConsentRequestOpenIDConnectContext(
                        acr_values = [
                            ''
                            ], 
                        display = '', 
                        id_token_hint_claims = {
                            'key' : null
                            }, 
                        login_hint = '', 
                        ui_locales = [
                            ''
                            ], ), 
                    request_url = '', 
                    requested_access_token_audience = [
                        ''
                        ], 
                    requested_scope = [
                        ''
                        ], 
                    session_id = '', 
                    skip = True, 
                    subject = '', ),
                organization_id = '',
                refresh = True,
                request_url = '',
                requested_aal = 'aal0',
                return_to = '',
                session_token_exchange_code = '',
                state = None,
                transient_payload = None,
                type = '',
                ui = ory_kratos_client.models.ui_container.uiContainer(
                    action = '', 
                    messages = [
                        ory_kratos_client.models.ui_text.uiText(
                            context = ory_kratos_client.models.context.context(), 
                            id = 56, 
                            text = '', 
                            type = 'info', )
                        ], 
                    method = '', 
                    nodes = [
                        ory_kratos_client.models.node_represents_a_flow's_nodes.Node represents a flow's nodes(
                            attributes = null, 
                            group = 'default', 
                            messages = [
                                ory_kratos_client.models.ui_text.uiText(
                                    context = ory_kratos_client.models.context.context(), 
                                    id = 56, 
                                    text = '', 
                                    type = 'info', )
                                ], 
                            meta = ory_kratos_client.models.a_node's_meta_information.A Node's Meta Information(
                                label = , ), 
                            type = 'text', )
                        ], ),
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return LoginFlow(
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                id = '',
                issued_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                request_url = '',
                state = None,
                type = '',
                ui = ory_kratos_client.models.ui_container.uiContainer(
                    action = '', 
                    messages = [
                        ory_kratos_client.models.ui_text.uiText(
                            context = ory_kratos_client.models.context.context(), 
                            id = 56, 
                            text = '', 
                            type = 'info', )
                        ], 
                    method = '', 
                    nodes = [
                        ory_kratos_client.models.node_represents_a_flow's_nodes.Node represents a flow's nodes(
                            attributes = null, 
                            group = 'default', 
                            messages = [
                                ory_kratos_client.models.ui_text.uiText(
                                    context = ory_kratos_client.models.context.context(), 
                                    id = 56, 
                                    text = '', 
                                    type = 'info', )
                                ], 
                            meta = ory_kratos_client.models.a_node's_meta_information.A Node's Meta Information(
                                label = , ), 
                            type = 'text', )
                        ], ),
        )
        """

    def testLoginFlow(self):
        """Test LoginFlow"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
