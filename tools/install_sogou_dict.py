#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import shutil

if sys.version >= '3':
    import urllib.request as url_request
    import urllib.parse as url_parse
else:
    import urllib as url_request
    import urllib as url_parse


def download(url, file):
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))
    remote = url_request.urlopen(url)
    with open(file, 'wb') as local:
        BLOCK_SIZE = 1024 * 1024
        while True:
            buffer = remote.read(BLOCK_SIZE)
            local.write(buffer)
            if len(buffer) < BLOCK_SIZE:
                break
    return True


dicts = {
    '搜狗标准词库': 11640,
    '计算机词汇大全': 15117,
}

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)
if os.path.exists('scel2txt'):
    shutil.rmtree('scel2txt')
os.system('git clone https://github.com/lewangdev/scel2txt.git')
os.chdir('scel2txt')

for dict in dicts:
    url = 'https://pinyin.sogou.com/d/dict/download_cell.php?id=%d&name=%s' % (
        dicts[dict], url_parse.quote(dict))
    print('下载"%s": %s ...' % (dict, url))
    download(url, os.path.join('scel', dict + '.scel'))

if sys.version >= '3':
    os.system('%s scel2txt.py' % sys.executable)
elif (sys.platform == 'win32' and os.system('where go') == 0) or (sys.platform != 'win32' and os.system('which go') == 0):
    os.system('go build scel2txt.go')
    os.system('./scel2txt')
else:
    assert False, '需要 python3 环境或者 golang 环境'

shutil.copy2(os.path.join('out', 'luna_pinyin.sogou.dict.yaml'),
             os.path.dirname(script_dir))

os.chdir(script_dir)
shutil.rmtree('scel2txt')
