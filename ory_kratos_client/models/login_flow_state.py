# coding: utf-8

"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more. 

    The version of the OpenAPI document: v1.3.5
    Contact: office@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LoginFlowState(str, Enum):
    """
    The experimental state represents the state of a login flow. This field is EXPERIMENTAL and subject to change!
    """

    """
    allowed enum values
    """
    CHOOSE_METHOD = 'choose_method'
    SENT_EMAIL = 'sent_email'
    PASSED_CHALLENGE = 'passed_challenge'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LoginFlowState from a JSON string"""
        return cls(json.loads(json_str))


