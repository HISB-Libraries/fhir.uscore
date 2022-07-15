# -*- coding: utf-8 -*-
"""
Profile: http://hl7.org/fhir/us/core/StructureDefinition/us-core-race
Release: STU4
Version: 4.0.0
"""

import typing
import os

from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.extension import Extension
from fhir.resources.valueset import ValueSet
from fhir.resources import fhirtypes

from pydantic import Field, root_validator, validator

from ..helpers import check_cc_in_valueset


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

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

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

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        yield cls.validate

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

    @classmethod
    def __get_validators__(cls):
        # one or more validators may be yielded which will be called in the
        # order to validate the input, each validator will receive as an input
        # the value returned from the previous validator
        # This is needed when defining custom types in classes
        yield cls.validate

    @root_validator(allow_reuse=True)
    def validate_only_value_string(cls, values: typing.Dict[str, typing.Any]):
        '''
        This extension only allows a valueString, none of the other value[x] choices
        '''

        if len(list(filter(lambda x: x is not None, list(values.values())))) > 3:
            raise ValueError("Theres too many elements in this extension, it should only contain url and valueString")

        return values


class USCoreRace(Extension):
    '''
    US Core Race Extension
    '''

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

    extension: typing.List[typing.Union[USCoreRaceOMBCategory, USCoreRaceDetailed, USCoreRaceText]] = Field(
        None,
        alias="extension",
        title="Additional content defined by implementations",
        description=(
            "May be used to represent additional information that is not part of "
            "the basic definition of the element. To make the use of extensions "
            "safe and manageable, there is a strict set of governance  applied to "
            "the definition and use of extensions. Though any implementer can "
            "define an extension, there is a set of requirements that SHALL be met "
            "as part of the definition of the extension."
        ),
        discriminator='url',
        # if property is element of this resource.
        element_property=True,

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
                cc_check = check_cc_in_valueset(CodeableConcept(coding=[omb_category_ext.valueCoding]), omb_race_category_vs)
                if isinstance(cc_check, ValueError):
                    raise cc_check
            elif extension_obj.url == 'detailed':
                # TODO: this cannot be done with the package-downloaded ValueSet, need to find a work-around
                pass
        if not text_extension:
            raise ValueError('text extension required for US Core Race Extension')

        return extensions
