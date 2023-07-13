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

class TransactionReportRequestData(object):
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
        'type': 'str',
        'external_processing': 'str',
        'wallet_id': 'int',
        'transaction_type': 'str',
        'from_date': 'str',
        'to_date': 'str',
        'format': 'str',
        'language_tag': 'str',
        'category': 'int',
        'account_name': 'str',
        'include': 'str',
        'exclude': 'str'
    }

    attribute_map = {
        'type': 'type',
        'external_processing': 'externalProcessing',
        'wallet_id': 'walletId',
        'transaction_type': 'transactionType',
        'from_date': 'fromDate',
        'to_date': 'toDate',
        'format': 'format',
        'language_tag': 'languageTag',
        'category': 'category',
        'account_name': 'accountName',
        'include': 'include',
        'exclude': 'exclude'
    }

    def __init__(self, type=None, external_processing=None, wallet_id=None, transaction_type=None, from_date=None, to_date=None, format=None, language_tag=None, category=None, account_name=None, include=None, exclude=None):  # noqa: E501
        """TransactionReportRequestData - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._external_processing = None
        self._wallet_id = None
        self._transaction_type = None
        self._from_date = None
        self._to_date = None
        self._format = None
        self._language_tag = None
        self._category = None
        self._account_name = None
        self._include = None
        self._exclude = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if external_processing is not None:
            self.external_processing = external_processing
        if wallet_id is not None:
            self.wallet_id = wallet_id
        if transaction_type is not None:
            self.transaction_type = transaction_type
        if from_date is not None:
            self.from_date = from_date
        if to_date is not None:
            self.to_date = to_date
        if format is not None:
            self.format = format
        if language_tag is not None:
            self.language_tag = language_tag
        if category is not None:
            self.category = category
        if account_name is not None:
            self.account_name = account_name
        if include is not None:
            self.include = include
        if exclude is not None:
            self.exclude = exclude

    @property
    def type(self):
        """Gets the type of this TransactionReportRequestData.  # noqa: E501


        :return: The type of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionReportRequestData.


        :param type: The type of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def external_processing(self):
        """Gets the external_processing of this TransactionReportRequestData.  # noqa: E501


        :return: The external_processing of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._external_processing

    @external_processing.setter
    def external_processing(self, external_processing):
        """Sets the external_processing of this TransactionReportRequestData.


        :param external_processing: The external_processing of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._external_processing = external_processing

    @property
    def wallet_id(self):
        """Gets the wallet_id of this TransactionReportRequestData.  # noqa: E501


        :return: The wallet_id of this TransactionReportRequestData.  # noqa: E501
        :rtype: int
        """
        return self._wallet_id

    @wallet_id.setter
    def wallet_id(self, wallet_id):
        """Sets the wallet_id of this TransactionReportRequestData.


        :param wallet_id: The wallet_id of this TransactionReportRequestData.  # noqa: E501
        :type: int
        """

        self._wallet_id = wallet_id

    @property
    def transaction_type(self):
        """Gets the transaction_type of this TransactionReportRequestData.  # noqa: E501


        :return: The transaction_type of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._transaction_type

    @transaction_type.setter
    def transaction_type(self, transaction_type):
        """Sets the transaction_type of this TransactionReportRequestData.


        :param transaction_type: The transaction_type of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._transaction_type = transaction_type

    @property
    def from_date(self):
        """Gets the from_date of this TransactionReportRequestData.  # noqa: E501


        :return: The from_date of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._from_date

    @from_date.setter
    def from_date(self, from_date):
        """Sets the from_date of this TransactionReportRequestData.


        :param from_date: The from_date of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._from_date = from_date

    @property
    def to_date(self):
        """Gets the to_date of this TransactionReportRequestData.  # noqa: E501


        :return: The to_date of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._to_date

    @to_date.setter
    def to_date(self, to_date):
        """Sets the to_date of this TransactionReportRequestData.


        :param to_date: The to_date of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._to_date = to_date

    @property
    def format(self):
        """Gets the format of this TransactionReportRequestData.  # noqa: E501


        :return: The format of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this TransactionReportRequestData.


        :param format: The format of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._format = format

    @property
    def language_tag(self):
        """Gets the language_tag of this TransactionReportRequestData.  # noqa: E501


        :return: The language_tag of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._language_tag

    @language_tag.setter
    def language_tag(self, language_tag):
        """Sets the language_tag of this TransactionReportRequestData.


        :param language_tag: The language_tag of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._language_tag = language_tag

    @property
    def category(self):
        """Gets the category of this TransactionReportRequestData.  # noqa: E501


        :return: The category of this TransactionReportRequestData.  # noqa: E501
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this TransactionReportRequestData.


        :param category: The category of this TransactionReportRequestData.  # noqa: E501
        :type: int
        """

        self._category = category

    @property
    def account_name(self):
        """Gets the account_name of this TransactionReportRequestData.  # noqa: E501


        :return: The account_name of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this TransactionReportRequestData.


        :param account_name: The account_name of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._account_name = account_name

    @property
    def include(self):
        """Gets the include of this TransactionReportRequestData.  # noqa: E501


        :return: The include of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._include

    @include.setter
    def include(self, include):
        """Sets the include of this TransactionReportRequestData.


        :param include: The include of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._include = include

    @property
    def exclude(self):
        """Gets the exclude of this TransactionReportRequestData.  # noqa: E501


        :return: The exclude of this TransactionReportRequestData.  # noqa: E501
        :rtype: str
        """
        return self._exclude

    @exclude.setter
    def exclude(self, exclude):
        """Sets the exclude of this TransactionReportRequestData.


        :param exclude: The exclude of this TransactionReportRequestData.  # noqa: E501
        :type: str
        """

        self._exclude = exclude

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
        if issubclass(TransactionReportRequestData, dict):
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
        if not isinstance(other, TransactionReportRequestData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
