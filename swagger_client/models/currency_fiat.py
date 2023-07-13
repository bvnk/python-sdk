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

class CurrencyFiat(object):
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
        'code': 'str',
        'deposit_fee': 'float',
        'fiat': 'bool',
        'icon': 'str',
        'id': 'int',
        'name': 'str',
        'options': 'object',
        'price_precision': 'int',
        'protocols': 'list[object]',
        'quantity_precision': 'int',
        'supports_deposits': 'bool',
        'supports_withdrawals': 'bool',
        'withdrawal_fee': 'float',
        'withdrawal_parameters': 'list[object]'
    }

    attribute_map = {
        'code': 'code',
        'deposit_fee': 'depositFee',
        'fiat': 'fiat',
        'icon': 'icon',
        'id': 'id',
        'name': 'name',
        'options': 'options',
        'price_precision': 'pricePrecision',
        'protocols': 'protocols',
        'quantity_precision': 'quantityPrecision',
        'supports_deposits': 'supportsDeposits',
        'supports_withdrawals': 'supportsWithdrawals',
        'withdrawal_fee': 'withdrawalFee',
        'withdrawal_parameters': 'withdrawalParameters'
    }

    def __init__(self, code=None, deposit_fee=None, fiat=True, icon=None, id=None, name=None, options=None, price_precision=2, protocols=None, quantity_precision=2, supports_deposits=True, supports_withdrawals=True, withdrawal_fee=None, withdrawal_parameters=None):  # noqa: E501
        """CurrencyFiat - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._deposit_fee = None
        self._fiat = None
        self._icon = None
        self._id = None
        self._name = None
        self._options = None
        self._price_precision = None
        self._protocols = None
        self._quantity_precision = None
        self._supports_deposits = None
        self._supports_withdrawals = None
        self._withdrawal_fee = None
        self._withdrawal_parameters = None
        self.discriminator = None
        if code is not None:
            self.code = code
        if deposit_fee is not None:
            self.deposit_fee = deposit_fee
        if fiat is not None:
            self.fiat = fiat
        if icon is not None:
            self.icon = icon
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if options is not None:
            self.options = options
        if price_precision is not None:
            self.price_precision = price_precision
        if protocols is not None:
            self.protocols = protocols
        if quantity_precision is not None:
            self.quantity_precision = quantity_precision
        if supports_deposits is not None:
            self.supports_deposits = supports_deposits
        if supports_withdrawals is not None:
            self.supports_withdrawals = supports_withdrawals
        if withdrawal_fee is not None:
            self.withdrawal_fee = withdrawal_fee
        if withdrawal_parameters is not None:
            self.withdrawal_parameters = withdrawal_parameters

    @property
    def code(self):
        """Gets the code of this CurrencyFiat.  # noqa: E501


        :return: The code of this CurrencyFiat.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CurrencyFiat.


        :param code: The code of this CurrencyFiat.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def deposit_fee(self):
        """Gets the deposit_fee of this CurrencyFiat.  # noqa: E501


        :return: The deposit_fee of this CurrencyFiat.  # noqa: E501
        :rtype: float
        """
        return self._deposit_fee

    @deposit_fee.setter
    def deposit_fee(self, deposit_fee):
        """Sets the deposit_fee of this CurrencyFiat.


        :param deposit_fee: The deposit_fee of this CurrencyFiat.  # noqa: E501
        :type: float
        """

        self._deposit_fee = deposit_fee

    @property
    def fiat(self):
        """Gets the fiat of this CurrencyFiat.  # noqa: E501


        :return: The fiat of this CurrencyFiat.  # noqa: E501
        :rtype: bool
        """
        return self._fiat

    @fiat.setter
    def fiat(self, fiat):
        """Sets the fiat of this CurrencyFiat.


        :param fiat: The fiat of this CurrencyFiat.  # noqa: E501
        :type: bool
        """

        self._fiat = fiat

    @property
    def icon(self):
        """Gets the icon of this CurrencyFiat.  # noqa: E501


        :return: The icon of this CurrencyFiat.  # noqa: E501
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this CurrencyFiat.


        :param icon: The icon of this CurrencyFiat.  # noqa: E501
        :type: str
        """

        self._icon = icon

    @property
    def id(self):
        """Gets the id of this CurrencyFiat.  # noqa: E501


        :return: The id of this CurrencyFiat.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CurrencyFiat.


        :param id: The id of this CurrencyFiat.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CurrencyFiat.  # noqa: E501


        :return: The name of this CurrencyFiat.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CurrencyFiat.


        :param name: The name of this CurrencyFiat.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def options(self):
        """Gets the options of this CurrencyFiat.  # noqa: E501


        :return: The options of this CurrencyFiat.  # noqa: E501
        :rtype: object
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this CurrencyFiat.


        :param options: The options of this CurrencyFiat.  # noqa: E501
        :type: object
        """

        self._options = options

    @property
    def price_precision(self):
        """Gets the price_precision of this CurrencyFiat.  # noqa: E501


        :return: The price_precision of this CurrencyFiat.  # noqa: E501
        :rtype: int
        """
        return self._price_precision

    @price_precision.setter
    def price_precision(self, price_precision):
        """Sets the price_precision of this CurrencyFiat.


        :param price_precision: The price_precision of this CurrencyFiat.  # noqa: E501
        :type: int
        """

        self._price_precision = price_precision

    @property
    def protocols(self):
        """Gets the protocols of this CurrencyFiat.  # noqa: E501


        :return: The protocols of this CurrencyFiat.  # noqa: E501
        :rtype: list[object]
        """
        return self._protocols

    @protocols.setter
    def protocols(self, protocols):
        """Sets the protocols of this CurrencyFiat.


        :param protocols: The protocols of this CurrencyFiat.  # noqa: E501
        :type: list[object]
        """

        self._protocols = protocols

    @property
    def quantity_precision(self):
        """Gets the quantity_precision of this CurrencyFiat.  # noqa: E501


        :return: The quantity_precision of this CurrencyFiat.  # noqa: E501
        :rtype: int
        """
        return self._quantity_precision

    @quantity_precision.setter
    def quantity_precision(self, quantity_precision):
        """Sets the quantity_precision of this CurrencyFiat.


        :param quantity_precision: The quantity_precision of this CurrencyFiat.  # noqa: E501
        :type: int
        """

        self._quantity_precision = quantity_precision

    @property
    def supports_deposits(self):
        """Gets the supports_deposits of this CurrencyFiat.  # noqa: E501


        :return: The supports_deposits of this CurrencyFiat.  # noqa: E501
        :rtype: bool
        """
        return self._supports_deposits

    @supports_deposits.setter
    def supports_deposits(self, supports_deposits):
        """Sets the supports_deposits of this CurrencyFiat.


        :param supports_deposits: The supports_deposits of this CurrencyFiat.  # noqa: E501
        :type: bool
        """

        self._supports_deposits = supports_deposits

    @property
    def supports_withdrawals(self):
        """Gets the supports_withdrawals of this CurrencyFiat.  # noqa: E501


        :return: The supports_withdrawals of this CurrencyFiat.  # noqa: E501
        :rtype: bool
        """
        return self._supports_withdrawals

    @supports_withdrawals.setter
    def supports_withdrawals(self, supports_withdrawals):
        """Sets the supports_withdrawals of this CurrencyFiat.


        :param supports_withdrawals: The supports_withdrawals of this CurrencyFiat.  # noqa: E501
        :type: bool
        """

        self._supports_withdrawals = supports_withdrawals

    @property
    def withdrawal_fee(self):
        """Gets the withdrawal_fee of this CurrencyFiat.  # noqa: E501


        :return: The withdrawal_fee of this CurrencyFiat.  # noqa: E501
        :rtype: float
        """
        return self._withdrawal_fee

    @withdrawal_fee.setter
    def withdrawal_fee(self, withdrawal_fee):
        """Sets the withdrawal_fee of this CurrencyFiat.


        :param withdrawal_fee: The withdrawal_fee of this CurrencyFiat.  # noqa: E501
        :type: float
        """

        self._withdrawal_fee = withdrawal_fee

    @property
    def withdrawal_parameters(self):
        """Gets the withdrawal_parameters of this CurrencyFiat.  # noqa: E501


        :return: The withdrawal_parameters of this CurrencyFiat.  # noqa: E501
        :rtype: list[object]
        """
        return self._withdrawal_parameters

    @withdrawal_parameters.setter
    def withdrawal_parameters(self, withdrawal_parameters):
        """Sets the withdrawal_parameters of this CurrencyFiat.


        :param withdrawal_parameters: The withdrawal_parameters of this CurrencyFiat.  # noqa: E501
        :type: list[object]
        """

        self._withdrawal_parameters = withdrawal_parameters

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
        if issubclass(CurrencyFiat, dict):
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
        if not isinstance(other, CurrencyFiat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other