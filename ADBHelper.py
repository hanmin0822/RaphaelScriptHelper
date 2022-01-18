import os, time

# 获取设备列表，每一个为deviceID
def getDevicesList():
    content = os.popen('adb devices').read()
    if "daemon not running" in content:
        content = os.popen('adb devices').read()
    row_list = content.split('List of devices attached\n')[1].split('\n')
    devices_list = [i for i in row_list if len(i) > 1]
    res = []
    for d in devices_list:
        res.append(d.split('\t')[0])
    return res

# 杀死ADB进程
def killADBServer():
    os.system("adb kill-server")

# 设备屏幕截图，需给定did和本机截图保存路径
def screenCapture(deviceID, capPath):
    a = "adb -s " + deviceID + " shell screencap -p sdcard/adb_screenCap.png"
    b = "adb pull sdcard/adb_screenCap.png " + capPath
    for row in [a, b]:
        time.sleep(0.1)
        os.system(row)
    if os.path.exists(capPath) == True:
        return True
    else:
        return False

# 模拟点击屏幕，参数pos为目标坐标(x, y)
def touch(deviceID, pos):
    x, y = pos
    a = "adb -s " + deviceID + " shell input touchscreen tap {0} {1}".format(x, y)
    os.system(a)

# 模拟滑动屏幕，posStart为起始坐标(x, y)，posStop为终点坐标(x, y)，time为滑动时间
def slide(deviceID, posStart, posStop, time):
    x1, y1 = posStart
    x2, y2 = posStop
    a = "adb -s " + deviceID + " shell input swipe {0} {1} {2} {3} {4}".format(x1, y1, x2, y2, time)
    os.system(a)

# 模拟长按屏幕，参数pos为目标坐标(x, y)，time为长按时间
def longTouch(deviceID, pos, time):
    x, y = pos
    a = "adb -s " + deviceID + " shell input swipe {0} {1} {2} {3} {4}".format(x, y, x, y, time)
    os.system(a)
