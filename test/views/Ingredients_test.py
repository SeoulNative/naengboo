from test.app_test import client

def test_get_ingredients(client):
    response = client.get("/refrigerators/ingredients")
    print(response.json)
    assert 1==2


def test_second_get_ingredients(client):
    response = client.get("/refrigerators/ingredients")
    print(response.json)
    assert 1==2
    