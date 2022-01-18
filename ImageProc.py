import cv2, numpy

# 从source图片中查找wanted图片所在的位置，当置信度大于accuracy时返回找到的最大置信度位置的左上角坐标
def locate(source, wanted, accuracy=0.90):
    screen_cv2 = cv2.imread(source)
    wanted_cv2 = cv2.imread(wanted)

    result = cv2.matchTemplate(screen_cv2, wanted_cv2, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= accuracy:
        return max_loc
    else:
        return None

# 从source图片中查找wanted图片所在的位置，当置信度大于accuracy时返回找到的所有位置的左上角坐标（自动去重）
def locate_all(source, wanted, accuracy=0.90):
    loc_pos = []
    screen_cv2 = cv2.imread(source)
    wanted_cv2 = cv2.imread(wanted)

    result = cv2.matchTemplate(screen_cv2, wanted_cv2, cv2.TM_CCOEFF_NORMED)
    location = numpy.where(result >= accuracy)

    ex, ey = 0, 0
    for pt in zip(*location[::-1]):
        x = pt[0]
        y = pt[1]

        if (x - ex) + (y - ey) < 15:  # 去掉邻近重复的点
            continue
        ex, ey = x, y

        loc_pos.append([int(x), int(y)])


    return loc_pos

# 给定目标尺寸大小和目标左上角顶点坐标，即可给出目标中心的坐标
def centerOfTouchArea(wantedSize, topLeftPos):
    tlx, tly = topLeftPos
    h_src, w_src, tongdao = wantedSize
    if tlx < 0 or tly < 0 or w_src <=0 or h_src <= 0:
        return None
    return (tlx + w_src/2, tly + h_src/2)