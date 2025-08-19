import logging

logger = logging.getLogger("myapp")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("app.log")  
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)
