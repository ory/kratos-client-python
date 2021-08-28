# SubmitSelfServiceLoginFlowBody


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | Method should be set to \&quot;password\&quot; when logging in using the identifier and password strategy. | 
**csrf_token** | **str** | Sending the anti-csrf token is only required for browser login flows. | [optional] 
**password** | **str** | The user&#39;s password. | [optional] 
**password_identifier** | **str** | Identifier is the email or username of the user trying to log in. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


