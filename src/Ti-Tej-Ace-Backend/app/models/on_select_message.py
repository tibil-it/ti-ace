# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.on_select_message_order import OnSelectMessageOrder  # noqa: F401,E501


class OnSelectMessage(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, order: OnSelectMessageOrder=None):  # noqa: E501
        """OnSelectMessage - a model defined in Swagger

        :param order: The order of this OnSelectMessage.  # noqa: E501
        :type order: OnSelectMessageOrder
        """
        self.swagger_types = {
            'order': OnSelectMessageOrder
        }

        self.attribute_map = {
            'order': 'order'
        }
        self._order = order

    @classmethod
    def from_dict(cls, dikt) -> 'OnSelectMessage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The on_select_message of this OnSelectMessage.  # noqa: E501
        :rtype: OnSelectMessage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def order(self) -> OnSelectMessageOrder:
        """Gets the order of this OnSelectMessage.


        :return: The order of this OnSelectMessage.
        :rtype: OnSelectMessageOrder
        """
        return self._order

    @order.setter
    def order(self, order: OnSelectMessageOrder):
        """Sets the order of this OnSelectMessage.


        :param order: The order of this OnSelectMessage.
        :type order: OnSelectMessageOrder
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order
