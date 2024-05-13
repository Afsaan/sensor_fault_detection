from sensor.exception import SensorException
from sensor.logger import logging
import sys

def test_exception():
    try:
        a = 1/0
    except Exception as e:
        raise SensorException(e, sys)

if __name__ == "__main__":
    try:
        logging.info("error purposly thrown here")
    except Exception as e:
        print(e)