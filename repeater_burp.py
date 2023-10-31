from haralyzer import HarParser
from curl_cffi import requests
from rich.console import Console
from filediff.diff import file_diff_compare
import argparse
import time

parser = argparse.ArgumentParser(description="Single repeater burpsuite text for bash")
parser.add_argument("-t","--text", help="Text to repeat", required=True)
parser.add_argument("-u","--url", help="URL to repeat", required=True)
parser.add_argument("-c","--compare", help="Compare the old respone", required=False)
args = parser.parse_args()

def read_text(fname):
    headers = {}
    method,path,body = "","",""
    with open(fname, "r") as f:
        lines = f.readlines()
    tmp = 0
    lenl = len(lines)
    for line in lines:
        if tmp == 0:
            tmpl = line.split(" ")
            method = tmpl[0]
            path = tmpl[1]
        else:
            if line == '\n':
                if lines.index(line) < lenl - 1:  
                    body = lines[lines.index(line) + 1].strip() 
                else:
                    break
            else:
                tmpl = line.split(": ")
                headers[tmpl[0]] = tmpl[1]
        tmp += 1
    return method,path,body,headers


def send_message(method,url,body,headers):
    if method == "GET":
        response = requests.get(url,headers=headers)
    elif method == "POST":
        response = requests.post(url,headers=headers,data=body)
    elif method == "PUT":
        response = requests.put(url,headers=headers,data=body)
    elif method == "DELETE":
        response = requests.delete(url,headers=headers)
    else:
        print("目前不支持该方法，请联系blackconsine")
        return False
    new_text = response.text
    new_text = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+'.txt'
    with open(new_text,'w') as f:
        f.write(new_text)
    return response,new_text
    

def print_line(response):
    console = Console()
    console.log("发送的 http 请求头为\n")
    console.log(response.request.headers)
    console.log("发送的 http 请求体为\n")
    console.log(response.request.body)
    console.log("发送的 http 响应状态码为\n")
    console.log(response.status_code)
    console.log("发送的 http 响应头为\n")
    console.log(response.headers)
    console.log("发送的 http 响应体为\n")
    console.log(response.text)


def compare_text(old_text,new_text,Host):
    outfile = Host+"_"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+"_"+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())+".html"
    file_diff_compare(old_text, new_text, diff_out=outfile, max_width=70, numlines=0, show_all=False, no_browser=False)
    return outfile


def main():
    method,path,body,headers = read_text(args.text)
    url = url + path
    try:
        response,new_text = send_message(method,url,body,headers)
    except:
        return False
    print_line(response)
    if args.compare:
        outfile = compare_text(args.compare,new_text,response.request.headers['Host'])
        print("对比结果在:"+outfile)
    

if __name__ == "__main__":
    main()