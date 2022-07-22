# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole
Release: STU4
Version: 4.0.0
"""

import os

from fhir.resources.bundle import Bundle

from ..profiles import uscorepractitionerrole


def test_us_core_practitionerrole_1():
    '''
    Test practitionerrole example from US Core IG (this should pass)
    '''

    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/example/Bundle-66c8856b-ba11-4876-8aa8-467aad8c11a2.json'))
    bundle = Bundle.parse_file(filename, content_type="application/json", encoding="utf-8")
    us_core_practitioner = uscorepractitionerrole.USCorePractitionerRole(**bundle.entry[0].resource.dict())

    assert us_core_practitioner.meta.profile[0] == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole'
