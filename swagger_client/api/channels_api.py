# coding: utf-8

"""
    BVNK API Endpoints

    The BVNK API is designed to facilitate seamless and secure transactions including payments, channels, anddigital wallet transactions.  # noqa: E501

    OpenAPI spec version: 1.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ChannelsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_v2_channel_get(self, merchant_id, **kwargs):  # noqa: E501
        """List Channels  # noqa: E501

        Retrieves all channels related to a Merchant ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_get(merchant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_id: The merchant ID that the channels belong to (required)
        :param str offset: Offset
        :param str max: Maximum number of items in response
        :param PaymentStatusDto sort: The attribute used to sort the data
        :param str order: Ordering direction
        :return: list[MerchantChannel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_channel_get_with_http_info(merchant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_channel_get_with_http_info(merchant_id, **kwargs)  # noqa: E501
            return data

    def api_v2_channel_get_with_http_info(self, merchant_id, **kwargs):  # noqa: E501
        """List Channels  # noqa: E501

        Retrieves all channels related to a Merchant ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_get_with_http_info(merchant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_id: The merchant ID that the channels belong to (required)
        :param str offset: Offset
        :param str max: Maximum number of items in response
        :param PaymentStatusDto sort: The attribute used to sort the data
        :param str order: Ordering direction
        :return: list[MerchantChannel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_id', 'offset', 'max', 'sort', 'order']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_channel_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_id' is set
        if ('merchant_id' not in params or
                params['merchant_id'] is None):
            raise ValueError("Missing the required parameter `merchant_id` when calling `api_v2_channel_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'merchant_id' in params:
            query_params.append(('merchantId', params['merchant_id']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'max' in params:
            query_params.append(('max', params['max']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Hawk']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/channel', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MerchantChannel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_channel_payment_get(self, merchant_id, **kwargs):  # noqa: E501
        """List Channel Payments  # noqa: E501

        Retrieves a list of payments to a channel on a specific Merchant ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_payment_get(merchant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_id: The Merchant ID (required)
        :param str status:
        :param str from_date: From which date to start searching.
        :param str to_date: At which date to stop searching.
        :param str offset: Where to start fetching records.
        :param str max: Maximum number of items in response
        :param str order: Ordering direction
        :param str q: Can be UUID of the payment, reference, channel UUID, transaction hash, or wallet code.
        :return: list[MerchantChannelPayment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_channel_payment_get_with_http_info(merchant_id, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_channel_payment_get_with_http_info(merchant_id, **kwargs)  # noqa: E501
            return data

    def api_v2_channel_payment_get_with_http_info(self, merchant_id, **kwargs):  # noqa: E501
        """List Channel Payments  # noqa: E501

        Retrieves a list of payments to a channel on a specific Merchant ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_payment_get_with_http_info(merchant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str merchant_id: The Merchant ID (required)
        :param str status:
        :param str from_date: From which date to start searching.
        :param str to_date: At which date to stop searching.
        :param str offset: Where to start fetching records.
        :param str max: Maximum number of items in response
        :param str order: Ordering direction
        :param str q: Can be UUID of the payment, reference, channel UUID, transaction hash, or wallet code.
        :return: list[MerchantChannelPayment]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['merchant_id', 'status', 'from_date', 'to_date', 'offset', 'max', 'order', 'q']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_channel_payment_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'merchant_id' is set
        if ('merchant_id' not in params or
                params['merchant_id'] is None):
            raise ValueError("Missing the required parameter `merchant_id` when calling `api_v2_channel_payment_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'merchant_id' in params:
            query_params.append(('merchantId', params['merchant_id']))  # noqa: E501
        if 'status' in params:
            query_params.append(('status', params['status']))  # noqa: E501
        if 'from_date' in params:
            query_params.append(('fromDate', params['from_date']))  # noqa: E501
        if 'to_date' in params:
            query_params.append(('toDate', params['to_date']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'max' in params:
            query_params.append(('max', params['max']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'q' in params:
            query_params.append(('q', params['q']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Hawk']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/channel/payment', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MerchantChannelPayment]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_channel_payment_uuid_get(self, uuid, **kwargs):  # noqa: E501
        """Get Channel Payment  # noqa: E501

        Retrieves a specific payment made into a channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_payment_uuid_get(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: The UUID of the payment you are querying. (required)
        :return: MerchantChannelPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_channel_payment_uuid_get_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_channel_payment_uuid_get_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def api_v2_channel_payment_uuid_get_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Get Channel Payment  # noqa: E501

        Retrieves a specific payment made into a channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_payment_uuid_get_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: The UUID of the payment you are querying. (required)
        :return: MerchantChannelPayment
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_channel_payment_uuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `api_v2_channel_payment_uuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Hawk']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/channel/payment/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MerchantChannelPayment',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_channel_post(self, **kwargs):  # noqa: E501
        """Create Channel  # noqa: E501

        Creates a channel that your end users can openly send payments to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MerchantChannelRequest body:
        :return: MerchantChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_channel_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_channel_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def api_v2_channel_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create Channel  # noqa: E501

        Creates a channel that your end users can openly send payments to.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MerchantChannelRequest body:
        :return: MerchantChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_channel_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Hawk']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/channel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MerchantChannel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_v2_channel_uuid_get(self, uuid, **kwargs):  # noqa: E501
        """Get Channel  # noqa: E501

        Retrieves a specific channel by UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_uuid_get(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: The UUID of the channel you are querying (required)
        :return: MerchantChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.api_v2_channel_uuid_get_with_http_info(uuid, **kwargs)  # noqa: E501
        else:
            (data) = self.api_v2_channel_uuid_get_with_http_info(uuid, **kwargs)  # noqa: E501
            return data

    def api_v2_channel_uuid_get_with_http_info(self, uuid, **kwargs):  # noqa: E501
        """Get Channel  # noqa: E501

        Retrieves a specific channel by UUID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_v2_channel_uuid_get_with_http_info(uuid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str uuid: The UUID of the channel you are querying (required)
        :return: MerchantChannel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['uuid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v2_channel_uuid_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'uuid' is set
        if ('uuid' not in params or
                params['uuid'] is None):
            raise ValueError("Missing the required parameter `uuid` when calling `api_v2_channel_uuid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'uuid' in params:
            path_params['uuid'] = params['uuid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['Hawk']  # noqa: E501

        return self.api_client.call_api(
            '/api/v2/channel/{uuid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MerchantChannel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
