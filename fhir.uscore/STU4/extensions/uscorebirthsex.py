# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex
Release: STU4
Version: 4.0.0
"""

from fhir.resources.extension import Extension
from fhir.resources import fhirtypes

from pydantic import Field


class USCoreBirthSex(Extension):
    '''
    US Core Birth Sex Extension
    '''

    url: fhirtypes.Uri = Field(
        'http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex',
        const=True,
        alias="url",
        title="identifies the meaning of the extension",
        description=(
            "Source of the definition for the extension code - a logical name or a "
            "URL."
        ),
        # if property is element of this resource.
        element_property=True,
        element_required=True
    )

    valueCode: fhirtypes.Code = Field(
        ...,
        alias="valueCode",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=False,
        enum_values=['F', 'M', 'UNK']
    )
