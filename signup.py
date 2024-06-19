import streamlit as st
import glob
signup_header = st.empty()
username_input = st.empty()
password_input = st.empty()
signup_button = st.empty()
# Initialize session state variables if they don't exist
if "username" not in st.session_state:
    st.session_state.username = ""
if "password" not in st.session_state:
    st.session_state.password = ""
if "todos" not in st.session_state:
    st.session_state.todos = []
if "signed_up" not in st.session_state:
    st.session_state.signed_up = False  # New session state variable


if not st.session_state.signed_up:
    signup_header.subheader("Signup")
    username = username_input.text_input("Username", value=st.session_state.username)
    password = password_input.text_input("Password", value=st.session_state.password, type="password")
    signup = signup_button.button("Signup")

    if signup:
        file = f"passwords/{username}-{password}.txt"
        if "file" not in st.session_state:
            st.session_state.file = file
        files = glob.glob(f"passwords/{file}")
        if files != []:
            st.warning("Username/Password is already taken.")
        else:
            with open(file, "w") as txt:
                pass
            st.session_state.username = username
            st.session_state.password = password
            st.session_state.signed_up = True  # Update the session state variable

if st.session_state.signed_up:
    def get_todos(filepath=st.session_state.file):
        """Reads a text file and returns a list of all the to-do items."""
        with open(filepath, 'r') as file_local:
            todos_local = file_local.readlines()
        return todos_local
    def write_todos(todos_arg, file_path=st.session_state.file):
        """Writes a list of to-do items in the text file."""
        with open(file_path, 'w') as file_local:
            file_local.writelines(todos_arg)
    todos = get_todos()
    st.session_state.todos = todos

    def add_todo():
        todo = st.session_state["new_todo"] + '\n'
        todos.append(todo)
        write_todos(todos)
    def update_checkboxes():
        for index, todo in enumerate(st.session_state.todos):
            checkbox_key = f"checkbox_{index}"
    st.title("My Todo App")
    st.subheader("This is my todo app.")
    st.write("This app is to increase your productivity.")
    signup_header.empty()
    username_input.empty()
    password_input.empty()
    signup_button.empty()
    checkbox_states = []
    for index, todo in enumerate(st.session_state.todos):
        checkbox = st.checkbox(todo, key=f"{index} {todo}")
        if checkbox:
            st.session_state.todos.pop(index)
            write_todos(st.session_state.todos)
            del st.session_state[f"{index} {todo}"]
            st.experimental_rerun()

    new_todo = st.text_input(label="Enter a todo:", placeholder="Add a new todo", key="new_todo")
    add2_todo = st.button("Add Todo")

    if add2_todo and new_todo:
        add_todo()
        st.experimental_rerun()
