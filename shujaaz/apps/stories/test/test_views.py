import pytest
from django.urls import reverse

import shujaaz.apps.stories.test.fixtures.stories as \
    fixtures

@pytest.mark.parametrize(
    "story_details, expected_response",
    [
        (fixtures.fetch_stories, fixtures.fetch_stories_response),

    ],
)
def test_fetch_stories(client, create_user, story_details, expected_response):
    """Test fetching of all stories."""
    stories_url = reverse("stories:stories", args=[9])
    response = client.get(stories_url, story_details)

    if response.status_code == 200:
        assert response.data["message"] == expected_response
