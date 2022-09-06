# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location
Release: STU4
Version: 4.0.0
"""

import os

from ..profiles import uscorelocation


def test_us_core_location_1():
    '''
    Test location example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Location-hl7east.json'))
    us_core_location = uscorelocation.USCoreLocation.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_location.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-location'
