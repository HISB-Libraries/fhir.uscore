# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-vital-signs
Release: STU4
Version: 4.0.0
"""

import typing
import os

from pydantic import validator, Field, root_validator

from fhir.resources.observation import Observation
from fhir.resources.valueset import ValueSet
from fhir.resources import fhirtypes

from ..helpers import validate_code_tx_server


class USCoreVitalSigns(Observation):
    '''Defines constraints on the Observation resource to represent vital signs observations. This profile is used as the base definition for the other US Core Vital Signs Profiles and based on the FHIR VitalSigns Profile.'''

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/observation-category', 'code': 'vital-signs'}]}],
        alias="category",
        title="Classification of  type of observation",
        description="A code that classifies the general type of observation being made.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Type of observation (code / type)",
        description=(
            "Describes what was observed. Sometimes this is called the observation "
            '"name".'
        ),
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who and/or what the observation is about",
        description=(
            "The patient, or group of patients, location, or device this "
            "observation is about and into whose record the observation is placed. "
            "If the actual focus of the observation is different from the subject "
            "(or a sample of, part, or region of the subject), the `focus` element "
            "or the `code` itself specifies the actual focus of the observation."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["USCorePatient"],
    )

    @validator('category')
    def check_catgory(cls, categories):
        for category in categories:
            if category.coding[0].system != 'http://terminology.hl7.org/CodeSystem/observation-category' and category.coding[0].code != 'vital-signs':
                raise ValueError('Category.coding.system must be http://terminology.hl7.org/CodeSystem/observation-category and Category.coding.code must be vital-signs')
            elif category.coding[0].system != 'http://terminology.hl7.org/CodeSystem/observation-category':
                raise ValueError('Category.coding.system must be http://terminology.hl7.org/CodeSystem/observation-category')
            elif category.coding[0].code != 'vital-signs':
                raise ValueError('Category.coding.code must be vital-signs')
        return categories

    @validator('code')
    def check_code(cls, code):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/ValueSet-us-core-vital-signs.json'))
        vital_signs_vs = ValueSet.parse_file(filename, content_type='application/json', encoding='utf-8')
        cc_check = validate_code_tx_server(code, vital_signs_vs)
        if cc_check:
            raise cc_check
        return code

    @validator('component')
    def check_comoponent_code(cls, components):
        for component in components:
            filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/ValueSet-us-core-vital-signs.json'))
            vital_signs_vs = ValueSet.parse_file(filename, content_type='application/json', encoding='utf-8')
            cc_check = validate_code_tx_server(component.code, vital_signs_vs)
            if cc_check:
                raise cc_check
        return components

    @root_validator(allow_reuse=True)
    def check_effective_and_value(cls, values: typing.Dict[str, typing.Any]):
        effective_bool = False
        for k, v in values.items():
            if not v:
                continue
            if k.startswith('effective') and k not in ['effectiveDateTime', 'effectivePeriod']:
                raise ValueError('Only effectiveDateTime or effectivePeriod is allowed in the US Core Vital Signs resource')
            if k in ['effectiveDateTime', 'effectivePeriod']:
                if not effective_bool:
                    effective_bool = True
                else:
                    raise ValueError('Only one of effectiveDateTime or effectivePeriod is allowed')
        return values
