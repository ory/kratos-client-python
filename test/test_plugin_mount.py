"""
    Ory Kratos API

    Documentation for all public and administrative Ory Kratos APIs. Public and administrative APIs are exposed on different ports. Public APIs can face the public internet without any protection while administrative APIs should never be exposed without prior authorization. To protect the administative API port you should use something like Nginx, Ory Oathkeeper, or any other technology capable of authorizing incoming requests.   # noqa: E501

    The version of the OpenAPI document: v0.0.0-alpha.38
    Contact: hi@ory.sh
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import ory_kratos_client
from ory_kratos_client.model.plugin_mount import PluginMount


class TestPluginMount(unittest.TestCase):
    """PluginMount unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPluginMount(self):
        """Test PluginMount"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PluginMount()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
