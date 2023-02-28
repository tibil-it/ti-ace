import json

import requests

from models.order import Order
from models.select_message import SelectMessage
from resources.constants import BPP_URI
from resources.utils import create_context
from worker import celery


@celery.task()
def confirm(request_data):
    print(request_data)
    transaction_id = request_data["transaction_id"]
    context = create_context("init", transaction_id)

    order = Order.from_dict(request_data)
    message = SelectMessage(order=order)

    select_request_body = {"context": context.to_dict(), "message": message.to_dict()}
    print("Confirm request is ----")
    print(select_request_body)

    req_body = json.dumps(select_request_body, separators=(',', ':'))
    requests.post(url=BPP_URI + "/bpp/confirm", json=json.loads(req_body))
    return "Ok"

