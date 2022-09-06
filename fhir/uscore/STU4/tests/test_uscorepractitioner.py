# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner
Release: STU4
Version: 4.0.0
"""

import os

from ..profiles import uscorepractitioner


def test_us_core_practitioner_1():
    '''
    Test practitioner 1 example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Practitioner-practitioner-1.json'))
    us_core_practitioner = uscorepractitioner.USCorePractitioner.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_practitioner.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner'


def test_us_core_practitioner_2():
    '''
    Test practitioner 2 example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Practitioner-practitioner-2.json'))
    us_core_practitioner = uscorepractitioner.USCorePractitioner.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_practitioner.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner'
