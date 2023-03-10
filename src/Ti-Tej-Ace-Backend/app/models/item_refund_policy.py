# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model


class ItemRefundPolicy(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, refundable: bool=None, refund_applicable_till: datetime=None, refund_type: str=None, refund_amount_type: str=None, refund_amount_value: float=None):  # noqa: E501
        """ItemRefundPolicy - a model defined in Swagger

        :param refundable: The refundable of this ItemRefundPolicy.  # noqa: E501
        :type refundable: bool
        :param refund_applicable_till: The refund_applicable_till of this ItemRefundPolicy.  # noqa: E501
        :type refund_applicable_till: datetime
        :param refund_type: The refund_type of this ItemRefundPolicy.  # noqa: E501
        :type refund_type: str
        :param refund_amount_type: The refund_amount_type of this ItemRefundPolicy.  # noqa: E501
        :type refund_amount_type: str
        :param refund_amount_value: The refund_amount_value of this ItemRefundPolicy.  # noqa: E501
        :type refund_amount_value: float
        """
        self.swagger_types = {
            'refundable': bool,
            'refund_applicable_till': datetime,
            'refund_type': str,
            'refund_amount_type': str,
            'refund_amount_value': float
        }

        self.attribute_map = {
            'refundable': 'refundable',
            'refund_applicable_till': 'refund_applicable_till',
            'refund_type': 'refund_type',
            'refund_amount_type': 'refund_amount_type',
            'refund_amount_value': 'refund_amount_value'
        }
        self._refundable = refundable
        self._refund_applicable_till = refund_applicable_till
        self._refund_type = refund_type
        self._refund_amount_type = refund_amount_type
        self._refund_amount_value = refund_amount_value

    @classmethod
    def from_dict(cls, dikt) -> 'ItemRefundPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ItemRefundPolicy of this ItemRefundPolicy.  # noqa: E501
        :rtype: ItemRefundPolicy
        """
        return util.deserialize_model(dikt, cls)

    @property
    def refundable(self) -> bool:
        """Gets the refundable of this ItemRefundPolicy.


        :return: The refundable of this ItemRefundPolicy.
        :rtype: bool
        """
        return self._refundable

    @refundable.setter
    def refundable(self, refundable: bool):
        """Sets the refundable of this ItemRefundPolicy.


        :param refundable: The refundable of this ItemRefundPolicy.
        :type refundable: bool
        """

        self._refundable = refundable

    @property
    def refund_applicable_till(self) -> datetime:
        """Gets the refund_applicable_till of this ItemRefundPolicy.


        :return: The refund_applicable_till of this ItemRefundPolicy.
        :rtype: datetime
        """
        return self._refund_applicable_till

    @refund_applicable_till.setter
    def refund_applicable_till(self, refund_applicable_till: datetime):
        """Sets the refund_applicable_till of this ItemRefundPolicy.


        :param refund_applicable_till: The refund_applicable_till of this ItemRefundPolicy.
        :type refund_applicable_till: datetime
        """

        self._refund_applicable_till = refund_applicable_till

    @property
    def refund_type(self) -> str:
        """Gets the refund_type of this ItemRefundPolicy.


        :return: The refund_type of this ItemRefundPolicy.
        :rtype: str
        """
        return self._refund_type

    @refund_type.setter
    def refund_type(self, refund_type: str):
        """Sets the refund_type of this ItemRefundPolicy.


        :param refund_type: The refund_type of this ItemRefundPolicy.
        :type refund_type: str
        """
        allowed_values = ["FULLY-REFUNDABLE", "PARTLY-REFUNDABLE", "VARIABLE-REFUND"]  # noqa: E501
        if refund_type not in allowed_values:
            raise ValueError(
                "Invalid value for `refund_type` ({0}), must be one of {1}"
                .format(refund_type, allowed_values)
            )

        self._refund_type = refund_type

    @property
    def refund_amount_type(self) -> str:
        """Gets the refund_amount_type of this ItemRefundPolicy.


        :return: The refund_amount_type of this ItemRefundPolicy.
        :rtype: str
        """
        return self._refund_amount_type

    @refund_amount_type.setter
    def refund_amount_type(self, refund_amount_type: str):
        """Sets the refund_amount_type of this ItemRefundPolicy.


        :param refund_amount_type: The refund_amount_type of this ItemRefundPolicy.
        :type refund_amount_type: str
        """
        allowed_values = ["CONSTANT-AMOUNT", "CONSTANT-PERCENTAGE", "VARIABLE-AMOUNT", "VARIABLE-PERCENTAGE"]  # noqa: E501
        if refund_amount_type not in allowed_values:
            raise ValueError(
                "Invalid value for `refund_amount_type` ({0}), must be one of {1}"
                .format(refund_amount_type, allowed_values)
            )

        self._refund_amount_type = refund_amount_type

    @property
    def refund_amount_value(self) -> float:
        """Gets the refund_amount_value of this ItemRefundPolicy.


        :return: The refund_amount_value of this ItemRefundPolicy.
        :rtype: float
        """
        return self._refund_amount_value

    @refund_amount_value.setter
    def refund_amount_value(self, refund_amount_value: float):
        """Sets the refund_amount_value of this ItemRefundPolicy.


        :param refund_amount_value: The refund_amount_value of this ItemRefundPolicy.
        :type refund_amount_value: float
        """

        self._refund_amount_value = refund_amount_value
