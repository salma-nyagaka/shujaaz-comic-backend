import pytest

from shujaaz.apps.user.models import User


@pytest.fixture
def create_user(db):
    """Create a db user."""
    user_details = {
        "pk": "1",
        "username": "ronaldnyagaka",
        "first_name": "ronald",
        "last_name": "nyagaka",
        "email": "ronaldnyagaka@gmail.com",
    }
    user1 = User.objects.create(**user_details)
    user1.save()
    return user1
