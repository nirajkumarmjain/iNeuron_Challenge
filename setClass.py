from LoggerModule import logClass

class Set:
    def __init__(self,data):
        self.__data = data
        self.__lg = logClass.loggerClass("Set")
        self.__lg.logFunc("INFO","New Set Object Created: "+str(data))
    
    def __str__(self):
        return str(self.__data)
        
    def add(self,newData):
        """Function to add data into Set. 
        While using the function provide new data to add to Set."""
        self.__lg.logFunc("INFO","Using add function of Set - Start")
        self.__lg.logFunc("INFO","Set Data before add: "+str(self.__data))
        try:
            self.__data.add(newData)
            self.__lg.logFunc("INFO","Set Data After add: "+str(self.__data))
            self.__lg.logFunc("INFO","Using add function of Set - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def clear(self):
        """Function to Clear Set Data."""
        self.__lg.logFunc("INFO","Using clear function of Set - Start")
        self.__lg.logFunc("INFO","Set Data before Clear: "+str(self.__data))
        try:
            self.__data.clear()
            self.__lg.logFunc("INFO","Set Data After Clear: "+str(self.__data))
            self.__lg.logFunc("INFO","Using clear function of Set - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def copy(self):
        """Function to Create a Copy of Set Data. You Can access the new Set from your object using newSet attribute"""
        self.__lg.logFunc("INFO","Using Copy function of Set - Start")
        try:
            self.newSet = self.__data.copy()
            self.__lg.logFunc("INFO","New Set Created (newSet) : "+str(self.newSet))
            self.__lg.logFunc("INFO","Using Copy function of Set - End")
            return self.newSet
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def pop(self):
        """Function to Pop an element from Set. 
        While using the function provide index of the element that needs to be popped from Set.Default index=-1"""
        self.__lg.logFunc("INFO","Using Pop function of Set - Start")
        self.__lg.logFunc("INFO","Set Data before Pop: "+str(self.__data))
        try:
            p = self.__data.pop()
            self.__lg.logFunc("INFO","Set Data After Pop: "+str(self.__data))
            self.__lg.logFunc("INFO","Using Pop function of Set - End")
            return p
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def discard(self,value):
        """Function to discard an element from Set. 
        While using the function provide value of the element that needs to be discard from Set.First Occurence of value removed"""
        self.__lg.logFunc("INFO","Using discard function of Set - Start")
        self.__lg.logFunc("INFO","Set Data before discard: "+str(self.__data))
        try:
            self.__data.discard(value)
            self.__lg.logFunc("INFO","Set Data After discard: "+str(self.__data))
            self.__lg.logFunc("INFO","Using discard function of Set - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def remove(self,value):
        """Function to Remove an element from Set. 
        While using the function provide value of the element that needs to be removed from Set.First Occurence of value removed"""
        self.__lg.logFunc("INFO","Using Remove function of Set - Start")
        self.__lg.logFunc("INFO","Set Data before Remove: "+str(self.__data))
        try:
            self.__data.remove(value)
            self.__lg.logFunc("INFO","Set Data After Remove: "+str(self.__data))
            self.__lg.logFunc("INFO","Using Remove function of Set - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)