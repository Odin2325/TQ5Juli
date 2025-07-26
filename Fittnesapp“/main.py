from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.base import runTouchApp
import sqlite3

class UserLogin:
    def __init__(self):
        self.conn = sqlite3.connect('users.db')
        self.cursor = self.conn.cursor()

    def create_table(self, table_name):
        if not self.is_table_exists(table_name):
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (_id INTEGER PRIMARY KEY, username TEXT, password TEXT)")

    def insert_user(self, username, password):
        query = f"INSERT INTO users VALUES (NULL, ?, ?)"
        self.cursor.execute(query, (username, password))

    def check_login(self, username, password):
        query = f"SELECT 1 FROM users WHERE username = ? AND password = ?"
        self.cursor.execute(query, (username, password))
        return len(self.cursor.fetchall()) > 0

class TrainingScheduleDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name):
        if not self.is_table_exists(table_name):
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (_id INTEGER PRIMARY KEY, userId INTEGER, date DATE, exercise TEXT, weight INTEGER, reps INTEGER)")

    def insert_data(self, table_name, data_dict):
        query = f"INSERT INTO {table_name} VALUES (NULL, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (data_dict['userId'], data_dict['date'], data_dict['exercise'], data_dict['weight'], data_dict['reps']))

    def get_data(self, table_name, condition):
        query = f"SELECT * FROM {table_name} WHERE userId = ?"
        self.cursor.execute(query, (condition,))
        return self.cursor.fetchall()

    def is_table_exists(self, table_name):
        query = f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'"
        self.cursor.execute(query)
        if len(self.cursor.fetchall()) > 0:
            return True
        else:
            return False

class TrainingScheduleApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical')

        user_label = Label(text='Username:')
        password_label = Label(text='Password:')

        username_input = TextInput(multiline=False)
        password_input = TextInput(multiline=False, hint_text='password', password=True)

        login_button = Button(text='Login', size_hint=(1, 0.2))
        load_button = Button(text='Load', size_hint=(1, 0.2))

        main_layout.add_widget(user_label)
        main_layout.add_widget(password_label)
        main_layout.add_widget(username_input)
        main_layout.add_widget(password_input)

        main_layout.add_widget(login_button)
        main_layout.add_widget(load_button)

        login_button.bind(on_press=self.login_user)
        load_button.bind(on_press=self.load_data)

        return main_layout

    def login_user(self, instance):
        username = self.username_input.text
        password = self.password_input.text

        user_login = UserLogin()
        if user_login.check_login(username, password):
            print('User logged in successfully!')
            # Show the training schedule app
            self.show_training_schedule()
        else:
            print('Invalid username or password')

    def load_data(self, instance):
        # Load data from database here
        pass

    def show_training_schedule(self):
        # Create a new layout for the training schedule app
        training_schedule_layout = BoxLayout(orientation='vertical')

        date_input = TextInput(multiline=False, hint_text='Date')
        exercise_input = TextInput(multiline=False, hint_text='Exercise')
        weight_input = TextInput(multiline=False, hint_text='Weight')
        reps_input = TextInput(multiline=False, hint_text='Repetitions')

        save_button = Button(text='Save', size_hint=(1, 0.2))
        load_button = Button(text='Load', size_hint=(1, 0.2))

        training_schedule_layout.add_widget(date_input)
        training_schedule_layout.add_widget(exercise_input)
        training_schedule_layout.add_widget(weight_input)
        training_schedule_layout.add_widget(reps_input)

        training_schedule_layout.add_widget(save_button)
        training_schedule_layout.add_widget(load_button)

        save_button.bind(on_press=self.save_data)
        load_button.bind(on_press=self.load_data)

        # Show the training schedule app
        self.root_window.remove_widget(self.build())
        self.root_window.add_widget(training_schedule_layout)

    def save_data(self, instance):
        user_id = 1
        date = self.date_input.text
        exercise = self.exercise_input.text
        weight = int(self.weight_input.text)
        reps = int(self.reps_input.text)

        training_db = TrainingScheduleDB('training_ schedules.db')
        training_db.create_table('training_schedules')
        training_db.insert_data('training_schedules', {'userId': user_id, 'date': date, 'exercise': exercise, 'weight': weight, 'reps': reps})

    def load_data(self, instance):
        # Load data from database here
        pass

runTouchApp(TrainingScheduleApp())