import logging
logging.basicConfig(level=logging.DEBUG)
from yapsy.IPlugin import IPlugin 
from yapsy.PluginManager import PluginManager

def main():
    global path
    # Load the plugins from the plugin directory.
    manager = PluginManager()
    manager.setPluginPlaces(["plugins"])
    manager.collectPlugins()

    # Loop round the plugins and print their names.
    for plugin in manager.getAllPlugins():
        path=plugin.plugin_object.print_name()
        print("path Value Is",path)
        
if __name__ == "__main__":
    main()





