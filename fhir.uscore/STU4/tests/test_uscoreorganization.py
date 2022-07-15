# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location
Release: STU4
Version: 4.0.0
"""

import os

from ..profiles import uscoreorganization


def test_us_core_organization_1():
    '''
    Test Acme Lab organization example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Organization-acme-lab.json'))
    us_core_organization = uscoreorganization.USCoreOrganization.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_organization.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization'


def test_us_core_organization_2():
    '''
    Test organization example 2 from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Organization-example-organization-2.json'))
    us_core_organization = uscoreorganization.USCoreOrganization.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_organization.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization'


def test_us_core_organization_3():
    '''
    Test Saint Luke organization example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Organization-saint-luke-w-endpoint.json'))
    us_core_organization = uscoreorganization.USCoreOrganization.parse_file(filename, content_type="application/json", encoding="utf-8")

    assert us_core_organization.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization'
