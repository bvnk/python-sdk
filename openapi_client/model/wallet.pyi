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


class Wallet(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        class properties:
            address = schemas.StrSchema
            
            
            class alternatives(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    items = schemas.AnyTypeSchema
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]], typing.List[typing.Union[MetaOapg.items, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ]]],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'alternatives':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> MetaOapg.items:
                    return super().__getitem__(i)
            approxAvailable = schemas.StrSchema
            approxBalance = schemas.StrSchema
            available = schemas.Float32Schema
            balance = schemas.Float32Schema
            convertedAvailable = schemas.Float32Schema
        
            @staticmethod
            def currency() -> typing.Type['Currency']:
                return Currency
            custodianWallet = schemas.BoolSchema
            depositFee = schemas.Float32Schema
            description = schemas.StrSchema
            id = schemas.Int64Schema
            isEmoney = schemas.BoolSchema
            lookup = schemas.StrSchema
            protocol = schemas.StrSchema
            supportsDeposits = schemas.BoolSchema
            supportsThirdParty = schemas.BoolSchema
            supportsWithdrawals = schemas.BoolSchema
            withdrawalFee = schemas.Float32Schema
            __annotations__ = {
                "address": address,
                "alternatives": alternatives,
                "approxAvailable": approxAvailable,
                "approxBalance": approxBalance,
                "available": available,
                "balance": balance,
                "convertedAvailable": convertedAvailable,
                "currency": currency,
                "custodianWallet": custodianWallet,
                "depositFee": depositFee,
                "description": description,
                "id": id,
                "isEmoney": isEmoney,
                "lookup": lookup,
                "protocol": protocol,
                "supportsDeposits": supportsDeposits,
                "supportsThirdParty": supportsThirdParty,
                "supportsWithdrawals": supportsWithdrawals,
                "withdrawalFee": withdrawalFee,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["alternatives"]) -> MetaOapg.properties.alternatives: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approxAvailable"]) -> MetaOapg.properties.approxAvailable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approxBalance"]) -> MetaOapg.properties.approxBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["available"]) -> MetaOapg.properties.available: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["convertedAvailable"]) -> MetaOapg.properties.convertedAvailable: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'Currency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custodianWallet"]) -> MetaOapg.properties.custodianWallet: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["depositFee"]) -> MetaOapg.properties.depositFee: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isEmoney"]) -> MetaOapg.properties.isEmoney: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lookup"]) -> MetaOapg.properties.lookup: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["protocol"]) -> MetaOapg.properties.protocol: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportsDeposits"]) -> MetaOapg.properties.supportsDeposits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportsThirdParty"]) -> MetaOapg.properties.supportsThirdParty: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["supportsWithdrawals"]) -> MetaOapg.properties.supportsWithdrawals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withdrawalFee"]) -> MetaOapg.properties.withdrawalFee: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["address", "alternatives", "approxAvailable", "approxBalance", "available", "balance", "convertedAvailable", "currency", "custodianWallet", "depositFee", "description", "id", "isEmoney", "lookup", "protocol", "supportsDeposits", "supportsThirdParty", "supportsWithdrawals", "withdrawalFee", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["alternatives"]) -> typing.Union[MetaOapg.properties.alternatives, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approxAvailable"]) -> typing.Union[MetaOapg.properties.approxAvailable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approxBalance"]) -> typing.Union[MetaOapg.properties.approxBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["available"]) -> typing.Union[MetaOapg.properties.available, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> typing.Union[MetaOapg.properties.balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["convertedAvailable"]) -> typing.Union[MetaOapg.properties.convertedAvailable, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union['Currency', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custodianWallet"]) -> typing.Union[MetaOapg.properties.custodianWallet, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["depositFee"]) -> typing.Union[MetaOapg.properties.depositFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isEmoney"]) -> typing.Union[MetaOapg.properties.isEmoney, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lookup"]) -> typing.Union[MetaOapg.properties.lookup, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["protocol"]) -> typing.Union[MetaOapg.properties.protocol, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportsDeposits"]) -> typing.Union[MetaOapg.properties.supportsDeposits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportsThirdParty"]) -> typing.Union[MetaOapg.properties.supportsThirdParty, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["supportsWithdrawals"]) -> typing.Union[MetaOapg.properties.supportsWithdrawals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withdrawalFee"]) -> typing.Union[MetaOapg.properties.withdrawalFee, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["address", "alternatives", "approxAvailable", "approxBalance", "available", "balance", "convertedAvailable", "currency", "custodianWallet", "depositFee", "description", "id", "isEmoney", "lookup", "protocol", "supportsDeposits", "supportsThirdParty", "supportsWithdrawals", "withdrawalFee", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        address: typing.Union[MetaOapg.properties.address, str, schemas.Unset] = schemas.unset,
        alternatives: typing.Union[MetaOapg.properties.alternatives, list, tuple, schemas.Unset] = schemas.unset,
        approxAvailable: typing.Union[MetaOapg.properties.approxAvailable, str, schemas.Unset] = schemas.unset,
        approxBalance: typing.Union[MetaOapg.properties.approxBalance, str, schemas.Unset] = schemas.unset,
        available: typing.Union[MetaOapg.properties.available, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        balance: typing.Union[MetaOapg.properties.balance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        convertedAvailable: typing.Union[MetaOapg.properties.convertedAvailable, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        currency: typing.Union['Currency', schemas.Unset] = schemas.unset,
        custodianWallet: typing.Union[MetaOapg.properties.custodianWallet, bool, schemas.Unset] = schemas.unset,
        depositFee: typing.Union[MetaOapg.properties.depositFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        isEmoney: typing.Union[MetaOapg.properties.isEmoney, bool, schemas.Unset] = schemas.unset,
        lookup: typing.Union[MetaOapg.properties.lookup, str, schemas.Unset] = schemas.unset,
        protocol: typing.Union[MetaOapg.properties.protocol, str, schemas.Unset] = schemas.unset,
        supportsDeposits: typing.Union[MetaOapg.properties.supportsDeposits, bool, schemas.Unset] = schemas.unset,
        supportsThirdParty: typing.Union[MetaOapg.properties.supportsThirdParty, bool, schemas.Unset] = schemas.unset,
        supportsWithdrawals: typing.Union[MetaOapg.properties.supportsWithdrawals, bool, schemas.Unset] = schemas.unset,
        withdrawalFee: typing.Union[MetaOapg.properties.withdrawalFee, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'Wallet':
        return super().__new__(
            cls,
            *_args,
            address=address,
            alternatives=alternatives,
            approxAvailable=approxAvailable,
            approxBalance=approxBalance,
            available=available,
            balance=balance,
            convertedAvailable=convertedAvailable,
            currency=currency,
            custodianWallet=custodianWallet,
            depositFee=depositFee,
            description=description,
            id=id,
            isEmoney=isEmoney,
            lookup=lookup,
            protocol=protocol,
            supportsDeposits=supportsDeposits,
            supportsThirdParty=supportsThirdParty,
            supportsWithdrawals=supportsWithdrawals,
            withdrawalFee=withdrawalFee,
            _configuration=_configuration,
            **kwargs,
        )

from openapi_client.model.currency import Currency
