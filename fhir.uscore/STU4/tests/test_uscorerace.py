# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-race
Release: STU4
Version: 4.0.0
"""

from ..extensions import uscorerace


def test_us_core_extension_1():
    '''
    First test for US Core Race Extension, this should pass
    '''

    extension_test_1 = [
        {
            "url": "ombCategory",
            "valueCoding": {
                "system": "urn:oid:2.16.840.1.113883.6.238",
                "code": "2028-9",
                "display": "Asian"
            }
        },
        {
            "url": "detailed",
            "valueCoding": {
                "system": "urn:oid:2.16.840.1.113883.6.238",
                "code": "2036-2",
                "display": "Filipino"
            }
        },
        {
            "url": "text",
            "valueString": "Mixed"
        }
    ]

    us_core_race_extension = uscorerace.USCoreRace(extension=extension_test_1)

    assert us_core_race_extension.url == 'http://hl7.org/fhir/us/core/StructureDefinition/us-core-race'
    for extension in us_core_race_extension.extension:
        print(type(extension))
