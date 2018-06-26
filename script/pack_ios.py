#!/usr/bin/env python
# coding=utf-8
# encoding=utf-8

# from unzip_dsym import *
# from unload_syms import *
# from pack_robot import *
from pack_tools import *

import os
import base
import sys

basePath = base.get_base_path()

infoPlistPath = basePath + '/ios/dvatest/Info.plist'

def change_Version_file(content, version_name, version_code):
    start = content.find('<key>CFBundleShortVersionString</key>') + 47
    end = content.find('</string>', start)
    content = content[:start] + version_name + content[end:]

    start = content.find('<key>CFBundleVersion</key>') + 36
    end = content.find('</string>', start)
    content = content[:start] + version_code + content[end:]
    
    return content
    

def change_version(version_name):
    if version_name is None:
        return
    
    source_file = open(infoPlistPath, 'r')
    content = source_file.read()
    source_file.close()

    content = change_Version_file(content, version_name, get_build(version_name))

    traget_file = open(infoPlistPath, 'w')
    traget_file.write(content)
    traget_file.close()

    print 'Change version code to : ' + version_name

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print """
        =============warning==========
        Please first param
        Please second param
        Please third param
        Please forth param
        =============warning==========
        """
        exit()

    command = sys.argv[1]
    changeLog = sys.argv[2]
    version_name = sys.argv[3]

    change_version(version_name)

    result = os.system(
        "echo 'engine' | sudo -S sudo xcode-select --switch "  # 使用Xcode9.2
        "'/Applications/Xcode9.2.app/Contents/Developer' && "
        'yarn setup && '
        'cd ios && '
        'pod update Yoga && '   # update pod
        'pod install && '
        'fastlane ' + command)  # start pack

    print '打包结果参数：' + str(result)