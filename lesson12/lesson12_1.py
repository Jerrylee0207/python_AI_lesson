import requests
from requests import Response
from requests import HTTPError, ConnectionError, Timeout, RequestException, JSONDecodeError

def fetch_json(url:str)->list[dict]:
    headers = {
    "User-Agent": "Chrome/137.0.0.0"
    }
    try:
        response:Response = requests.get(url, headers = headers);
        response.raise_for_status();
        print("success");
        return response.json();
        
    except HTTPError:
        print("status code not 200");
    except ConnectionError:
        print("connection error");
    except Timeout:
        print("time out");
    except RequestException as errtxt:
        print(f"error as {errtxt}");
    except JSONDecodeError:
        print("JSON format error");
    except Exception:
        print("unknown error");

url:str = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json";
data = fetch_json(url);

print(data);


