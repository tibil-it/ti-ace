# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.context import Context  # noqa: F401,E501
from models.select_message import SelectMessage  # noqa: F401,E501


class ConfirmBody(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, context: Context=None, message: SelectMessage=None):  # noqa: E501
        """ConfirmBody - a model defined in Swagger

        :param context: The context of this ConfirmBody.  # noqa: E501
        :type context: Context
        :param message: The message of this ConfirmBody.  # noqa: E501
        :type message: SelectMessage
        """
        self.swagger_types = {
            'context': Context,
            'message': SelectMessage
        }

        self.attribute_map = {
            'context': 'context',
            'message': 'message'
        }
        self._context = context
        self._message = message

    @classmethod
    def from_dict(cls, dikt) -> 'ConfirmBody':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The confirm_body of this ConfirmBody.  # noqa: E501
        :rtype: ConfirmBody
        """
        return util.deserialize_model(dikt, cls)

    @property
    def context(self) -> Context:
        """Gets the context of this ConfirmBody.


        :return: The context of this ConfirmBody.
        :rtype: Context
        """
        return self._context

    @context.setter
    def context(self, context: Context):
        """Sets the context of this ConfirmBody.


        :param context: The context of this ConfirmBody.
        :type context: Context
        """
        if context is None:
            raise ValueError("Invalid value for `context`, must not be `None`")  # noqa: E501

        self._context = context

    @property
    def message(self) -> SelectMessage:
        """Gets the message of this ConfirmBody.


        :return: The message of this ConfirmBody.
        :rtype: SelectMessage
        """
        return self._message

    @message.setter
    def message(self, message: SelectMessage):
        """Sets the message of this ConfirmBody.


        :param message: The message of this ConfirmBody.
        :type message: SelectMessage
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message
