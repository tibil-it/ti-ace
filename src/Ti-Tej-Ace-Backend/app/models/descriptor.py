# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.image import Image  # noqa: F401,E501


class Descriptor(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, name: str=None, code: str=None, symbol: str=None, short_desc: str=None, long_desc: str=None, images: List[Image]=None, audio: str=None, _3d_render: str=None):  # noqa: E501
        """Descriptor - a model defined in Swagger

        :param name: The name of this Descriptor.  # noqa: E501
        :type name: str
        :param code: The code of this Descriptor.  # noqa: E501
        :type code: str
        :param symbol: The symbol of this Descriptor.  # noqa: E501
        :type symbol: str
        :param short_desc: The short_desc of this Descriptor.  # noqa: E501
        :type short_desc: str
        :param long_desc: The long_desc of this Descriptor.  # noqa: E501
        :type long_desc: str
        :param images: The images of this Descriptor.  # noqa: E501
        :type images: List[Image]
        :param audio: The audio of this Descriptor.  # noqa: E501
        :type audio: str
        :param _3d_render: The _3d_render of this Descriptor.  # noqa: E501
        :type _3d_render: str
        """
        self.swagger_types = {
            'name': str,
            'code': str,
            'symbol': str,
            'short_desc': str,
            'long_desc': str,
            'images': List[Image],
            'audio': str,
            '_3d_render': str
        }

        self.attribute_map = {
            'name': 'name',
            'code': 'code',
            'symbol': 'symbol',
            'short_desc': 'short_desc',
            'long_desc': 'long_desc',
            'images': 'images',
            'audio': 'audio',
            '_3d_render': '3d_render'
        }
        self._name = name
        self._code = code
        self._symbol = symbol
        self._short_desc = short_desc
        self._long_desc = long_desc
        self._images = images
        self._audio = audio
        self.__3d_render = _3d_render

    @classmethod
    def from_dict(cls, dikt) -> 'Descriptor':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Descriptor of this Descriptor.  # noqa: E501
        :rtype: Descriptor
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self) -> str:
        """Gets the name of this Descriptor.


        :return: The name of this Descriptor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this Descriptor.


        :param name: The name of this Descriptor.
        :type name: str
        """

        self._name = name

    @property
    def code(self) -> str:
        """Gets the code of this Descriptor.


        :return: The code of this Descriptor.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this Descriptor.


        :param code: The code of this Descriptor.
        :type code: str
        """

        self._code = code

    @property
    def symbol(self) -> str:
        """Gets the symbol of this Descriptor.


        :return: The symbol of this Descriptor.
        :rtype: str
        """
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """Sets the symbol of this Descriptor.


        :param symbol: The symbol of this Descriptor.
        :type symbol: str
        """

        self._symbol = symbol

    @property
    def short_desc(self) -> str:
        """Gets the short_desc of this Descriptor.


        :return: The short_desc of this Descriptor.
        :rtype: str
        """
        return self._short_desc

    @short_desc.setter
    def short_desc(self, short_desc: str):
        """Sets the short_desc of this Descriptor.


        :param short_desc: The short_desc of this Descriptor.
        :type short_desc: str
        """

        self._short_desc = short_desc

    @property
    def long_desc(self) -> str:
        """Gets the long_desc of this Descriptor.


        :return: The long_desc of this Descriptor.
        :rtype: str
        """
        return self._long_desc

    @long_desc.setter
    def long_desc(self, long_desc: str):
        """Sets the long_desc of this Descriptor.


        :param long_desc: The long_desc of this Descriptor.
        :type long_desc: str
        """

        self._long_desc = long_desc

    @property
    def images(self) -> List[Image]:
        """Gets the images of this Descriptor.


        :return: The images of this Descriptor.
        :rtype: List[Image]
        """
        return self._images

    @images.setter
    def images(self, images: List[Image]):
        """Sets the images of this Descriptor.


        :param images: The images of this Descriptor.
        :type images: List[Image]
        """

        self._images = images

    @property
    def audio(self) -> str:
        """Gets the audio of this Descriptor.


        :return: The audio of this Descriptor.
        :rtype: str
        """
        return self._audio

    @audio.setter
    def audio(self, audio: str):
        """Sets the audio of this Descriptor.


        :param audio: The audio of this Descriptor.
        :type audio: str
        """

        self._audio = audio

    @property
    def _3d_render(self) -> str:
        """Gets the _3d_render of this Descriptor.


        :return: The _3d_render of this Descriptor.
        :rtype: str
        """
        return self.__3d_render

    @_3d_render.setter
    def _3d_render(self, _3d_render: str):
        """Sets the _3d_render of this Descriptor.


        :param _3d_render: The _3d_render of this Descriptor.
        :type _3d_render: str
        """

        self.__3d_render = _3d_render
