from senesor.exception import SensorException
import sys
from senesor.logger import logging
def test_exception():
    try:
        logging.info("yaha pr error hai")
        a=1/0
    except Exception as e:
        raise SensorException(e,sys)


if __name__=="__main__":
    try:
        test_exception()
    except Exception as e:
        print(e)