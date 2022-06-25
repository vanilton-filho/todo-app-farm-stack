import { List } from "@mui/material";
import TodoItem from "./TodoItem";

const TodoList = (props) => {
  const removeTodo = (id) => {
    props.onRemoveTodoList(id);
  };

  return (
    <List>
      {props.todos.map((todo) => (
        <TodoItem key={todo.id} todo={todo} onRemoveTodo={removeTodo} />
      ))}
    </List>
  );
};

export default TodoList;
