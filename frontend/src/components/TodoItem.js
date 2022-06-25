import {
  Checkbox,
  IconButton,
  ListItem,
  ListItemText,
  Typography,
} from "@mui/material";
import { green } from "@mui/material/colors";
import DeleteIcon from "@mui/icons-material/Delete";
import { useEffect, useState } from "react";

const TodoItem = (props) => {
  const [todoDone, setTodoDone] = useState(false);
  const [trashColor, setTrashColor] = useState("default");

  useEffect(() => {
    setTodoDone(props.todo["is_done"]);
  }, [props.todo]);

  return (
    <ListItem
      secondaryAction={
        <IconButton
          edge="end"
          aria-label="delete"
          color={trashColor}
          onMouseOver={
            () => setTrashColor("error")
          }
          onMouseOut={
            () => setTrashColor("default")
          }
          onClick={() => {
            fetch(`http://localhost:8000/api/v1/todo/${props.todo.id}`, {
              method: "DELETE",
            })
              .then((_) => props.onRemoveTodo(props.todo.id))
              .catch((err) => console.log(err));
          }}
        >
          <DeleteIcon />
        </IconButton>
      }
    >
      <ListItemText>
        <Typography
          style={{ textDecorationLine: todoDone ? "line-through" : "none" }}
        >
          <Checkbox
            checked={todoDone}
            onClick={() => {
              fetch(`http://localhost:8000/api/v1/todo/${props.todo.id}/done`, {
                method: "PUT",
              })
                .then((_) => setTodoDone(!todoDone))
                .catch((err) => console.log(err));
            }}
            sx={{
              "&.Mui-checked": {
                color: green[600],
              },
            }}
          />
          <b>{props.todo.title}</b>: {props.todo.description}
        </Typography>
      </ListItemText>
    </ListItem>
  );
};

export default TodoItem;
