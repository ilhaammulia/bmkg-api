import requests, json

base_url = 'https://data.bmkg.go.id/DataMKG/TEWS/'

class Api:
    def __init__(self):
        """
        Initialize url for request
        """
        self.url = ['autogempa.json']

    def request(self, option):
        """
        HTTP Request to BMKG API
        Select:
            0 = autogempa
        """
        try:
            with requests.Session() as session:
                with session.get(base_url + self.url[int(option)], headers={'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.77 Mobile/15E148 Safari/604.1', 'Upgrade-Insecure-Requests': '1'}) as response:
                    data = response.json()
                    return data
        except:
            return None