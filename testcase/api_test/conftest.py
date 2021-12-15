import pytest
from testcase.config import api_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    """
    request.function.__name__ : 自动获取到当前执行用例的函数名
    """
    return api_data.get(testcase_name)