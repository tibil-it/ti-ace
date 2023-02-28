import datetime
import uuid

from models.context import Context
from resources.constants import BAP_URI, BAP_ID, DOMAIN


def create_context(action, transaction_id):
    context = Context(
        domain=DOMAIN,
        core_version="1.0.0",
        city="BLR",
        country="IND",
        message_id=str(uuid.uuid4()),
        action=action,
        bap_uri=BAP_URI,
        bap_id=BAP_ID,
        transaction_id=transaction_id,
        timestamp=str(datetime.datetime.now())
    )
    return context
