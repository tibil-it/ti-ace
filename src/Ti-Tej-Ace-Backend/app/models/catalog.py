# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.category import Category  # noqa: F401,E501
from models.descriptor import Descriptor  # noqa: F401,E501
from models.fulfillment import Fulfillment  # noqa: F401,E501
from models.offer import Offer  # noqa: F401,E501
from models.payment import Payment  # noqa: F401,E501
from models.provider import Provider  # noqa: F401,E501


class Catalog(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, descriptor: Descriptor=None, categories: List[Category]=None, fulfillments: List[Fulfillment]=None, payments: List[Payment]=None, offers: List[Offer]=None, providers: List[Provider]=None, exp: datetime=None):  # noqa: E501
        """Catalog - a model defined in Swagger

        :param descriptor: The descriptor of this Catalog.  # noqa: E501
        :type descriptor: Descriptor
        :param categories: The categories of this Catalog.  # noqa: E501
        :type categories: List[Category]
        :param fulfillments: The fulfillments of this Catalog.  # noqa: E501
        :type fulfillments: List[Fulfillment]
        :param payments: The payments of this Catalog.  # noqa: E501
        :type payments: List[Payment]
        :param offers: The offers of this Catalog.  # noqa: E501
        :type offers: List[Offer]
        :param providers: The providers of this Catalog.  # noqa: E501
        :type providers: List[Provider]
        :param exp: The exp of this Catalog.  # noqa: E501
        :type exp: datetime
        """
        self.swagger_types = {
            'descriptor': Descriptor,
            'categories': List[Category],
            'fulfillments': List[Fulfillment],
            'payments': List[Payment],
            'offers': List[Offer],
            'providers': List[Provider],
            'exp': datetime
        }

        self.attribute_map = {
            'descriptor': 'descriptor',
            'categories': 'categories',
            'fulfillments': 'fulfillments',
            'payments': 'payments',
            'offers': 'offers',
            'providers': 'providers',
            'exp': 'exp'
        }
        self._descriptor = descriptor
        self._categories = categories
        self._fulfillments = fulfillments
        self._payments = payments
        self._offers = offers
        self._providers = providers
        self._exp = exp

    @classmethod
    def from_dict(cls, dikt) -> 'Catalog':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Catalog of this Catalog.  # noqa: E501
        :rtype: Catalog
        """
        return util.deserialize_model(dikt, cls)

    @property
    def descriptor(self) -> Descriptor:
        """Gets the descriptor of this Catalog.


        :return: The descriptor of this Catalog.
        :rtype: Descriptor
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor: Descriptor):
        """Sets the descriptor of this Catalog.


        :param descriptor: The descriptor of this Catalog.
        :type descriptor: Descriptor
        """

        self._descriptor = descriptor

    @property
    def categories(self) -> List[Category]:
        """Gets the categories of this Catalog.


        :return: The categories of this Catalog.
        :rtype: List[Category]
        """
        return self._categories

    @categories.setter
    def categories(self, categories: List[Category]):
        """Sets the categories of this Catalog.


        :param categories: The categories of this Catalog.
        :type categories: List[Category]
        """

        self._categories = categories

    @property
    def fulfillments(self) -> List[Fulfillment]:
        """Gets the fulfillments of this Catalog.


        :return: The fulfillments of this Catalog.
        :rtype: List[Fulfillment]
        """
        return self._fulfillments

    @fulfillments.setter
    def fulfillments(self, fulfillments: List[Fulfillment]):
        """Sets the fulfillments of this Catalog.


        :param fulfillments: The fulfillments of this Catalog.
        :type fulfillments: List[Fulfillment]
        """

        self._fulfillments = fulfillments

    @property
    def payments(self) -> List[Payment]:
        """Gets the payments of this Catalog.


        :return: The payments of this Catalog.
        :rtype: List[Payment]
        """
        return self._payments

    @payments.setter
    def payments(self, payments: List[Payment]):
        """Sets the payments of this Catalog.


        :param payments: The payments of this Catalog.
        :type payments: List[Payment]
        """

        self._payments = payments

    @property
    def offers(self) -> List[Offer]:
        """Gets the offers of this Catalog.


        :return: The offers of this Catalog.
        :rtype: List[Offer]
        """
        return self._offers

    @offers.setter
    def offers(self, offers: List[Offer]):
        """Sets the offers of this Catalog.


        :param offers: The offers of this Catalog.
        :type offers: List[Offer]
        """

        self._offers = offers

    @property
    def providers(self) -> List[Provider]:
        """Gets the providers of this Catalog.


        :return: The providers of this Catalog.
        :rtype: List[Provider]
        """
        return self._providers

    @providers.setter
    def providers(self, providers: List[Provider]):
        """Sets the providers of this Catalog.


        :param providers: The providers of this Catalog.
        :type providers: List[Provider]
        """

        self._providers = providers

    @property
    def exp(self) -> datetime:
        """Gets the exp of this Catalog.

        Time after which catalog has to be refreshed  # noqa: E501

        :return: The exp of this Catalog.
        :rtype: datetime
        """
        return self._exp

    @exp.setter
    def exp(self, exp: datetime):
        """Sets the exp of this Catalog.

        Time after which catalog has to be refreshed  # noqa: E501

        :param exp: The exp of this Catalog.
        :type exp: datetime
        """

        self._exp = exp
