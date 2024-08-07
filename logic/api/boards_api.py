from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIBoard:
    BOARDS_END_POINT = "/1/boards/"
    NAME_EP = "?name="
    KEY_EP = "&key="
    TOKEN_EP = "&token="


    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.key = self.secret['key']
        self.token = self.secret['token']
        self.headers = self.config['headers']
        self.url = self.config['url']
        self.boards = self.config["url_ep"]["Boards"]
        self.id = self.config["API"]["id"]
        self.Key_ep = self.config["url_ep"]["Key"]
        self.Token_ep = self.config["url_ep"]["Token"]



    def get_a_board(self):
        url = f"{self.url}/1/{self.boards}/{self.id}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.get_request(url , headers=self.headers)

    def delete_a_board(self):
        url = f"{self.url}/1/{self.boards}/{self.id}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.delete_request(url, headers=self.headers)
