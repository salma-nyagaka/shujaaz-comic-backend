import pytest
from django.urls import reverse


import shujaaz.apps.user.test.fixtures.user as \
    fixtures


@pytest.mark.parametrize(
    "creator_details, expected_response",
    [
        (fixtures.fetch_creator_details, fixtures.fetch_creator_message_response),

    ],
)
def test_fetch_user(client, create_user, creator_details, expected_response):
    """Test login user."""
    creators_url = reverse("user:content_creators")
    response = client.get(creators_url, creator_details)

    if response.status_code == 200:
        assert response.data["message"] == expected_response
    else:
        encoded_data = str(expected_response).encode()
        converted_data = encoded_data.decode('utf-8')
        expected = converted_data.replace("'", '"')
   
        assert expected in response.content.decode('utf-8')


@pytest.mark.parametrize(
    "expected_response",
    [
        (fixtures.fetch_specific_creator_message_response),

    ],
)
def test_fetch_specific_user(client, create_user, expected_response):
    """Test login user."""
    
    creator_url = reverse("user:specific_content_creator", args=[1])
    response = client.get(creator_url)
     
    if response.status_code == 200:
        assert response.data["message"] == expected_response
    else:
        
        
        encoded_data = str(expected_response).encode()
        converted_data = encoded_data.decode('utf-8')
        expected = converted_data.replace("'", '"')
   
        assert expected in response.content.decode('utf-8')



