#! /usr/bin/env python

import sys
import objc

plistFile = 'build/Deployment/CronniX.app/Contents/Info.plist'
key = 'CFBundleShortVersionString'

NSMutableDictionary = objc.lookUpClass('NSMutableDictionary')

obj = NSMutableDictionary.dictionaryWithContentsOfFile_( plistFile )

print obj[key]