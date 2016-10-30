from json import dumps as json

class Figi:
    """
    Container for OpenFIGI symbols
    """
    def __init__(self, figi, name, ticker, exchcode, compositefigi, uniqueid, securitytype, marketsector,
                 shareclassfigi, uniqueidfutopt):
        self.figi = figi
        self.name = name
        self.ticker = ticker
        self.exchcode = exchcode
        self.compositefigi = compositefigi
        self.uniqueid = uniqueid
        self.securitytype = securitytype
        self.marketsector = marketsector
        self.shareclassfigi = shareclassfigi
        self.uniqueidfutopt = uniqueidfutopt


class FigiRequest:
    def __init__(self, idtype, idvalue, exchcode=None, miccode=None, currency=None, marketsecdes=None):
        self.idtype = idtype
        self.idvalue = idvalue
        self.exchcode = exchcode
        self.miccode = miccode
        self.currency = currency
        self.marketsecdes = marketsecdes

    def tojson(self):
        return json.dumps(
            {'idType': self.idType, 'idValue': self.idvalue, 'exchCode': self.exchcode, 'micCode': self.miccode,
             'currency': self.currency,
             'marketSecDes': self.marketsecdes})


class RequestFIGI:
    """
    Class to build requests from the OpenFIGI API
    """
    def __init__(self):
        pass

    def


r = Request()
