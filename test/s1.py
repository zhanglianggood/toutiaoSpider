import requests, json
from bs4 import BeautifulSoup
from requests.exceptions import RequestException


def get_page():
    url = 'https://www.toutiao.com/api/search/content/?'
    params = {
        'offset': ' 0',
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab',
    }
    # requests自带params参数能够补全URL可代替urllib.urlopen()的拼接
    response = requests.get(url, params=params)
    try:
        if response.status_code == 200:
            # 如果状态码为200（即响应成功）则返回json格式的响应内容
            # 在requests中自带json()方法
            return response.json()
        else:
            return None
    except RequestException as f:
        return f


def main():
    html = get_page()
    # 输出响应内容
    print(html)


if __name__ == '__main__':
    main()
