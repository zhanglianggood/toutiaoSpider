from urllib import parse
import json
url = "https://www.toutiao.com/api/search/content/?"
offset = 0
param = """{
        "offset": "re_offset",
        "format": "json",
        "keyword": "街拍",
        "autoload": "true",
        "count": "20",
        "en_qc": "1",
        "cur_tab": "1",
        "from": "search_tab",
        "pd": "synthesis"
    }"""
meta = param.replace('re_offset', str(offset))
print(meta)
start_urls = [url + parse.urlencode(json.loads(meta))]
print(start_urls)