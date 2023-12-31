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

class Wallet(object):
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
        'address': 'str',
        'alternatives': 'list[object]',
        'approx_available': 'str',
        'approx_balance': 'str',
        'available': 'float',
        'balance': 'float',
        'converted_available': 'float',
        'currency': 'Currency',
        'custodian_wallet': 'bool',
        'deposit_fee': 'float',
        'description': 'str',
        'id': 'int',
        'is_emoney': 'bool',
        'lookup': 'str',
        'protocol': 'str',
        'supports_deposits': 'bool',
        'supports_third_party': 'bool',
        'supports_withdrawals': 'bool',
        'withdrawal_fee': 'float'
    }

    attribute_map = {
        'address': 'address',
        'alternatives': 'alternatives',
        'approx_available': 'approxAvailable',
        'approx_balance': 'approxBalance',
        'available': 'available',
        'balance': 'balance',
        'converted_available': 'convertedAvailable',
        'currency': 'currency',
        'custodian_wallet': 'custodianWallet',
        'deposit_fee': 'depositFee',
        'description': 'description',
        'id': 'id',
        'is_emoney': 'isEmoney',
        'lookup': 'lookup',
        'protocol': 'protocol',
        'supports_deposits': 'supportsDeposits',
        'supports_third_party': 'supportsThirdParty',
        'supports_withdrawals': 'supportsWithdrawals',
        'withdrawal_fee': 'withdrawalFee'
    }

    def __init__(self, address=None, alternatives=None, approx_available=None, approx_balance=None, available=None, balance=None, converted_available=None, currency=None, custodian_wallet=None, deposit_fee=None, description=None, id=None, is_emoney=False, lookup=None, protocol=None, supports_deposits=True, supports_third_party=False, supports_withdrawals=True, withdrawal_fee=None):  # noqa: E501
        """Wallet - a model defined in Swagger"""  # noqa: E501
        self._address = None
        self._alternatives = None
        self._approx_available = None
        self._approx_balance = None
        self._available = None
        self._balance = None
        self._converted_available = None
        self._currency = None
        self._custodian_wallet = None
        self._deposit_fee = None
        self._description = None
        self._id = None
        self._is_emoney = None
        self._lookup = None
        self._protocol = None
        self._supports_deposits = None
        self._supports_third_party = None
        self._supports_withdrawals = None
        self._withdrawal_fee = None
        self.discriminator = None
        if address is not None:
            self.address = address
        if alternatives is not None:
            self.alternatives = alternatives
        if approx_available is not None:
            self.approx_available = approx_available
        if approx_balance is not None:
            self.approx_balance = approx_balance
        if available is not None:
            self.available = available
        if balance is not None:
            self.balance = balance
        if converted_available is not None:
            self.converted_available = converted_available
        if currency is not None:
            self.currency = currency
        if custodian_wallet is not None:
            self.custodian_wallet = custodian_wallet
        if deposit_fee is not None:
            self.deposit_fee = deposit_fee
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if is_emoney is not None:
            self.is_emoney = is_emoney
        if lookup is not None:
            self.lookup = lookup
        if protocol is not None:
            self.protocol = protocol
        if supports_deposits is not None:
            self.supports_deposits = supports_deposits
        if supports_third_party is not None:
            self.supports_third_party = supports_third_party
        if supports_withdrawals is not None:
            self.supports_withdrawals = supports_withdrawals
        if withdrawal_fee is not None:
            self.withdrawal_fee = withdrawal_fee

    @property
    def address(self):
        """Gets the address of this Wallet.  # noqa: E501


        :return: The address of this Wallet.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Wallet.


        :param address: The address of this Wallet.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def alternatives(self):
        """Gets the alternatives of this Wallet.  # noqa: E501


        :return: The alternatives of this Wallet.  # noqa: E501
        :rtype: list[object]
        """
        return self._alternatives

    @alternatives.setter
    def alternatives(self, alternatives):
        """Sets the alternatives of this Wallet.


        :param alternatives: The alternatives of this Wallet.  # noqa: E501
        :type: list[object]
        """

        self._alternatives = alternatives

    @property
    def approx_available(self):
        """Gets the approx_available of this Wallet.  # noqa: E501


        :return: The approx_available of this Wallet.  # noqa: E501
        :rtype: str
        """
        return self._approx_available

    @approx_available.setter
    def approx_available(self, approx_available):
        """Sets the approx_available of this Wallet.


        :param approx_available: The approx_available of this Wallet.  # noqa: E501
        :type: str
        """

        self._approx_available = approx_available

    @property
    def approx_balance(self):
        """Gets the approx_balance of this Wallet.  # noqa: E501


        :return: The approx_balance of this Wallet.  # noqa: E501
        :rtype: str
        """
        return self._approx_balance

    @approx_balance.setter
    def approx_balance(self, approx_balance):
        """Sets the approx_balance of this Wallet.


        :param approx_balance: The approx_balance of this Wallet.  # noqa: E501
        :type: str
        """

        self._approx_balance = approx_balance

    @property
    def available(self):
        """Gets the available of this Wallet.  # noqa: E501


        :return: The available of this Wallet.  # noqa: E501
        :rtype: float
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this Wallet.


        :param available: The available of this Wallet.  # noqa: E501
        :type: float
        """

        self._available = available

    @property
    def balance(self):
        """Gets the balance of this Wallet.  # noqa: E501


        :return: The balance of this Wallet.  # noqa: E501
        :rtype: float
        """
        return self._balance

    @balance.setter
    def balance(self, balance):
        """Sets the balance of this Wallet.


        :param balance: The balance of this Wallet.  # noqa: E501
        :type: float
        """

        self._balance = balance

    @property
    def converted_available(self):
        """Gets the converted_available of this Wallet.  # noqa: E501


        :return: The converted_available of this Wallet.  # noqa: E501
        :rtype: float
        """
        return self._converted_available

    @converted_available.setter
    def converted_available(self, converted_available):
        """Sets the converted_available of this Wallet.


        :param converted_available: The converted_available of this Wallet.  # noqa: E501
        :type: float
        """

        self._converted_available = converted_available

    @property
    def currency(self):
        """Gets the currency of this Wallet.  # noqa: E501


        :return: The currency of this Wallet.  # noqa: E501
        :rtype: Currency
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Wallet.


        :param currency: The currency of this Wallet.  # noqa: E501
        :type: Currency
        """

        self._currency = currency

    @property
    def custodian_wallet(self):
        """Gets the custodian_wallet of this Wallet.  # noqa: E501


        :return: The custodian_wallet of this Wallet.  # noqa: E501
        :rtype: bool
        """
        return self._custodian_wallet

    @custodian_wallet.setter
    def custodian_wallet(self, custodian_wallet):
        """Sets the custodian_wallet of this Wallet.


        :param custodian_wallet: The custodian_wallet of this Wallet.  # noqa: E501
        :type: bool
        """

        self._custodian_wallet = custodian_wallet

    @property
    def deposit_fee(self):
        """Gets the deposit_fee of this Wallet.  # noqa: E501


        :return: The deposit_fee of this Wallet.  # noqa: E501
        :rtype: float
        """
        return self._deposit_fee

    @deposit_fee.setter
    def deposit_fee(self, deposit_fee):
        """Sets the deposit_fee of this Wallet.


        :param deposit_fee: The deposit_fee of this Wallet.  # noqa: E501
        :type: float
        """

        self._deposit_fee = deposit_fee

    @property
    def description(self):
        """Gets the description of this Wallet.  # noqa: E501


        :return: The description of this Wallet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Wallet.


        :param description: The description of this Wallet.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def id(self):
        """Gets the id of this Wallet.  # noqa: E501


        :return: The id of this Wallet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Wallet.


        :param id: The id of this Wallet.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def is_emoney(self):
        """Gets the is_emoney of this Wallet.  # noqa: E501


        :return: The is_emoney of this Wallet.  # noqa: E501
        :rtype: bool
        """
        return self._is_emoney

    @is_emoney.setter
    def is_emoney(self, is_emoney):
        """Sets the is_emoney of this Wallet.


        :param is_emoney: The is_emoney of this Wallet.  # noqa: E501
        :type: bool
        """

        self._is_emoney = is_emoney

    @property
    def lookup(self):
        """Gets the lookup of this Wallet.  # noqa: E501


        :return: The lookup of this Wallet.  # noqa: E501
        :rtype: str
        """
        return self._lookup

    @lookup.setter
    def lookup(self, lookup):
        """Sets the lookup of this Wallet.


        :param lookup: The lookup of this Wallet.  # noqa: E501
        :type: str
        """

        self._lookup = lookup

    @property
    def protocol(self):
        """Gets the protocol of this Wallet.  # noqa: E501


        :return: The protocol of this Wallet.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this Wallet.


        :param protocol: The protocol of this Wallet.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def supports_deposits(self):
        """Gets the supports_deposits of this Wallet.  # noqa: E501


        :return: The supports_deposits of this Wallet.  # noqa: E501
        :rtype: bool
        """
        return self._supports_deposits

    @supports_deposits.setter
    def supports_deposits(self, supports_deposits):
        """Sets the supports_deposits of this Wallet.


        :param supports_deposits: The supports_deposits of this Wallet.  # noqa: E501
        :type: bool
        """

        self._supports_deposits = supports_deposits

    @property
    def supports_third_party(self):
        """Gets the supports_third_party of this Wallet.  # noqa: E501


        :return: The supports_third_party of this Wallet.  # noqa: E501
        :rtype: bool
        """
        return self._supports_third_party

    @supports_third_party.setter
    def supports_third_party(self, supports_third_party):
        """Sets the supports_third_party of this Wallet.


        :param supports_third_party: The supports_third_party of this Wallet.  # noqa: E501
        :type: bool
        """

        self._supports_third_party = supports_third_party

    @property
    def supports_withdrawals(self):
        """Gets the supports_withdrawals of this Wallet.  # noqa: E501


        :return: The supports_withdrawals of this Wallet.  # noqa: E501
        :rtype: bool
        """
        return self._supports_withdrawals

    @supports_withdrawals.setter
    def supports_withdrawals(self, supports_withdrawals):
        """Sets the supports_withdrawals of this Wallet.


        :param supports_withdrawals: The supports_withdrawals of this Wallet.  # noqa: E501
        :type: bool
        """

        self._supports_withdrawals = supports_withdrawals

    @property
    def withdrawal_fee(self):
        """Gets the withdrawal_fee of this Wallet.  # noqa: E501


        :return: The withdrawal_fee of this Wallet.  # noqa: E501
        :rtype: float
        """
        return self._withdrawal_fee

    @withdrawal_fee.setter
    def withdrawal_fee(self, withdrawal_fee):
        """Sets the withdrawal_fee of this Wallet.


        :param withdrawal_fee: The withdrawal_fee of this Wallet.  # noqa: E501
        :type: float
        """

        self._withdrawal_fee = withdrawal_fee

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
        if issubclass(Wallet, dict):
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
        if not isinstance(other, Wallet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
