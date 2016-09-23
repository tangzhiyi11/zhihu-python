# coding=utf-8


def test_into_file(text, result_file='test_result.txt'):
    with open(result_file, 'w') as result:
        result_file.write(text)