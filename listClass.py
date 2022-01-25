from LoggerModule import logClass

class List:
    def __init__(self,data):
        self.__data = data
        self.__lg = logClass.loggerClass("List")
        self.__lg.logFunc("INFO","New List Object Created: "+str(data))
    
    def __str__(self):
        return str(self.__data)
        
    def append(self,newData):
        """Function to append data into List. 
        While using the function provide new data to append to list."""
        self.__lg.logFunc("INFO","Using append function of List - Start")
        self.__lg.logFunc("INFO","List Data before Append: "+str(self.__data))
        try:
            self.__data.append(newData)
            self.__lg.logFunc("INFO","List Data After Append: "+str(self.__data))
            self.__lg.logFunc("INFO","Using append function of List - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def clear(self):
        """Function to Clear List Data."""
        self.__lg.logFunc("INFO","Using clear function of List - Start")
        self.__lg.logFunc("INFO","List Data before Clear: "+str(self.__data))
        try:
            self.__data.clear()
            self.__lg.logFunc("INFO","List Data After Clear: "+str(self.__data))
            self.__lg.logFunc("INFO","Using clear function of List - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def copy(self):
        """Function to Create a Copy of List Data. You Can access the new list from your object using newList attribute"""
        self.__lg.logFunc("INFO","Using Copy function of List - Start")
        try:
            self.newList = self.__data.copy()
            self.__lg.logFunc("INFO","New List Created (newList) : "+str(self.newList))
            self.__lg.logFunc("INFO","Using Copy function of List - End")
            return self.newList
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def count(self,value):
        """Function to Find Count of Particular Value in the List. 
        While using the function provide value for which count needs to be found."""
        self.__lg.logFunc("INFO","Using Count function of List - Start")
        try:
            c = self.__data.count(value)
            self.__lg.logFunc("INFO","Found "+str(self.__data.count(value)) + " Occurences in the list " + str(self.__data))
            self.__lg.logFunc("INFO","Using Count function of List - End")
            return c
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def extend(self,newData):
        """Function to Extend data into List. 
        While using the function provide new data to extend/add to list."""
        self.__lg.logFunc("INFO","Using extend function of List - Start")
        self.__lg.logFunc("INFO","List Data before extend: "+str(self.__data))
        try:
            self.__data.extend(newData)
            self.__lg.logFunc("INFO","List Data After extend: "+str(self.__data))
            self.__lg.logFunc("INFO","Using extend function of List - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def index(self,idx_value):
        """Function to Find First Index of Particular Value in the List. 
        While using the function provide value for which index needs to be found."""
        self.__lg.logFunc("INFO","Using Index function of List - Start")
        try:
            i = self.__data.index(idx_value)
            self.__lg.logFunc("INFO","Found "+str(idx_value) + " at position "+ str(i) + " in the list ")
            self.__lg.logFunc("INFO","Using Index function of List - End")
            return i
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
                       
    def insert(self,index,newData):
        """Function to Insert data into List. 
        While using the function provide index and new data to insert to list."""
        self.__lg.logFunc("INFO","Using Insert function of List - Start")
        self.__lg.logFunc("INFO","List Data before extend: "+str(self.__data))
        try:
            self.__data.insert(index,newData)
            self.__lg.logFunc("INFO","List Data After Insert: "+str(self.__data))
            self.__lg.logFunc("INFO","Using Insert function of List - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def pop(self,index=-1):
        """Function to Pop an element from List. 
        While using the function provide index of the element that needs to be popped from list.Default index=-1"""
        self.__lg.logFunc("INFO","Using Pop function of List - Start")
        self.__lg.logFunc("INFO","List Data before Pop: "+str(self.__data))
        try:
            p = self.__data.pop(index)
            self.__lg.logFunc("INFO","List Data After Pop: "+str(self.__data))
            self.__lg.logFunc("INFO","Using Pop function of List - End")
            return p
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def remove(self,value):
        """Function to Remove an element from List. 
        While using the function provide value of the element that needs to be removed from list.First Occurence of value removed"""
        self.__lg.logFunc("INFO","Using Remove function of List - Start")
        self.__lg.logFunc("INFO","List Data before Remove: "+str(self.__data))
        try:
            self.__data.remove(value)
            self.__lg.logFunc("INFO","List Data After Remove: "+str(self.__data))
            self.__lg.logFunc("INFO","Using Remove function of List - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def reverse(self):
        """Function to Reverse elements in the List."""
        self.__lg.logFunc("INFO","Using Reverse function of List - Start")
        self.__lg.logFunc("INFO","List Data before Reverse: "+str(self.__data))
        try:
            self.__data.reverse()
            self.__lg.logFunc("INFO","List Data After Reverse: "+str(self.__data))
            self.__lg.logFunc("INFO","Using Reverse function of List - End")
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)
            
    def sort(self,reverse=False):
        """Function to Sort elements in the List."""
        self.__lg.logFunc("INFO","Using Sort function of List - Start")
        self.__lg.logFunc("INFO","List Data before Sort: "+str(self.__data))
        try:
            if reverse == False:
                self.__data.sort()
                self.__lg.logFunc("INFO","List Data After Sort: "+str(self.__data))
                self.__lg.logFunc("INFO","Using Sort function of List - End")
            elif reverse == True:
                self.__data.sort(reverse=True)
                self.__lg.logFunc("INFO","List Data After Sort: "+str(self.__data))
                self.__lg.logFunc("INFO","Using Sort function of List - End")
            else:
                raise Exception
                self.__lg.logFunc("ERROR",e)
            return self.__data
        except Exception as e:
            self.__lg.logFunc("ERROR",e)