# from config import app
# from Routes.TrackRoutes import *
# from HelperFunctions import *
# from ErrorHandler import *

# -- TEST SOL 1 --

# from multiprocessing import Process
# import psutil
# import pytest
# import requests
# import time
# import uvicorn

# HOST = "127.0.0.1"
# PORT = 8765
# WORKERS = 3

# def run_server(host: str, port: int, workers: int, wait: int = 15) -> Process:
#     proc = Process(
#         target=uvicorn.run,
#         args=("main:app",),
#         kwargs={
#             "host": host,
#             "port": port,
#             "workers": workers,
#         },
#     )
#     proc.start()
#     time.sleep(wait)
#     assert proc.is_alive()
#     return proc

# def shutdown_server(proc: Process):

#     ##### SOLUTION #####
#     pid = proc.pid
#     parent = psutil.Process(pid)
#     for child in parent.children(recursive=True):
#         child.kill()
#     ##### SOLUTION END ####

#     proc.terminate()
#     for _ in range(5):
#         if proc.is_alive():
#             time.sleep(5)
#         else:
#             return
#     else:
#         raise Exception("Process still alive")

# def check_response(host: str, port: int):
#     assert requests.get(f"http://{host}:{port}").text == '"OK"'


# def check_response_time(host: str, port: int, tol: float = 1e-2):
#     s = time.time()
#     requests.get(f"http://{host}:{port}")
#     e = time.time()
#     assert e-s < tol

# @pytest.fixture(scope="session")
# def server():
#     proc = run_server(HOST, PORT, WORKERS)
#     try:
#         yield
#     finally:
#         shutdown_server(proc)

# def test_main(server):
#     check_response(HOST, PORT)
#     check_response_time(HOST, PORT)
#     check_response(HOST, PORT)
#     check_response_time(HOST, PORT)

# -- TEST SOL 2 --
from multiprocessing import Process
from multiprocessing.pool import ApplyResult
import uvicorn

# global process variable
proc = None

def run(): 
    """
    This function to run configured uvicorn server.
    """
    uvicorn.run(app="main:app", host="127.0.0.1", port=8765)


def start():
    """
    This function to start a new process (start the server).
    """
    global proc
    # create process instance and set the target to run function.
    # use daemon mode to stop the process whenever the program stopped.
    proc = Process(target=run, args=(), daemon=True)
    proc.start()


def stop(): 
    """
    This function to join (stop) the process (stop the server).
    """
    global proc
    # check if the process is not None
    if proc: 
        # join (stop) the process with a timeout setten to 0.25 seconds.
        # using timeout (the optional arg) is too important in order to
        # enforce the server to stop.
        proc.join(0.25)