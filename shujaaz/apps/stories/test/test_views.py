import pytest
from django.urls import reverse

import shujaaz.apps.stories.test.fixtures.stories as \
    story_fixtures
import shujaaz.apps.stories.test.fixtures.characters as \
    characters_fixtures


@pytest.mark.parametrize(
    "story_details, expected_response",
    [
        (story_fixtures.fetch_stories, story_fixtures.fetch_stories_response),

    ],
)
def test_fetch_stories(client, create_user, story_details, expected_response):
    """Test fetching of all stories."""
    stories_url = reverse("stories:stories", args=[9])
    response = client.get(stories_url, story_details)

    if response.status_code == 200:
        assert response.data["message"] == expected_response


@pytest.mark.parametrize(
    "character_details, expected_response",
    [
        (characters_fixtures.fetch_character, characters_fixtures.fetch_character_response),
    ],
)
def test_fetch_characters(client, create_user, character_details, expected_response):
    """Test fetching of all stories."""
    characters_url = reverse("stories:characters", args=[1])
    response = client.get(characters_url, character_details)

    if response.status_code == 200:
        assert response.data["message"] == expected_response
