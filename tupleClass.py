from LoggerModule import logClass

class Tuple:
    def __init__(self,data):
        self.__data = data
        self.__lg = logClass.loggerClass("Tuple")
        self.__lg.logFunc("INFO","New Tupe Object Created: "+str(data))
    
    def __str__(self):
        return str(self.__data)
    
    def count(self,value):
        """Function to Find Count of Particular Value in the Tuple. 
        While using the function provide value for which count needs to be found."""
        self.__lg.logFunc("INFO","Using Count function of Tuple - Start")
        try:
            c = self.__data.count(value)
            self.__lg.logFunc("INFO","Found "+str(self.__data.count(value)) + " Occurences in the Tuple " + str(self.__data))
            self.__lg.logFunc("INFO","Using Count function of Tuple - End")
            return c
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
                       
    def index(self,idx_value):
        """Function to Find First Index of Particular Value in the Tuple. 
        While using the function provide value for which index needs to be found."""
        self.__lg.logFunc("INFO","Using Index function of Tuple - Start")
        try:
            i = self.__data.index(idx_value)
            self.__lg.logFunc("INFO","Found "+str(idx_value) + " at position "+ str(i) + " in the Tuple ")
            self.__lg.logFunc("INFO","Using Index function of Tuple - End")
            return i
        except Exception as e:
            self.__lg.logFunc("ERROR",e)