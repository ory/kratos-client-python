# UpdateLoginFlowBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**csrf_token** | **str** | Sending the anti-csrf token is only required for browser login flows. | 
**identifier** | **str** | Identifier is the email or username of the user trying to log in. | 
**method** | **str** | Method should be set to \&quot;password\&quot; when logging in using the identifier and password strategy. | 
**password** | **str** | The user&#39;s password. | 
**password_identifier** | **str** | Identifier is the email or username of the user trying to log in. This field is deprecated! | [optional] 
**transient_payload** | **object** | Transient data to pass along to any webhooks | [optional] 
**id_token** | **str** | IDToken is an optional id token provided by an OIDC provider  If submitted, it is verified using the OIDC provider&#39;s public key set and the claims are used to populate the OIDC credentials of the identity. If the OIDC provider does not store additional claims (such as name, etc.) in the IDToken itself, you can use the &#x60;traits&#x60; field to populate the identity&#39;s traits. Note, that Apple only includes the users email in the IDToken.  Supported providers are Apple Google | [optional] 
**id_token_nonce** | **str** | IDTokenNonce is the nonce, used when generating the IDToken. If the provider supports nonce validation, the nonce will be validated against this value and required. | [optional] 
**provider** | **str** | The provider to register with | 
**traits** | **object** | The identity traits. This is a placeholder for the registration flow. | [optional] 
**upstream_parameters** | **object** | UpstreamParameters are the parameters that are passed to the upstream identity provider.  These parameters are optional and depend on what the upstream identity provider supports. Supported parameters are: &#x60;login_hint&#x60; (string): The &#x60;login_hint&#x60; parameter suppresses the account chooser and either pre-fills the email box on the sign-in form, or selects the proper session. &#x60;hd&#x60; (string): The &#x60;hd&#x60; parameter limits the login/registration process to a Google Organization, e.g. &#x60;mycollege.edu&#x60;. &#x60;prompt&#x60; (string): The &#x60;prompt&#x60; specifies whether the Authorization Server prompts the End-User for reauthentication and consent, e.g. &#x60;select_account&#x60;. | [optional] 
**totp_code** | **str** | The TOTP code. | 
**webauthn_login** | **str** | Login a WebAuthn Security Key  This must contain the ID of the WebAuthN connection. | [optional] 
**lookup_secret** | **str** | The lookup secret. | 
**address** | **str** | Address is the address to send the code to, in case that there are multiple addresses. This field is only used in two-factor flows and is ineffective for passwordless flows. | [optional] 
**code** | **str** | Code is the 6 digits code sent to the user | [optional] 
**resend** | **str** | Resend is set when the user wants to resend the code | [optional] 
**passkey_login** | **str** | Login a WebAuthn Security Key  This must contain the ID of the WebAuthN connection. | [optional] 

## Example

```python
from ory_kratos_client.models.update_login_flow_body import UpdateLoginFlowBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLoginFlowBody from a JSON string
update_login_flow_body_instance = UpdateLoginFlowBody.from_json(json)
# print the JSON string representation of the object
print(UpdateLoginFlowBody.to_json())

# convert the object into a dict
update_login_flow_body_dict = update_login_flow_body_instance.to_dict()
# create an instance of UpdateLoginFlowBody from a dict
update_login_flow_body_from_dict = UpdateLoginFlowBody.from_dict(update_login_flow_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


