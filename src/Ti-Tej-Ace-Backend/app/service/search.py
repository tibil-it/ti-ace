import json
import uuid

import requests

from models.descriptor import Descriptor
from models.intent import Intent
from models.item import Item
from models.search_message import SearchMessage
from resources.constants import BPP_URI
from resources.utils import create_context
from worker import celery


@celery.task()
def search(request_data):
    print(request_data)
    transaction_id = str(uuid.uuid4())
    context = create_context("search", transaction_id)

    career_path = request_data.get("intent", {}).get("item", {}).get("descriptor", {}).get("name", None)
    print(career_path)
    descriptor = Descriptor(name=career_path)
    intent = Intent(
        item=Item(descriptor=descriptor)
    )
    print(intent.to_dict())
    message = SearchMessage(intent=intent)
    search_request_body = {"context": context.to_dict(), "message": message.to_dict()}
    print("Search request is ----")
    print(search_request_body)

    req_body = json.dumps(search_request_body, separators=(',', ':'))
    response = requests.post(url=BPP_URI + "/bpp/search", json=json.loads(req_body))
    return response.json()
