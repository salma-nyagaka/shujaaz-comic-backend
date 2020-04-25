# import pytest

# from shujaaz.apps.authentication.models import User

# # from .fixtures import signup as fixtures


# @pytest.mark.django_db
# @pytest.fixture
# def create_user(db):
#     """
#     create a db user
#     """
#     user_details = {
#        "username": "user1",
#         "password": "pbkdf2_sha256$150000$QK5Wp847GJrP$DiAhOOWRGm2nzACaMq+2K+b94RtXpk9GpftJb19loRE=",
#         "email": "user1@quexl.com",
#     }
#     user1 = User.objects.create(**user_details)
#     # import pdb
#     # pdb.set_trace()
#     # user1.is_active = True  # activate user account
#     user1.save()
#     return user1

# def test_create_user(user_details, expected_output):
#     """
#     test creating new user
#     """
#     with pytest.raises(TypeError, match=expected_output):
#         User.objects.create_user(**user_details)

