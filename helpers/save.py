import pickle as cPickle
from helpers.logHelper import logger
import classes.paper_trade_class


def save(e, name):
    try:
        with open("userdata/" + name + ".pickle", "wb") as output_file:
            cPickle.dump(e, output_file)
            print("Saved!")
    except Exception as e:
        logger.warning(e)


# pickle_file will be closed at this point, preventing your from accessing it any further
def load(name):
    try:
        with open("userdata/" + name + ".pickle", "rb") as input_file:
            e = cPickle.load(input_file)
            print(e)
            print("Loaded!")
            return e
    except Exception as e:
        logger.warning(e)
