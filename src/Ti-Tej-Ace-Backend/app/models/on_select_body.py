# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.context import Context  # noqa: F401,E501
from models.error import Error  # noqa: F401,E501
from models.on_select_message import OnSelectMessage  # noqa: F401,E501


class OnSelectBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, context: Context=None, message: OnSelectMessage=None, error: Error=None):  # noqa: E501
        """OnSelectBody - a model defined in Swagger

        :param context: The context of this OnSelectBody.  # noqa: E501
        :type context: Context
        :param message: The message of this OnSelectBody.  # noqa: E501
        :type message: OnSelectMessage
        :param error: The error of this OnSelectBody.  # noqa: E501
        :type error: Error
        """
        self.swagger_types = {
            'context': Context,
            'message': OnSelectMessage,
            'error': Error
        }

        self.attribute_map = {
            'context': 'context',
            'message': 'message',
            'error': 'error'
        }
        self._context = context
        self._message = message
        self._error = error

    @classmethod
    def from_dict(cls, dikt) -> 'OnSelectBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The on_select_body of this OnSelectBody.  # noqa: E501
        :rtype: OnSelectBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self) -> Context:
        """Gets the context of this OnSelectBody.


        :return: The context of this OnSelectBody.
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context: Context):
        """Sets the context of this OnSelectBody.


        :param context: The context of this OnSelectBody.
        :type context: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def message(self) -> OnSelectMessage:
        """Gets the message of this OnSelectBody.


        :return: The message of this OnSelectBody.
        :rtype: OnSelectMessage
        """
        return self._message

    @message.setter
    def message(self, message: OnSelectMessage):
        """Sets the message of this OnSelectBody.


        :param message: The message of this OnSelectBody.
        :type message: OnSelectMessage
        """

        self._message = message

    @property
    def error(self) -> Error:
        """Gets the error of this OnSelectBody.


        :return: The error of this OnSelectBody.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error: Error):
        """Sets the error of this OnSelectBody.


        :param error: The error of this OnSelectBody.
        :type error: Error
        """

        self._error = error
