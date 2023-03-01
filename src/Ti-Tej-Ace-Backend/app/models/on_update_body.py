# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.context import Context  # noqa: F401,E501
from models.error import Error  # noqa: F401,E501
from models.select_message import SelectMessage  # noqa: F401,E501


class OnUpdateBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, context: Context=None, message: SelectMessage=None, error: Error=None):  # noqa: E501
        """OnUpdateBody - a model defined in Swagger

        :param context: The context of this OnUpdateBody.  # noqa: E501
        :type context: Context
        :param message: The message of this OnUpdateBody.  # noqa: E501
        :type message: SelectMessage
        :param error: The error of this OnUpdateBody.  # noqa: E501
        :type error: Error
        """
        self.swagger_types = {
            'context': Context,
            'message': SelectMessage,
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
    def from_dict(cls, dikt) -> 'OnUpdateBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The on_update_body of this OnUpdateBody.  # noqa: E501
        :rtype: OnUpdateBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self) -> Context:
        """Gets the context of this OnUpdateBody.


        :return: The context of this OnUpdateBody.
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context: Context):
        """Sets the context of this OnUpdateBody.


        :param context: The context of this OnUpdateBody.
        :type context: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def message(self) -> SelectMessage:
        """Gets the message of this OnUpdateBody.


        :return: The message of this OnUpdateBody.
        :rtype: SelectMessage
        """
        return self._message

    @message.setter
    def message(self, message: SelectMessage):
        """Sets the message of this OnUpdateBody.


        :param message: The message of this OnUpdateBody.
        :type message: SelectMessage
        """

        self._message = message

    @property
    def error(self) -> Error:
        """Gets the error of this OnUpdateBody.


        :return: The error of this OnUpdateBody.
        :rtype: Error
        """
        return self._error

    @error.setter
    def error(self, error: Error):
        """Sets the error of this OnUpdateBody.


        :param error: The error of this OnUpdateBody.
        :type error: Error
        """

        self._error = error
