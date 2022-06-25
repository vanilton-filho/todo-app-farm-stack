from backend.core.database.database_config import todo_collection
from bson.objectid import ObjectId

async def fetch_by_id(id):
    return await todo_collection.find_one({"_id": ObjectId(id)})
    

async def fetch_all():
    todos = []
    cursor = todo_collection.find({})
    async for document in cursor:
        todos.append({**document})
    return todos

async def create(todo):
    document = todo
    document_created = await todo_collection.insert_one(document)
    return {"id": str(document_created.inserted_id), **document}

async def update(id, todo):
    _ = await todo_collection.update_one({"_id": ObjectId(id)}, {"$set": {
        "title": todo["title"],
        "description": todo["description"]
    }})
    return await fetch_by_id(id)

async def update_status(id):
    document = await fetch_by_id(id)
    if document is not None:
        document_updated = await todo_collection.update_one({"_id": ObjectId(id)}, {"$set": {
            "is_done": not document["is_done"]
        }})
        return document_updated.acknowledged
    return False

async def remove(id):
    document = await fetch_by_id(id)
    if document is not None:
        document_removed = await todo_collection.delete_one({"_id": ObjectId(id)})
        return document_removed.acknowledged
    return False