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


class Currency(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            code = schemas.StrSchema
            depositFee = schemas.NumberSchema
            fiat = schemas.BoolSchema
            icon = schemas.StrSchema
            id = schemas.Int64Schema
            name = schemas.StrSchema
        
            @staticmethod
            def options() -> typing.Type['CurrencyOptions']:
                return CurrencyOptions
            pricePrecision = schemas.Int32Schema
            
            
            class protocols(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CurrencyProtocol']:
                        return CurrencyProtocol
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['CurrencyProtocol'], typing.List['CurrencyProtocol']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'protocols':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CurrencyProtocol':
                    return super().__getitem__(i)
            quantityPrecision = schemas.Int32Schema
            supportsDeposits = schemas.BoolSchema
            supportsWithdrawals = schemas.BoolSchema
            withdrawalFee = schemas.NumberSchema
            
            
            class withdrawalParameters(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ExternalCurrencyWithdrawalParameter']:
                        return ExternalCurrencyWithdrawalParameter
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['ExternalCurrencyWithdrawalParameter'], typing.List['ExternalCurrencyWithdrawalParameter']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'withdrawalParameters':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ExternalCurrencyWithdrawalParameter':
                    return super().__getitem__(i)
            __annotations__ = {
                "code": code,
                "depositFee": depositFee,
                "fiat": fiat,
                "icon": icon,
                "id": id,
                "name": name,
                "options": options,
                "pricePrecision": pricePrecision,
                "protocols": protocols,
                "quantityPrecision": quantityPrecision,
                "supportsDeposits": supportsDeposits,
                "supportsWithdrawals": supportsWithdrawals,
                "withdrawalFee": withdrawalFee,
                "withdrawalParameters": withdrawalParameters,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["code"]) -> MetaOapg.properties.code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depositFee"]) -> MetaOapg.properties.depositFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fiat"]) -> MetaOapg.properties.fiat: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["icon"]) -> MetaOapg.properties.icon: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> 'CurrencyOptions': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pricePrecision"]) -> MetaOapg.properties.pricePrecision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocols"]) -> MetaOapg.properties.protocols: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["quantityPrecision"]) -> MetaOapg.properties.quantityPrecision: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportsDeposits"]) -> MetaOapg.properties.supportsDeposits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportsWithdrawals"]) -> MetaOapg.properties.supportsWithdrawals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withdrawalFee"]) -> MetaOapg.properties.withdrawalFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withdrawalParameters"]) -> MetaOapg.properties.withdrawalParameters: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["code", "depositFee", "fiat", "icon", "id", "name", "options", "pricePrecision", "protocols", "quantityPrecision", "supportsDeposits", "supportsWithdrawals", "withdrawalFee", "withdrawalParameters", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["code"]) -> typing.Union[MetaOapg.properties.code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depositFee"]) -> typing.Union[MetaOapg.properties.depositFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fiat"]) -> typing.Union[MetaOapg.properties.fiat, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["icon"]) -> typing.Union[MetaOapg.properties.icon, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union['CurrencyOptions', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pricePrecision"]) -> typing.Union[MetaOapg.properties.pricePrecision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocols"]) -> typing.Union[MetaOapg.properties.protocols, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["quantityPrecision"]) -> typing.Union[MetaOapg.properties.quantityPrecision, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportsDeposits"]) -> typing.Union[MetaOapg.properties.supportsDeposits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportsWithdrawals"]) -> typing.Union[MetaOapg.properties.supportsWithdrawals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withdrawalFee"]) -> typing.Union[MetaOapg.properties.withdrawalFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withdrawalParameters"]) -> typing.Union[MetaOapg.properties.withdrawalParameters, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["code", "depositFee", "fiat", "icon", "id", "name", "options", "pricePrecision", "protocols", "quantityPrecision", "supportsDeposits", "supportsWithdrawals", "withdrawalFee", "withdrawalParameters", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        code: typing.Union[MetaOapg.properties.code, str, schemas.Unset] = schemas.unset,
        depositFee: typing.Union[MetaOapg.properties.depositFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        fiat: typing.Union[MetaOapg.properties.fiat, bool, schemas.Unset] = schemas.unset,
        icon: typing.Union[MetaOapg.properties.icon, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        options: typing.Union['CurrencyOptions', schemas.Unset] = schemas.unset,
        pricePrecision: typing.Union[MetaOapg.properties.pricePrecision, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        protocols: typing.Union[MetaOapg.properties.protocols, list, tuple, schemas.Unset] = schemas.unset,
        quantityPrecision: typing.Union[MetaOapg.properties.quantityPrecision, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        supportsDeposits: typing.Union[MetaOapg.properties.supportsDeposits, bool, schemas.Unset] = schemas.unset,
        supportsWithdrawals: typing.Union[MetaOapg.properties.supportsWithdrawals, bool, schemas.Unset] = schemas.unset,
        withdrawalFee: typing.Union[MetaOapg.properties.withdrawalFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        withdrawalParameters: typing.Union[MetaOapg.properties.withdrawalParameters, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Currency':
        return super().__new__(
            cls,
            *_args,
            code=code,
            depositFee=depositFee,
            fiat=fiat,
            icon=icon,
            id=id,
            name=name,
            options=options,
            pricePrecision=pricePrecision,
            protocols=protocols,
            quantityPrecision=quantityPrecision,
            supportsDeposits=supportsDeposits,
            supportsWithdrawals=supportsWithdrawals,
            withdrawalFee=withdrawalFee,
            withdrawalParameters=withdrawalParameters,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.currency_options import CurrencyOptions
from openapi_client.model.currency_protocol import CurrencyProtocol
from openapi_client.model.external_currency_withdrawal_parameter import ExternalCurrencyWithdrawalParameter
