import importlib
import sys
import re
from tools.aspect import decorate_members

#sys.meta_path = MyLIst(sys.MetaPath)
class PostImportFinder:
    def __init__(self, param, exclusions):
        self._skip=set()
        self.param = param
        self. exclusions = exclusions
    
    def find_module(self, fullname, path = None):
        if fullname in self._skip:
            return None
        self._skip.add(fullname)
        return PostImportLoader(self, self.param, self.exclusions)


class PostImportLoader:
    def __init__(self, finder, param, exclusions):
        self._finder = finder
        self.param = param
        self.exclusions = exclusions
        
    
    def load_module(self, fullname):
       # print(fullname)
        importlib.import_module(fullname)
        module = sys.modules[fullname]
        if self.param.search(fullname) is not None :
           # for ex in self.exclusions:
            #    if ex.match(fullname):
             #       return
            decorate_members(module)
        self._finder._skip.remove(fullname)
        return module
