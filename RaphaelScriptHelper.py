import ImageProc, ADBHelper, random, time, cv2
import settings as st

deviceType = 1
deviceID = ""

def random_delay():
    t = random.uniform(st.randomDelayMin, st.randomDelayMax)
    print("【随机延时】将随机延时 {0} 秒".format(t))
    time.sleep(t)

def delay(t):
    print("【主动延时】延时 {0} 秒".format(t))
    time.sleep(t)

def random_pos(pos):
    x, y = pos
    rand = random.randint(1, 10000)
    if rand % 2 == 0:
        x = x + random.randint(0, st.touchPosRange)
    else:
        x = x - random.randint(0, st.touchPosRange)

    rand = random.randint(1, 10000)
    if rand % 2 == 0:
        y = y + random.randint(0, st.touchPosRange)
    else:
        y = y - random.randint(0, st.touchPosRange)

    return (x, y)

# 智能模拟点击某个点，将会随机点击以这个点为中心一定范围内的某个点，并随机按下时长
def touch(pos):
    randTime = random.randint(0, st.touchDelayRange)
    _pos = random_pos(pos)
    print("【模拟点击】点击坐标 {0} {1} 毫秒".format(_pos, randTime))
    if randTime < 10:
        ADBHelper.touch(deviceID, _pos)
    else:
        ADBHelper.longTouch(deviceID, _pos, randTime)

# 智能模拟滑屏，给定起始点和终点的二元组，模拟一次随机智能滑屏
def slide(vector):
    startPos, stopPos = vector
    _startPos = random_pos(startPos)
    _stopPos = random_pos(stopPos)
    randTime = random.randint(st.slideMinVer, st.slideMaxVer)
    print("【模拟滑屏】使用 {0} 毫秒从坐标 {1} 滑动到坐标 {2}".format(randTime, _startPos, _stopPos))
    ADBHelper.slide(deviceID, _startPos, _stopPos, randTime)

# 截屏，识图，返回坐标
def find_pic(target, returnCenter = False):
    ADBHelper.screenCapture(deviceID, st.cache_path + "screenCap.png")
    time.sleep(0.1)
    if returnCenter == True:
        leftTopPos = ImageProc.locate(st.cache_path + "screenCap.png", target, st.accuracy)
        img = cv2.imread(target)
        centerPos = ImageProc.centerOfTouchArea(img.shape, leftTopPos)
        return centerPos
    else:
        leftTopPos = ImageProc.locate(st.cache_path + "screenCap.png", target, st.accuracy)
        return leftTopPos

# 截屏，识图，返回所有坐标
def find_pic_all(target):
    ADBHelper.screenCapture(deviceID, st.cache_path + "screenCap.png")
    time.sleep(0.1)
    leftTopPos = ImageProc.locate_all(st.cache_path + "screenCap.png", target, st.accuracy)
    return leftTopPos

# 寻找目标区块并在其范围内随机点击
def find_pic_touch(target):
    leftTopPos = find_pic(target)
    if leftTopPos is None:
        print("【识图】识别 {0} 失败".format(target))
        return False
    print("【识图】识别 {0} 成功，图块左上角坐标 {1}".format(target, leftTopPos))
    img = cv2.imread(target)
    tlx, tly = leftTopPos
    h_src, w_src, tongdao = img.shape
    x = random.randint(tlx, tlx + w_src)
    y = random.randint(tly, tly + h_src)
    touch((x, y))
    return True

# 寻找目标区块并将其拖动到某个位置
def find_pic_slide(target,pos):
    leftTopPos = find_pic(target)
    if leftTopPos is None:
        print("【识图】识别 {0} 失败".format(target))
        return False
    print("【识图】识别 {0} 成功，图块左上角坐标 {1}".format(target, leftTopPos))
    img = cv2.imread(target)
    centerPos = ImageProc.centerOfTouchArea(img.shape,leftTopPos)
    slide((centerPos, pos))
    return True