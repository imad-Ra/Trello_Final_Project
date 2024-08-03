from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class NewBoard:
    BOARDS_END_POINT = "/1/boards/"
    NAME_EP = "?name="
    KEY_EP = "&key="
    TOKEN_EP = "&token="

    def __init__(self, request: APIWrapper):
        self._request = request
        self.config = ConfigProvider().load_from_file(r"C:\Users\nraba\PycharmProjects\Trello_Final_Project\config.json")
        self.secret = ConfigProvider.load_from_file(r"C:\Users\nraba\PycharmProjects\Trello_Final_Project\secret.json")

    def create_new_board(self, name):
        key = self.secret['api_key']
        token = self.secret['api_token']
        url = f"{self.config['base_url']}{self.BOARDS_END_POINT}{self.NAME_EP}{name}{self.KEY_EP}{key}{self.TOKEN_EP}{token}"
        return self._request.post_request(url)

    def delete_board_by_id(self, board_id):
        key = self.secret['api_key']
        token = self.secret['api_token']
        url = f"{self.config['base_url']}{self.BOARDS_END_POINT}{board_id}?key={key}&token={token}"
        return self._request.delete_request(url)

