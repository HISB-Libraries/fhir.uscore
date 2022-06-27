# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-race
Release: STU4
Version: 4.0.0
"""

from multiprocessing.sharedctypes import Value
import typing
import os

from fhir.resources.extension import Extension
from fhir.resources.valueset import ValueSet
from fhir.resources import fhirtypes

from pydantic import Field, root_validator, validator


class USCoreRace(Extension):
    '''
    US Core Race Extension
    '''
    # TODO: get extensions to be of the right type when it returns the object

    url: fhirtypes.Uri = Field(
        'http://hl7.org/fhir/us/core/StructureDefinition/us-core-race',
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

    @validator('extension')
    def validate_extensions(cls, extensions):
        '''
        The text extension is required in the US Core Race Extension and the only extensions
        allowed are ombCategory, detailed, and text
        '''

        text_extension = None

        for extension_obj in extensions:
            if extension_obj.url not in ['ombCategory', 'detailed', 'text']:
                raise ValueError(f'Extension {extension_obj.url} is not allowed within the US Core Race extension')
            elif extension_obj.url == 'text':
                text_extension = extension_obj
            elif extension_obj.url == 'ombCategory':
                # Do something here to check ombCategory
                omb_category_ext = USCoreRaceOMBCategory(**extension_obj.dict())
                filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'hl7.fhir.us.core#4.0.0/ValueSet-omb-race-category.json'))
                omb_race_category_vs = ValueSet.parse_file(
                    filename, content_type="application/json", encoding="utf-8")
                filtered_code_system = list(filter(lambda x: x.system == omb_category_ext.valueCoding.system, omb_race_category_vs.compose.include))
                if len(filtered_code_system) == 0:
                    raise ValueError(f'The code {omb_category_ext.valueCoding.code} from system {omb_category_ext.valueCoding.system} is not in the OMB Race Category ValueSet')
                filtered_codes = list(filter(lambda x: x.code == omb_category_ext.valueCoding.code, filtered_code_system[0].concept))
                if len(filtered_codes) == 0:
                    raise ValueError(f'Code {omb_category_ext.valueCoding.code} is not in the OMB Race Category ValueSet')
                if omb_category_ext.valueCoding.display != filtered_codes[0].display:
                    raise ValueError(f'The display for the ombCategory was found to be {omb_category_ext.valueCoding.display}. It should be {filtered_codes[0].display}')
            elif extension_obj.url == 'detailed':
                # TODO: this cannot be done with the package-downloaded ValueSet, need to find a work-around
                pass
        if not text_extension:
            raise ValueError('text extension required for US Core Race Extension')

        return extensions


class USCoreRaceOMBCategory(Extension):
    '''
    American Indian or Alaska Native|Asian|Black or African American|Native Hawaiian or Other Pacific Islander|White
    '''

    url: fhirtypes.Uri = Field(
        'ombCategory',
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

    valueCoding: fhirtypes.CodingType = Field(
        ...,
        alias="valueCoding",
        title="Value of extension",
        description=(
            "Value of extension - must be one of a constrained set of the data "
            "types (see [Extensibility](extensibility.html) for a list)."
        ),
        # if property is element of this resource.
        element_property=True,
        # Choice of Data Types. i.e value[x]
        one_of_many="value",
        one_of_many_required=True,
    )

    @root_validator(allow_reuse=True)
    def validate_only_value_coding(cls, values: typing.Dict[str, typing.Any]):
        '''
        This extension only allows a valueCoding, none of the other value[x] choices
        '''

        if len(list(filter(lambda x: x is not None, list(values.values())))) > 3:
            raise ValueError("Theres too many elements in this extension, it should only contain url and valueCoding")

        return values


class USCoreRaceDetailed(Extension):
    '''
    Extended race codes
    '''

    url: fhirtypes.Uri = Field(
        'detailed',
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

    valueCoding: fhirtypes.CodingType = Field(
        ...,
        alias="valueCoding",
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
    )

    @root_validator(allow_reuse=True)
    def validate_only_value_coding(cls, values: typing.Dict[str, typing.Any]):
        '''
        This extension only allows a valueCoding, none of the other value[x] choices
        '''

        if len(list(filter(lambda x: x is not None, list(values.values())))) > 3:
            raise ValueError("Theres too many elements in this extension, it should only contain url and valueCoding")

        return values


class USCoreRaceText(Extension):
    '''
    Race Text
    '''

    url: fhirtypes.Uri = Field(
        'text',
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

    valueString: fhirtypes.String = Field(
        ...,
        alias="valueString",
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
    )

    @root_validator(allow_reuse=True)
    def validate_only_value_string(cls, values: typing.Dict[str, typing.Any]):
        '''
        This extension only allows a valueString, none of the other value[x] choices
        '''

        if len(list(filter(lambda x: x is not None, list(values.values())))) > 3:
            raise ValueError("Theres too many elements in this extension, it should only contain url and valueString")

        return values
