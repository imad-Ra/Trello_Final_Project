from infra.api.api_wrapper import APIWrapper
from infra.config_provider import ConfigProvider


class APIBoard:
    """Handles API operations related to Trello boards."""

    def __init__(self, request: APIWrapper):
        """
        Initialize APIBoard with configuration and API credentials.

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
        self.members_ep = self.config["url_ep"]["Members"]
        self.me_ep = self.config["url_ep"]["Me"]
        self.search_ep = self.config["url_ep"]["Search"]
        self.one_ep = self.config["url_ep"]["1"]

    def get_a_board(self):
        """
        Fetch a specific board.

        :return: API response for the get request.
        """
        url = f"{self.url}{self.one_ep}{self.boards_ep}/{self.board_id}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.get_request(url, headers=self.headers)

    def delete_a_board(self, id):
        """
        Delete a board by its ID.

        :param id: ID of the board to be deleted.
        :return: API response for the delete request.
        """
        url = f"{self.url}{self.one_ep}{self.boards_ep}/{id}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.delete_request(url, headers=self.headers)

    def get_search_board(self, name):
        """
        Search for a board by name.

        :param name: Name of the board to search for.
        :return: API response for the get request.
        """
        query = {
            'query': name,
            'key': self.key,
            'token': self.token
        }
        url = f"{self.url}{self.one_ep}{self.search_ep}"
        return self._request.get_request(url, headers=self.headers, params=query)

    def get_all_boards(self):
        """
        Fetch all boards for the authenticated user.

        :return: API response for the get request.
        """
        url = f"{self.url}{self.one_ep}{self.members_ep}{self.me_ep}{self.boards_ep}{self.Key_ep}{self.key}{self.Token_ep}{self.token}"
        return self._request.get_request(url, headers=self.headers)

    def delete_board_by_name(self, name):
        """
        Delete a board by its name.

        :param name: Name of the board to be deleted.
        """
        response = self.get_all_boards()
        for board in response.data:
            if board['name'] == name:
                self.delete_a_board(board['id'])

    def post_create_a_board(self, params):
        """
        Create a new board with given parameters.

        :param params: Dictionary containing board creation parameters.
        :return: API response for the post request.
        """
        url = f"{self.url}{self.one_ep}{self.boards_ep}"
        query_params = {
            "key": self.key,
            "token": self.token
        }
        query_params.update(params)
        return self._request.post_request(url, params=query_params)