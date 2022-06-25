def todo_serializer(todo):
    return {
        "id": str(todo["_id"]),
        "title": todo["title"],
        "description": todo["description"],
        "is_done": todo["is_done"]
    }
    
def todo_list_serializer(todos):
    todo_list = []
    for todo in todos:
        todo_list.append(todo_serializer(todo))
    return todo_list


