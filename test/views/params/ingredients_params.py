def get_test_case_list():
    test_case_list = [
        {
            "input": {
                "테스트케이스11111input":"1111-input"
            },
            "output": {
                "테스트케이스11111output":"1111-output"
            }
        },
        {
            "input": {
                "테스트케이스2222input":"2222-input"
            },
            "output": {
                "테스트케이스2222output":"2222-output"
            }
        },
    ]
    return [(test_case["input"], test_case["output"]) for test_case in test_case_list]