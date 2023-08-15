#from pydantic import BaseModel
#
#
#
#class Plugin(BaseModel):
#    def __init__(
#            self,
#            name: str, init_function):
#        self.name = name
#        self.register_plugin(init_function)
#
#    def register_plugin(self, init_function) -> None:
#        registration = init_function()
#    def enable(self):
#        return self.init_function()
#
#    def disable(self):
#        pass
#
#
#class PluginManager:
#    def __init__(self):
#        self.plugins = {}
#
#    def register_plugin(self, plugin: Plugin):
#        self.plugins[plugin.name] = plugin.init_function
#        self.save_to_file()  # mock function for saving to a file
#
#    def unregister_plugin(self, plugin: Plugin):
#        if plugin.name in self.plugins:
#            del self.plugins[plugin.name]
#            self.save_to_file()  # mock function for saving to a file
#
#    def save_to_file(self):
#        # This is a mock function for writing the plugins to a file
#        # In a real implementation, you might convert the plugins to a suitable format and write to a file
#        print(f"Saving {len(self.plugins)} plugins to file.")
#
#
#
##
##
##  # Create a PluginManager and register the plugins
##  pm = PluginManager()
##  pm.register_plugin(plugin1)
##  pm.register_plugin(plugin2)
##
##  # Test enabling a plugin
##  print(plugin1.enable())
##
##  # Test unregistering a plugin
##  pm.unregister_plugin(plugin1)
##
##  # The PluginManager should now only have 1 plugin
##  print(f"The PluginManager has {len(pm.plugins)} plugins.")