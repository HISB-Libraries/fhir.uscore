# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-location
Release: STU4
Version: 4.0.0
"""

from pydantic import validator, Field

from fhir.resources.location import Location
from fhir.resources import fhirtypes


class USCoreLocation(Location):
    '''Defines basic constraints and extensions on the Location resource for use with other US Core resources'''

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name of the location as used by humans",
        description="Name of the location as used by humans. Does not need to be unique.",
        # if property is element of this resource.
        element_property=True,
    )

    managingOrganization: fhirtypes.ReferenceType = Field(
        None,
        alias="managingOrganization",
        title="Organization responsible for provisioning and upkeep",
        description=(
            "The organization responsible for the provisioning and upkeep of the "
            "location."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Listed Resource Type(s) should be allowed as Reference.
        enum_reference_types=["USCoreOrganization"],
    )

    @validator('meta')
    def check_meta(cls, meta):
        '''profile url set properly'''
        profile_url = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-location"
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
