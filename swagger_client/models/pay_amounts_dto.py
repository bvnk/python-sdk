# coding: utf-8

"""
    BVNK API Endpoints

    The BVNK API is designed to facilitate seamless and secure transactions including payments, channels, anddigital wallet transactions.  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PayAmountsDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'currency': 'str',
        'amount': 'float',
        'actual': 'float'
    }

    attribute_map = {
        'currency': 'currency',
        'amount': 'amount',
        'actual': 'actual'
    }

    def __init__(self, currency=None, amount=None, actual=None):  # noqa: E501
        """PayAmountsDto - a model defined in Swagger"""  # noqa: E501
        self._currency = None
        self._amount = None
        self._actual = None
        self.discriminator = None
        if currency is not None:
            self.currency = currency
        if amount is not None:
            self.amount = amount
        if actual is not None:
            self.actual = actual

    @property
    def currency(self):
        """Gets the currency of this PayAmountsDto.  # noqa: E501

        currency acronym  # noqa: E501

        :return: The currency of this PayAmountsDto.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PayAmountsDto.

        currency acronym  # noqa: E501

        :param currency: The currency of this PayAmountsDto.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def amount(self):
        """Gets the amount of this PayAmountsDto.  # noqa: E501

        amount to be paid  # noqa: E501

        :return: The amount of this PayAmountsDto.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PayAmountsDto.

        amount to be paid  # noqa: E501

        :param amount: The amount of this PayAmountsDto.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def actual(self):
        """Gets the actual of this PayAmountsDto.  # noqa: E501

        actual amount paid/ received  # noqa: E501

        :return: The actual of this PayAmountsDto.  # noqa: E501
        :rtype: float
        """
        return self._actual

    @actual.setter
    def actual(self, actual):
        """Sets the actual of this PayAmountsDto.

        actual amount paid/ received  # noqa: E501

        :param actual: The actual of this PayAmountsDto.  # noqa: E501
        :type: float
        """

        self._actual = actual

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(PayAmountsDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PayAmountsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other