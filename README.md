基于 curl_cffi 制作的burp_repeater 简化版
从浏览器保存请求包为 har 文件并指定模拟的浏览器
例如 python repeater_har.py -t blog.csdn.net.har -b chrome110
从保存的 burp 请求中发送请求并指定模拟的浏览器
例如 python repeater_burp.py -t tencent.txt -b chrome110
与上一次保存的返回值做对比并输出html文件
例如 python repeater_compare.py -t tencent.txt -b chrome110 -c old_response.txt

支持的模拟浏览器版本
chrome99
chrome100
chrome101
chrome104
chrome107
chrome110
chrome99_android
edge99
edge101
safari15_3
safari15_5