import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.text

    def load_json(self):
        response_body = self.get_response_body()
        json_data = None

        try:
            json_data = json.loads(response_body)
        except ValueError as e:
            print(f"Error loading JSON: {e}")

        return json_data
