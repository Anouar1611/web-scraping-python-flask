from abc import ABCMeta, abstractmethod

class CRUDInterface():
    __metaclass__ = ABCMeta                                                     

    @abstractmethod
    def select(self):
        pass
    
    @abstractmethod
    def selectWhereURL(self):
        pass

    @abstractmethod
    def insert(self):
        pass

    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def create(self):
        pass
    