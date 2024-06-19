import streamlit as st
import glob
login_header = st.empty()
username_input = st.empty()
password_input = st.empty()
login_button = st.empty()
# Initialize session state variables if they don't exist
if "username" not in st.session_state:
    st.session_state.username = ""
if "password" not in st.session_state:
    st.session_state.password = ""
if "todos" not in st.session_state:
    st.session_state.todos = []
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False  # New session state variable

if not st.session_state.logged_in:
    login_header.subheader("Login")
    username = username_input.text_input("Username", value=st.session_state.username)
    password = password_input.text_input("Password", value=st.session_state.password)
    st.session_state.username = username
    st.session_state.password = password
    login = login_button.button("Login")

    if login:
        file = f"passwords/{st.session_state.username}-{st.session_state.password}.txt"
        if "file" not in st.session_state:
            st.session_state.file = file
        st.session_state.file = file
        files = glob.glob(st.session_state.file)
        if len(files)==0:
            st.warning("The password/username is not valid.")
        else:
            with open(file, "r") as txt:
                pass
            st.session_state.logged_in = True  # Update the session state variable
if st.session_state.logged_in:
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


    st.title("My Todo App")
    st.subheader("This is my todo app.")
    st.write("This app is to increase your productivity.")
    login_header.empty()
    username_input.empty()
    password_input.empty()
    login_button.empty()
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
#login
