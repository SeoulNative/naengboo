def test_post_ingredients():
    cast_list = [
        {
            "input": {
                "username": "db-post-case-1",
                "msg": "db-post-test-case-1",
            },
            "output": [
                {
                    'username': 'db-original',
                    'msg': 'original',
                },
                {
                    'username': 'db-post-case-1',
                    'msg': 'db-post-test-case-1',
                }
            ]
        },
        {
            "input": {
                "username": "db-post-case-2",
                "msg": "db-post-test-case-2",
            },
            "output": [
                {
                    'username': 'db-original',
                    'msg': 'original',
                },
                {
                    'username': 'db-post-case-2',
                    'msg': 'db-post-test-case-2',
                }
            ]
        },
    ]
    return [(test_case["input"], test_case["output"]) for test_case in cast_list]
