# coding: utf-8

"""
    BVNK API Endpoints

    The BVNK API is designed to facilitate seamless and secure transactions including payments, channels, anddigital wallet transactions.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from openapi_client import schemas  # noqa: F401


class PayRequestDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    DTO required to create a payment in or a payment out
    """


    class MetaOapg:
        required = {
            "reference",
            "amount",
            "merchantId",
            "currency",
            "type",
        }
        
        class properties:
            
            
            class merchantId(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
                    min_length = 6
            
            
            class amount(
                schemas.NumberSchema
            ):
            
            
                class MetaOapg:
                    exclusive_minimuminclusive_minimum = 0
            
            
            class currency(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
                    min_length = 2
            
            
            class reference(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
                    min_length = 6
        
            @staticmethod
            def type() -> typing.Type['DirectionDto']:
                return DirectionDto
            expiryMinutes = schemas.IntSchema
            returnUrl = schemas.StrSchema
        
            @staticmethod
            def payInDetails() -> typing.Type['PayInDetailDto']:
                return PayInDetailDto
        
            @staticmethod
            def payOutDetails() -> typing.Type['PayOutDetailDto']:
                return PayOutDetailDto
            __annotations__ = {
                "merchantId": merchantId,
                "amount": amount,
                "currency": currency,
                "reference": reference,
                "type": type,
                "expiryMinutes": expiryMinutes,
                "returnUrl": returnUrl,
                "payInDetails": payInDetails,
                "payOutDetails": payOutDetails,
            }
    
    reference: MetaOapg.properties.reference
    amount: MetaOapg.properties.amount
    merchantId: MetaOapg.properties.merchantId
    currency: MetaOapg.properties.currency
    type: 'DirectionDto'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["merchantId"]) -> MetaOapg.properties.merchantId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'DirectionDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiryMinutes"]) -> MetaOapg.properties.expiryMinutes: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["returnUrl"]) -> MetaOapg.properties.returnUrl: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payInDetails"]) -> 'PayInDetailDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payOutDetails"]) -> 'PayOutDetailDto': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["merchantId", "amount", "currency", "reference", "type", "expiryMinutes", "returnUrl", "payInDetails", "payOutDetails", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["merchantId"]) -> MetaOapg.properties.merchantId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reference"]) -> MetaOapg.properties.reference: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'DirectionDto': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiryMinutes"]) -> typing.Union[MetaOapg.properties.expiryMinutes, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["returnUrl"]) -> typing.Union[MetaOapg.properties.returnUrl, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payInDetails"]) -> typing.Union['PayInDetailDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payOutDetails"]) -> typing.Union['PayOutDetailDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["merchantId", "amount", "currency", "reference", "type", "expiryMinutes", "returnUrl", "payInDetails", "payOutDetails", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        reference: typing.Union[MetaOapg.properties.reference, str, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        merchantId: typing.Union[MetaOapg.properties.merchantId, str, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        type: 'DirectionDto',
        expiryMinutes: typing.Union[MetaOapg.properties.expiryMinutes, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        returnUrl: typing.Union[MetaOapg.properties.returnUrl, str, schemas.Unset] = schemas.unset,
        payInDetails: typing.Union['PayInDetailDto', schemas.Unset] = schemas.unset,
        payOutDetails: typing.Union['PayOutDetailDto', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PayRequestDto':
        return super().__new__(
            cls,
            *_args,
            reference=reference,
            amount=amount,
            merchantId=merchantId,
            currency=currency,
            type=type,
            expiryMinutes=expiryMinutes,
            returnUrl=returnUrl,
            payInDetails=payInDetails,
            payOutDetails=payOutDetails,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.direction_dto import DirectionDto
from openapi_client.model.pay_in_detail_dto import PayInDetailDto
from openapi_client.model.pay_out_detail_dto import PayOutDetailDto
