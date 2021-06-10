from typing import List

from bson import ObjectId
from multipledispatch import dispatch

from app import db


class BaseDao:
    def __init__(self, collection_name):
        self.__db = db
        self.collection_name = collection_name

    @dispatch(list, ordered=bool)
    def insert(self, item_lst: List[dict], ordered: bool=True) -> List[str]:
        inserted_lst = self.__db[self.collection_name].insert_many(item_lst, ordered)
        return [str(inserted_id) for inserted_id in inserted_lst.inserted_ids]

    @dispatch(dict)
    def insert(self, item: dict) -> str:
        inserted = self.__db[self.collection_name].insert_one(item)
        return str(inserted.inserted_id)
    
    def find_list_by_filter(self, filter: dict={}, projection=None, sort=None, skip: int=0, limit: int=0)-> List[dict]:
        if "_id" in filter:
            filter["_id"] = ObjectId(filter["_id"])

        found = self.__db[self.collection_name].find(filter=filter, projection=projection, skip=skip, limit=limit, sort=sort)
        
        found = list(found)
        
        for i in range(len(found)):
            if "_id" in found[i]:
                found[i]["_id"] = str(found[i]["_id"])

        return found

    def find_one_by_id(self, id:str)-> object:
        found = self.__db[self.collection_name].find_one({"_id": ObjectId(id)})
        
        if found:
            found["_id"] = str(found["_id"])
    
        return found

    def update_one_by_id(self, id:str, element:dict)-> bool:
        criteria = {"_id": ObjectId(id)}
        set_obj = {"$set": element}
        updated = self.__db[self.collection_name].update_one(criteria, set_obj)
        return updated.matched_count == 1
            
    def delete_one_by_id(self, id)-> bool:
        deleted = self.__db[self.collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count)