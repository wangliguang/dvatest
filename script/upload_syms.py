from sys import argv
from os import listdir, system

import base
basePath = base.get_base_path()


def upload_symbol_file():
    iosPath = basePath + '/ios'

    symPath = iosPath + '/fastlane/build/ofoEngineIntl.app.dSYM'

    command = iosPath + '/Pods/FirebaseCrash/batch-upload -i '
    command += iosPath + '/ofoEngineIntl/Info.plist -p '
    command += iosPath + '/ofoEngineIntl/GoogleService-Info.plist '
    command += iosPath + '/ServiceAccount.json '
    command += symPath + '/'

    symFiles = [f for f in listdir(symPath) if f != '.DS_Store']

    for sym in symFiles:
        print 'Upload [' + sym + '] ...'
        system(command + sym)
        print

    print 'Uploaded ' + str(len(symFiles)) + ' dSYM files'

