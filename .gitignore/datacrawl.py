import json
import time
from queue import Queue
from threading import Thread as T, Lock as L

url = "https://desolate-ravine-43301.herokuapp.com"

class Threads(T):
    def __init__(self, myq, h):
        T.__init__(self)
        self.myq = myq
        self.headers = h

    def run(self):
        while True:
            with L():
                response = request(self.myq.get(), self.headers, self.name)
            self.myq.task_done()
class Requests(object):
    def __init__(self,url):


