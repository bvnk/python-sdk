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


class GatewayTransactionDto(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Specify details about transaction (onchain or offchain) linked to the payment
    """


    class MetaOapg:
        
        class properties:
            dateCreated = schemas.Int64Schema
            dateConfirmed = schemas.Int64Schema
            hash = schemas.StrSchema
            amount = schemas.NumberSchema
            risk = schemas.DictSchema
            networkFeeCurrency = schemas.StrSchema
            networkFeeAmount = schemas.NumberSchema
            
            
            class sources(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.StrSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'sources':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
        
            @staticmethod
            def displayRate() -> typing.Type['ExchangeRateDto']:
                return ExchangeRateDto
        
            @staticmethod
            def exchangeRate() -> typing.Type['ExchangeRateDto']:
                return ExchangeRateDto
            __annotations__ = {
                "dateCreated": dateCreated,
                "dateConfirmed": dateConfirmed,
                "hash": hash,
                "amount": amount,
                "risk": risk,
                "networkFeeCurrency": networkFeeCurrency,
                "networkFeeAmount": networkFeeAmount,
                "sources": sources,
                "displayRate": displayRate,
                "exchangeRate": exchangeRate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateConfirmed"]) -> MetaOapg.properties.dateConfirmed: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["hash"]) -> MetaOapg.properties.hash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["risk"]) -> MetaOapg.properties.risk: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkFeeCurrency"]) -> MetaOapg.properties.networkFeeCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["networkFeeAmount"]) -> MetaOapg.properties.networkFeeAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sources"]) -> MetaOapg.properties.sources: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["displayRate"]) -> 'ExchangeRateDto': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exchangeRate"]) -> 'ExchangeRateDto': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["dateCreated", "dateConfirmed", "hash", "amount", "risk", "networkFeeCurrency", "networkFeeAmount", "sources", "displayRate", "exchangeRate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateCreated"]) -> typing.Union[MetaOapg.properties.dateCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateConfirmed"]) -> typing.Union[MetaOapg.properties.dateConfirmed, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["hash"]) -> typing.Union[MetaOapg.properties.hash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["risk"]) -> typing.Union[MetaOapg.properties.risk, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkFeeCurrency"]) -> typing.Union[MetaOapg.properties.networkFeeCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["networkFeeAmount"]) -> typing.Union[MetaOapg.properties.networkFeeAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sources"]) -> typing.Union[MetaOapg.properties.sources, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["displayRate"]) -> typing.Union['ExchangeRateDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exchangeRate"]) -> typing.Union['ExchangeRateDto', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["dateCreated", "dateConfirmed", "hash", "amount", "risk", "networkFeeCurrency", "networkFeeAmount", "sources", "displayRate", "exchangeRate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        dateCreated: typing.Union[MetaOapg.properties.dateCreated, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dateConfirmed: typing.Union[MetaOapg.properties.dateConfirmed, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        hash: typing.Union[MetaOapg.properties.hash, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        risk: typing.Union[MetaOapg.properties.risk, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        networkFeeCurrency: typing.Union[MetaOapg.properties.networkFeeCurrency, str, schemas.Unset] = schemas.unset,
        networkFeeAmount: typing.Union[MetaOapg.properties.networkFeeAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        sources: typing.Union[MetaOapg.properties.sources, list, tuple, schemas.Unset] = schemas.unset,
        displayRate: typing.Union['ExchangeRateDto', schemas.Unset] = schemas.unset,
        exchangeRate: typing.Union['ExchangeRateDto', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'GatewayTransactionDto':
        return super().__new__(
            cls,
            *_args,
            dateCreated=dateCreated,
            dateConfirmed=dateConfirmed,
            hash=hash,
            amount=amount,
            risk=risk,
            networkFeeCurrency=networkFeeCurrency,
            networkFeeAmount=networkFeeAmount,
            sources=sources,
            displayRate=displayRate,
            exchangeRate=exchangeRate,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.exchange_rate_dto import ExchangeRateDto