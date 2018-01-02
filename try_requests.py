#!/usr/bin/env python
#coding: utf-8
import requests

def get_url(url, params, headers):
    r = requests.get(url, params=params, headers=headers)
    return r.text

def post_url(url, data, headers):
    r = requests.post(url, data=data, headers=headers)
    return r.text

def run(method):
    headers = {'user-agent': 'my-app/0.0.1'}
    if method.upper() == 'GET':
        payload = {'key1': 'value1', 'key2': 'value2', 'key3': None}
        #payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
        url = "http://httpbin.org/get"
        response = get_url(url,params=payload, headers=headers)
        print response
    elif method.upper() == 'POST':
        url = "http://httpbin.org/post"
        payload = {'key1': 'value1', 'key2': 'value2'}
        response = post_url(url, data=payload, headers=headers)
        print response

if __name__ == "__main__":
    #run('get')
    run('post')
        