from models.user_model import UserModel
from views.main_menu import MainMenuView

class UserController:
    def __init__(self):
        self.model = UserModel()
        self.view = MainMenuView()

    def login(self):
        username, password = self.view.get_login_input()
        user = self.model.get_user_by_credentials(username, password)

        if user:
            self.view.show_login_success(user)
            return user
        else:
            self.view.show_login_failure()
            return None
