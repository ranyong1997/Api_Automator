import pytest
import allure
from operation.user import login_user
from testcase.config import api_data
from common.logger import logger


@allure.step("步骤一: ===>> 登录用户")
def step_1(username):
    logger.info("步骤一: ===>> 登录用户: {}".format(username))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("针对单个接口的测试")
@allure.feature("用户登录模块")
class TestUserLogin():
    @allure.story("用例--登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("#", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("#", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {username}，{password}，{except_result}，{except_code}，{except_msg}】")
    @pytest.mark.single
    @pytest.mark.parametrize("username,password,except_result,except_code,except_msg",
                             api_data["test_login_user"])
    def test_login_user(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = login_user(username, password)
        step_1(username)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        login.info("code ===>> 期望结果: {}，实际结果: 【 {} 】".format(except_code,result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_login.py"])