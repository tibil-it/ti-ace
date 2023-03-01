# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import List, Dict  # noqa: F401

from models import util
from models.base_model_ import Model
from models.feedback_form import FeedbackForm  # noqa: F401,E501
from models import \
    FeedbackUrlpropertiesparamspropertiesfeedbackId  # noqa: F401,E501


class Rating(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, rating_category: str=None, id: str=None, value: float=None, feedback_form: FeedbackForm=None, feedback_id: FeedbackUrlpropertiesparamspropertiesfeedbackId=None):  # noqa: E501
        """Rating - a model defined in Swagger

        :param rating_category: The rating_category of this Rating.  # noqa: E501
        :type rating_category: str
        :param id: The id of this Rating.  # noqa: E501
        :type id: str
        :param value: The value of this Rating.  # noqa: E501
        :type value: float
        :param feedback_form: The feedback_form of this Rating.  # noqa: E501
        :type feedback_form: FeedbackForm
        :param feedback_id: The feedback_id of this Rating.  # noqa: E501
        :type feedback_id: FeedbackUrlpropertiesparamspropertiesfeedbackId
        """
        self.swagger_types = {
            'rating_category': str,
            'id': str,
            'value': float,
            'feedback_form': FeedbackForm,
            'feedback_id': FeedbackUrlpropertiesparamspropertiesfeedbackId
        }

        self.attribute_map = {
            'rating_category': 'rating_category',
            'id': 'id',
            'value': 'value',
            'feedback_form': 'feedback_form',
            'feedback_id': 'feedback_id'
        }
        self._rating_category = rating_category
        self._id = id
        self._value = value
        self._feedback_form = feedback_form
        self._feedback_id = feedback_id

    @classmethod
    def from_dict(cls, dikt) -> 'Rating':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Rating of this Rating.  # noqa: E501
        :rtype: Rating
        """
        return util.deserialize_model(dikt, cls)

    @property
    def rating_category(self) -> str:
        """Gets the rating_category of this Rating.

        Category of the object being rated  # noqa: E501

        :return: The rating_category of this Rating.
        :rtype: str
        """
        return self._rating_category

    @rating_category.setter
    def rating_category(self, rating_category: str):
        """Sets the rating_category of this Rating.

        Category of the object being rated  # noqa: E501

        :param rating_category: The rating_category of this Rating.
        :type rating_category: str
        """

        self._rating_category = rating_category

    @property
    def id(self) -> str:
        """Gets the id of this Rating.

        Id of the object being rated  # noqa: E501

        :return: The id of this Rating.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this Rating.

        Id of the object being rated  # noqa: E501

        :param id: The id of this Rating.
        :type id: str
        """

        self._id = id

    @property
    def value(self) -> float:
        """Gets the value of this Rating.

        Rating value given to the object  # noqa: E501

        :return: The value of this Rating.
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value: float):
        """Sets the value of this Rating.

        Rating value given to the object  # noqa: E501

        :param value: The value of this Rating.
        :type value: float
        """

        self._value = value

    @property
    def feedback_form(self) -> FeedbackForm:
        """Gets the feedback_form of this Rating.


        :return: The feedback_form of this Rating.
        :rtype: FeedbackForm
        """
        return self._feedback_form

    @feedback_form.setter
    def feedback_form(self, feedback_form: FeedbackForm):
        """Sets the feedback_form of this Rating.


        :param feedback_form: The feedback_form of this Rating.
        :type feedback_form: FeedbackForm
        """

        self._feedback_form = feedback_form

    @property
    def feedback_id(self) -> FeedbackUrlpropertiesparamspropertiesfeedbackId:
        """Gets the feedback_id of this Rating.


        :return: The feedback_id of this Rating.
        :rtype: FeedbackUrlpropertiesparamspropertiesfeedbackId
        """
        return self._feedback_id

    @feedback_id.setter
    def feedback_id(self, feedback_id: FeedbackUrlpropertiesparamspropertiesfeedbackId):
        """Sets the feedback_id of this Rating.


        :param feedback_id: The feedback_id of this Rating.
        :type feedback_id: FeedbackUrlpropertiesparamspropertiesfeedbackId
        """

        self._feedback_id = feedback_id
