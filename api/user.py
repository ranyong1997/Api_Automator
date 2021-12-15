import os
from core.rest_client import RestClient
from common.read_data import data

###################################################
# 将二次封装的HTTP接口再次封装为不不同的接口
###################################################

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]


class User(RestClient):

    def __init__(self, api_root_url, **kwargs):
        super(User, self).__init__(api_root_url, **kwargs)

    def login(self, **kwargs):
        return self.post("/login", **kwargs)

    # def list_all_users(self, **kwargs):
    #     return self.get("/users", **kwargs)


user = User(api_root_url)
