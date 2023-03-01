import json

from flask import request
from flask_restful import Resource

from models.ack import Ack
from models.error import Error
from models.inline_response200 import InlineResponse200
from models.inline_response200_message import InlineResponse200Message
from service.confirm import confirm
from service.init import init
from service.select import select
from service.search import search


class InternalHandler(Resource):

    def post(self, action):
        print("Inside controller")
        input_json = request.get_json()
        if action == "search":

            return search(input_json,)
        elif action == "select":
            return select(input_json)
        elif action == "init":
            return init(input_json)
        elif action == "confirm":
            return confirm(input_json)
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

        ack = InlineResponse200(
            message=InlineResponse200Message(
                ack=Ack(
                    status="ACK"
                )
            )
        )
        return ack.to_dict()
