from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIList:


    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file()
        self.secret = ConfigProvider.load_from_secret()
        self.key = self.secret['key']
        self.token = self.secret['token']
        self.headers = self.config['headers']
        self.url = self.config['url']
        self.board_id = self.config["Board"]["id"]
        self.Key_ep = self.config["url_ep"]["Key"]
        self.Token_ep = self.config["url_ep"]["Token"]
        self.boards_ep = self.config["url_ep"]["Boards"]
        self.cards_ep = self.config["url_ep"]["Cards"]
        self.lists_ep = self.config["url_ep"]["Lists"]
        self.one_ep = self.config["url_ep"]["1"]




    def get_a_list(self):
        url = f"{self.url}{self.one_ep}{self.boards_ep}/{self.board_id}{self.lists_ep}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.get_request(url , headers=self.headers)

