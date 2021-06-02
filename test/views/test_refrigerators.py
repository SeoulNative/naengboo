from json import loads

import pytest

from test import client
from test.views.params import refrigerators_params as params
from utils.test_utils import subset_checker 


@pytest.mark.parametrize('input, output', params.test_post_ingredients())
def test_post_ingredients(client, input, output):
    response = client.post(
        '/refrigerators/ingredients',
        json=input,
    )

    response_json = loads(response.json)
    for i in range(len(output)):
        assert subset_checker(response_json[i], output[i])
