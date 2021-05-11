import pytest
from test.app_test import client

@pytest.mark.usefixtures("client")
def test_get_ingredients(client):
    response = client.get("/refrigerators/ingredients")
    print(response.json)
    assert 1==2