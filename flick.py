"""
flick.py Library
~~~~~~~~~~~~~~~~~~~~~
Modern minimalist python 3+ pocket knife.

Basic example usage:
   >>> import flick as f
   >>> urls = ['https://google.com/humans.txt', 'https://twitter.com/robots.txt']
   >>> def fetch_that(url):
        print(requests.get(url).text)
   >>> f.together(fetch_that, urls), {
        'tasks': 2, // how many tasks to run together?
        'done': lambda x: print('Done fetching!')
        })
    ...url contents...
    Done fetching!

"""
import time
import base64
import multiprocessing
import json as jsonlib
from typing import Callable, List, Any, Dict


def _is_byte(data):
    return isinstance(data, (bytes, bytearray))


def b64(data):
    data = data if _is_byte(data) else b(data)
    return s(base64.b64encode(data))


def b64d(data):
    return s(base64.b64decode(data))


def s(data: Any):
    """s - convert anything possible to a string.
    
    Arguments:
        data {[Any]} -- What you want to convert
    
    Returns:
        str -- the data as a string
    """
    if not isinstance(data, (list, dict)):
        if _is_byte(data):
            return data.decode("utf-8")
        string = str(data)
        return string
    try:
        return json(data)
    except jsonlib.JSONDecodeError:
        return data.decode("utf-8")


def b(data):
    return data.encode("utf-8")


def json(obj: Any, bytes=False) -> str:
    jsoned = jsonlib.dumps(obj, ensure_ascii=False).encode("utf8")
    if bytes:
        return jsoned
    return s(jsoned)


def jsond(obj: Any) -> str:
    return jsonlib.loads(obj, ensure_ascii=False).decode("utf8")


def together(worker: Callable, args: List, options: Dict[str, Any]):
    """
    Run a function concurrently.

    TODO: If IO bound use multiprocessing.dummy (threading)
    """
    DEFAULT_TASKS_COUNT = 4
    # Let's find if we can use multiprocessing
    cpu_count = multiprocessing.cpu_count()

    if cpu_count < 2:
        raise Exception("Please run together with more than 1 cpu.")

    tasks_count = min(options.get("tasks", DEFAULT_TASKS_COUNT), cpu_count)
    with multiprocessing.Pool(tasks_count) as p:
        p.map(worker, args)


def timeit(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"It took {end - start}s to run {func.__name__}")

    return wrapper

def get_time(func):
    start = time.time()
    func()
    end = time.time()
    return end - start