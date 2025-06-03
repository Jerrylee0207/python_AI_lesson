import requests
from requests import Response
import io
from io import StringIO
import csv

##url:str = "https://tsis.dbas.gov.taipei/statis/webMain.aspx?sys=220&ymf=&kind=21&type=0&funid=A05041901&cycle=&outmode=12&compmode=0&outkind=1&deflst=2&nzo=1"
url:str = "https://data.moenv.gov.tw/api/v2/aqx_p_432?api_key=9b651a1b-0732-418e-b4e9-e784417cadef&limit=1000&sort=ImportDate desc&format=JSON";

headers = {
    "User-Agent": "Chrome/137.0.0.0"
}

try:
    response:Response = requests.get(url, headers = headers);
    response.raise_for_status();
    
except HTTPError:
    print("status code not 200");
except ConnectionError:
    print("connection error");
except Timeout:
    print("time out");
except RequestException as errtxt:
    print(f"error as {errtxt}");
except Exception:
    print("unknown error");
else:
    print("success");
    content:str = response.text;
    '''
    file:StringIO = io.StringIO(content);
    reader = csv.DictReader(file);
    power = [row for row in reader];
    file.close();

    for year_data in power:
        print(year_data);
    '''

    AQI_json = response.json()

    for key in AQI_json:
        print(key, AQI_json[key]);
