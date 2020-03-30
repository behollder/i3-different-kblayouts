import i3ipc
from subprocess import call
import subprocess
import threading
from threading import Thread, Event

windows = {}
default = "us"
event = Event()

i3 = i3ipc.Connection()


def get_win_id(i3):
    return i3.get_tree().find_focused().id


def get_cur_lay():
    curlay = subprocess.Popen(
        "xkb-switch", stdout=subprocess.PIPE).stdout.read()[:-1]
    return curlay.decode("utf-8")


def on_focus(i3, e):
    id = get_win_id(i3)
    cur_lay = get_cur_lay()
    lay = windows.get(id, default)
    if not cur_lay == lay:
        event.set()
        subprocess.call(["xkb-switch", "-n"])
        windows[id] = get_cur_lay()


def on_close(i3, e):
    windows.pop(e.container.id)


class LayoutListener(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

    def run(self):
        while True:
            subprocess.call(["xkb-switch", "-w"])
            if not event.is_set():
                windows[get_win_id(i3)] = get_cur_lay()
            event.clear()


LayoutListener()
i3.on("window::focus", on_focus)
i3.on("window::close", on_close)
i3.main()
