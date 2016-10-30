import requests


class Requests:
    def __init__(self,url,header):
        self.url = url
        self.header = header

    def post_requests(self, json):
        result = requests.post(self.url, data=None, json=json, headers=self.header)
        return result

    def generate_request(self,idtype, idvalue, exchcode='', currency='', marketsecdes=''):
        return {'idType': idtype, 'idValue': idvalue, 'exchCode': exchcode,
                'currency': currency,
                'marketSecDes': marketsecdes}
