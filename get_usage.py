import requests
import pprint
from bs4 import BeautifulSoup as bs


def getUsage(username, password):
    with requests.Session() as s:

        headers = {
            "Host": "10.220.20.12",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            # 'Accept-Encoding': 'gzip, deflate',
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "close",
        }

        response = requests.get("http://10.220.20.12/", headers=headers, verify=False)

        r = s.get("http://10.220.20.12/", headers=headers, verify=False)

        headers = {
            "Host": "10.220.20.12",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "http://10.220.20.12",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.5195.102 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "Referer": "http://10.220.20.12/index.php/home/login",
            # 'Accept-Encoding': 'gzip, deflate',
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "close",
            # 'Cookie': 'ci_session=cookie',
        }

        data = "username=" + username + "&password=" + password

        r = s.post(
            "http://10.220.20.12/index.php/home/loginProcess",
            headers=headers,
            data=data,
            verify=False,
        )

        soup = bs(r.content.decode("utf-8"), "html.parser")

        table = soup.find("table", attrs={"class": "table invoicefor"})
        table_body = table.find("tbody")

        rows = table_body.find_all("tr")

        data = []

        for row in rows:
            cols = row.find_all("td")
            cols = [ele.text.strip() for ele in cols]
            data.append([ele for ele in cols if ele])  # Get rid of empty values

        # for e in data:
        #     print(*e)

        data = data[5][1].strip(' Minute')
        data = int(data)

        return data
