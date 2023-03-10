# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.context import Context  # noqa: F401,E501
from models.error import Error  # noqa: F401,E501
from models.on_init_message import OnInitMessage  # noqa: F401,E501


class OnInitBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, context: Context=None, message: OnInitMessage=None, error: Error=None):  # noqa: E501
        """OnInitBody - a model defined in Swagger

        :param context: The context of this OnInitBody.  # noqa: E501
        :type context: Context
        :param message: The message of this OnInitBody.  # noqa: E501
        :type message: OnInitMessage
        :param error: The error of this OnInitBody.  # noqa: E501
        :type error: Error
        """
        self.swagger_types = {
            'context': Context,
            'message': OnInitMessage,
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
    def from_dict(cls, dikt) -> 'OnInitBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The on_init_body of this OnInitBody.  # noqa: E501
        :rtype: OnInitBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self) -> Context:
        """Gets the context of this OnInitBody.


        :return: The context of this OnInitBody.
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context: Context):
        """Sets the context of this OnInitBody.


        :param context: The context of this OnInitBody.
        :type context: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def message(self) -> OnInitMessage:
        """Gets the message of this OnInitBody.


        :return: The message of this OnInitBody.
        :rtype: OnInitMessage
        """
        return self._message

    @message.setter
    def message(self, message: OnInitMessage):
        """Sets the message of this OnInitBody.


        :param message: The message of this OnInitBody.
        :type message: OnInitMessage
        """

        self._message = message

    @property
    def error(self) -> Error:
        """Gets the error of this OnInitBody.


        :return: The error of this OnInitBody.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error: Error):
        """Sets the error of this OnInitBody.


        :param error: The error of this OnInitBody.
        :type error: Error
        """

        self._error = error
