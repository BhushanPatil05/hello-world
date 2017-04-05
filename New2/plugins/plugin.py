from yapsy.IPlugin import IPlugin
from configparser import ConfigParser
from xml.etree.ElementTree import ElementTree
import os,glob
class PluginOne(IPlugin):
    def print_name(self):
        print("This is plugin 1")
        parser = ConfigParser()
        print(parser.read('C:\Python34\Programs\config3.ini'))
        print(parser.get('path', 'dirpath'))
        path=parser.get('path', 'dirpath')
        return path
