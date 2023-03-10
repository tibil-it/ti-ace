# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.option import Option  # noqa: F401,E501


class CancellationReasonsMessage(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, cancellation_reasons: List[Option]=None):  # noqa: E501
        """CancellationReasonsMessage - a model defined in Swagger

        :param cancellation_reasons: The cancellation_reasons of this CancellationReasonsMessage.  # noqa: E501
        :type cancellation_reasons: List[Option]
        """
        self.swagger_types = {
            'cancellation_reasons': List[Option]
        }

        self.attribute_map = {
            'cancellation_reasons': 'cancellation_reasons'
        }
        self._cancellation_reasons = cancellation_reasons

    @classmethod
    def from_dict(cls, dikt) -> 'CancellationReasonsMessage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The cancellation_reasons_message of this CancellationReasonsMessage.  # noqa: E501
        :rtype: CancellationReasonsMessage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cancellation_reasons(self) -> List[Option]:
        """Gets the cancellation_reasons of this CancellationReasonsMessage.


        :return: The cancellation_reasons of this CancellationReasonsMessage.
        :rtype: List[Option]
        """
        return self._cancellation_reasons

    @cancellation_reasons.setter
    def cancellation_reasons(self, cancellation_reasons: List[Option]):
        """Sets the cancellation_reasons of this CancellationReasonsMessage.


        :param cancellation_reasons: The cancellation_reasons of this CancellationReasonsMessage.
        :type cancellation_reasons: List[Option]
        """

        self._cancellation_reasons = cancellation_reasons
