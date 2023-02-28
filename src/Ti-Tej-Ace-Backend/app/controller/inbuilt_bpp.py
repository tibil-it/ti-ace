import json

import requests
from flask import request
from flask_restful import Resource

from resources import sample_bpp_data
from resources.constants import BAP_URI


class BppProvider(Resource):

    def post(self, action):

        print("Inside BPP controller")
        print(request.data)
        input_json = request.get_json()
        if action == "search":
            return self.on_search(input_json)
        elif action == "select":
            return self.on_select(input_json)
        elif action == "init":
            return self.on_init(input_json)
        elif action == "confirm":
            return self.on_confirm(input_json)
        else:
            return "Method not implemented", 501

    def on_search(self, input):

        print("inside on_search")
        sample_bpp_data.on_search["context"] = input["context"]
        sample_bpp_data.on_search["context"]["action"] = "on_search"
        requests.post(url=BAP_URI + "/bap/on_search", json=sample_bpp_data.on_search)
        return "ok"

    def on_select(self, input):

        print("inside on_select")
        sample_bpp_data.on_select["context"] = input["context"]
        sample_bpp_data.on_select["context"]["action"] = "on_select"
        requests.post(url=BAP_URI + "/bap/on_select", json=sample_bpp_data.on_select)
        return "ok"
    
    def on_init(self, input):

        print("inside on_init")
        sample_bpp_data.on_init["context"] = input["context"]
        sample_bpp_data.on_init["context"]["action"] = "on_init"
        requests.post(url=BAP_URI + "/bap/on_init", json=sample_bpp_data.on_init)
        return "ok"

    def on_confirm(self, input):

        print("inside on_confirm")
        sample_bpp_data.on_confirm["context"] = input["context"]
        sample_bpp_data.on_confirm["context"]["action"] = "on_confirm"
        requests.post(url=BAP_URI + "/bap/on_confirm", json=sample_bpp_data.on_confirm)
        return "ok"
