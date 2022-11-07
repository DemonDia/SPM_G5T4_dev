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
import logging
from fastapi import FastAPI

class App:
    """ Core application to test. """

    def __init__(self):
        self.api = FastAPI()
        # register endpoints
        self.api.get("/")(self.read_root)
        self.api.on_event("shutdown")(self.close)

    async def close(self):
        """ Gracefull shutdown. """
        logging.warning("Shutting down the app.")

    async def read_root(self):
        """ Read the root. """
        return {"Hello": "World"}

""" Testing part."""
from multiprocessing import Process
import asynctest
import asyncio
import aiohttp
import uvicorn

class TestApp(asynctest.TestCase):
    """ Test the app class. """

    async def setUp(self):
        """ Bring server up. """
        app = App()
        self.proc = Process(target=uvicorn.run,
                            args=(app.api,),
                            kwargs={
                                "host": "127.0.0.1",
                                "port": 5000,
                                "log_level": "info"},
                            daemon=True)
        self.proc.start()
        await asyncio.sleep(0.1)  # time for the server to start

    async def tearDown(self):
        """ Shutdown the app. """
        self.proc.terminate()

    async def test_read_root(self):
        """ Fetch an endpoint from the app. """
        async with aiohttp.ClientSession() as session:
            async with session.get("http://127.0.0.1:5000/") as resp:
                data = await resp.json()
        self.assertEqual(data, {"Hello": "World"})