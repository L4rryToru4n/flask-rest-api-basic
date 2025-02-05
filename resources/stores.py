import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schemas import StoreSchema
from uuid import uuid4
from db import stores, items

blp = Blueprint("stores", __name__, description="Operation on stores")


@blp.route("/store/<string:store_id>")
class Store(MethodView):
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found.")
            
    @blp.arguments(StoreSchema)
    def put(self, store_data, store_id):
        
        stores[store_id] = {"id": store_id, **store_data} 
        
        return stores[store_id], 200
    
    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted"}, 200
        except KeyError:
            abort(404, message="Store not found")
            

@blp.route("/store")
class StoreList(MethodView):
    def get(self):
        return {"stores": list(stores.values())}
    
    @blp.arguments(StoreSchema)
    def post(self, store_data):
    
        if "name" not in store_data:
            abort(400, message="Bad request. Ensure that 'name' is included in JSON payload.")
        
        for store in stores.values():
            if (
                store_data["name"] == store["name"]
                and store_data["store_id"] == store["store_id"]
            ):
                abort(400, message="Store already exists.")
            
            
        store_id = uuid4().hex
        
        new_store = {"id": store_id, **store_data}
        stores[store_id] = new_store
        items[store_id] = []
        
        return stores[store_id], 201