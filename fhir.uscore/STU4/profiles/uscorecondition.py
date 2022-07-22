# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition
Release: STU4
Version: 4.0.0
"""

import typing
import os

from pydantic import validator, Field

from fhir.resources.condition import Condition
from fhir.resources.valueset import ValueSet
from fhir.resources import fhirtypes

from ..helpers import check_cc_in_valueset, validate_code_tx_server


class USCoreCondition(Condition):
    '''Defines constraints and extensions on the Condition resource for the minimal set of data to query and retrieve problems and health concerns information.'''

    meta: fhirtypes.MetaType = Field(
        {"profile": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"]},
        alias="meta",
        title="Metadata about the resource",
        description=(
            "The metadata about the resource. This is content that is maintained by"
            " the infrastructure. Changes to the content might not always be "
            "associated with version changes to the resource."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    category: typing.List[fhirtypes.CodeableConceptType] = Field(
        ...,
        alias="category",
        title="problem-list-item | encounter-diagnosis | health-concern | 16100001",
        description="A category assigned to the condition.",
        # if property is element of this resource.
        element_property=True,
    )

    code: fhirtypes.CodeableConceptType = Field(
        ...,
        alias="code",
        title="Identification of the condition, problem or diagnosis",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    subject: fhirtypes.ReferenceType = Field(
        ...,
        alias="subject",
        title="Who has the condition?",
        description=(
            "Indicates the patient or group who the condition record is associated "
            "with."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["USCorePatient"],
    )

    @validator('meta')
    def check_meta(cls, meta):
        '''profile url set properly'''
        profile_url = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-condition"
        meta_dict = meta.dict()
        if meta is None:
            raise ValueError('meta.profile must exist')
        else:
            if 'profile' not in meta_dict:
                raise ValueError('meta.profile must exist')
            elif isinstance(meta_dict["profile"], list):
                for profile in meta_dict["profile"]:
                    if not isinstance(profile, str):
                        raise TypeError("profile.meta elements must be str")
                if profile_url not in meta_dict["profile"]:
                    raise ValueError("Missing profile url from meta.profile")
            else:
                raise TypeError('meta.profile must be list')
        return meta

    @validator('category')
    def check_category(cls, category):
        '''Category has one of allowed CodeableConcepts'''
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/ValueSet-us-core-condition-category.json'))
        us_core_condition_category = ValueSet.parse_file(filename, content_type="application/json", encoding="utf-8")
        for single in category:
            cc_check = check_cc_in_valueset(single, us_core_condition_category)
            if isinstance(cc_check, ValueError):
                raise cc_check
        return category

    @validator('code')
    def check_code(cls, code):
        '''Code has one of allowed CodeableConcepts'''
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/ValueSet-us-core-condition-code.json'))
        us_core_condition_code = ValueSet.parse_file(filename, content_type="application/json", encoding="utf-8")
        cc_check = validate_code_tx_server(code, us_core_condition_code)
        if isinstance(cc_check, ValueError):
            raise cc_check
        return code
