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

class MerchantChannel(object):
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
        'id': 'int',
        'date_created': 'int',
        'last_updated': 'int',
        'merchant_id': 'str',
        'wallet_currency': 'str',
        'display_currency': 'str',
        'pay_currency': 'str',
        'address': 'str',
        'tag': 'str',
        'protocol': 'str',
        'reference': 'str',
        'status': 'str',
        'uuid': 'str',
        'redirect_url': 'str',
        'uri': 'str',
        'alternatives': 'list[AlternativeAddress]'
    }

    attribute_map = {
        'id': 'id',
        'date_created': 'dateCreated',
        'last_updated': 'lastUpdated',
        'merchant_id': 'merchantId',
        'wallet_currency': 'walletCurrency',
        'display_currency': 'displayCurrency',
        'pay_currency': 'payCurrency',
        'address': 'address',
        'tag': 'tag',
        'protocol': 'protocol',
        'reference': 'reference',
        'status': 'status',
        'uuid': 'uuid',
        'redirect_url': 'redirectUrl',
        'uri': 'uri',
        'alternatives': 'alternatives'
    }

    def __init__(self, id=0, date_created=0, last_updated=0, merchant_id=None, wallet_currency=None, display_currency=None, pay_currency=None, address=None, tag=None, protocol=None, reference=None, status=None, uuid=None, redirect_url=None, uri=None, alternatives=None):  # noqa: E501
        """MerchantChannel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._date_created = None
        self._last_updated = None
        self._merchant_id = None
        self._wallet_currency = None
        self._display_currency = None
        self._pay_currency = None
        self._address = None
        self._tag = None
        self._protocol = None
        self._reference = None
        self._status = None
        self._uuid = None
        self._redirect_url = None
        self._uri = None
        self._alternatives = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if date_created is not None:
            self.date_created = date_created
        if last_updated is not None:
            self.last_updated = last_updated
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if wallet_currency is not None:
            self.wallet_currency = wallet_currency
        if display_currency is not None:
            self.display_currency = display_currency
        if pay_currency is not None:
            self.pay_currency = pay_currency
        if address is not None:
            self.address = address
        if tag is not None:
            self.tag = tag
        if protocol is not None:
            self.protocol = protocol
        if reference is not None:
            self.reference = reference
        if status is not None:
            self.status = status
        if uuid is not None:
            self.uuid = uuid
        if redirect_url is not None:
            self.redirect_url = redirect_url
        if uri is not None:
            self.uri = uri
        if alternatives is not None:
            self.alternatives = alternatives

    @property
    def id(self):
        """Gets the id of this MerchantChannel.  # noqa: E501


        :return: The id of this MerchantChannel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MerchantChannel.


        :param id: The id of this MerchantChannel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def date_created(self):
        """Gets the date_created of this MerchantChannel.  # noqa: E501


        :return: The date_created of this MerchantChannel.  # noqa: E501
        :rtype: int
        """
        return self._date_created

    @date_created.setter
    def date_created(self, date_created):
        """Sets the date_created of this MerchantChannel.


        :param date_created: The date_created of this MerchantChannel.  # noqa: E501
        :type: int
        """

        self._date_created = date_created

    @property
    def last_updated(self):
        """Gets the last_updated of this MerchantChannel.  # noqa: E501


        :return: The last_updated of this MerchantChannel.  # noqa: E501
        :rtype: int
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this MerchantChannel.


        :param last_updated: The last_updated of this MerchantChannel.  # noqa: E501
        :type: int
        """

        self._last_updated = last_updated

    @property
    def merchant_id(self):
        """Gets the merchant_id of this MerchantChannel.  # noqa: E501


        :return: The merchant_id of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this MerchantChannel.


        :param merchant_id: The merchant_id of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def wallet_currency(self):
        """Gets the wallet_currency of this MerchantChannel.  # noqa: E501


        :return: The wallet_currency of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._wallet_currency

    @wallet_currency.setter
    def wallet_currency(self, wallet_currency):
        """Sets the wallet_currency of this MerchantChannel.


        :param wallet_currency: The wallet_currency of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._wallet_currency = wallet_currency

    @property
    def display_currency(self):
        """Gets the display_currency of this MerchantChannel.  # noqa: E501


        :return: The display_currency of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._display_currency

    @display_currency.setter
    def display_currency(self, display_currency):
        """Sets the display_currency of this MerchantChannel.


        :param display_currency: The display_currency of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._display_currency = display_currency

    @property
    def pay_currency(self):
        """Gets the pay_currency of this MerchantChannel.  # noqa: E501


        :return: The pay_currency of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._pay_currency

    @pay_currency.setter
    def pay_currency(self, pay_currency):
        """Sets the pay_currency of this MerchantChannel.


        :param pay_currency: The pay_currency of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._pay_currency = pay_currency

    @property
    def address(self):
        """Gets the address of this MerchantChannel.  # noqa: E501


        :return: The address of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this MerchantChannel.


        :param address: The address of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def tag(self):
        """Gets the tag of this MerchantChannel.  # noqa: E501


        :return: The tag of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this MerchantChannel.


        :param tag: The tag of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def protocol(self):
        """Gets the protocol of this MerchantChannel.  # noqa: E501


        :return: The protocol of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this MerchantChannel.


        :param protocol: The protocol of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def reference(self):
        """Gets the reference of this MerchantChannel.  # noqa: E501


        :return: The reference of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this MerchantChannel.


        :param reference: The reference of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def status(self):
        """Gets the status of this MerchantChannel.  # noqa: E501


        :return: The status of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MerchantChannel.


        :param status: The status of this MerchantChannel.  # noqa: E501
        :type: str
        """
        allowed_values = ["OPEN", "CLOSED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def uuid(self):
        """Gets the uuid of this MerchantChannel.  # noqa: E501


        :return: The uuid of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this MerchantChannel.


        :param uuid: The uuid of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def redirect_url(self):
        """Gets the redirect_url of this MerchantChannel.  # noqa: E501


        :return: The redirect_url of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """Sets the redirect_url of this MerchantChannel.


        :param redirect_url: The redirect_url of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._redirect_url = redirect_url

    @property
    def uri(self):
        """Gets the uri of this MerchantChannel.  # noqa: E501


        :return: The uri of this MerchantChannel.  # noqa: E501
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """Sets the uri of this MerchantChannel.


        :param uri: The uri of this MerchantChannel.  # noqa: E501
        :type: str
        """

        self._uri = uri

    @property
    def alternatives(self):
        """Gets the alternatives of this MerchantChannel.  # noqa: E501


        :return: The alternatives of this MerchantChannel.  # noqa: E501
        :rtype: list[AlternativeAddress]
        """
        return self._alternatives

    @alternatives.setter
    def alternatives(self, alternatives):
        """Sets the alternatives of this MerchantChannel.


        :param alternatives: The alternatives of this MerchantChannel.  # noqa: E501
        :type: list[AlternativeAddress]
        """

        self._alternatives = alternatives

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
        if issubclass(MerchantChannel, dict):
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
        if not isinstance(other, MerchantChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
