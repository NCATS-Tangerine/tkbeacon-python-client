# coding: utf-8

"""
    Translator Knowledge Beacon API

    This is the Translator Knowledge Beacon web service application programming interface (API).   # noqa: E501

    The version of the OpenAPI document: 1.3.0
    Contact: richard@starinformatics.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tkbeacon
from tkbeacon.models.beacon_knowledge_map_predicate import BeaconKnowledgeMapPredicate  # noqa: E501
from tkbeacon.rest import ApiException

class TestBeaconKnowledgeMapPredicate(unittest.TestCase):
    """BeaconKnowledgeMapPredicate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test BeaconKnowledgeMapPredicate
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tkbeacon.models.beacon_knowledge_map_predicate.BeaconKnowledgeMapPredicate()  # noqa: E501
        if include_optional :
            return BeaconKnowledgeMapPredicate(
                edge_label = '0', 
                relation = '0', 
                negated = True
            )
        else :
            return BeaconKnowledgeMapPredicate(
        )

    def testBeaconKnowledgeMapPredicate(self):
        """Test BeaconKnowledgeMapPredicate"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
