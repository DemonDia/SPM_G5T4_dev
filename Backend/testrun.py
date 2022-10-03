from multiprocessing import Process
from Backend.main import *
server = Process(target=app.run)
server.start()
server.terminate()
