# ory_kratos_client.PublicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_schema**](PublicApi.md#get_schema) | **GET** /schemas/{id} | 
[**get_self_service_error**](PublicApi.md#get_self_service_error) | **GET** /self-service/errors | Get User-Facing Self-Service Errors
[**get_self_service_login_flow**](PublicApi.md#get_self_service_login_flow) | **GET** /self-service/login/flows | Get Login Flow
[**get_self_service_recovery_flow**](PublicApi.md#get_self_service_recovery_flow) | **GET** /self-service/recovery/flows | Get information about a recovery flow
[**get_self_service_registration_flow**](PublicApi.md#get_self_service_registration_flow) | **GET** /self-service/registration/flows | Get Registration Flow
[**get_self_service_settings_flow**](PublicApi.md#get_self_service_settings_flow) | **GET** /self-service/settings/flows | Get Settings Flow
[**get_self_service_verification_flow**](PublicApi.md#get_self_service_verification_flow) | **GET** /self-service/verification/flows | Get Verification Flow
[**initialize_self_service_browser_logout_flow**](PublicApi.md#initialize_self_service_browser_logout_flow) | **GET** /self-service/browser/flows/logout | Initialize Browser-Based Logout User Flow
[**initialize_self_service_login_for_browsers**](PublicApi.md#initialize_self_service_login_for_browsers) | **GET** /self-service/login/browser | Initialize Login Flow for browsers
[**initialize_self_service_login_for_native_apps**](PublicApi.md#initialize_self_service_login_for_native_apps) | **GET** /self-service/login/api | Initialize Login Flow for Native Apps and API clients
[**initialize_self_service_recovery_for_browsers**](PublicApi.md#initialize_self_service_recovery_for_browsers) | **GET** /self-service/recovery/browser | Initialize Recovery Flow for Browser Clients
[**initialize_self_service_recovery_for_native_apps**](PublicApi.md#initialize_self_service_recovery_for_native_apps) | **GET** /self-service/recovery/api | Initialize Recovery Flow for Native Apps and API clients
[**initialize_self_service_registration_for_browsers**](PublicApi.md#initialize_self_service_registration_for_browsers) | **GET** /self-service/registration/browser | Initialize Registration Flow for browsers
[**initialize_self_service_registration_for_native_apps**](PublicApi.md#initialize_self_service_registration_for_native_apps) | **GET** /self-service/registration/api | Initialize Registration Flow for Native Apps and API clients
[**initialize_self_service_settings_for_browsers**](PublicApi.md#initialize_self_service_settings_for_browsers) | **GET** /self-service/settings/browser | Initialize Settings Flow for Browsers
[**initialize_self_service_settings_for_native_apps**](PublicApi.md#initialize_self_service_settings_for_native_apps) | **GET** /self-service/settings/api | Initialize Settings Flow for Native Apps and API clients
[**initialize_self_service_verification_for_browsers**](PublicApi.md#initialize_self_service_verification_for_browsers) | **GET** /self-service/verification/browser | Initialize Verification Flow for Browser Clients
[**initialize_self_service_verification_for_native_apps**](PublicApi.md#initialize_self_service_verification_for_native_apps) | **GET** /self-service/verification/api | Initialize Verification Flow for Native Apps and API clients
[**revoke_session**](PublicApi.md#revoke_session) | **DELETE** /sessions | Initialize Logout Flow for API Clients - Revoke a Session
[**submit_self_service_login_flow**](PublicApi.md#submit_self_service_login_flow) | **POST** /self-service/login | Submit a Login Flow
[**submit_self_service_recovery_flow**](PublicApi.md#submit_self_service_recovery_flow) | **POST** /self-service/recovery | Complete Recovery Flow
[**submit_self_service_recovery_flow_with_link_method**](PublicApi.md#submit_self_service_recovery_flow_with_link_method) | **POST** /self-service/recovery/methods/link | Complete Recovery Flow with Link Method
[**submit_self_service_registration_flow**](PublicApi.md#submit_self_service_registration_flow) | **POST** /self-service/registration | Submit a Registration Flow
[**submit_self_service_settings_flow**](PublicApi.md#submit_self_service_settings_flow) | **POST** /self-service/settings | Complete Settings Flow
[**submit_self_service_verification_flow**](PublicApi.md#submit_self_service_verification_flow) | **POST** /self-service/verification/methods/link | Complete Verification Flow
[**to_session**](PublicApi.md#to_session) | **GET** /sessions/whoami | Check Who the Current HTTP Session Belongs To


# **get_schema**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_schema(id)



Get a Traits Schema Definition

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    id = "id_example" # str | ID must be set to the ID of schema you want to get

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_schema(id)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->get_schema: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID must be set to the ID of schema you want to get |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | jsonSchema |  -  |
**404** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_service_error**
> SelfServiceErrorContainer get_self_service_error(error)

Get User-Facing Self-Service Errors

This endpoint returns the error associated with a user-facing self service errors.  This endpoint supports stub values to help you implement the error UI:  `?error=stub:500` - returns a stub 500 (Internal Server Error) error.  More information can be found at [Ory Kratos User User Facing Error Documentation](https://www.ory.sh/docs/kratos/self-service/flows/user-facing-errors).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.self_service_error_container import SelfServiceErrorContainer
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    error = "error_example" # str | Error is the container's ID

    # example passing only required values which don't have defaults set
    try:
        # Get User-Facing Self-Service Errors
        api_response = api_instance.get_self_service_error(error)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->get_self_service_error: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **error** | **str**| Error is the container&#39;s ID |

### Return type

[**SelfServiceErrorContainer**](SelfServiceErrorContainer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User-facing error response |  -  |
**403** | jsonError |  -  |
**404** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_service_login_flow**
> LoginFlow get_self_service_login_flow(id)

Get Login Flow

This endpoint returns a login flow's context with, for example, error details and other information.  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.login_flow import LoginFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    id = "id_example" # str | The Login Flow ID  The value for this parameter comes from `flow` URL Query parameter sent to your application (e.g. `/login?flow=abcde`).

    # example passing only required values which don't have defaults set
    try:
        # Get Login Flow
        api_response = api_instance.get_self_service_login_flow(id)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->get_self_service_login_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Login Flow ID  The value for this parameter comes from &#x60;flow&#x60; URL Query parameter sent to your application (e.g. &#x60;/login?flow&#x3D;abcde&#x60;). |

### Return type

[**LoginFlow**](LoginFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | loginFlow |  -  |
**403** | jsonError |  -  |
**404** | jsonError |  -  |
**410** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_service_recovery_flow**
> RecoveryFlow get_self_service_recovery_flow(id)

Get information about a recovery flow

This endpoint returns a recovery flow's context with, for example, error details and other information.  More information can be found at [Ory Kratos Account Recovery Documentation](../self-service/flows/account-recovery.mdx).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.recovery_flow import RecoveryFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    id = "id_example" # str | The Flow ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/recovery?flow=abcde`).

    # example passing only required values which don't have defaults set
    try:
        # Get information about a recovery flow
        api_response = api_instance.get_self_service_recovery_flow(id)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->get_self_service_recovery_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Flow ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/recovery?flow&#x3D;abcde&#x60;). |

### Return type

[**RecoveryFlow**](RecoveryFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | recoveryFlow |  -  |
**404** | jsonError |  -  |
**410** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_service_registration_flow**
> RegistrationFlow get_self_service_registration_flow(id)

Get Registration Flow

This endpoint returns a registration flow's context with, for example, error details and other information.  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.registration_flow import RegistrationFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    id = "id_example" # str | The Registration Flow ID  The value for this parameter comes from `flow` URL Query parameter sent to your application (e.g. `/registration?flow=abcde`).

    # example passing only required values which don't have defaults set
    try:
        # Get Registration Flow
        api_response = api_instance.get_self_service_registration_flow(id)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->get_self_service_registration_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Registration Flow ID  The value for this parameter comes from &#x60;flow&#x60; URL Query parameter sent to your application (e.g. &#x60;/registration?flow&#x3D;abcde&#x60;). |

### Return type

[**RegistrationFlow**](RegistrationFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | registrationFlow |  -  |
**403** | jsonError |  -  |
**404** | jsonError |  -  |
**410** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_service_settings_flow**
> SettingsFlow get_self_service_settings_flow(id)

Get Settings Flow

When accessing this endpoint through Ory Kratos' Public API you must ensure that either the Ory Kratos Session Cookie or the Ory Kratos Session Token are set. The public endpoint does not return 404 status codes but instead 403 or 500 to improve data privacy.  You can access this endpoint without credentials when using Ory Kratos' Admin API.  More information can be found at [Ory Kratos User Settings & Profile Management Documentation](../self-service/flows/user-settings).

### Example

* Bearer Authentication (sessionToken):
```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.settings_flow import SettingsFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: sessionToken
configuration = ory_kratos_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    id = "id_example" # str | ID is the Settings Flow ID  The value for this parameter comes from `flow` URL Query parameter sent to your application (e.g. `/settings?flow=abcde`).
    x_session_token = "X-Session-Token_example" # str | The Session Token of the Identity performing the settings flow. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get Settings Flow
        api_response = api_instance.get_self_service_settings_flow(id)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->get_self_service_settings_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get Settings Flow
        api_response = api_instance.get_self_service_settings_flow(id, x_session_token=x_session_token)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->get_self_service_settings_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID is the Settings Flow ID  The value for this parameter comes from &#x60;flow&#x60; URL Query parameter sent to your application (e.g. &#x60;/settings?flow&#x3D;abcde&#x60;). |
 **x_session_token** | **str**| The Session Token of the Identity performing the settings flow. | [optional]

### Return type

[**SettingsFlow**](SettingsFlow.md)

### Authorization

[sessionToken](../README.md#sessionToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | settingsFlow |  -  |
**403** | jsonError |  -  |
**404** | jsonError |  -  |
**410** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_service_verification_flow**
> VerificationFlow get_self_service_verification_flow(id)

Get Verification Flow

This endpoint returns a verification flow's context with, for example, error details and other information.  More information can be found at [Ory Kratos Email and Phone Verification Documentation](https://www.ory.sh/docs/kratos/selfservice/flows/verify-email-account-activation).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.verification_flow import VerificationFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    id = "id_example" # str | The Flow ID  The value for this parameter comes from `request` URL Query parameter sent to your application (e.g. `/verification?flow=abcde`).

    # example passing only required values which don't have defaults set
    try:
        # Get Verification Flow
        api_response = api_instance.get_self_service_verification_flow(id)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->get_self_service_verification_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The Flow ID  The value for this parameter comes from &#x60;request&#x60; URL Query parameter sent to your application (e.g. &#x60;/verification?flow&#x3D;abcde&#x60;). |

### Return type

[**VerificationFlow**](VerificationFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | verificationFlow |  -  |
**403** | jsonError |  -  |
**404** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_browser_logout_flow**
> initialize_self_service_browser_logout_flow()

Initialize Browser-Based Logout User Flow

This endpoint initializes a logout flow.  > This endpoint is NOT INTENDED for API clients and only works with browsers (Chrome, Firefox, ...).  On successful logout, the browser will be redirected (HTTP 302 Found) to the `return_to` parameter of the initial request or fall back to `urls.default_return_to`.  More information can be found at [Ory Kratos User Logout Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-logout).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialize Browser-Based Logout User Flow
        api_instance.initialize_self_service_browser_logout_flow()
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_browser_logout_flow: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_login_for_browsers**
> initialize_self_service_login_for_browsers()

Initialize Login Flow for browsers

This endpoint initializes a browser-based user login flow. Once initialized, the browser will be redirected to `selfservice.flows.login.ui_url` with the flow ID set as the query parameter `?flow=`. If a valid user session exists already, the browser will be redirected to `urls.default_redirect_url` unless the query parameter `?refresh=true` was set.  This endpoint is NOT INTENDED for API clients and only works with browsers (Chrome, Firefox, ...).  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    refresh = True # bool | Refresh a login session  If set to true, this will refresh an existing login session by asking the user to sign in again. This will reset the authenticated_at time of the session. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initialize Login Flow for browsers
        api_instance.initialize_self_service_login_for_browsers(refresh=refresh)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_login_for_browsers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Refresh a login session  If set to true, this will refresh an existing login session by asking the user to sign in again. This will reset the authenticated_at time of the session. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_login_for_native_apps**
> LoginFlow initialize_self_service_login_for_native_apps()

Initialize Login Flow for Native Apps and API clients

This endpoint initiates a login flow for API clients such as mobile devices, smart TVs, and so on.  If a valid provided session cookie or session token is provided, a 400 Bad Request error will be returned unless the URL query parameter `?refresh=true` is set.  To fetch an existing login flow call `/self-service/login/flows?flow=<flow_id>`.  :::warning  You MUST NOT use this endpoint in client-side (Single Page Apps, ReactJS, AngularJS) nor server-side (Java Server Pages, NodeJS, PHP, Golang, ...) browser applications. Using this endpoint in these applications will make you vulnerable to a variety of CSRF attacks, including CSRF login attacks.  This endpoint MUST ONLY be used in scenarios such as native mobile apps (React Native, Objective C, Swift, Java, ...).  :::  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.login_flow import LoginFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    refresh = True # bool | Refresh a login session  If set to true, this will refresh an existing login session by asking the user to sign in again. This will reset the authenticated_at time of the session. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initialize Login Flow for Native Apps and API clients
        api_response = api_instance.initialize_self_service_login_for_native_apps(refresh=refresh)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_login_for_native_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Refresh a login session  If set to true, this will refresh an existing login session by asking the user to sign in again. This will reset the authenticated_at time of the session. | [optional]

### Return type

[**LoginFlow**](LoginFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | loginFlow |  -  |
**400** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_recovery_for_browsers**
> initialize_self_service_recovery_for_browsers()

Initialize Recovery Flow for Browser Clients

This endpoint initializes a browser-based account recovery flow. Once initialized, the browser will be redirected to `selfservice.flows.recovery.ui_url` with the flow ID set as the query parameter `?flow=`. If a valid user session exists, the browser is returned to the configured return URL.  This endpoint is NOT INTENDED for API clients and only works with browsers (Chrome, Firefox, ...).  More information can be found at [Ory Kratos Account Recovery Documentation](../self-service/flows/account-recovery.mdx).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialize Recovery Flow for Browser Clients
        api_instance.initialize_self_service_recovery_for_browsers()
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_recovery_for_browsers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_recovery_for_native_apps**
> RecoveryFlow initialize_self_service_recovery_for_native_apps()

Initialize Recovery Flow for Native Apps and API clients

This endpoint initiates a recovery flow for API clients such as mobile devices, smart TVs, and so on.  If a valid provided session cookie or session token is provided, a 400 Bad Request error.  To fetch an existing recovery flow call `/self-service/recovery/flows?flow=<flow_id>`.  :::warning  You MUST NOT use this endpoint in client-side (Single Page Apps, ReactJS, AngularJS) nor server-side (Java Server Pages, NodeJS, PHP, Golang, ...) browser applications. Using this endpoint in these applications will make you vulnerable to a variety of CSRF attacks.  This endpoint MUST ONLY be used in scenarios such as native mobile apps (React Native, Objective C, Swift, Java, ...).  :::  More information can be found at [Ory Kratos Account Recovery Documentation](../self-service/flows/account-recovery.mdx).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.recovery_flow import RecoveryFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialize Recovery Flow for Native Apps and API clients
        api_response = api_instance.initialize_self_service_recovery_for_native_apps()
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_recovery_for_native_apps: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RecoveryFlow**](RecoveryFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | recoveryFlow |  -  |
**400** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_registration_for_browsers**
> initialize_self_service_registration_for_browsers()

Initialize Registration Flow for browsers

This endpoint initializes a browser-based user registration flow. Once initialized, the browser will be redirected to `selfservice.flows.registration.ui_url` with the flow ID set as the query parameter `?flow=`. If a valid user session exists already, the browser will be redirected to `urls.default_redirect_url` unless the query parameter `?refresh=true` was set.  :::note  This endpoint is NOT INTENDED for API clients and only works with browsers (Chrome, Firefox, ...).  :::  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialize Registration Flow for browsers
        api_instance.initialize_self_service_registration_for_browsers()
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_registration_for_browsers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_registration_for_native_apps**
> RegistrationFlow initialize_self_service_registration_for_native_apps()

Initialize Registration Flow for Native Apps and API clients

This endpoint initiates a registration flow for API clients such as mobile devices, smart TVs, and so on.  If a valid provided session cookie or session token is provided, a 400 Bad Request error will be returned unless the URL query parameter `?refresh=true` is set.  To fetch an existing registration flow call `/self-service/registration/flows?flow=<flow_id>`.  :::warning  You MUST NOT use this endpoint in client-side (Single Page Apps, ReactJS, AngularJS) nor server-side (Java Server Pages, NodeJS, PHP, Golang, ...) browser applications. Using this endpoint in these applications will make you vulnerable to a variety of CSRF attacks.  This endpoint MUST ONLY be used in scenarios such as native mobile apps (React Native, Objective C, Swift, Java, ...).  :::  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.registration_flow import RegistrationFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialize Registration Flow for Native Apps and API clients
        api_response = api_instance.initialize_self_service_registration_for_native_apps()
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_registration_for_native_apps: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**RegistrationFlow**](RegistrationFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | registrationFlow |  -  |
**400** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_settings_for_browsers**
> initialize_self_service_settings_for_browsers()

Initialize Settings Flow for Browsers

This endpoint initializes a browser-based user settings flow. Once initialized, the browser will be redirected to `selfservice.flows.settings.ui_url` with the flow ID set as the query parameter `?flow=`. If no valid Ory Kratos Session Cookie is included in the request, a login flow will be initialized.  :::note  This endpoint is NOT INTENDED for API clients and only works with browsers (Chrome, Firefox, ...).  :::  More information can be found at [Ory Kratos User Settings & Profile Management Documentation](../self-service/flows/user-settings).

### Example

* Bearer Authentication (sessionToken):
```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: sessionToken
configuration = ory_kratos_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialize Settings Flow for Browsers
        api_instance.initialize_self_service_settings_for_browsers()
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_settings_for_browsers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[sessionToken](../README.md#sessionToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_settings_for_native_apps**
> SettingsFlow initialize_self_service_settings_for_native_apps()

Initialize Settings Flow for Native Apps and API clients

This endpoint initiates a settings flow for API clients such as mobile devices, smart TVs, and so on. You must provide a valid Ory Kratos Session Token for this endpoint to respond with HTTP 200 OK.  To fetch an existing settings flow call `/self-service/settings/flows?flow=<flow_id>`.  :::warning  You MUST NOT use this endpoint in client-side (Single Page Apps, ReactJS, AngularJS) nor server-side (Java Server Pages, NodeJS, PHP, Golang, ...) browser applications. Using this endpoint in these applications will make you vulnerable to a variety of CSRF attacks.  This endpoint MUST ONLY be used in scenarios such as native mobile apps (React Native, Objective C, Swift, Java, ...).  :::  More information can be found at [Ory Kratos User Settings & Profile Management Documentation](../self-service/flows/user-settings).

### Example

* Bearer Authentication (sessionToken):
```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.settings_flow import SettingsFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: sessionToken
configuration = ory_kratos_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    x_session_token = "X-Session-Token_example" # str | The Session Token of the Identity performing the settings flow. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Initialize Settings Flow for Native Apps and API clients
        api_response = api_instance.initialize_self_service_settings_for_native_apps(x_session_token=x_session_token)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_settings_for_native_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_session_token** | **str**| The Session Token of the Identity performing the settings flow. | [optional]

### Return type

[**SettingsFlow**](SettingsFlow.md)

### Authorization

[sessionToken](../README.md#sessionToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | settingsFlow |  -  |
**400** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_verification_for_browsers**
> initialize_self_service_verification_for_browsers()

Initialize Verification Flow for Browser Clients

This endpoint initializes a browser-based account verification flow. Once initialized, the browser will be redirected to `selfservice.flows.verification.ui_url` with the flow ID set as the query parameter `?flow=`.  This endpoint is NOT INTENDED for API clients and only works with browsers (Chrome, Firefox, ...).  More information can be found at [Ory Kratos Email and Phone Verification Documentation](https://www.ory.sh/docs/kratos/selfservice/flows/verify-email-account-activation).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialize Verification Flow for Browser Clients
        api_instance.initialize_self_service_verification_for_browsers()
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_verification_for_browsers: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **initialize_self_service_verification_for_native_apps**
> VerificationFlow initialize_self_service_verification_for_native_apps()

Initialize Verification Flow for Native Apps and API clients

This endpoint initiates a verification flow for API clients such as mobile devices, smart TVs, and so on.  To fetch an existing verification flow call `/self-service/verification/flows?flow=<flow_id>`.  :::warning  You MUST NOT use this endpoint in client-side (Single Page Apps, ReactJS, AngularJS) nor server-side (Java Server Pages, NodeJS, PHP, Golang, ...) browser applications. Using this endpoint in these applications will make you vulnerable to a variety of CSRF attacks.  This endpoint MUST ONLY be used in scenarios such as native mobile apps (React Native, Objective C, Swift, Java, ...).  :::  More information can be found at [Ory Kratos Email and Phone Verification Documentation](https://www.ory.sh/docs/kratos/selfservice/flows/verify-email-account-activation).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.verification_flow import VerificationFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Initialize Verification Flow for Native Apps and API clients
        api_response = api_instance.initialize_self_service_verification_for_native_apps()
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->initialize_self_service_verification_for_native_apps: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**VerificationFlow**](VerificationFlow.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | verificationFlow |  -  |
**400** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_session**
> revoke_session(revoke_session)

Initialize Logout Flow for API Clients - Revoke a Session

Use this endpoint to revoke a session using its token. This endpoint is particularly useful for API clients such as mobile apps to log the user out of the system and invalidate the session.  This endpoint does not remove any HTTP Cookies - use the Browser-Based Self-Service Logout Flow instead.

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.revoke_session import RevokeSession
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    revoke_session = RevokeSession(
        session_token="session_token_example",
    ) # RevokeSession | 

    # example passing only required values which don't have defaults set
    try:
        # Initialize Logout Flow for API Clients - Revoke a Session
        api_instance.revoke_session(revoke_session)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->revoke_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revoke_session** | [**RevokeSession**](RevokeSession.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**400** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_self_service_login_flow**
> LoginViaApiResponse submit_self_service_login_flow(flow)

Submit a Login Flow

Use this endpoint to complete a login flow. This endpoint behaves differently for API and browser flows.  API flows expect `application/json` to be sent in the body and responds with HTTP 200 and a application/json body with the session token on success; HTTP 302 redirect to a fresh login flow if the original flow expired with the appropriate error messages set; HTTP 400 on form validation errors.  Browser flows expect `application/x-www-form-urlencoded` to be sent in the body and responds with a HTTP 302 redirect to the post/after login URL or the `return_to` value if it was set and if the login succeeded; a HTTP 302 redirect to the login UI URL with the flow ID containing the validation errors otherwise.  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.login_flow import LoginFlow
from ory_kratos_client.model.login_via_api_response import LoginViaApiResponse
from ory_kratos_client.model.submit_self_service_login_flow import SubmitSelfServiceLoginFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    flow = "flow_example" # str | The Login Flow ID  The value for this parameter comes from `flow` URL Query parameter sent to your application (e.g. `/login?flow=abcde`).
    submit_self_service_login_flow = SubmitSelfServiceLoginFlow() # SubmitSelfServiceLoginFlow |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Submit a Login Flow
        api_response = api_instance.submit_self_service_login_flow(flow)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_login_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Submit a Login Flow
        api_response = api_instance.submit_self_service_login_flow(flow, submit_self_service_login_flow=submit_self_service_login_flow)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_login_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | **str**| The Login Flow ID  The value for this parameter comes from &#x60;flow&#x60; URL Query parameter sent to your application (e.g. &#x60;/login?flow&#x3D;abcde&#x60;). |
 **submit_self_service_login_flow** | [**SubmitSelfServiceLoginFlow**](SubmitSelfServiceLoginFlow.md)|  | [optional]

### Return type

[**LoginViaApiResponse**](LoginViaApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | loginViaApiResponse |  -  |
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**400** | loginFlow |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_self_service_recovery_flow**
> submit_self_service_recovery_flow(flow)

Complete Recovery Flow

Use this endpoint to complete a recovery flow. This endpoint behaves differently for API and browser flows and has several states:  `choose_method` expects `flow` (in the URL query) and `email` (in the body) to be sent and works with API- and Browser-initiated flows. For API clients it either returns a HTTP 200 OK when the form is valid and HTTP 400 OK when the form is invalid and a HTTP 302 Found redirect with a fresh recovery flow if the flow was otherwise invalid (e.g. expired). For Browser clients it returns a HTTP 302 Found redirect to the Recovery UI URL with the Recovery Flow ID appended. `sent_email` is the success state after `choose_method` for the `link` method and allows the user to request another recovery email. It works for both API and Browser-initiated flows and returns the same responses as the flow in `choose_method` state. `passed_challenge` expects a `token` to be sent in the URL query and given the nature of the flow (\"sending a recovery link\") does not have any API capabilities. The server responds with a HTTP 302 Found redirect either to the Settings UI URL (if the link was valid) and instructs the user to update their password, or a redirect to the Recover UI URL with a new Recovery Flow ID which contains an error message that the recovery link was invalid.  More information can be found at [Ory Kratos Account Recovery Documentation](../self-service/flows/account-recovery.mdx).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.recovery_flow import RecoveryFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    flow = "flow_example" # str | The Registration Flow ID  The value for this parameter comes from `flow` URL Query parameter sent to your application (e.g. `/registration?flow=abcde`).
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Complete Recovery Flow
        api_instance.submit_self_service_recovery_flow(flow)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_recovery_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Complete Recovery Flow
        api_instance.submit_self_service_recovery_flow(flow, body=body)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_recovery_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | **str**| The Registration Flow ID  The value for this parameter comes from &#x60;flow&#x60; URL Query parameter sent to your application (e.g. &#x60;/registration?flow&#x3D;abcde&#x60;). |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**400** | recoveryFlow |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_self_service_recovery_flow_with_link_method**
> submit_self_service_recovery_flow_with_link_method()

Complete Recovery Flow with Link Method

Use this endpoint to complete a recovery flow using the link method. This endpoint behaves differently for API and browser flows and has several states:  `choose_method` expects `flow` (in the URL query) and `email` (in the body) to be sent and works with API- and Browser-initiated flows. For API clients it either returns a HTTP 200 OK when the form is valid and HTTP 400 OK when the form is invalid and a HTTP 302 Found redirect with a fresh recovery flow if the flow was otherwise invalid (e.g. expired). For Browser clients it returns a HTTP 302 Found redirect to the Recovery UI URL with the Recovery Flow ID appended. `sent_email` is the success state after `choose_method` and allows the user to request another recovery email. It works for both API and Browser-initiated flows and returns the same responses as the flow in `choose_method` state. `passed_challenge` expects a `token` to be sent in the URL query and given the nature of the flow (\"sending a recovery link\") does not have any API capabilities. The server responds with a HTTP 302 Found redirect either to the Settings UI URL (if the link was valid) and instructs the user to update their password, or a redirect to the Recover UI URL with a new Recovery Flow ID which contains an error message that the recovery link was invalid.  More information can be found at [Ory Kratos Account Recovery Documentation](../self-service/flows/account-recovery.mdx).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.submit_self_service_recovery_flow_with_link_method import SubmitSelfServiceRecoveryFlowWithLinkMethod
from ory_kratos_client.model.recovery_flow import RecoveryFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    token = "token_example" # str | Recovery Token  The recovery token which completes the recovery request. If the token is invalid (e.g. expired) an error will be shown to the end-user. (optional)
    flow = "flow_example" # str | The Flow ID  format: uuid (optional)
    submit_self_service_recovery_flow_with_link_method = SubmitSelfServiceRecoveryFlowWithLinkMethod(
        csrf_token="csrf_token_example",
        email="email_example",
    ) # SubmitSelfServiceRecoveryFlowWithLinkMethod |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Complete Recovery Flow with Link Method
        api_instance.submit_self_service_recovery_flow_with_link_method(token=token, flow=flow, submit_self_service_recovery_flow_with_link_method=submit_self_service_recovery_flow_with_link_method)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_recovery_flow_with_link_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| Recovery Token  The recovery token which completes the recovery request. If the token is invalid (e.g. expired) an error will be shown to the end-user. | [optional]
 **flow** | **str**| The Flow ID  format: uuid | [optional]
 **submit_self_service_recovery_flow_with_link_method** | [**SubmitSelfServiceRecoveryFlowWithLinkMethod**](SubmitSelfServiceRecoveryFlowWithLinkMethod.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**400** | recoveryFlow |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_self_service_registration_flow**
> RegistrationViaApiResponse submit_self_service_registration_flow(flow)

Submit a Registration Flow

Use this endpoint to complete a registration flow by sending an identity's traits and password. This endpoint behaves differently for API and browser flows.  API flows expect `application/json` to be sent in the body and respond with HTTP 200 and a application/json body with the created identity success - if the session hook is configured the `session` and `session_token` will also be included; HTTP 302 redirect to a fresh registration flow if the original flow expired with the appropriate error messages set; HTTP 400 on form validation errors.  Browser flows expect `application/x-www-form-urlencoded` to be sent in the body and responds with a HTTP 302 redirect to the post/after registration URL or the `return_to` value if it was set and if the registration succeeded; a HTTP 302 redirect to the registration UI URL with the flow ID containing the validation errors otherwise.  More information can be found at [Ory Kratos User Login and User Registration Documentation](https://www.ory.sh/docs/next/kratos/self-service/flows/user-login-user-registration).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.submit_self_service_registration_flow import SubmitSelfServiceRegistrationFlow
from ory_kratos_client.model.registration_flow import RegistrationFlow
from ory_kratos_client.model.registration_via_api_response import RegistrationViaApiResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    flow = "flow_example" # str | The Registration Flow ID  The value for this parameter comes from `flow` URL Query parameter sent to your application (e.g. `/registration?flow=abcde`).
    submit_self_service_registration_flow = SubmitSelfServiceRegistrationFlow() # SubmitSelfServiceRegistrationFlow |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Submit a Registration Flow
        api_response = api_instance.submit_self_service_registration_flow(flow)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_registration_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Submit a Registration Flow
        api_response = api_instance.submit_self_service_registration_flow(flow, submit_self_service_registration_flow=submit_self_service_registration_flow)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_registration_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | **str**| The Registration Flow ID  The value for this parameter comes from &#x60;flow&#x60; URL Query parameter sent to your application (e.g. &#x60;/registration?flow&#x3D;abcde&#x60;). |
 **submit_self_service_registration_flow** | [**SubmitSelfServiceRegistrationFlow**](SubmitSelfServiceRegistrationFlow.md)|  | [optional]

### Return type

[**RegistrationViaApiResponse**](RegistrationViaApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | registrationViaApiResponse |  -  |
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**400** | registrationFlow |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_self_service_settings_flow**
> SettingsViaApiResponse submit_self_service_settings_flow(flow)

Complete Settings Flow

Use this endpoint to complete a settings flow by sending an identity's updated password. This endpoint behaves differently for API and browser flows.  API-initiated flows expect `application/json` to be sent in the body and respond with HTTP 200 and an application/json body with the session token on success; HTTP 302 redirect to a fresh settings flow if the original flow expired with the appropriate error messages set; HTTP 400 on form validation errors. HTTP 401 when the endpoint is called without a valid session token. HTTP 403 when `selfservice.flows.settings.privileged_session_max_age` was reached. Implies that the user needs to re-authenticate.  Browser flows expect `application/x-www-form-urlencoded` to be sent in the body and responds with a HTTP 302 redirect to the post/after settings URL or the `return_to` value if it was set and if the flow succeeded; a HTTP 302 redirect to the Settings UI URL with the flow ID containing the validation errors otherwise. a HTTP 302 redirect to the login endpoint when `selfservice.flows.settings.privileged_session_max_age` was reached.  More information can be found at [Ory Kratos User Settings & Profile Management Documentation](../self-service/flows/user-settings).

### Example

* Bearer Authentication (sessionToken):
```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.settings_via_api_response import SettingsViaApiResponse
from ory_kratos_client.model.submit_self_service_settings_flow import SubmitSelfServiceSettingsFlow
from ory_kratos_client.model.settings_flow import SettingsFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: sessionToken
configuration = ory_kratos_client.Configuration(
    access_token = 'YOUR_BEARER_TOKEN'
)

# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    flow = "flow_example" # str | The Settings Flow ID  The value for this parameter comes from `flow` URL Query parameter sent to your application (e.g. `/settings?flow=abcde`).
    x_session_token = "X-Session-Token_example" # str | The Session Token of the Identity performing the settings flow. (optional)
    submit_self_service_settings_flow = SubmitSelfServiceSettingsFlow() # SubmitSelfServiceSettingsFlow |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Complete Settings Flow
        api_response = api_instance.submit_self_service_settings_flow(flow)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_settings_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Complete Settings Flow
        api_response = api_instance.submit_self_service_settings_flow(flow, x_session_token=x_session_token, submit_self_service_settings_flow=submit_self_service_settings_flow)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_settings_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | **str**| The Settings Flow ID  The value for this parameter comes from &#x60;flow&#x60; URL Query parameter sent to your application (e.g. &#x60;/settings?flow&#x3D;abcde&#x60;). |
 **x_session_token** | **str**| The Session Token of the Identity performing the settings flow. | [optional]
 **submit_self_service_settings_flow** | [**SubmitSelfServiceSettingsFlow**](SubmitSelfServiceSettingsFlow.md)|  | [optional]

### Return type

[**SettingsViaApiResponse**](SettingsViaApiResponse.md)

### Authorization

[sessionToken](../README.md#sessionToken)

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | settingsViaApiResponse |  -  |
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**400** | settingsFlow |  -  |
**401** | jsonError |  -  |
**403** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_self_service_verification_flow**
> submit_self_service_verification_flow(flow)

Complete Verification Flow

Use this endpoint to complete a verification flow. This endpoint behaves differently for API and browser flows and has several states:  `choose_method` expects `flow` (in the URL query) and `email` (in the body) to be sent and works with API- and Browser-initiated flows. For API clients it either returns a HTTP 200 OK when the form is valid and HTTP 400 OK when the form is invalid and a HTTP 302 Found redirect with a fresh verification flow if the flow was otherwise invalid (e.g. expired). For Browser clients it returns a HTTP 302 Found redirect to the Verification UI URL with the Verification Flow ID appended. `sent_email` is the success state after `choose_method` when using the `link` method and allows the user to request another verification email. It works for both API and Browser-initiated flows and returns the same responses as the flow in `choose_method` state. `passed_challenge` expects a `token` to be sent in the URL query and given the nature of the flow (\"sending a verification link\") does not have any API capabilities. The server responds with a HTTP 302 Found redirect either to the Settings UI URL (if the link was valid) and instructs the user to update their password, or a redirect to the Verification UI URL with a new Verification Flow ID which contains an error message that the verification link was invalid.  More information can be found at [Ory Kratos Email and Phone Verification Documentation](https://www.ory.sh/docs/kratos/selfservice/flows/verify-email-account-activation).

### Example

```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.verification_flow import VerificationFlow
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    flow = "flow_example" # str | The Registration Flow ID  The value for this parameter comes from `flow` URL Query parameter sent to your application (e.g. `/registration?flow=abcde`).
    body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Complete Verification Flow
        api_instance.submit_self_service_verification_flow(flow)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_verification_flow: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Complete Verification Flow
        api_instance.submit_self_service_verification_flow(flow, body=body)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->submit_self_service_verification_flow: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **flow** | **str**| The Registration Flow ID  The value for this parameter comes from &#x60;flow&#x60; URL Query parameter sent to your application (e.g. &#x60;/registration?flow&#x3D;abcde&#x60;). |
 **body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Empty responses are sent when, for example, resources are deleted. The HTTP status code for empty responses is typically 201. |  -  |
**400** | verificationFlow |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **to_session**
> Session to_session()

Check Who the Current HTTP Session Belongs To

Uses the HTTP Headers in the GET request to determine (e.g. by using checking the cookies) who is authenticated. Returns a session object in the body or 401 if the credentials are invalid or no credentials were sent. Additionally when the request it successful it adds the user ID to the 'X-Kratos-Authenticated-Identity-Id' header in the response.  This endpoint is useful for:  AJAX calls. Remember to send credentials and set up CORS correctly! Reverse proxies and API Gateways Server-side calls - use the `X-Session-Token` header!

### Example

* Api Key Authentication (sessionCookie):
```python
import time
import ory_kratos_client
from ory_kratos_client.api import public_api
from ory_kratos_client.model.json_error import JsonError
from ory_kratos_client.model.session import Session
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ory_kratos_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: sessionCookie
configuration.api_key['sessionCookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['sessionCookie'] = 'Bearer'

# Enter a context with an instance of the API client
with ory_kratos_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = public_api.PublicApi(api_client)
    x_session_token = "X-Session-Token_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check Who the Current HTTP Session Belongs To
        api_response = api_instance.to_session(x_session_token=x_session_token)
        pprint(api_response)
    except ory_kratos_client.ApiException as e:
        print("Exception when calling PublicApi->to_session: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_session_token** | **str**|  | [optional]

### Return type

[**Session**](Session.md)

### Authorization

[sessionCookie](../README.md#sessionCookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | session |  -  |
**401** | jsonError |  -  |
**500** | jsonError |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

