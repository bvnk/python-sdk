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


class QuoteRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "fromWallet",
            "payInMethod",
            "useMinimum",
            "amountIn",
            "from",
            "to",
            "payOutMethod",
            "useMaximum",
            "toWallet",
        }
        
        class properties:
            _from = schemas.StrSchema
            to = schemas.StrSchema
            fromWallet = schemas.NumberSchema
            useMinimum = schemas.BoolSchema
            useMaximum = schemas.BoolSchema
            toWallet = schemas.NumberSchema
            amountIn = schemas.NumberSchema
            payInMethod = schemas.StrSchema
            payOutMethod = schemas.StrSchema
            __annotations__ = {
                "from": _from,
                "to": to,
                "fromWallet": fromWallet,
                "useMinimum": useMinimum,
                "useMaximum": useMaximum,
                "toWallet": toWallet,
                "amountIn": amountIn,
                "payInMethod": payInMethod,
                "payOutMethod": payOutMethod,
            }
    
    fromWallet: MetaOapg.properties.fromWallet
    payInMethod: MetaOapg.properties.payInMethod
    useMinimum: MetaOapg.properties.useMinimum
    amountIn: MetaOapg.properties.amountIn
    to: MetaOapg.properties.to
    payOutMethod: MetaOapg.properties.payOutMethod
    useMaximum: MetaOapg.properties.useMaximum
    toWallet: MetaOapg.properties.toWallet
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fromWallet"]) -> MetaOapg.properties.fromWallet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useMinimum"]) -> MetaOapg.properties.useMinimum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["useMaximum"]) -> MetaOapg.properties.useMaximum: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["toWallet"]) -> MetaOapg.properties.toWallet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amountIn"]) -> MetaOapg.properties.amountIn: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payInMethod"]) -> MetaOapg.properties.payInMethod: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payOutMethod"]) -> MetaOapg.properties.payOutMethod: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["from", "to", "fromWallet", "useMinimum", "useMaximum", "toWallet", "amountIn", "payInMethod", "payOutMethod", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["from"]) -> MetaOapg.properties._from: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["to"]) -> MetaOapg.properties.to: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fromWallet"]) -> MetaOapg.properties.fromWallet: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useMinimum"]) -> MetaOapg.properties.useMinimum: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["useMaximum"]) -> MetaOapg.properties.useMaximum: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["toWallet"]) -> MetaOapg.properties.toWallet: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amountIn"]) -> MetaOapg.properties.amountIn: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payInMethod"]) -> MetaOapg.properties.payInMethod: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payOutMethod"]) -> MetaOapg.properties.payOutMethod: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["from", "to", "fromWallet", "useMinimum", "useMaximum", "toWallet", "amountIn", "payInMethod", "payOutMethod", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        fromWallet: typing.Union[MetaOapg.properties.fromWallet, decimal.Decimal, int, float, ],
        payInMethod: typing.Union[MetaOapg.properties.payInMethod, str, ],
        useMinimum: typing.Union[MetaOapg.properties.useMinimum, bool, ],
        amountIn: typing.Union[MetaOapg.properties.amountIn, decimal.Decimal, int, float, ],
        to: typing.Union[MetaOapg.properties.to, str, ],
        payOutMethod: typing.Union[MetaOapg.properties.payOutMethod, str, ],
        useMaximum: typing.Union[MetaOapg.properties.useMaximum, bool, ],
        toWallet: typing.Union[MetaOapg.properties.toWallet, decimal.Decimal, int, float, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'QuoteRequest':
        return super().__new__(
            cls,
            *_args,
            fromWallet=fromWallet,
            payInMethod=payInMethod,
            useMinimum=useMinimum,
            amountIn=amountIn,
            to=to,
            payOutMethod=payOutMethod,
            useMaximum=useMaximum,
            toWallet=toWallet,
            _configuration=_configuration,
            **kwargs,
        )
