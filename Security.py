import OpenFIGI
import pandas as pd
import requests

def main():
    # OpenFIGI instance
    header = {'Content-Type': 'text/json'}
    url = 'https://api.openfigi.com/v1/mapping'

    of = OpenFIGI.Requests(url, header)

    # Generate request string from file
    df = pd.read_csv('sample.csv', sep=';')
    y = list(map(lambda x: of.generate_request(idtype='ID_SEDOL',idvalue=x),df.iloc[:,4]))

    result = of.post_requests(y)
    print(result.text)

if __name__ == '__main__':
    main()
