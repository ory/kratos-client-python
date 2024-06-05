# coding: utf-8

"""
    Ory Identities API

    This is the API specification for Ory Identities with features such as registration, login, recovery, account verification, profile settings, password reset, identity management, session management, email and sms delivery, and more. 

    The version of the OpenAPI document: v1.2.0
    Contact: office@ory.sh
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AuthenticatorAssuranceLevel(str, Enum):
    """
    The authenticator assurance level can be one of \"aal1\", \"aal2\", or \"aal3\". A higher number means that it is harder for an attacker to compromise the account.  Generally, \"aal1\" implies that one authentication factor was used while AAL2 implies that two factors (e.g. password + TOTP) have been used.  To learn more about these levels please head over to: https://www.ory.sh/kratos/docs/concepts/credentials
    """

    """
    allowed enum values
    """
    AAL0 = 'aal0'
    AAL1 = 'aal1'
    AAL2 = 'aal2'
    AAL3 = 'aal3'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AuthenticatorAssuranceLevel from a JSON string"""
        return cls(json.loads(json_str))


