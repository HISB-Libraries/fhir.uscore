# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient
Release: STU4
Version: 4.0.0
"""

import os

from ..profiles import uscorepatient
from fhir.resources.patient import Patient


def test_us_core_patient_1():
    '''
    Test patient example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Patient-example.json'))
    patient_resource = Patient.parse_file(filename, content_type="application/json", encoding="utf-8")

    us_core_patient = uscorepatient.USCorePatient(**patient_resource.dict())

    assert us_core_patient.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient'
