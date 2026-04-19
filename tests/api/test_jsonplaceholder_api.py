import pytest
import requests


@pytest.mark.api
def test_post_endpoint_returns_expected_payload(api_base_url: str) -> None:
    response = requests.get(f"{api_base_url}/posts/1", timeout=10)

    assert response.status_code == 200

    payload = response.json()
    assert payload["id"] == 1
    assert payload["userId"] == 1
    assert payload["title"]

