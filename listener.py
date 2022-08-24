import sys
import time
import ngrok
import threading
from event import NewEvent, TUNNEL_CLOSED, TUNNEL_OPENED

_last_list = []
_run = True


def _work(token: str, callback):
    global _last_list, _run
    client: ngrok.Client = ngrok.Client(token)
    while _run:
        current_ls = list(client.tunnels.list())
        if len(current_ls) > len(_last_list):
            for i in range(1, len(current_ls) - len(_last_list) + 1):
                callback(NewEvent(TUNNEL_OPENED, current_ls[-i]))
            _last_list = current_ls.copy()
        elif len(current_ls) < len(_last_list):
            for i in range(1, len(_last_list) - len(current_ls) + 1):
                callback(NewEvent(TUNNEL_CLOSED, _last_list[-i]))
            _last_list = current_ls.copy()
        time.sleep(1)
    sys.exit()


def start_listener(token: str, callback):
    thr = threading.Thread(target=_work, kwargs={'token': token, 'callback': callback})
    thr.start()


def stop_listener():
    global _run
    _run = False
