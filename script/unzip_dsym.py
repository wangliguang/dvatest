#!/usr/bin/env python
# coding=utf-8
# encoding=utf-8

from shutil import copyfile
import zipfile
import base
import time

basePath = base.get_base_path()

zipPath = basePath + '/ios/fastlane/build/'
zipPack = 'ofoEngineIntl.app.dSYM'
zipFile = 'ofoEngineIntl.app.dSYM.zip'


def unzip_symbol(source, target):
    fz = zipfile.ZipFile(source, 'r')
    for file in fz.namelist():
        fz.extract(file, target)


def back_up_symbol(version='dSYM'):
    now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    copyfile(zipPath + zipFile,
             zipPath + version + '_' + str(now) + '.zip')

