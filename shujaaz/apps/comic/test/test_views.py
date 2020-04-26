import pytest
from django.urls import reverse


import shujaaz.apps.comic.test.fixtures.comic as \
    fixtures
import shujaaz.apps.comic.test.fixtures.characters as \
    characters_fixtures


@pytest.mark.parametrize(
    "comic_details, expected_response",
    [
        (fixtures.fetch_comics, fixtures.fetch_all_comics_response),

    ],
)
def test_fetch_user(client, create_user, comic_details, expected_response):
    """Test fetching of all comcis."""
    comics_url = reverse("comic:comics")
    response = client.get(comics_url, comic_details)

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
        (fixtures.invalid_comic_id),

    ],
)
def test_fetch_specific_user(client, create_user, expected_response):

    """
    Test login user.
    """
    creator_url = reverse("comic:specific_comic", args=[1])
    response = client.get(creator_url)
    if response.status_code == 200:
        assert response.data["message"] == expected_response
    else:
        encoded_data = str(expected_response).encode()
        converted_data = encoded_data.decode('utf-8')
        expected = converted_data.replace("'", '"')
        assert expected.replace(": ", ':') in response.content.decode('utf-8')



@pytest.mark.parametrize(
    "character_details, expected_response",
    [
        (characters_fixtures.fetch_character, characters_fixtures.fetch_comics_characters),
    ],
)
def test_fetch_characters(client, create_user, character_details, expected_response):
    """Test fetching of all characters."""
    characters_url = reverse("comic:characters", args=[2])
    response = client.get(characters_url, character_details)

    if response.status_code == 200:
        assert response.data["message"] == expected_response
