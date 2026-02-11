import base64  # noqa: F401 # Unused import again?

import win32api  # ty:ignore[unresolved-import]
import win32con
import win32gui  # ty:ignore[unresolved-import]
import win32ui  # ty:ignore[unresolved-import]


def get_dimensions():
    width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
    height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
    left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
    top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

    return (width, height, left, top)


def screenshot(name="screenshot"):
    hdesktop = win32gui.GetDesktopWindow()
    width, height, left, top = get_dimensions()

    desktop_dc = win32gui.GetWindowDC(hdesktop)  # DC = Device Context
    img_dc = win32ui.CreateDCFromHandle(desktop_dc)
    mem_dc = img_dc.CreateCompatibleDC()

    screenshot = win32ui.CreateBitmap()
    screenshot.CreateCompatibleBitmap(img_dc, width, height)
    mem_dc.SelectObject(screenshot)
    # BitBlt() makes a bit-for-bit copy; a memcompy for GDI objects
    mem_dc.BitBlt((0, 0), (width, height), img_dc, (left, top), win32con.SRCCOPY)
    screenshot.SaveBitmapFile(mem_dc, f"{name}.bmp")

    mem_dc.DeleteDC()
    win32gui.DeleteObject(screenshot.GetHandle())


def run():
    screenshot()
    with open("screenshot.bmp") as f:
        img = f.read()
    return img


if __name__ == "__main__":
    screenshot()
