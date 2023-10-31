from haralyzer import HarParser
from curl_cffi import requests
from rich.console import Console
import argparse
import json
import time

# url = arg.url

parser = argparse.ArgumentParser(description="Single repeater for bash")
parser.add_argument("-t", "--text", help="read in text", required=False)
parser.add_argument("-b", "--browser", help="fake browser", required=False,default="chrome110")
args = parser.parse_args()

def Read_detail(text):
    with open(text, 'r') as f:
        har_parser = HarParser(json.loads(f.read()))
    data = har_parser.har_data
    return data['entries'][0]['request']

def Make_headers(url,header):
    surl = url.replace("https://","").replace("http://","").split('/')[0]
    fname = surl+' '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'.txt'
    headers = {}
    for i in header:
        print(i['name']+':'+i['value'])
        do = input("change?[y/n]")
        if do == 'y':
            headers[i['name']] = input(i['name']+':')
        headers[i['name']] = i['value']
    return headers

def Send_Repeater(data,header,browser):
    url = data['url']
    method = data['method']
    if method == 'GET':
        print("发送的是 GET 请求\n")
        response = requests.get(url, headers=header,impersonate=browser)
    elif method == 'POST':
        print("发送的是 POST 请求\n")
        print("do you need change body?")
        do = input("y/n")
        try:
            if do == 'n':
                body = data['postData']['text']
                response = requests.post(url, headers=header, data=body ,impersonate=browser)
            else:
                body = input("body:")
                response = requests.post(url, headers=header, impersonate=browser)
        except:
            response = requests.post(url, headers=header, impersonate=browser)
    else:
        print("method error")
    return response

def Pretty_print(response):
    print('-----status code-----')
    print(response.status_code)
    console=Console()
    print('-----header-----')
    headers = response.headers
    console.log(headers)
    print('------body-----')
    body = response.text
    console.log(body)

if __name__ == "__main__":
    data = Read_detail(args.text)
    header = Make_headers(data['url'],data['headers'])
    Pretty_print(Send_Repeater(data,header,args.browser))