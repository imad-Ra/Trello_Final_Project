from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIBoard:


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


    def get_a_board(self):
        url = f"{self.url}/1/{self.boards_ep}/{self.board_id}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.get_request(url , headers=self.headers)

    def delete_a_board(self , id):
        url = f"{self.url}/1/{self.boards_ep}/{id}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.delete_request(url, headers=self.headers)

    def get_search_board(self, name):
        query = {
        'query': name,
        'key': self.key,
        'token': self.token
    }
        url = f"{self.url}/1/search"
        return self._request.get_request(url, headers=self.headers, params=query)

    def get_all_boards(self):

        url = f"{self.url}/1/members/me{self.boards_ep}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.get_request(url, headers=self.headers)


    def delete_board_by_name(self, name):

        response = self.get_all_boards()
        for board in response.data:
            if board['name'] == name:
                self.delete_a_board(board['id'])

    def post_create_a_board(self, params):
        url = f"{self.url}/1/boards"
        query_params = {
            "key": self.key,
            "token": self.token
        }
        query_params.update(params)
        return self._request.post_request(url, params=query_params)