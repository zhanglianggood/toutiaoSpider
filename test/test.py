import json
from urllib import request, parse
import requests
from requests.exceptions import RequestException


# encoding:utf-8

def main():
    data = {
        # "aid": "24",
        # "app_name": "web_search",
        "offset": "20",
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "en_qc": "1",
        "cur_tab": "1",
        "from": "search_tab",
        "pd": "synthesis",
        # "timestamp": "1560475401606"
    }
    urls = "https: // www.toutiao.com / group / a6704085403353219588 /"
          # https: // www.toutiao.com / a6704085403353219588 /
    try:
        res = requests.get(urls, params=data)
        print(res.text)
        if res.status_code == 200:
            return res.text
    except RequestException:
        print("request failed")


def parse_page(html):
    data = json.loads(html)
    if 'data' in data.keys():
        for each in data.get('data'):
            if 'abstract' in each.keys() and 'article_url' in each.keys():
                abstract = each.get('abstract')
                article_url = each.get('article_url')
                print(abstract)
                print(article_url)


if __name__ == "__main__":
    html = main()
    print(html)
    # parse_page(html)
