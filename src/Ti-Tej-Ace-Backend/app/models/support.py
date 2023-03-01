# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.tags import Tags  # noqa: F401,E501


class Support(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, type: str=None, ref_id: str=None, channels: Tags=None):  # noqa: E501
        """Support - a model defined in Swagger

        :param type: The type of this Support.  # noqa: E501
        :type type: str
        :param ref_id: The ref_id of this Support.  # noqa: E501
        :type ref_id: str
        :param channels: The channels of this Support.  # noqa: E501
        :type channels: Tags
        """
        self.swagger_types = {
            'type': str,
            'ref_id': str,
            'channels': Tags
        }

        self.attribute_map = {
            'type': 'type',
            'ref_id': 'ref_id',
            'channels': 'channels'
        }
        self._type = type
        self._ref_id = ref_id
        self._channels = channels

    @classmethod
    def from_dict(cls, dikt) -> 'Support':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Support of this Support.  # noqa: E501
        :rtype: Support
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this Support.


        :return: The type of this Support.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this Support.


        :param type: The type of this Support.
        :type type: str
        """
        allowed_values = ["order", "billing", "fulfillment"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def ref_id(self) -> str:
        """Gets the ref_id of this Support.


        :return: The ref_id of this Support.
        :rtype: str
        """
        return self._ref_id

    @ref_id.setter
    def ref_id(self, ref_id: str):
        """Sets the ref_id of this Support.


        :param ref_id: The ref_id of this Support.
        :type ref_id: str
        """

        self._ref_id = ref_id

    @property
    def channels(self) -> Tags:
        """Gets the channels of this Support.


        :return: The channels of this Support.
        :rtype: Tags
        """
        return self._channels

    @channels.setter
    def channels(self, channels: Tags):
        """Sets the channels of this Support.


        :param channels: The channels of this Support.
        :type channels: Tags
        """

        self._channels = channels
