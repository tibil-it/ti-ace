# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.billing import Billing  # noqa: F401,E501
from models.fulfillment import Fulfillment  # noqa: F401,E501
from models.on_init_message_order_add_ons import OnInitMessageOrderAddOns  # noqa: F401,E501
from models.on_init_message_order_items import OnInitMessageOrderItems  # noqa: F401,E501
from models.on_init_message_order_offers import OnInitMessageOrderOffers  # noqa: F401,E501
from models.on_init_message_order_provider import OnInitMessageOrderProvider  # noqa: F401,E501
from models.on_init_message_order_provider_location import \
    OnInitMessageOrderProviderLocation  # noqa: F401,E501
from models.payment import Payment  # noqa: F401,E501
from models.quotation import Quotation  # noqa: F401,E501


class OnInitMessageOrder(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, provider: OnInitMessageOrderProvider=None, provider_location: OnInitMessageOrderProviderLocation=None, items: List[OnInitMessageOrderItems]=None, add_ons: List[OnInitMessageOrderAddOns]=None, offers: List[OnInitMessageOrderOffers]=None, billing: Billing=None, fulfillment: Fulfillment=None, quote: Quotation=None, payment: Payment=None):  # noqa: E501
        """OnInitMessageOrder - a model defined in Swagger

        :param provider: The provider of this OnInitMessageOrder.  # noqa: E501
        :type provider: OnInitMessageOrderProvider
        :param provider_location: The provider_location of this OnInitMessageOrder.  # noqa: E501
        :type provider_location: OnInitMessageOrderProviderLocation
        :param items: The items of this OnInitMessageOrder.  # noqa: E501
        :type items: List[OnInitMessageOrderItems]
        :param add_ons: The add_ons of this OnInitMessageOrder.  # noqa: E501
        :type add_ons: List[OnInitMessageOrderAddOns]
        :param offers: The offers of this OnInitMessageOrder.  # noqa: E501
        :type offers: List[OnInitMessageOrderOffers]
        :param billing: The billing of this OnInitMessageOrder.  # noqa: E501
        :type billing: Billing
        :param fulfillment: The fulfillment of this OnInitMessageOrder.  # noqa: E501
        :type fulfillment: Fulfillment
        :param quote: The quote of this OnInitMessageOrder.  # noqa: E501
        :type quote: Quotation
        :param payment: The payment of this OnInitMessageOrder.  # noqa: E501
        :type payment: Payment
        """
        self.swagger_types = {
            'provider': OnInitMessageOrderProvider,
            'provider_location': OnInitMessageOrderProviderLocation,
            'items': List[OnInitMessageOrderItems],
            'add_ons': List[OnInitMessageOrderAddOns],
            'offers': List[OnInitMessageOrderOffers],
            'billing': Billing,
            'fulfillment': Fulfillment,
            'quote': Quotation,
            'payment': Payment
        }

        self.attribute_map = {
            'provider': 'provider',
            'provider_location': 'provider_location',
            'items': 'items',
            'add_ons': 'add_ons',
            'offers': 'offers',
            'billing': 'billing',
            'fulfillment': 'fulfillment',
            'quote': 'quote',
            'payment': 'payment'
        }
        self._provider = provider
        self._provider_location = provider_location
        self._items = items
        self._add_ons = add_ons
        self._offers = offers
        self._billing = billing
        self._fulfillment = fulfillment
        self._quote = quote
        self._payment = payment

    @classmethod
    def from_dict(cls, dikt) -> 'OnInitMessageOrder':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The on_init_message_order of this OnInitMessageOrder.  # noqa: E501
        :rtype: OnInitMessageOrder
        """
        return util.deserialize_model(dikt, cls)

    @property
    def provider(self) -> OnInitMessageOrderProvider:
        """Gets the provider of this OnInitMessageOrder.


        :return: The provider of this OnInitMessageOrder.
        :rtype: OnInitMessageOrderProvider
        """
        return self._provider

    @provider.setter
    def provider(self, provider: OnInitMessageOrderProvider):
        """Sets the provider of this OnInitMessageOrder.


        :param provider: The provider of this OnInitMessageOrder.
        :type provider: OnInitMessageOrderProvider
        """

        self._provider = provider

    @property
    def provider_location(self) -> OnInitMessageOrderProviderLocation:
        """Gets the provider_location of this OnInitMessageOrder.


        :return: The provider_location of this OnInitMessageOrder.
        :rtype: OnInitMessageOrderProviderLocation
        """
        return self._provider_location

    @provider_location.setter
    def provider_location(self, provider_location: OnInitMessageOrderProviderLocation):
        """Sets the provider_location of this OnInitMessageOrder.


        :param provider_location: The provider_location of this OnInitMessageOrder.
        :type provider_location: OnInitMessageOrderProviderLocation
        """

        self._provider_location = provider_location

    @property
    def items(self) -> List[OnInitMessageOrderItems]:
        """Gets the items of this OnInitMessageOrder.


        :return: The items of this OnInitMessageOrder.
        :rtype: List[OnInitMessageOrderItems]
        """
        return self._items

    @items.setter
    def items(self, items: List[OnInitMessageOrderItems]):
        """Sets the items of this OnInitMessageOrder.


        :param items: The items of this OnInitMessageOrder.
        :type items: List[OnInitMessageOrderItems]
        """

        self._items = items

    @property
    def add_ons(self) -> List[OnInitMessageOrderAddOns]:
        """Gets the add_ons of this OnInitMessageOrder.


        :return: The add_ons of this OnInitMessageOrder.
        :rtype: List[OnInitMessageOrderAddOns]
        """
        return self._add_ons

    @add_ons.setter
    def add_ons(self, add_ons: List[OnInitMessageOrderAddOns]):
        """Sets the add_ons of this OnInitMessageOrder.


        :param add_ons: The add_ons of this OnInitMessageOrder.
        :type add_ons: List[OnInitMessageOrderAddOns]
        """

        self._add_ons = add_ons

    @property
    def offers(self) -> List[OnInitMessageOrderOffers]:
        """Gets the offers of this OnInitMessageOrder.


        :return: The offers of this OnInitMessageOrder.
        :rtype: List[OnInitMessageOrderOffers]
        """
        return self._offers

    @offers.setter
    def offers(self, offers: List[OnInitMessageOrderOffers]):
        """Sets the offers of this OnInitMessageOrder.


        :param offers: The offers of this OnInitMessageOrder.
        :type offers: List[OnInitMessageOrderOffers]
        """

        self._offers = offers

    @property
    def billing(self) -> Billing:
        """Gets the billing of this OnInitMessageOrder.


        :return: The billing of this OnInitMessageOrder.
        :rtype: Billing
        """
        return self._billing

    @billing.setter
    def billing(self, billing: Billing):
        """Sets the billing of this OnInitMessageOrder.


        :param billing: The billing of this OnInitMessageOrder.
        :type billing: Billing
        """

        self._billing = billing

    @property
    def fulfillment(self) -> Fulfillment:
        """Gets the fulfillment of this OnInitMessageOrder.


        :return: The fulfillment of this OnInitMessageOrder.
        :rtype: Fulfillment
        """
        return self._fulfillment

    @fulfillment.setter
    def fulfillment(self, fulfillment: Fulfillment):
        """Sets the fulfillment of this OnInitMessageOrder.


        :param fulfillment: The fulfillment of this OnInitMessageOrder.
        :type fulfillment: Fulfillment
        """

        self._fulfillment = fulfillment

    @property
    def quote(self) -> Quotation:
        """Gets the quote of this OnInitMessageOrder.


        :return: The quote of this OnInitMessageOrder.
        :rtype: Quotation
        """
        return self._quote

    @quote.setter
    def quote(self, quote: Quotation):
        """Sets the quote of this OnInitMessageOrder.


        :param quote: The quote of this OnInitMessageOrder.
        :type quote: Quotation
        """

        self._quote = quote

    @property
    def payment(self) -> Payment:
        """Gets the payment of this OnInitMessageOrder.


        :return: The payment of this OnInitMessageOrder.
        :rtype: Payment
        """
        return self._payment

    @payment.setter
    def payment(self, payment: Payment):
        """Sets the payment of this OnInitMessageOrder.


        :param payment: The payment of this OnInitMessageOrder.
        :type payment: Payment
        """

        self._payment = payment