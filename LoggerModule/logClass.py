import logging as lg

class loggerClass:
    def __init__(self,opType):
        self.__opType = opType
        logger = lg.getLogger()
        fhandler = lg.FileHandler(filename=str(opType)+'_Operation.log', mode='a')
        formatter = lg.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(lg.INFO)
     
    def logFunc(self,lg_type,content):
        if lg_type == "INFO":
            lg.info(str(self.__opType) + str("_Operation - ") + str(content))
        elif lg_type == "ERROR":
            lg.error(str(self.__opType) + str("_Operation - ") + str(content))
        else:
            lg.info(str(self.__opType) + str("_Operation - ") + str(content))