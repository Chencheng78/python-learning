import queue
import re
import sys
import threading
from events import Events
from tkinter import Tk, Label, EventType, Button

import adbutils
import uiautomator2
import websocket
from PIL import Image, ImageTk
from imageio import imread

if sys.platform == 'win32':
    try:
        import ctypes

        PROCESS_SYSTEM_DPI_AWARE = 1
        # noinspection SpellCheckingInspection
        ctypes.OleDLL('shcore').SetProcessDpiAwareness(PROCESS_SYSTEM_DPI_AWARE)
    except (ImportError, AttributeError, OSError):
        pass

stop = threading.Event()
q = queue.Queue(maxsize=1)

tk = Tk()
tk.wm_title("Android Screen")
label = Label(tk)
label.pack_configure(fill="both")
label.grid(row=0)


def on_click_home():
    adb.keyevent(3)


def on_click_back():
    adb.keyevent(4)


button_home = Button(tk, text='Home', command=on_click_home)
button_home.grid(row=1, column=1, sticky='NSEW')
button_back = Button(tk, text='<', command=on_click_back)
button_back.grid(row=1, column=0, sticky='NSEW')

adb = adbutils.AdbClient(host="127.0.0.1", port=5037).device()
wm_size = adb.window_size()
scaling = max(wm_size.height, wm_size.width) / 800
current_size = (800, wm_size.height // scaling) if wm_size.width > wm_size.height else (wm_size.width // scaling, 800)
press_point = [0, 0]
release_point = [0, 0]


def mouse_press(coords):
    global press_point
    press_point = coords


def mouse_release(coords):
    global press_point, release_point
    release_point = coords
    if abs(release_point[0] - press_point[0]) > 10 or abs(release_point[1] - press_point[1]) > 10:
        print('swipe')
        adb.swipe(press_point[0] * scaling, press_point[1] * scaling, release_point[0] * scaling, release_point[1] * scaling)
    else:
        print('click')
        adb.click(release_point[0] * scaling, release_point[1] * scaling)


def mouse_wheel(direction):
    print(f'in mouse_wheeling: {direction}')
    mid_point = [wm_size.width // 2, wm_size.height // 2]
    if direction == 'up':
        start_point = [mid_point[0], mid_point[1] - 300]
        end_point = [mid_point[0], mid_point[1] + 300]
    else:
        start_point = [mid_point[0], mid_point[1] + 300]
        end_point = [mid_point[0], mid_point[1] - 300]
    adb.swipe(start_point[0], start_point[1], end_point[0], end_point[1], 2.0)


e = Events()
e.on_press += mouse_press
e.on_release += mouse_release
e.on_wheeling += mouse_wheel


def mouse_handler(event):
    if event.x > current_size[0] or event.y > current_size[1]:
        return
    if event.type == EventType.ButtonPress:
        start_point = [event.x, event.y]
        print(start_point)
        e.on_press(start_point)
    elif event.type == EventType.ButtonRelease:
        end_point = [event.x, event.y]
        print(end_point)
        e.on_release(end_point)
    elif event.type == EventType.MouseWheel:
        if event.delta > 0:
            e.on_wheeling('up')
        else:
            e.on_wheeling('down')


label.bind("<ButtonRelease-1>", mouse_handler)
label.bind("<Button-1>", mouse_handler)
label.bind("<MouseWheel>", mouse_handler)


def cast_android_screen():
    try:
        print("等待Android设备...")
        adbutils.adb.wait_for(transport="usb")
    except TimeoutError:
        return
    try:
        d = uiautomator2.connect()
        print("Android设备", d.serial)
        screenshot = d.screenshot()
        print("屏幕尺寸", screenshot.size)
        scale = max(screenshot.width, screenshot.height) / 800
        print("屏幕缩放比率", scale)
        img = screenshot.resize((int(screenshot.width / scale), int(screenshot.height / scale)))
        print("缩放后尺寸", img.size)
        q.put(img)
    except RuntimeError:
        return
    except Exception as e:
        print(type(e))
        print(e)
        return
    while not stop.is_set():
        try:
            http_url = d.path2url("/minicap")
            ws_url = re.sub("^http", "ws", http_url)
            ws = websocket.create_connection(ws_url)
            try:
                while not stop.is_set():
                    msg = ws.recv()
                    if isinstance(msg, bytes):
                        arr = imread(msg)
                        img = Image.fromarray(arr)
                        q.put(img)
            finally:
                ws.close()
        except Exception as e:
            print(type(e))
            print(e)
            break


def show_android_screen():
    while True:
        try:
            img = q.get(timeout=0.04)
            image = ImageTk.PhotoImage(img)
            label["image"] = image
            if not hasattr(label, "image"):
                tk.update()
                sw, sh = tk.winfo_screenwidth(), tk.winfo_screenheight()
                w, h = tk.winfo_width(), tk.winfo_height()
                x, y = (sw - w) // 2, (sh - h) // 2
                print(sw, sh, x, y, w, h)
                geometry = f"{w}x{h}+{x}+{y}"
                tk.wm_geometry(geometry)
            label.image = image
        except (RuntimeError, queue.Empty):
            pass
        except Exception as e:
            print(type(e))
            print(e)


th1 = threading.Thread(target=cast_android_screen, daemon=True)
th1.start()

th2 = threading.Thread(target=show_android_screen, daemon=True)
th2.start()



tk.mainloop()

stop.set()
th1.join(0.5)
th2.join(0.5)
