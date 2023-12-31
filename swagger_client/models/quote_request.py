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

class QuoteRequest(object):
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
        '_from': 'str',
        'to': 'str',
        'from_wallet': 'float',
        'use_minimum': 'bool',
        'use_maximum': 'bool',
        'to_wallet': 'float',
        'amount_in': 'float',
        'pay_in_method': 'str',
        'pay_out_method': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'from_wallet': 'fromWallet',
        'use_minimum': 'useMinimum',
        'use_maximum': 'useMaximum',
        'to_wallet': 'toWallet',
        'amount_in': 'amountIn',
        'pay_in_method': 'payInMethod',
        'pay_out_method': 'payOutMethod'
    }

    def __init__(self, _from='EUR', to='USDC', from_wallet=3598236, use_minimum=False, use_maximum=False, to_wallet=3598514, amount_in=10, pay_in_method='wallet', pay_out_method='wallet'):  # noqa: E501
        """QuoteRequest - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._to = None
        self._from_wallet = None
        self._use_minimum = None
        self._use_maximum = None
        self._to_wallet = None
        self._amount_in = None
        self._pay_in_method = None
        self._pay_out_method = None
        self.discriminator = None
        self._from = _from
        self.to = to
        self.from_wallet = from_wallet
        self.use_minimum = use_minimum
        self.use_maximum = use_maximum
        self.to_wallet = to_wallet
        self.amount_in = amount_in
        self.pay_in_method = pay_in_method
        self.pay_out_method = pay_out_method

    @property
    def _from(self):
        """Gets the _from of this QuoteRequest.  # noqa: E501


        :return: The _from of this QuoteRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this QuoteRequest.


        :param _from: The _from of this QuoteRequest.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this QuoteRequest.  # noqa: E501


        :return: The to of this QuoteRequest.  # noqa: E501
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this QuoteRequest.


        :param to: The to of this QuoteRequest.  # noqa: E501
        :type: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def from_wallet(self):
        """Gets the from_wallet of this QuoteRequest.  # noqa: E501


        :return: The from_wallet of this QuoteRequest.  # noqa: E501
        :rtype: float
        """
        return self._from_wallet

    @from_wallet.setter
    def from_wallet(self, from_wallet):
        """Sets the from_wallet of this QuoteRequest.


        :param from_wallet: The from_wallet of this QuoteRequest.  # noqa: E501
        :type: float
        """
        if from_wallet is None:
            raise ValueError("Invalid value for `from_wallet`, must not be `None`")  # noqa: E501

        self._from_wallet = from_wallet

    @property
    def use_minimum(self):
        """Gets the use_minimum of this QuoteRequest.  # noqa: E501


        :return: The use_minimum of this QuoteRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_minimum

    @use_minimum.setter
    def use_minimum(self, use_minimum):
        """Sets the use_minimum of this QuoteRequest.


        :param use_minimum: The use_minimum of this QuoteRequest.  # noqa: E501
        :type: bool
        """
        if use_minimum is None:
            raise ValueError("Invalid value for `use_minimum`, must not be `None`")  # noqa: E501

        self._use_minimum = use_minimum

    @property
    def use_maximum(self):
        """Gets the use_maximum of this QuoteRequest.  # noqa: E501


        :return: The use_maximum of this QuoteRequest.  # noqa: E501
        :rtype: bool
        """
        return self._use_maximum

    @use_maximum.setter
    def use_maximum(self, use_maximum):
        """Sets the use_maximum of this QuoteRequest.


        :param use_maximum: The use_maximum of this QuoteRequest.  # noqa: E501
        :type: bool
        """
        if use_maximum is None:
            raise ValueError("Invalid value for `use_maximum`, must not be `None`")  # noqa: E501

        self._use_maximum = use_maximum

    @property
    def to_wallet(self):
        """Gets the to_wallet of this QuoteRequest.  # noqa: E501


        :return: The to_wallet of this QuoteRequest.  # noqa: E501
        :rtype: float
        """
        return self._to_wallet

    @to_wallet.setter
    def to_wallet(self, to_wallet):
        """Sets the to_wallet of this QuoteRequest.


        :param to_wallet: The to_wallet of this QuoteRequest.  # noqa: E501
        :type: float
        """
        if to_wallet is None:
            raise ValueError("Invalid value for `to_wallet`, must not be `None`")  # noqa: E501

        self._to_wallet = to_wallet

    @property
    def amount_in(self):
        """Gets the amount_in of this QuoteRequest.  # noqa: E501


        :return: The amount_in of this QuoteRequest.  # noqa: E501
        :rtype: float
        """
        return self._amount_in

    @amount_in.setter
    def amount_in(self, amount_in):
        """Sets the amount_in of this QuoteRequest.


        :param amount_in: The amount_in of this QuoteRequest.  # noqa: E501
        :type: float
        """
        if amount_in is None:
            raise ValueError("Invalid value for `amount_in`, must not be `None`")  # noqa: E501

        self._amount_in = amount_in

    @property
    def pay_in_method(self):
        """Gets the pay_in_method of this QuoteRequest.  # noqa: E501


        :return: The pay_in_method of this QuoteRequest.  # noqa: E501
        :rtype: str
        """
        return self._pay_in_method

    @pay_in_method.setter
    def pay_in_method(self, pay_in_method):
        """Sets the pay_in_method of this QuoteRequest.


        :param pay_in_method: The pay_in_method of this QuoteRequest.  # noqa: E501
        :type: str
        """
        if pay_in_method is None:
            raise ValueError("Invalid value for `pay_in_method`, must not be `None`")  # noqa: E501

        self._pay_in_method = pay_in_method

    @property
    def pay_out_method(self):
        """Gets the pay_out_method of this QuoteRequest.  # noqa: E501


        :return: The pay_out_method of this QuoteRequest.  # noqa: E501
        :rtype: str
        """
        return self._pay_out_method

    @pay_out_method.setter
    def pay_out_method(self, pay_out_method):
        """Sets the pay_out_method of this QuoteRequest.


        :param pay_out_method: The pay_out_method of this QuoteRequest.  # noqa: E501
        :type: str
        """
        if pay_out_method is None:
            raise ValueError("Invalid value for `pay_out_method`, must not be `None`")  # noqa: E501

        self._pay_out_method = pay_out_method

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
        if issubclass(QuoteRequest, dict):
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
        if not isinstance(other, QuoteRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
