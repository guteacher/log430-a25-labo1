from controllers.user_controller import UserController
from daos.user_dao import UserDAO
from models.user import User
from views.user_view import UserView

dao = UserDAO()

def test_product_select():
    user_list = dao.select_all()
    assert len(user_list) >= 3

def test_product_insert():
    assert "Le test n'est pas encore là" == 1

def test_product_update():
    assert "Le test n'est pas encore là" == 1

def test_product_delete():
    assert "Le test n'est pas encore là" == 1