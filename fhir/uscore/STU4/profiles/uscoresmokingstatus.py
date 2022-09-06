# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-smokingstatus
Release: STU4
Version: 4.0.0
"""

import typing
import os

from pydantic import validator, Field, root_validator

from fhir.resources.observation import Observation
from fhir.resources.valueset import ValueSet
from fhir.resources import fhirtypes

from ..helpers import check_cc_in_valueset


class USCoreSmokingStatus(Observation):
    '''Defines constraints and extensions on the Observation resource for the minimal set of data to query and retrieve patient's Smoking Status information.'''

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        [{'coding': [{'system': 'http://terminology.hl7.org/CodeSystem/observation-category', 'code': 'social-history'}]}],
        alias="category",
        title="Classification of  type of observation",
        description="A code that classifies the general type of observation being made.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        {'coding': [{'system': 'http://loinc.org', 'code': '72166-2', 'display': 'Tobacco smoking status'}]},
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

    effectiveDateTime: fhirtypes.DateTime = Field(
        ...,
        alias="effectiveDateTime",
        title="Clinically relevant time/time-period for observation",
        description=(
            "The time or time-period the observed value is asserted as being true. "
            "For biological subjects - e.g. human patients - this is usually called"
            ' the "physiologically relevant time". This is usually either the time '
            "of the procedure or of specimen collection, but very often the source "
            "of the date/time is not known, only the date/time itself."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e effective[x]
        one_of_many="effective",
        one_of_many_required=True,
    )

    valueCodeableConcept: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="valueCodeableConcept",
        title="Actual result",
        description=(
            "The information determined as a result of making the observation, if "
            "the information has a simple value."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
    )

    @validator('category')
    def check_catgory(cls, categories):
        for category in categories:
            if category.coding[0].system != 'http://terminology.hl7.org/CodeSystem/observation-category' and category.coding[0].code != 'social-history':
                raise ValueError('Category.coding.system must be http://terminology.hl7.org/CodeSystem/observation-category and Category.coding.code must be social-history')
            elif category.coding[0].system != 'http://terminology.hl7.org/CodeSystem/observation-category':
                raise ValueError('Category.coding.system must be http://terminology.hl7.org/CodeSystem/observation-category')
            elif category.coding[0].code != 'social-history':
                raise ValueError('Category.coding.code must be social-history')
        return categories

    @validator('code')
    def check_code(cls, code):
        if code.coding[0].system != 'http://loinc.org' and code.coding[0].code != '72166-2':
            print('\nWARNING: SmokingStatus.code has an extensible binding, therefore the validator cannot determine what is acceptable for this element')
            return code
        if code.coding[0].display != 'Tobacco smoking status':
            print(f'\nWARNING: The display was found to be {code.coding[0].display}. It should be "Tobacco smoking status"')
        return code

    @validator('valueCodeableConcept')
    def check_codeable_concept(cls, cc):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/ValueSet-Smoking-Status.json'))
        smoking_status_vs = ValueSet.parse_file(filename, content_type='application/json', encoding='utf-8')
        cc_check = check_cc_in_valueset(cc, smoking_status_vs)
        if cc_check:
            raise cc_check
        return cc

    @root_validator(allow_reuse=True)
    def check_effective_and_value(cls, values: typing.Dict[str, typing.Any]):
        for k, v in values.items():
            if not v:
                continue
            if k.startswith('effective') and k != 'effectiveDateTime':
                raise ValueError('Only effectiveDateTime is allowed in the US Core Smoking Status resource')
            if k.startswith('value') and k != 'valueCodeableConcept':
                raise ValueError('Only valueCodeableConcept is allowed in the US Core Smoking Status resource')
        return values
