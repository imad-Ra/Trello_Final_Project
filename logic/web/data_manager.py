from infra.config_provider import ConfigProvider

class DataManager:
    def __init__(self):
        self.config = ConfigProvider.load_from_file()

    def get_move_list_test_data(self):
        return {
            "list_to_move_id": self.config["List"]["id"],
            "list_to_move_name": self.config["List"]["name"],
            "original_board_id": self.config["Board"]["id"],
            "target_board_id": self.config["Board"]["id2"]
        }