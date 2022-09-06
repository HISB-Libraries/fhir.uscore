# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole
Release: STU4
Version: 4.0.0
"""

import typing

from pydantic import validator, Field

from fhir.resources.practitionerrole import PractitionerRole
from fhir.resources import fhirtypes


class USCorePractitionerRole(PractitionerRole):
    '''The practitioner roles referenced in the US Core profiles.'''

    organization: fhirtypes.ReferenceType = Field(
        None,
        alias="organization",
        title="Organization where the roles are available",
        description="The organization where the Practitioner performs the roles associated.",
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["USCoreOrganization"],
    )

    practitioner: fhirtypes.ReferenceType = Field(
        None,
        alias="practitioner",
        title=(
            "Practitioner that is able to provide the defined services for the "
            "organization"
        ),
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["USCorePractitioner"],
    )

    location: typing.List[fhirtypes.ReferenceType] = Field(
        None,
        alias="location",
        title="The location(s) at which this practitioner provides care",
        description=None,
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["USCoreLocation"],
    )

    @validator('meta')
    def check_meta(cls, meta):
        '''profile url set properly'''
        profile_url = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitionerrole"
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

    @validator('code')
    def check_code(cls, codes):
        for code in codes:
            if code.coding[0].system != 'http://nucc.org/provider-taxonomy':
                raise ValueError(f'Code {code.coding[0].code} must be from system http://nucc.org/provider-taxonomy')
        return codes

    @validator('specialty')
    def check_specialty(cls, specialties):
        for specialty in specialties:
            if specialty.coding[0].system != 'http://nucc.org/provider-taxonomy':
                raise ValueError('Specialty.coding.system must be http://nucc.org/provider-taxonomy')
        return specialties

    @validator('telecom')
    def check_telecom(cls, telecoms):
        '''telecom 0..*, telecom.system 1..1, telecom.value 1..1'''
        for telecom in telecoms:
            if telecom.system is None and telecom.value is None:
                raise ValueError('Telecom.system and Telecom.value are required')
            elif telecom.system is None:
                raise ValueError('Telecom.system is required')
            elif telecom.value is None:
                raise ValueError('Telecom.value is required')
        return telecoms
