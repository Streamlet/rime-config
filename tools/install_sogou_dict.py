#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import shutil

if sys.version >= '3':
    import urllib.request as urllib
else:
    import urllib


def download(url, file):
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))
    try:
        remote = urllib.urlopen(url)
    except Exception as e:
        print(e)
        return False
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
if not os.path.exists('scel2txt'):
    os.system('git clone https://github.com/lewangdev/scel2txt.git')
os.chdir('scel2txt')

for dict in dicts:
    url = 'https://pinyin.sogou.com/d/dict/download_cell.php?id=%d&name=%s' % (
        dicts[dict], dict)
    download(url, os.path.join('scel', dict + '.scel'))

if os.system('which go') == 0:
    os.system('go build scel2txt.go')
    os.system('./scel2txt')
else:
    os.system('%s scel2txt.py' % sys.executable)

shutil.copy2(os.path.join('out', 'luna_pinyin.sogou.dict.yaml'),
             os.path.dirname(script_dir))

os.chdir(script_dir)
shutil.rmtree('scel2txt')
