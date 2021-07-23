import requests
from requests.auth import HTTPBasicAuth
import json

url = 'https://api.github.com/users/octocat/repos'

req = requests.get(url)

text = req.text

ugly_json = json.loads(text)
parsed = json.dumps(ugly_json, indent=2)

string_to_find = 'html_url'

def finder(string, string_to_find):
    count = 0
    begin_index = 0
    list_begin = []
    list_end = []

    while count < string.count(string_to_find):
        begin = string.index(string_to_find, begin_index)
        end = string.index(',', begin)
        list_begin.append(begin)
        list_end.append(end)
        begin_index = begin + 1
        count = count + 1

    return (list_begin, list_end)


begin_list = finder(parsed, string_to_find)[0]
end_list = finder(parsed, string_to_find)[1]

for i in range(0, len(begin_list)):
    a = parsed[begin_list[i]:end_list[i]]
    if a != 'html_url": "https://github.com/octocat"':
        print(a)
