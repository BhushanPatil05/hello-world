from yapsy.IPlugin import IPlugin
from configparser import ConfigParser
import os,glob

class PluginOne(IPlugin):
    def print_name(self):
        print ("This is plugin 1")
        parser = ConfigParser()
        print(parser.read('C:\Python34\Programs\config4.ini'))
        print(parser.get('path','dirpath'))
        #print(parser.get('path','username'))
        #print(parser.get('path','password'))
        path=parser.get('path','dirpath')
        return path

