import "./App.css";
import {
  Box,
  Button,
  Container,
  Grid,
  Paper,
  TextField,
  Typography,
} from "@mui/material";
import React, { useEffect, useState } from "react";
import TodoList from "./components/TodoList";

function App() {
  const [todoList, setTodoList] = useState([]);
  const [todoTitle, setTodoTitle] = useState("");
  const [todoDescription, setTodoDescription] = useState("");

  useEffect(() => {
    fetch("http://localhost:8000/api/v1/todo")
      .then((response) => response.json())
      .then((data) => setTodoList(data));
  }, []);

  const addTodoHandler = () => {
    fetch("http://localhost:8000/api/v1/todo", {
      method: "POST",
      body: JSON.stringify({ title: todoTitle, description: todoDescription }),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    })
      .then((response) => response.json())
      .then((todo) =>
        setTodoList((prevState) => {
          return [todo, ...prevState];
        })
      )
      .catch((err) => console.log(err));

    setTodoTitle("");
    setTodoDescription("");    
  };

  const removeTodoHandler = (id) => {
    const todoIndex = todoList.findIndex((todo) => todo.id === id);

    todoList.splice(todoIndex, 1);
    setTodoList(() => [...todoList]);
  };

  const todoTitleHandler = (event) => {
    setTodoTitle(event.target.value);
  };

  const todoDescriptionHandler = (event) => {
    setTodoDescription(event.target.value);
  };

  return (
    <div>
      <Container component="main" maxWidth="sm" sx={{ mb: 4 }}>
        <Paper
          variant="outlined"
          sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}
        >
          <Typography component="h1" variant="h4" align="center" sx={{ mb: 4 }}>
            TODO App
          </Typography>
          <Grid container spacing={3}>
            <Grid item xs={12} sm={6}>
              <TextField
                onChange={todoTitleHandler}
                id="title"
                name="title"
                label="Título"
                fullWidth
                variant="standard"
                value={todoTitle}
              />
            </Grid>
            <Grid item xs={12} sm={6}>
              <TextField
                onChange={todoDescriptionHandler}
                id="description"
                name="description"
                label="Descrição"
                fullWidth
                variant="standard"
                value={todoDescription}
              />
            </Grid>
          </Grid>
          <React.Fragment>
            <Box sx={{ display: "flex", justifyContent: "flex" }}>
              <Button
                variant="contained"
                onClick={addTodoHandler}
                sx={{ mt: 3, ml: 1 }}
              >
                Adicionar
              </Button>
            </Box>
          </React.Fragment>
          <React.Fragment>
            <TodoList todos={todoList} onRemoveTodoList={removeTodoHandler} />
          </React.Fragment>
        </Paper>
      </Container>
    </div>
  );
}

export default App;
