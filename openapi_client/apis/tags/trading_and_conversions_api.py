# coding: utf-8

"""
    BVNK API Endpoints

    The BVNK API is designed to facilitate seamless and secure transactions including payments, channels, anddigital wallet transactions.  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""

from openapi_client.paths.api_v1_quote_accept_uuid.put import QuoteAccept
from openapi_client.paths.api_v1_quote.post import QuoteCreate
from openapi_client.paths.api_v1_quote_merchant_id.get import QuoteList
from openapi_client.paths.api_v1_quote_uuid.get import QuoteRead


class TradingAndConversionsApi(
    QuoteAccept,
    QuoteCreate,
    QuoteList,
    QuoteRead,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass
