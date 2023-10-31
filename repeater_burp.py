from haralyzer import HarParser
from curl_cffi import requests
from rich.console import Console
import argparse
import time

parser = argparse.ArgumentParser(description="Single repeater burpsuite text for bash")
parser.add_argument("-t","--text", help="Text to repeat", required=True)
parser.add_argument("-u","--url", help="URL to repeat", required=True)
parser.add_argument("-c","--compare", help="Compare the old respone", required=False)
args = parser.parse_args()

def read_text():
    pass

def send_message():
    pass

def print_line():
    pass

def compare_text():
    pass

def main():
    pass

if __name__ == "__main__":
    pass