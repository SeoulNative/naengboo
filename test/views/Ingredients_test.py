import pytest

from test.app_test import client
from test.views.params.ingredients_params import get_test_case_list


@pytest.mark.parametrize("input, output", get_test_case_list())
def test_get_ingredients(client, input, output):
    print(input)
    print(output)
    response = client.get("/refrigerators/ingredients")
    print(len(response.json))
    assert 1==2