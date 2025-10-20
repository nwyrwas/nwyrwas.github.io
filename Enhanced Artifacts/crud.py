from __future__ import annotations

import os
from typing import Any, Dict, Iterable, List, Optional

from pymongo import MongoClient
from pymongo.errors import PyMongoError
from dotenv import load_dotenv

load_dotenv()


class AnimalShelter:
    """
    Thin CRUD wrapper for the AAC.animals collection.

    ENV VARS:
      MONGODB_URI  required (Atlas connection string)
      MONGODB_DB   default: 'ACC'
      MONGODB_COL  default: 'animals'
    """

    def __init__(
        self,
        uri: Optional[str] = None,
        db_name: str | None = None,
        col_name: str | None = None,
    ) -> None:
        uri = uri or os.getenv("MONGODB_URI")
        if not uri:
            raise RuntimeError("Missing MONGODB_URI in environment or constructor.")
        self.client = MongoClient(uri)
        self.database = self.client[db_name or os.getenv("MONGODB_DB", "ACC")]
        self.collection = self.database[col_name or os.getenv("MONGODB_COL", "animals")]

    # Create
    def create(self, data: Dict[str, Any]) -> Optional[str]:
        try:
            if not isinstance(data, dict) or not data:
                raise ValueError("create() expects a non-empty dict")
            res = self.collection.insert_one(data)
            return str(res.inserted_id)
        except (ValueError, PyMongoError) as e:
            print("CRUD create error:", e)
            return None

    # Read (query dict)
    def read(self, query: Dict[str, Any] | None = None, projection: Dict[str, int] | None = None) -> List[Dict[str, Any]]:
        try:
            return list(self.collection.find(query or {}, projection))
        except PyMongoError as e:
            print("CRUD read error:", e)
            return []

    # Read all convenience
    def read_all(self) -> List[Dict[str, Any]]:
        return self.read({})

    # Update
    def update(self, query: Dict[str, Any], new_data: Dict[str, Any], multiple: bool = False) -> int:
        try:
            if not query or not new_data:
                raise ValueError("update() requires query and new_data")
            op = self.collection.update_many if multiple else self.collection.update_one
            res = op(query, {"$set": new_data})
            return res.modified_count
        except (ValueError, PyMongoError) as e:
            print("CRUD update error:", e)
            return 0

    # Delete
    def delete(self, query: Dict[str, Any], multiple: bool = False) -> int:
        try:
            if not query:
                raise ValueError("delete() requires query")
            op = self.collection.delete_many if multiple else self.collection.delete_one
            res = op(query)
            return res.deleted_count
        except (ValueError, PyMongoError) as e:
            print("CRUD delete error:", e)
            return 0

    # Count
    def count(self, query: Dict[str, Any] | None = None) -> int:
        try:
            return self.collection.count_documents(query or {})
        except PyMongoError as e:
            print("CRUD count error:", e)
            return 0
