# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient
Release: STU4
Version: 4.0.0
"""

import typing

from pydantic import validator, Field

from fhir.resources.patient import Patient
from fhir.resources import fhirtypes

from ..extensions import uscorerace, uscoreethnicity, uscorebirthsex


class USCorePatient(Patient):
    '''Defines constraints and extensions on the patient resource for the minimal set of data to query and retrieve patient demographic information.'''

    meta: fhirtypes.MetaType = Field(
        {"profile": ["http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"]},
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

    extension: typing.List[typing.Union[uscorerace.USCoreRace, uscoreethnicity.USCoreEthnicity, uscorebirthsex.USCoreBirthSex]] = Field(
        None,
        alias="extension",
        title="Additional content defined by implementations",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the resource. To make the use of extensions "
            "safe and manageable, there is a strict set of governance  applied to "
            "the definition and use of extensions. Though any implementer can "
            "define an extension, there is a set of requirements that SHALL be met "
            "as part of the definition of the extension."
        ),
        # if property is element of this resource.
        element_property=True,
    )

    gender: fhirtypes.Code = Field(
        ...,
        alias="gender",
        title="male | female | other | unknown",
        description=(
            "Administrative Gender - the gender that the patient is considered to "
            "have for administration and record keeping purposes."
        ),
        # if property is element of this resource.
        element_property=True,
        # note: Enum values can be used in validation,
        # but use in your own responsibilities, read official FHIR documentation.
        enum_values=["male", "female", "other", "unknown"],
    )

    identifier: typing.List[fhirtypes.IdentifierType] = Field(
        ...,
        alias="identifier",
        title="An identifier for this patient",
        description=None,
        # if property is element of this resource.
        element_property=True,
    )

    name: typing.List[fhirtypes.HumanNameType] = Field(
        ...,
        alias="name",
        title="A name associated with the patient",
        description="A name associated with the individual.",
        # if property is element of this resource.
        element_property=True,
    )

    @validator('identifier')
    def check_identifier(cls, identifiers):
        '''Identifier 1..*, Identifier.system 1..1, Identifier.value 1..1'''
        for identifier in identifiers:
            if identifier.system is None and identifier.value is None:
                raise ValueError('system and value are required')
            elif identifier.system is None:
                raise ValueError('system is required')
            elif identifier.value is None:
                raise ValueError('value is required')
        return identifiers

    @validator('telecom')
    def check_telecom(cls, telecoms):
        '''telecom 0..*, telecom.system 1..1, telecom.value 1..1'''
        for telecom in telecoms:
            if telecom.system is None and telecom.value is None:
                raise ValueError('system and value are required')
            elif telecom.system is None:
                raise ValueError('system is required')
            elif telecom.value is None:
                raise ValueError('value is required')
        return telecoms

    @validator('meta')
    def check_meta(cls, meta):
        '''profile url set properly'''
        profile_url = "http://hl7.org/fhir/us/core/StructureDefinition/us-core-patient"
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
