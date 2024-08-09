import requests
from infra.api.response_wrapper import ResponseWrapper


class APIWrapper:
    def __init__(self):
        self._request = None

    @staticmethod
    def get_request(url, headers=None, body=None,params=None):
        try:
            result = requests.get(url, headers=headers, json=body,params=params)
            return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            return ResponseWrapper(ok=False, status_code=None, data={"error": str(e)})

    @staticmethod
    def post_request(url, headers=None, body=None,params=None):
        try:
            result = requests.post(url, headers=headers, json=body,params=params)
            return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            return ResponseWrapper(ok=False, status_code=None, data={"error": str(e)})
    @staticmethod
    def patch_request(url, headers=None, body=None , params=None):
        try:
            result = requests.patch(url, headers=headers, json=body, params=params)
            return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            return ResponseWrapper(ok=False, status_code=None, data={"error": str(e)})

    @staticmethod
    def delete_request(url, headers=None, body=None, params=None):
        try:
            result = requests.delete(url, headers=headers, json=body, params=params)
            return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            return ResponseWrapper(ok=False, status_code=None, data={"error": str(e)})

    @staticmethod
    def put_request(url, headers=None, body=None, params=None):
        try:
            result = requests.put(url, headers=headers, json=body, params=params)
            return ResponseWrapper(ok=result.ok, status_code=result.status_code, data=result.json())
        except requests.exceptions.RequestException as e:
            # Handle any request exceptions
            return ResponseWrapper(ok=False, status_code=None, data={"error": str(e)})
