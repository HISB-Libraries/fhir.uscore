# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-smokingstatus
Release: STU4
Version: 4.0.0
"""

import os

from ..profiles import uscoresmokingstatus


def test_us_core_smokingstatus_1():
    '''
    Test smoking status example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Observation-some-day-smoker.json'))
    us_core_smoking_status = uscoresmokingstatus.USCoreSmokingStatus.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_smoking_status.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-smokingstatus'
