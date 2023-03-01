import json

import requests
from flask import request
from flask_restful import Resource

from resources import sample_bpp_data
from resources.constants import BAP_URI
from resources.sample_bpp_data import items_on_category


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
        category_id = input["message"]["intent"]["item"]["descriptor"]["name"]
        items = items_on_category.get(category_id, [])
        if not items:
            sample_bpp_data.on_search["message"]["catalog"]["providers"][0]["categories"] = []
        else:
            sample_bpp_data.on_search["message"]["catalog"]["providers"][0]["categories"][0]["id"] = category_id
            sample_bpp_data.on_search["message"]["catalog"]["providers"][0]["categories"][0]["parent_category_id"] = category_id
        sample_bpp_data.on_search["message"]["catalog"]["providers"][0]["items"] = items
        #return requests.post(url=BAP_URI + "/bap/on_search", json=sample_bpp_data.on_search)
        return sample_bpp_data.on_search
        # return "ok"

    def on_select(self, input):

        print("inside on_select")
        sample_bpp_data.on_select["context"] = input["context"]
        sample_bpp_data.on_select["context"]["action"] = "on_select"

        req_items = input["message"]["order"]["provider"]["items"]
        selected_items = self.get_selected_items(req_items)
        sample_bpp_data.on_select["message"]["order"]["provider"]["items"] = selected_items
        sample_bpp_data.on_select["message"]["order"]["provider"]["category_id"] = req_items[0]["category_id"]
        #requests.post(url=BAP_URI + "/bap/on_select", json=sample_bpp_data.on_select)
        return sample_bpp_data.on_select
        #return "ok"
    
    def on_init(self, input):

        print("inside on_init")
        sample_bpp_data.on_init["context"] = input["context"]
        sample_bpp_data.on_init["context"]["action"] = "on_init"

        req_items = input["message"]["order"]["provider"]["items"]
        selected_items = self.get_selected_items(req_items)
        sample_bpp_data.on_init["message"]["order"]["provider"]["items"] = selected_items
        sample_bpp_data.on_init["message"]["order"]["provider"]["category_id"] = req_items[0]["category_id"]

        # requests.post(url=BAP_URI + "/bap/on_init", json=sample_bpp_data.on_init)
        # return "ok"
        return sample_bpp_data.on_init

    def on_confirm(self, input):

        print("inside on_confirm")
        sample_bpp_data.on_confirm["context"] = input["context"]
        sample_bpp_data.on_confirm["context"]["action"] = "on_confirm"

        req_items = input["message"]["order"]["provider"]["items"]
        selected_items = self.get_selected_items(req_items)
        sample_bpp_data.on_confirm["message"]["order"]["provider"]["items"] = selected_items
        sample_bpp_data.on_confirm["message"]["order"]["provider"]["category_id"] = req_items[0]["category_id"]

        # requests.post(url=BAP_URI + "/bap/on_confirm", json=sample_bpp_data.on_confirm)
        # return "ok"
        return sample_bpp_data.on_confirm

    def get_selected_items(self, req_items):
        selected_items = []
        for item in req_items:
            category = item["category_id"]
            item_id = item["id"]

            avail_items = items_on_category.get(category, [])
            for itm in avail_items:
                if itm["id"] == item_id:
                    selected_items.append(itm)
        return selected_items
