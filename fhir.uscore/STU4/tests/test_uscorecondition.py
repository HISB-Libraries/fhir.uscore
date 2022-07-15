# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition
Release: STU4
Version: 4.0.0
"""

import os

from ..profiles import uscorecondition


def test_us_core_condition_1():
    '''
    Test condition example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Condition-example.json'))
    us_core_condition = uscorecondition.USCoreCondition.parse_file(filename, content_type='application/json', encoding='utf-8')

    assert us_core_condition.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition'


def test_us_core_condition_2():
    '''
    Test condition hc1 from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Condition-hc1.json'))
    us_core_condition = uscorecondition.USCoreCondition.parse_file(filename, content_type='application/json', encoding='utf-8')

    assert us_core_condition.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition'
