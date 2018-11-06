# coding: utf-8

"""
    Translator Knowledge Beacon API

    This is the Translator Knowledge Beacon web service application programming interface (API).   # noqa: E501

    OpenAPI spec version: 1.3.0
    Contact: richard@starinformatics.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

from tkbeacon import BeaconClient, KnowledgeSource
from tkbeacon.rest import ApiException


class TestBeaconClient(unittest.TestCase):
    """BeaconClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testGetConcepts(self):
        b = BeaconClient(KnowledgeSource.SMPDB)
        concepts = b.get_concepts(keywords='H2')

        if len(concepts) < 1:
            self.fail('The response should not be empty')

        for concept in concepts:
            if 'H2' not in concept.name:
                self.fail('get_concepts filter keywords=["H2"] failed for {}'.format(concept.id))

        concepts = b.get_concepts(categories='protein', size=30)

        if len(concepts) != 30:
            self.fail('Expected len(concepts)==30, got: {}'.format(len(concepts)))

        for concept in concepts:
            if 'protein' not in concept.categories:
                self.fail('get_concepts filter categories=["protein"] failed for {}'.format(concept.id))


if __name__ == '__main__':
    unittest.main()
