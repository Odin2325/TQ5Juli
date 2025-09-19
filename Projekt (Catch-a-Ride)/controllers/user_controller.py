# controllers/user_controller.py
from models.user_model import UserModel
from views.user_view import UserView

class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = UserView()

    def login(self):
        username, password = self.view.get_login_input()
        user = self.model.get_user_by_credentials(username, password)

        if user:
            self.view.show_login_success(user)
        else:
            self.view.show_login_failure()
