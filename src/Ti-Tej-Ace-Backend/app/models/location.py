# coding: utf-8

from __future__ import absolute_import

import re  # noqa: F401,E501
from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.address import Address  # noqa: F401,E501
from models.base_model_ import Model
from models.circle import Circle  # noqa: F401,E501
from models.city import City  # noqa: F401,E501
from models.country import Country  # noqa: F401,E501
from models.descriptor import Descriptor  # noqa: F401,E501
from models.gps import Gps  # noqa: F401,E501
from models.time import Time  # noqa: F401,E501


class Location(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, id: str=None, descriptor: Descriptor=None, gps: Gps=None, address: Address=None, station_code: str=None, city: City=None, country: Country=None, circle: Circle=None, polygon: str=None, _3dspace: str=None, time: Time=None):  # noqa: E501
        """Location - a model defined in Swagger

        :param id: The id of this Location.  # noqa: E501
        :type id: str
        :param descriptor: The descriptor of this Location.  # noqa: E501
        :type descriptor: Descriptor
        :param gps: The gps of this Location.  # noqa: E501
        :type gps: Gps
        :param address: The address of this Location.  # noqa: E501
        :type address: Address
        :param station_code: The station_code of this Location.  # noqa: E501
        :type station_code: str
        :param city: The city of this Location.  # noqa: E501
        :type city: City
        :param country: The country of this Location.  # noqa: E501
        :type country: Country
        :param circle: The circle of this Location.  # noqa: E501
        :type circle: Circle
        :param polygon: The polygon of this Location.  # noqa: E501
        :type polygon: str
        :param _3dspace: The _3dspace of this Location.  # noqa: E501
        :type _3dspace: str
        :param time: The time of this Location.  # noqa: E501
        :type time: Time
        """
        self.swagger_types = {
            'id': str,
            'descriptor': Descriptor,
            'gps': Gps,
            'address': Address,
            'station_code': str,
            'city': City,
            'country': Country,
            'circle': Circle,
            'polygon': str,
            '_3dspace': str,
            'time': Time
        }

        self.attribute_map = {
            'id': 'id',
            'descriptor': 'descriptor',
            'gps': 'gps',
            'address': 'address',
            'station_code': 'station_code',
            'city': 'city',
            'country': 'country',
            'circle': 'circle',
            'polygon': 'polygon',
            '_3dspace': '3dspace',
            'time': 'time'
        }
        self._id = id
        self._descriptor = descriptor
        self._gps = gps
        self._address = address
        self._station_code = station_code
        self._city = city
        self._country = country
        self._circle = circle
        self._polygon = polygon
        self.__3dspace = _3dspace
        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'Location':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Location of this Location.  # noqa: E501
        :rtype: Location
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this Location.


        :return: The id of this Location.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Location.


        :param id: The id of this Location.
        :type id: str
        """

        self._id = id

    @property
    def descriptor(self) -> Descriptor:
        """Gets the descriptor of this Location.


        :return: The descriptor of this Location.
        :rtype: Descriptor
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor: Descriptor):
        """Sets the descriptor of this Location.


        :param descriptor: The descriptor of this Location.
        :type descriptor: Descriptor
        """

        self._descriptor = descriptor

    @property
    def gps(self) -> Gps:
        """Gets the gps of this Location.


        :return: The gps of this Location.
        :rtype: Gps
        """
        return self._gps

    @gps.setter
    def gps(self, gps: Gps):
        """Sets the gps of this Location.


        :param gps: The gps of this Location.
        :type gps: Gps
        """

        self._gps = gps

    @property
    def address(self) -> Address:
        """Gets the address of this Location.


        :return: The address of this Location.
        :rtype: Address
        """
        return self._address

    @address.setter
    def address(self, address: Address):
        """Sets the address of this Location.


        :param address: The address of this Location.
        :type address: Address
        """

        self._address = address

    @property
    def station_code(self) -> str:
        """Gets the station_code of this Location.


        :return: The station_code of this Location.
        :rtype: str
        """
        return self._station_code

    @station_code.setter
    def station_code(self, station_code: str):
        """Sets the station_code of this Location.


        :param station_code: The station_code of this Location.
        :type station_code: str
        """

        self._station_code = station_code

    @property
    def city(self) -> City:
        """Gets the city of this Location.


        :return: The city of this Location.
        :rtype: City
        """
        return self._city

    @city.setter
    def city(self, city: City):
        """Sets the city of this Location.


        :param city: The city of this Location.
        :type city: City
        """

        self._city = city

    @property
    def country(self) -> Country:
        """Gets the country of this Location.


        :return: The country of this Location.
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country: Country):
        """Sets the country of this Location.


        :param country: The country of this Location.
        :type country: Country
        """

        self._country = country

    @property
    def circle(self) -> Circle:
        """Gets the circle of this Location.


        :return: The circle of this Location.
        :rtype: Circle
        """
        return self._circle

    @circle.setter
    def circle(self, circle: Circle):
        """Sets the circle of this Location.


        :param circle: The circle of this Location.
        :type circle: Circle
        """

        self._circle = circle

    @property
    def polygon(self) -> str:
        """Gets the polygon of this Location.


        :return: The polygon of this Location.
        :rtype: str
        """
        return self._polygon

    @polygon.setter
    def polygon(self, polygon: str):
        """Sets the polygon of this Location.


        :param polygon: The polygon of this Location.
        :type polygon: str
        """

        self._polygon = polygon

    @property
    def _3dspace(self) -> str:
        """Gets the _3dspace of this Location.


        :return: The _3dspace of this Location.
        :rtype: str
        """
        return self.__3dspace

    @_3dspace.setter
    def _3dspace(self, _3dspace: str):
        """Sets the _3dspace of this Location.


        :param _3dspace: The _3dspace of this Location.
        :type _3dspace: str
        """

        self.__3dspace = _3dspace

    @property
    def time(self) -> Time:
        """Gets the time of this Location.


        :return: The time of this Location.
        :rtype: Time
        """
        return self._time

    @time.setter
    def time(self, time: Time):
        """Sets the time of this Location.


        :param time: The time of this Location.
        :type time: Time
        """

        self._time = time
