# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model


class FullAddress(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, full: str=None):  # noqa: E501
        """FullAddress - a model defined in Swagger

        :param full: The full of this FullAddress.  # noqa: E501
        :type full: str
        """
        self.swagger_types = {
            'full': str
        }

        self.attribute_map = {
            'full': 'full'
        }
        self._full = full

    @classmethod
    def from_dict(cls, dikt) -> 'FullAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FullAddress of this FullAddress.  # noqa: E501
        :rtype: FullAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def full(self) -> str:
        """Gets the full of this FullAddress.

        This is an unstructured string that describes the complete postal address in one line. If supported, the format of this field should be defined in the network policy. If this field is set, then the validator must ignore all the other fields. If this field is unavailable or null, then the validator must validate all the other fields of this object.  # noqa: E501

        :return: The full of this FullAddress.
        :rtype: str
        """
        return self._full

    @full.setter
    def full(self, full: str):
        """Sets the full of this FullAddress.

        This is an unstructured string that describes the complete postal address in one line. If supported, the format of this field should be defined in the network policy. If this field is set, then the validator must ignore all the other fields. If this field is unavailable or null, then the validator must validate all the other fields of this object.  # noqa: E501

        :param full: The full of this FullAddress.
        :type full: str
        """

        self._full = full
