# coding: utf-8

# flake8: noqa

"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more. 

    The version of the OpenAPI document: v1.3.5
    Contact: office@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "v1.3.5"

# import apis into sdk package
from ory_kratos_client.api.courier_api import CourierApi
from ory_kratos_client.api.frontend_api import FrontendApi
from ory_kratos_client.api.identity_api import IdentityApi
from ory_kratos_client.api.metadata_api import MetadataApi

# import ApiClient
from ory_kratos_client.api_response import ApiResponse
from ory_kratos_client.api_client import ApiClient
from ory_kratos_client.configuration import Configuration
from ory_kratos_client.exceptions import OpenApiException
from ory_kratos_client.exceptions import ApiTypeError
from ory_kratos_client.exceptions import ApiValueError
from ory_kratos_client.exceptions import ApiKeyError
from ory_kratos_client.exceptions import ApiAttributeError
from ory_kratos_client.exceptions import ApiException

# import models into sdk package
from ory_kratos_client.models.authenticator_assurance_level import AuthenticatorAssuranceLevel
from ory_kratos_client.models.batch_patch_identities_response import BatchPatchIdentitiesResponse
from ory_kratos_client.models.consistency_request_parameters import ConsistencyRequestParameters
from ory_kratos_client.models.continue_with import ContinueWith
from ory_kratos_client.models.continue_with_recovery_ui import ContinueWithRecoveryUi
from ory_kratos_client.models.continue_with_recovery_ui_flow import ContinueWithRecoveryUiFlow
from ory_kratos_client.models.continue_with_redirect_browser_to import ContinueWithRedirectBrowserTo
from ory_kratos_client.models.continue_with_set_ory_session_token import ContinueWithSetOrySessionToken
from ory_kratos_client.models.continue_with_settings_ui import ContinueWithSettingsUi
from ory_kratos_client.models.continue_with_settings_ui_flow import ContinueWithSettingsUiFlow
from ory_kratos_client.models.continue_with_verification_ui import ContinueWithVerificationUi
from ory_kratos_client.models.continue_with_verification_ui_flow import ContinueWithVerificationUiFlow
from ory_kratos_client.models.courier_message_status import CourierMessageStatus
from ory_kratos_client.models.courier_message_type import CourierMessageType
from ory_kratos_client.models.create_fedcm_flow_response import CreateFedcmFlowResponse
from ory_kratos_client.models.create_identity_body import CreateIdentityBody
from ory_kratos_client.models.create_recovery_code_for_identity_body import CreateRecoveryCodeForIdentityBody
from ory_kratos_client.models.create_recovery_link_for_identity_body import CreateRecoveryLinkForIdentityBody
from ory_kratos_client.models.delete_my_sessions_count import DeleteMySessionsCount
from ory_kratos_client.models.error_authenticator_assurance_level_not_satisfied import ErrorAuthenticatorAssuranceLevelNotSatisfied
from ory_kratos_client.models.error_browser_location_change_required import ErrorBrowserLocationChangeRequired
from ory_kratos_client.models.error_flow_replaced import ErrorFlowReplaced
from ory_kratos_client.models.error_generic import ErrorGeneric
from ory_kratos_client.models.flow_error import FlowError
from ory_kratos_client.models.generic_error import GenericError
from ory_kratos_client.models.get_version200_response import GetVersion200Response
from ory_kratos_client.models.health_not_ready_status import HealthNotReadyStatus
from ory_kratos_client.models.health_status import HealthStatus
from ory_kratos_client.models.identity import Identity
from ory_kratos_client.models.identity_credentials import IdentityCredentials
from ory_kratos_client.models.identity_credentials_code import IdentityCredentialsCode
from ory_kratos_client.models.identity_credentials_code_address import IdentityCredentialsCodeAddress
from ory_kratos_client.models.identity_credentials_oidc import IdentityCredentialsOidc
from ory_kratos_client.models.identity_credentials_oidc_provider import IdentityCredentialsOidcProvider
from ory_kratos_client.models.identity_credentials_password import IdentityCredentialsPassword
from ory_kratos_client.models.identity_patch import IdentityPatch
from ory_kratos_client.models.identity_patch_response import IdentityPatchResponse
from ory_kratos_client.models.identity_schema_container import IdentitySchemaContainer
from ory_kratos_client.models.identity_with_credentials import IdentityWithCredentials
from ory_kratos_client.models.identity_with_credentials_oidc import IdentityWithCredentialsOidc
from ory_kratos_client.models.identity_with_credentials_oidc_config import IdentityWithCredentialsOidcConfig
from ory_kratos_client.models.identity_with_credentials_oidc_config_provider import IdentityWithCredentialsOidcConfigProvider
from ory_kratos_client.models.identity_with_credentials_password import IdentityWithCredentialsPassword
from ory_kratos_client.models.identity_with_credentials_password_config import IdentityWithCredentialsPasswordConfig
from ory_kratos_client.models.is_alive200_response import IsAlive200Response
from ory_kratos_client.models.is_ready503_response import IsReady503Response
from ory_kratos_client.models.json_patch import JsonPatch
from ory_kratos_client.models.login_flow import LoginFlow
from ory_kratos_client.models.login_flow_state import LoginFlowState
from ory_kratos_client.models.logout_flow import LogoutFlow
from ory_kratos_client.models.message import Message
from ory_kratos_client.models.message_dispatch import MessageDispatch
from ory_kratos_client.models.needs_privileged_session_error import NeedsPrivilegedSessionError
from ory_kratos_client.models.o_auth2_client import OAuth2Client
from ory_kratos_client.models.o_auth2_consent_request_open_id_connect_context import OAuth2ConsentRequestOpenIDConnectContext
from ory_kratos_client.models.o_auth2_login_request import OAuth2LoginRequest
from ory_kratos_client.models.patch_identities_body import PatchIdentitiesBody
from ory_kratos_client.models.perform_native_logout_body import PerformNativeLogoutBody
from ory_kratos_client.models.provider import Provider
from ory_kratos_client.models.recovery_code_for_identity import RecoveryCodeForIdentity
from ory_kratos_client.models.recovery_flow import RecoveryFlow
from ory_kratos_client.models.recovery_flow_state import RecoveryFlowState
from ory_kratos_client.models.recovery_identity_address import RecoveryIdentityAddress
from ory_kratos_client.models.recovery_link_for_identity import RecoveryLinkForIdentity
from ory_kratos_client.models.registration_flow import RegistrationFlow
from ory_kratos_client.models.registration_flow_state import RegistrationFlowState
from ory_kratos_client.models.self_service_flow_expired_error import SelfServiceFlowExpiredError
from ory_kratos_client.models.session import Session
from ory_kratos_client.models.session_authentication_method import SessionAuthenticationMethod
from ory_kratos_client.models.session_device import SessionDevice
from ory_kratos_client.models.settings_flow import SettingsFlow
from ory_kratos_client.models.settings_flow_state import SettingsFlowState
from ory_kratos_client.models.successful_code_exchange_response import SuccessfulCodeExchangeResponse
from ory_kratos_client.models.successful_native_login import SuccessfulNativeLogin
from ory_kratos_client.models.successful_native_registration import SuccessfulNativeRegistration
from ory_kratos_client.models.token_pagination import TokenPagination
from ory_kratos_client.models.token_pagination_headers import TokenPaginationHeaders
from ory_kratos_client.models.ui_container import UiContainer
from ory_kratos_client.models.ui_node import UiNode
from ory_kratos_client.models.ui_node_anchor_attributes import UiNodeAnchorAttributes
from ory_kratos_client.models.ui_node_attributes import UiNodeAttributes
from ory_kratos_client.models.ui_node_image_attributes import UiNodeImageAttributes
from ory_kratos_client.models.ui_node_input_attributes import UiNodeInputAttributes
from ory_kratos_client.models.ui_node_meta import UiNodeMeta
from ory_kratos_client.models.ui_node_script_attributes import UiNodeScriptAttributes
from ory_kratos_client.models.ui_node_text_attributes import UiNodeTextAttributes
from ory_kratos_client.models.ui_text import UiText
from ory_kratos_client.models.update_fedcm_flow_body import UpdateFedcmFlowBody
from ory_kratos_client.models.update_identity_body import UpdateIdentityBody
from ory_kratos_client.models.update_login_flow_body import UpdateLoginFlowBody
from ory_kratos_client.models.update_login_flow_with_code_method import UpdateLoginFlowWithCodeMethod
from ory_kratos_client.models.update_login_flow_with_identifier_first_method import UpdateLoginFlowWithIdentifierFirstMethod
from ory_kratos_client.models.update_login_flow_with_lookup_secret_method import UpdateLoginFlowWithLookupSecretMethod
from ory_kratos_client.models.update_login_flow_with_oidc_method import UpdateLoginFlowWithOidcMethod
from ory_kratos_client.models.update_login_flow_with_passkey_method import UpdateLoginFlowWithPasskeyMethod
from ory_kratos_client.models.update_login_flow_with_password_method import UpdateLoginFlowWithPasswordMethod
from ory_kratos_client.models.update_login_flow_with_totp_method import UpdateLoginFlowWithTotpMethod
from ory_kratos_client.models.update_login_flow_with_web_authn_method import UpdateLoginFlowWithWebAuthnMethod
from ory_kratos_client.models.update_recovery_flow_body import UpdateRecoveryFlowBody
from ory_kratos_client.models.update_recovery_flow_with_code_method import UpdateRecoveryFlowWithCodeMethod
from ory_kratos_client.models.update_recovery_flow_with_link_method import UpdateRecoveryFlowWithLinkMethod
from ory_kratos_client.models.update_registration_flow_body import UpdateRegistrationFlowBody
from ory_kratos_client.models.update_registration_flow_with_code_method import UpdateRegistrationFlowWithCodeMethod
from ory_kratos_client.models.update_registration_flow_with_oidc_method import UpdateRegistrationFlowWithOidcMethod
from ory_kratos_client.models.update_registration_flow_with_passkey_method import UpdateRegistrationFlowWithPasskeyMethod
from ory_kratos_client.models.update_registration_flow_with_password_method import UpdateRegistrationFlowWithPasswordMethod
from ory_kratos_client.models.update_registration_flow_with_profile_method import UpdateRegistrationFlowWithProfileMethod
from ory_kratos_client.models.update_registration_flow_with_web_authn_method import UpdateRegistrationFlowWithWebAuthnMethod
from ory_kratos_client.models.update_settings_flow_body import UpdateSettingsFlowBody
from ory_kratos_client.models.update_settings_flow_with_lookup_method import UpdateSettingsFlowWithLookupMethod
from ory_kratos_client.models.update_settings_flow_with_oidc_method import UpdateSettingsFlowWithOidcMethod
from ory_kratos_client.models.update_settings_flow_with_passkey_method import UpdateSettingsFlowWithPasskeyMethod
from ory_kratos_client.models.update_settings_flow_with_password_method import UpdateSettingsFlowWithPasswordMethod
from ory_kratos_client.models.update_settings_flow_with_profile_method import UpdateSettingsFlowWithProfileMethod
from ory_kratos_client.models.update_settings_flow_with_totp_method import UpdateSettingsFlowWithTotpMethod
from ory_kratos_client.models.update_settings_flow_with_web_authn_method import UpdateSettingsFlowWithWebAuthnMethod
from ory_kratos_client.models.update_verification_flow_body import UpdateVerificationFlowBody
from ory_kratos_client.models.update_verification_flow_with_code_method import UpdateVerificationFlowWithCodeMethod
from ory_kratos_client.models.update_verification_flow_with_link_method import UpdateVerificationFlowWithLinkMethod
from ory_kratos_client.models.verifiable_identity_address import VerifiableIdentityAddress
from ory_kratos_client.models.verification_flow import VerificationFlow
from ory_kratos_client.models.verification_flow_state import VerificationFlowState
from ory_kratos_client.models.version import Version
