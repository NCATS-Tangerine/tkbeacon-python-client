#!/usr/bin/env python

from __future__ import print_function
from tkbeacon import build, KnowledgeSource
from tkbeacon.rest import ApiException

# create an instance of the BeaconApi class pointing at the remote SMPDB beacon
b = build(KnowledgeSource.SMPDB)

try:
  concepts = b.get_concepts(categories=['protein'], size=10)

  for concept in concepts:
    print(concept.id, concept.name)

  print('All results are proteins:', all('protein' in concept.categories for concept in concepts))

except ApiException as e:
  print("Exception when calling BeaconApi->get_concepts: %s\n" % e)

