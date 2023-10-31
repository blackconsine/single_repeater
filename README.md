#### 基于 curl_cffi 制作的burp_repeater 简化版

1. 从浏览器保存请求包为 har 文件并指定模拟的浏览器
  例如 python repeater_har.py -t blog.csdn.net.har -b chrome110
2. 从保存的 burp 请求中发送请求并指定模拟的浏览器
  2.1 单独模拟发送不对比结果
     例如 python repeater_burp.py -t tencent.txt -b chrome110
  2.2 与上一次保存的返回值做对比并输出html文件 *需要将上一次请求的返回体保存成 txt 文件*
     例如 python repeater_compare.py -t tencent.txt -b chrome110 -c old_response.txt

#### 支持的模拟浏览器版本(与 curl_cffi 相同)
1. chrome99
2. chrome100
3. chrome101
4. chrome104
5. chrome107
6. chrome110
7. chrome99_android
8. edge99
9. edge101
10. safari15_3
11. safari15_5
