import logging

logger = logging.getLogger("NUUB_BOT_LOG")
hdlr = logging.FileHandler("NUUB_BOT.log")
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)
logger.info(
    "Initialised Logger Successfully\n----------------------------------- START OF SESSION"
)
