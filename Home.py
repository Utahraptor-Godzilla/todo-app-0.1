import streamlit as st
import glob
import hashlib
import pyautogui
login = st.empty()
signup = st.empty()
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)
if "log" not in st.session_state:
    st.session_state.log = False
if "sign" not in st.session_state:
    st.session_state.sign = False
if not st.session_state.log or st.session_state.sign:
    col1, col2, col3 = st.columns(3)
    with col1:
        pass
    with col2:
        login_button = login.button("Login", key="login", use_container_width=50)
        signup_button = signup.button("Signup", use_container_width=50)
    with col3:
        pass
    if login_button:
        login.empty()
        signup.empty()
        st.session_state.log = True
    if signup_button:
        login.empty()
        signup.empty()
        st.session_state.sign = True
if st.session_state.log:
    login.empty()
    signup.empty()
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
        password = hash_password(password_input.text_input("Password", type="password"))
        st.session_state.username = username
        st.session_state.password = password
        login = login_button.button("Login")
        if login:
            file = f"passwords/{st.session_state.username}-{st.session_state.password}.txt"
            if "file" not in st.session_state:
                st.session_state.file = file
            st.session_state.file = file
            files = glob.glob(st.session_state.file)
            if len(files) == 0:
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
if st.session_state.sign:
    login.empty()
    signup.empty()
    signup_header = st.empty()
    username_input = st.empty()
    password_input = st.empty()
    signup_button = st.empty()
    # Initialize session state variables if they don't exist
    if "username" not in st.session_state:
        st.session_state.username = ""
    if "password" not in st.session_state:
        st.session_state.password = ""
    if "create_file" not in st.session_state:
        st.session_state.create_file = False
    signup_header.subheader("Signup")
    username = username_input.text_input("Username", value=st.session_state.username, key="user")
    password = hash_password(password_input.text_input("Password", type="password"))
    signup = signup_button.button("Signup")
    if signup:
        file = f"passwords/{username}-{password}.txt"
        if "file" not in st.session_state:
            st.session_state.file = file
        files = glob.glob(f"{file}")
        if files != []:
            st.warning("Username/Password is already taken.")
        else:
            with open(file, "w") as txt:
                pass
            st.session_state.username = username
            st.session_state.password = password
            st.session_state.create_file = True
    if st.session_state.create_file:
        pyautogui.hotkey("f5")
#app