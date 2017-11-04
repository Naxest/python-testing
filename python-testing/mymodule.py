
import requests

def get_headers_from_url(url):
    requester = Requester(url)
    result = requester.make_request()
    headers = result.headers
    return headers

class Requester(object):

    def __init__(self, url):
        self.__url = url

    def make_request(self):
        return requests.get(url=self.__url)