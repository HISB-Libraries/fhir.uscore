# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient
Release: STU4
Version: 4.0.0
"""

import os

from ..profiles import uscorepatient


def test_us_core_patient_1():
    '''
    Test patient example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Patient-example.json'))
    us_core_patient = uscorepatient.USCorePatient.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_patient.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient'


def test_us_core_patient_2():
    '''
    Test patient child example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Patient-child-example.json'))
    us_core_patient = uscorepatient.USCorePatient.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_patient.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient'


def test_us_core_patient_3():
    '''
    Test patient infant example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Patient-infant-example.json'))
    us_core_patient = uscorepatient.USCorePatient.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_patient.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient'
