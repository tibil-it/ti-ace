# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.descriptor import Descriptor  # noqa: F401,E501


class Option(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, descriptor: Descriptor=None):  # noqa: E501
        """Option - a model defined in Swagger

        :param id: The id of this Option.  # noqa: E501
        :type id: str
        :param descriptor: The descriptor of this Option.  # noqa: E501
        :type descriptor: Descriptor
        """
        self.swagger_types = {
            'id': str,
            'descriptor': Descriptor
        }

        self.attribute_map = {
            'id': 'id',
            'descriptor': 'descriptor'
        }
        self._id = id
        self._descriptor = descriptor

    @classmethod
    def from_dict(cls, dikt) -> 'Option':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Option of this Option.  # noqa: E501
        :rtype: Option
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Option.


        :return: The id of this Option.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Option.


        :param id: The id of this Option.
        :type id: str
        """

        self._id = id

    @property
    def descriptor(self) -> Descriptor:
        """Gets the descriptor of this Option.


        :return: The descriptor of this Option.
        :rtype: Descriptor
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor: Descriptor):
        """Sets the descriptor of this Option.


        :param descriptor: The descriptor of this Option.
        :type descriptor: Descriptor
        """

        self._descriptor = descriptor
