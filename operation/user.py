from core.result_base import ResultrBase
from api.user import user
from common.logger import logger


def get_all_user_info():
    """
    获取全部数据
    :return:
    """
    result = ResultrBase()
    res = user.list_all_users()
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是【 {} 】,返回信息: {}".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    return result


def get_one_user_info(username):
    """
    获取单个用户信息
    :param username: 用户名
    :return: 自定义的关键字返回结果 result
    """
    result = ResultrBase()
    res = user.list_one_user(username)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "查询用户 ===>> 接口返回码是 【 {} 】,返回信息: {}".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("查看单个用户 ===>> 返回结果 ===>> {}".format(result.response.text))
    return result


def login_user(username, password):
    """
    登录用户
    :param username:用户名
    :param password:密码
    :return:自定义的关键字返回结果 result
    """
    result = ResultrBase()
    payload = {
        "username": username,
        "password": password
    }
    header = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    res = user.login(data=payload, header=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
        resule.token = res.json()["login_info"]["token"]
    else:
        result.error = "接口返回码是 【 {} 】,返回信息: {}".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("登录用户 ===>> 返回结果 ===>> {}".format(result.response.text))
    return result


def delete_user(username, admin_user, token):
    """
    根据用户名，删除用户信息
    :param username: 用户名
    :param admin_user: 当前操作的管理员用户
    :param token: 当前管理员用户的token
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json_data = {
        "admin_user": admin_user,
        "token": token,
    }
    header = {
        "Content-Type": "application/json"
    }
    res = user.delete(username, json=json_data, headers=header)
    result.success = False
    if res.json()["code"] == 0:
        result.success = True
    else:
        result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
    result.msg = res.json()["msg"]
    result.response = res
    logger.info("删除用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


if __name__ == '__main__':
    login_user("admin", "123456")
