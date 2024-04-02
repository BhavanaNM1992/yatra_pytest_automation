import logging
logging.basicConfig(level=logging.DEBUG, filename="demologs.log", filemode="w",
                     format='%(asctime)s-%(levelname)s:%(message)s %(name)s')


logging.info("hey bhavana")
logging.error("ksjd")
logging.critical("hello")
