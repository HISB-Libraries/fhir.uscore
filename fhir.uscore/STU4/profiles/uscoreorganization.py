# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization
Release: STU4
Version: 4.0.0
"""

from pydantic import validator, Field

from fhir.resources.organization import Organization
from fhir.resources import fhirtypes


class USCoreOrganization(Organization):
    '''Defines basic constraints and extensions on the Organization resource for use with other US Core resources'''

    active: bool = Field(
        ...,
        alias="active",
        title="Whether the organization's record is still in active use",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: fhirtypes.String = Field(
        ...,
        alias="name",
        title="Name used for the organization",
        description="A name associated with the organization.",
        # if property is element of this resource.
        element_property=True,
    )

    @validator('meta')
    def check_meta(cls, meta):
        '''profile url set properly'''
        profile_url = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-organization"
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

    @validator('address')
    def check_address_line(cls, addresses):
        for address in addresses:
            if address.line and len(address.line) > 4:
                raise ValueError('There is a maximum cardinality of 4 for Address.line')
        return addresses
