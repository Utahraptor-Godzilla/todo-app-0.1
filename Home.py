import streamlit as st
import glob
import hashlib
st.set_page_config(layout="wide")
signup_b = st.empty()
login_b = st.empty()
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def verify_password(stored_password, provided_password):
    return stored_password == hash_password(provided_password)
if "username" not in st.session_state:
    st.session_state.username = ""
if "password" not in st.session_state:
    st.session_state.password = ""
if "todos" not in st.session_state:
    st.session_state.todos = []
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if 'log' not in st.session_state:
    st.session_state.log = False
if 'sign' not in st.session_state:
    st.session_state.sign = False
if 'con' not in st.session_state:
    st.session_state.con = False
if 'notMatch' not in st.session_state:
    st.session_state.notMatch = False
if 'notCon' not in st.session_state:
    st.session_state.notCon = False
if 'confirmed' not in st.session_state:
    st.session_state.confirmed = False
if 'matched' not in st.session_state:
    st.session_state.matched = False
if 'file' not in st.session_state:
    st.session_state.file = ''
if 'a' not in st.session_state:
    st.session_state.a = ''
if not st.session_state["log"] and not st.session_state["sign"]:
    col1, col2, col3, col4, col5 = st.columns([1, 1, 2, 1, 1])
    with col1:
        pass
    with col2:
        pass
    with col3:
        signup_b = st.empty()
        login_b = st.empty()
        login_button = login_b.button("Login", key="login", use_container_width=True)
        signup_button = signup_b.button("Signup", key="signup-", use_container_width=True)
    with col4:
        pass
    with col5:
        pass
    if login_button:
        login_b.empty()
        signup_b.empty()
        st.session_state.log = True
        st.session_state.sign = False
    if signup_button:
        login_b.empty()
        signup_b.empty()
        st.session_state.sign = True
        st.session_state.log = False
if st.session_state.log:
    cole1, cole2, cole3 = st.columns([1, 9, 1])
    col1, col2, col3 = st.columns([1, 2, 1])
    with cole1:
        place_holder = st.empty()
        loge_out = place_holder.button("Home", key="hibye")
        if loge_out:
            st.session_state.log = False
            st.session_state.logged_in = False
            st.experimental_rerun()
    with col1:
        pass
    with col2:
        login_b.empty()
        signup_b.empty()
        login_header = st.empty()
        username_input = st.empty()
        password_input = st.empty()
        login_button = st.empty()
        if not st.session_state.logged_in:
            login_header.subheader("Login")
            username = username_input.text_input("Username")
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
                print(files, st.session_state.file)
                if len(files) == 0:
                    st.warning("The password/username is not valid.")
                else:
                    with open(file, "r") as txt:
                        pass
                    st.session_state.logged_in = True
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
                st.session_state["new_todo"] = ""
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
            new_todo = st.text_input(label="Enter a todo:", placeholder="Add a new todo", key="new_todo", value="", on_change=add_todo)
    with col3:
        pass
    if st.session_state.logged_in:
        place_holder.empty()
        if st.session_state.logged_in:
            place_holder.empty()
            with cole3:
                with st.expander(f"Hi {st.session_state.username}"):
                    logout = st.button("Logout", key="hi")
        if logout:
            st.session_state.log = False
            st.session_state.logged_in = False
            st.experimental_rerun()
if st.session_state.sign:
    cole1, cole2 = st.columns([1, 10])
    col1, col2, col3 = st.columns([1, 2, 1])
    with cole1:
        place_holder = st.empty()
        home = place_holder.button("Home")
        if home:
            st.session_state.sign = False
            st.experimental_rerun()
    with col1:
        pass
    with col2:
        st.session_state.signup = False
        homer = st.empty()
        login_b.empty()
        signup_b.empty()
        signup_header = st.empty()
        username_input = st.empty()
        password_input = st.empty()
        signup_button = st.empty()
        if "username" not in st.session_state:
            st.session_state.username = ""
        if "password" not in st.session_state:
            st.session_state.password = ""
        if "create_file" not in st.session_state:
            st.session_state.create_file = False
        signup_header.subheader("Signup")
        username = username_input.text_input("Username", key="user")
        password = hash_password(password_input.text_input("Password", type="password"))
        st.session_state.username = username
        st.session_state.password = password
        signup = signup_button.button("Signup")
        if signup:
            files = glob.glob("passwords/*")
            counter = 0
            for file in files:
                if file.split("/")[1].split("-")[0] == st.session_state.username:
                    counter += 1
            if counter > 0:
                st.session_state.matched = False
                st.warning("Username is already taken.")
            else:
                st.session_state.matched = True
            if st.session_state.matched:
                st.session_state.sign = False
                st.session_state.con = True
                signup_header.empty()
                username_input.empty()
                password_input.empty()
                signup_button.empty()
                place_holder.empty()
    with col3:
        pass
if st.session_state.con:
    cole1, cole2, cole3 = st.columns([1, 9, 1])
    col1, col2, col3 = st.columns([1, 2, 1])
    with cole1:
        place_holder = st.empty()
        home = place_holder.button("Home", key="bye")
        if home:
            st.session_state.con = False
            st.experimental_rerun()
    with col1:
        pass
    with col2:
        login_b.empty()
        signup_b.empty()
        con_header = st.empty()
        con_username_input = st.empty()
        con_password_input = st.empty()
        con_button = st.empty()
        con_header.subheader("Confirmation")
        con_username = con_username_input.text_input("Confirm Username")
        con_password = con_password_input.text_input("Confirm Password", type="password")
        con = con_button.button("Confirm")
        if con:
            st.session_state.sign = False
            if st.session_state.username != con_username or st.session_state.password != hash_password(con_password):
                st.session_state.confirmed = False
                st.warning("Username/Password does not match.")
            else:
                with open(f"passwords/{st.session_state.username}-{st.session_state.password}.txt", "w") as txt:
                    pass
                st.session_state.sign = False
                file = f"passwords/{st.session_state.username}-{st.session_state.password}.txt"
                if "file" not in st.session_state:
                    st.session_state.file = file
                st.session_state.file = file
                con_header.empty()
                con_username_input.empty()
                con_password_input.empty()
                con_button.empty()
                st.session_state.confirmed = True
        if st.session_state.confirmed:
            con_header.empty()
            con_username_input.empty()
            con_password_input.empty()
            con_button.empty()
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
                st.session_state["new_todo"] = ""
            st.title("My Todo App")
            st.subheader("This is my todo app.")
            st.write("This app is to increase your productivity.")
            for index, todo in enumerate(st.session_state.todos):
                checkbox = st.checkbox(todo, key=f"{index} {todo}")
                if checkbox:
                    st.session_state.todos.pop(index)
                    write_todos(st.session_state.todos)
                    del st.session_state[f"{index} {todo}"]
                    st.experimental_rerun()
            new_todo = st.text_input(label="Enter a todo:", placeholder="Add a new todo", key="new_todo", value="",
                                     on_change=add_todo)
    with col3:
        pass
    if st.session_state.confirmed:
        place_holder.empty()
        with cole3:
            with st.expander(f"Hi {st.session_state.username}"):
                logoot = st.button("Logout", key="abracadabra")
        if logoot:
            st.session_state.con = False
            st.session_state.confirmed = False
            st.experimental_rerun()
