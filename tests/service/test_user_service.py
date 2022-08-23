from src.service.user_service import UserService


patch_user_db = 'src.db.user_db.UserDB'
patch_user = 'src.service.user_service.UserService'


user = {
    'name': 'Pedro',
    'email': 'ppcantidio@gmail.com',
    'id': 1
}


def test_create_user_sucess(mocker):
    mocker.patch(f'{patch_user}.user_db.get_user_by_email', return_value=None)
    mocker.patch(f'{patch_user}.user_db.create_user', return_value=user)
    result = UserService('', '', '').create_user(user)
