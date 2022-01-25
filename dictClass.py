from LoggerModule import logClass

class Dict:
    def __init__(self,data):
        self.__data = data
        self.__lg = logClass.loggerClass("Dict")
        self.__lg.logFunc("INFO","New Dict Object Created: "+str(data))
    
    def __str__(self):
        return str(self.__data)
                
    def clear(self):
        """Function to Clear Dict Data."""
        self.__lg.logFunc("INFO","Using clear function of Dict - Start")
        self.__lg.logFunc("INFO","Dict Data before Clear: "+str(self.__data))
        try:
            self.__data.clear()
            self.__lg.logFunc("INFO","Dict Data After Clear: "+str(self.__data))
            self.__lg.logFunc("INFO","Using clear function of Dict - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def copy(self):
        """Function to Create a Copy of Dict Data. You Can access the new Dict from your object using newDict attribute"""
        self.__lg.logFunc("INFO","Using Copy function of Dict - Start")
        try:
            self.newDict = self.__data.copy()
            self.__lg.logFunc("INFO","New Dict Created (newDict) : "+str(self.newDict))
            self.__lg.logFunc("INFO","Using Copy function of Dict - End")
            return self.newDict
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def pop(self,key):
        """Function to Pop an element from Dict. 
        While using the function provide key of the element that needs to be popped from Dict."""
        self.__lg.logFunc("INFO","Using Pop function of Dict - Start")
        self.__lg.logFunc("INFO","Dict Data before Pop: "+str(self.__data))
        try:
            p = self.__data.pop(key)
            self.__lg.logFunc("INFO","Dict Data After Pop: "+str(self.__data))
            self.__lg.logFunc("INFO","Using Pop function of Dict - End")
            return p
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def fromkeys(self,iterable,value=None):
        """Function to create Dict from an iterable object. 
        While using the function provide iterable data to create to Dict."""
        self.__lg.logFunc("INFO","Using fromkeys function of Dict - Start")
        self.__lg.logFunc("INFO","Dict Data before fromkeys: "+str(self.__data))
        try:
            self.__data = self.__data.fromkeys(iterable,value)
            self.__lg.logFunc("INFO","Dict Data After fromkeys: "+str(self.__data))
            self.__lg.logFunc("INFO","Using fromkeys function of Dict - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def get(self,key):
        """Function to get value from Dict using key as input."""
        self.__lg.logFunc("INFO","Using Get function of Dict - Start")
        try:
            v = self.__data.get(key)
            self.__lg.logFunc("INFO","Value Extracted: "+str(v))
            self.__lg.logFunc("INFO","Using Get function of Dict - End")
            return v
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def items(self):
        """Function to get items from dictionary."""
        self.__lg.logFunc("INFO","Using items function of Dict - Start")
        try:
            item = self.__data.items()
            self.__lg.logFunc("INFO","Dict Data Extracted using items function: "+str(item))
            self.__lg.logFunc("INFO","Using items function of Dict - End")
            return item
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def keys(self):
        """Function to get keys from dictionary."""
        self.__lg.logFunc("INFO","Using keys function of Dict - Start")
        try:
            key = self.__data.keys()
            self.__lg.logFunc("INFO","Dict Data Extracted using keys function: "+str(key))
            self.__lg.logFunc("INFO","Using keys function of Dict - End")
            return key
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def values(self):
        """Function to get values from dictionary."""
        self.__lg.logFunc("INFO","Using values function of Dict - Start")
        try:
            value = self.__data.values()
            self.__lg.logFunc("INFO","Dict Data Extracted using values function: "+str(value))
            self.__lg.logFunc("INFO","Using values function of Dict - End")
            return value
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def popitem(self):
        """Function to Pop some element in key,value pair from Dict."""
        self.__lg.logFunc("INFO","Using Popitem function of Dict - Start")
        self.__lg.logFunc("INFO","Dict Data before Pop: "+str(self.__data))
        try:
            p = self.__data.popitem()
            self.__lg.logFunc("INFO","Popped " + str(p) + " from dictionary")
            self.__lg.logFunc("INFO","Dict Data After Pop: "+str(self.__data))
            self.__lg.logFunc("INFO","Using Popitem function of Dict - End")
            return p
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def setdefault(self,key,default=None):
        """Function to Insert a key to existing Dict Data with default value if not given"""
        self.__lg.logFunc("INFO","Using setdefault function of Dict - Start")
        self.__lg.logFunc("INFO","Dict Data before setdefault: "+str(self.__data))
        try:
            self.__data.setdefault(key,default)
            self.__lg.logFunc("INFO","Dict Data After setdefault: "+str(self.__data))
            self.__lg.logFunc("INFO","Using setdefault function of Dict - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def update(self,value):
        """Function to Update Dictionary using a iterable"""
        self.__lg.logFunc("INFO","Using update function of Dict - Start")
        self.__lg.logFunc("INFO","Dict Data before update: "+str(self.__data))
        try:
            self.__data.update(value)
            self.__lg.logFunc("INFO","Dict Data After update: "+str(self.__data))
            self.__lg.logFunc("INFO","Using update function of Dict - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)