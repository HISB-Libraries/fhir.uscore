# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner
Release: STU4
Version: 4.0.0
"""

import typing

from pydantic import validator, Field

from fhir.resources.practitioner import Practitioner
from fhir.resources import fhirtypes


class USCorePractitioner(Practitioner):
    '''Defines basic constraints and extensions on the Practitioner resource for use with other US Core resources'''

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        ...,
        alias="identifier",
        title="An identifier for this qualification for the practitioner",
        description=(
            "An identifier that applies to this person's qualification in this " "role."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    name: typing.List[fhirtypes.HumanNameType] = Field(
        ...,
        alias="name",
        title="The name(s) associated with the practitioner",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    @validator('meta')
    def check_meta(cls, meta):
        '''profile url set properly'''
        profile_url = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-practitioner"
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

    @validator('identifier')
    def check_identifier(cls, identifiers):
        for identifier in identifiers:
            if not identifier.system and identifier.value:
                raise ValueError('Identifier.system and Identifier.value is required')
            if not identifier.system:
                raise ValueError('Identifier.system is required')
            if not identifier.value:
                raise ValueError('Identifier.value is required')
        return identifiers

    @validator('name')
    def check_name(cls, names):
        for name in names:
            if not name.family:
                raise ValueError('Name.family is required')
        return names
