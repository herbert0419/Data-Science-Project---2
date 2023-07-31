import sys
from ANPR.src.ANPR.exception import CustomException
from ANPR.src.ANPR.logger import logging

def test():
    try:
        logging.info("Testing our logging module")
        x = 1/0
    except Exception as e:
        raise CustomException(e,sys)
    
if __name__=="__main__":
    try:
        test()
    except Exception as e:
        print(e)