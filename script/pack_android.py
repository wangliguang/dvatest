#!/usr/bin/env python
# coding=utf-8
# encoding=utf-8

from pack_robot import *
from pack_tools import *

import sys
import os.path
import base

basePath = base.get_base_path()

apkDir = basePath + '/android/app/build/outputs/apk/'

rnPicker = basePath + '/node_modules/react-native-picker/android/build.gradle'
rnConfig = basePath + '/node_modules/react-native-config/android/build.gradle'
rnSpinkit = basePath + '/node_modules/react-native-spinkit/android/build.gradle'

gradlePath = basePath + '/android/gradle.properties'


def change_version(content, name, code):
    start = content.find('VERSION_NAME=') + 13
    end = content.find('\n', start)
    content = content[:start] + name + content[end:]

    start = content.find('VERSION_CODE=') + 13
    end = content.find('\n', start)
    content = content[:start] + code + content[end:]
    return content


def change_gradle_properties(version_code, is_production=False):
    if version_code is None:
        return

    source_file = open(gradlePath, "r")
    content = source_file.read()
    source_file.close()

    if is_production:
        content = content.replace(
            '=.env.development',
            '=.env.production',
        )

    content = change_version(content, version_code, get_build(version_code))

    target_file = open(gradlePath, "w")
    target_file.write(content)
    target_file.close()

    print 'Change version code to : ' + version_code


def change_gradle_version(path):
    if path is None:
        return

    source_file = open(path, "r")
    content = source_file.read()
    source_file.close()

    content = content.replace(
        'buildToolsVersion "23.0.1"',
        'buildToolsVersion "25.0.0"')

    target_file = open(path, "w")
    target_file.write(content)
    target_file.close()


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print """
        Please input command (alpha/beta/rc) as first argument!
        Please input changeLog as second argument!
        Please input version_code as third argument!
        """
        exit()

    command = sys.argv[1]
    changeLog = sys.argv[2]
    version = sys.argv[3]

    change_gradle_properties(version, command == 'rc')

    os.system('yarn setup')
    change_gradle_version(rnConfig)
    change_gradle_version(rnPicker)
    change_gradle_version(rnSpinkit)

    result = os.system(
        'rm -rf ' + apkDir + ' && '     # 删除apk文件夹
        'yarn bundle-android && '       # 打jsbundle
        'cd android && '                # 进入android项目
        'chmod +x gradlew && '          # 获取gradle权限
        './gradlew assembleRelease'     # 打包gradle apk
    )

    print '打包结果参数：' + str(result)

    if result == 0:

        apkName = None
        for _, _, file_names in os.walk(apkDir):
            apkName = file_names[0]

        if apkName is not None:
            os.system('fir publish -c "' + changeLog + '" ' + apkDir + apkName)

        call_ding_robot(False,
                        get_current_datetime() + '\n'
                        'Android提测自动化打包流程结束：\n'
                        '打包日志Log信息：' + changeLog + '\n'
                        '版本号：' + version + '\n'
                        '请点击链接获取最新包 http://fir.im/EngineAndroidDebug\n')
    else:
        call_ding_robot(False,
                        get_current_datetime() + '\n'
                        'Android提测自动化打包流程中断。\n'
                        '请登录engine vnc://192.168.121.135 检查故障原因\n')

    os.system('git checkout -- .')
    os.system('git clean -df')
    print 'Android Auto Packing Finished !'
