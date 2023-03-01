import json

import requests
from flask import request
from flask_restful import Resource

from models.ack import Ack
from models.error import Error
from models.inline_response200 import InlineResponse200
from models.inline_response200_message import InlineResponse200Message
from resources.constants import FONTEND_URL


class BppHandler(Resource):

    def post(self, action):
        print("Inside Handler")
        input_json = request.get_json()
        print("Data for Front end")
        print(input_json)
        if action == "on_search":
            return requests.post(url=FONTEND_URL + "/on_search", json=input_json)
        elif action == "select":
            return requests.post(url=FONTEND_URL + "/on_select", json=input_json)
        elif action == "init":
            return requests.post(url=FONTEND_URL + "/on_init", json=input_json)
        elif action == "confirm":
            return requests.post(url=FONTEND_URL + "/on_confirm", json=input_json)
        else:
            ack = InlineResponse200(
                message=InlineResponse200Message(
                    ack=Ack(
                        status="NACK"
                    )
                ),
                error=Error(
                    type="DOMAIN-ERROR",
                    message="Not implemented"
                )
            )
            return ack.to_dict()
