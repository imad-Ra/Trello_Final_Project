from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIList:
    """Handles API operations related to Trello lists."""

    def __init__(self, request: APIWrapper):
        """
        Initialize APIList with configuration and API credentials.

        :param request: An instance of APIWrapper for making HTTP requests.
        """
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
        self.lists_ep = self.config["url_ep"]["Lists"]
        self.one_ep = self.config["url_ep"]["1"]
        self.idboard_ep = self.config["url_ep"]["idBoard"]

    def get_a_list(self):
        """
        Fetch a list from the board.

        :return: API response for the get request.
        """
        url = f"{self.url}{self.one_ep}{self.boards_ep}/{self.board_id}{self.lists_ep}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.get_request(url, headers=self.headers)

    def move_list(self, list_id, new_board_id):
        """
        Move a list to a different board.

        :param list_id: ID of the list to move.
        :param new_board_id: ID of the board to move the list to.
        :return: API response for the put request.
        """
        url = f"{self.url}{self.one_ep}{self.lists_ep}/{list_id}{self.idboard_ep}"
        params = {
            "value": new_board_id,
            "key": self.key,
            "token": self.token
        }
        return self._request.put_request(url, params=params)

    def get_lists_on_board(self, board_id):
        """
        Get all lists on a specific board.

        :param board_id: ID of the board to get lists from.
        :return: API response for the get request.
        """
        url = f"{self.url}{self.one_ep}{self.boards_ep}/{board_id}{self.lists_ep}"
        params = {
            "key": self.key,
            "token": self.token
        }
        return self._request.get_request(url, params=params, headers=self.headers)