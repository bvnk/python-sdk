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

class ValidationErrorDto(object):
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
        'parameter': 'str',
        'message': 'str'
    }

    attribute_map = {
        'code': 'code',
        'parameter': 'parameter',
        'message': 'message'
    }

    def __init__(self, code=None, parameter=None, message=None):  # noqa: E501
        """ValidationErrorDto - a model defined in Swagger"""  # noqa: E501
        self._code = None
        self._parameter = None
        self._message = None
        self.discriminator = None
        self.code = code
        self.parameter = parameter
        self.message = message

    @property
    def code(self):
        """Gets the code of this ValidationErrorDto.  # noqa: E501

        this is used to get internationalisation translation  # noqa: E501

        :return: The code of this ValidationErrorDto.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ValidationErrorDto.

        this is used to get internationalisation translation  # noqa: E501

        :param code: The code of this ValidationErrorDto.  # noqa: E501
        :type: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")  # noqa: E501

        self._code = code

    @property
    def parameter(self):
        """Gets the parameter of this ValidationErrorDto.  # noqa: E501

        input that is causing the error  # noqa: E501

        :return: The parameter of this ValidationErrorDto.  # noqa: E501
        :rtype: str
        """
        return self._parameter

    @parameter.setter
    def parameter(self, parameter):
        """Sets the parameter of this ValidationErrorDto.

        input that is causing the error  # noqa: E501

        :param parameter: The parameter of this ValidationErrorDto.  # noqa: E501
        :type: str
        """
        if parameter is None:
            raise ValueError("Invalid value for `parameter`, must not be `None`")  # noqa: E501

        self._parameter = parameter

    @property
    def message(self):
        """Gets the message of this ValidationErrorDto.  # noqa: E501

        exception message  # noqa: E501

        :return: The message of this ValidationErrorDto.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ValidationErrorDto.

        exception message  # noqa: E501

        :param message: The message of this ValidationErrorDto.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

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
        if issubclass(ValidationErrorDto, dict):
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
        if not isinstance(other, ValidationErrorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other