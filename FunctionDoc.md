# 功能使用文档
* [标点截取工具使用说明](#标点截取工具使用说明)

* [settings文件配置说明](#settings文件配置说明)

* [RaphaelScriptHelper](#RaphaelScriptHelper)

* [ImageProc 图片处理类](#ImageProc-图片处理类)

* [ADBHelper ADB助手类](#ADBHelper-ADB助手类)

<br/>

<br/>

## 标点截取工具使用说明
使用`CaptureMarkHelper.py`脚本

根据需要修改以下变量
```python
# 修改以下参数来运行

# 原图缩放比例，用于展示在窗口里
scale = 0.5

# 截图保存路径，以/结束
save_file_path = "./img/"

# py变量字典文件
pos_img_dict = "./testDict.py"

# 动作类型 1=截图  2=标点  3=标线（取起终点组成向量） 4=标记区域
action = 4

# 图片来源替换输入你的did
ADBHelper.screenCapture("did", "screen.png")
img_file = "./screen.png"
```

其中各个变量的解释如下：

* `scale`: 原图缩放比例，某些情况下需要标记或截图的图片尺寸很大，按照原图比例展示可能会超出屏幕边界，因此需要缩放，请根据实际情况填写此值，缩放比例仅作窗口展示用，不影响原图实际大小
* `save_file_path`: 截图保存路径，当`action`为1，即截图功能时，脚本将把截图保存在此路径下
* `pos_img_dict`: 变量字典文件，所有保存的图片路径名变量、点位置变量、向量变量等都以变量形式写入到此文件，之后只需要在其他脚本中引入此变量字典文件，就可以直接使用
* `action` : 脚本功能类型，相见功能说明
* `img_file`: 原图路径，如果需要ADB设备立即截图一张，可使用[screenCapture](#screenCapture)方法立即截图，并取截图结果

**功能说明**

* 1: 截图，在原图中按下鼠标左键并拖动鼠标，勾选出需要截图的区域，松开鼠标左键完成框选，点击鼠标滚轮（鼠标中键）预览截图效果，点击鼠标右键确认结果，在弹出的输入框中输入变量名并完成变量创建
* 2: 标点，在原图中单击鼠标左键，在图片上标记一个点，左上角显示点位置，点击鼠标右键确认结果，在弹出的输入框中输入变量名并完成变量创建
* 3: 标线，在原图中按下鼠标左键并拖动鼠标，画直线，松开鼠标左键完成画线，点击鼠标右键确认结果，在弹出的输入框中输入变量名并完成变量创建
* 4: 标记矩形，在原图中按下鼠标左键并拖动鼠标，勾选出需要的区域，松开鼠标左键完成框选，点击鼠标滚轮（鼠标中键）预览效果，点击鼠标右键确认结果，在弹出的输入框中输入变量名并完成变量创建

<br/>

## settings文件配置说明

* `accuracy`: 图片匹配算法的置信度阈值，取值范围在0-1之间，默认0.93，在使用寻找图片类的功能时，如果匹配出错误目标则提高此值，如果要模糊匹配或高置信度无法匹配则降低此值
* `cache_path`: 缓存文件路径，部分截图或其他缓存文件将存储在这个指定路径内
* `randomDelayMin`: 调用[random_delay](#random_delay)方法时，延时取随机数的最小值，单位为秒
* `randomDelayMax`: 调用[random_delay](#random_delay)方法时，延时取随机数的最大值，单位为秒
* `touchPosRange`: 调用[touch](#touch)方法时，随机偏移量的最大值，单位为像素
* `touchDelayRange`: 调用[touch](#touch)方法时，随机延时时长的最大值，单位为毫秒
* `slideMinVer`: 调用[slide](#slide)方法时，滑屏所需时长取随机数的最小值，单位为毫秒
* `slideMaxVer`: 调用[slide](#slide)方法时，滑屏所需时长取随机数的最大值，单位为毫秒

<br/>

## RaphaelScriptHelper
引入
```python
import RaphaelScriptHelper
```

> **使用以前，请参考[settings配置说明](#settings文件配置说明)配置好相关属性**

<br/>

### random_delay

随机延时，随机范围从`randomDelayMin`到`randomDelayMax`

**原型**

```python
def random_delay()
```
**参数解释**

无入参

**返回值**

无返回

**注意**

对当前线程延时

<br/>

### delay

延时指定时间

**原型**

```python
def delay(t)
```
**参数解释**

`t`: 延时时间，单位为秒

**返回值**

无返回

**注意**

对当前线程延时

<br/>

### touch

智能模拟点击某个点，将会随机点击以这个点为中心一定范围内的某个点，并随机按下时长，让操作更接近人为操作

**原型**

```python
def touch(pos)
```
**参数解释**

`pos`: 点击位置，描述为一个二元组 (x, y)

**返回值**

无返回

**注意**

点击偏移的范围为settings配置中的`touchPosRange`（单位为像素），点击时长的范围为settings配置中的`touchDelayRange`（单位为毫秒，此值不建议设置太高，对于部分游戏较高的按下时长会被视为长按）

<br/>

### find_pic

截取屏幕，在截图中寻找`target`图片，返回满足置信度要求的，置信度最高的区块的左上角坐标或中心坐标

**原型**

```python
def find_pic(target, returnCenter = False)
```
**参数解释**

`target`: 欲寻找的图片路径
`returnCenter`: 是否返回中心坐标，默认值为`False`，为`True`时返回满足置信度要求的，置信度最高的区块的中心坐标

**返回值**

返回一个点坐标 (x,y)，当没有任何满足要求的结果时，返回None

**注意**

置信度阈值为settings配置中的`accuracy`，其余注意事项同[locate](#locate)

<br/>

### find_pic_all

截取屏幕，在截图中寻找`target`图片，返回满足置信度要求的所有区块的左上角坐标

**原型**

```python
def find_pic_all(target)
```
**参数解释**

`target`: 欲寻找的图片路径

**返回值**

返回一个点坐标数组 \[(x1,y1), (x2,y2), ...\]，当没有任何满足要求的结果时，返回一个空数组

**注意**

置信度阈值为settings配置中的`accuracy`，其余注意事项同[locate_all](#locate_all)

<br/>

### find_pic_touch

截取屏幕，在截图中寻找`target`图片，找到满足置信度要求的且置信度最高的区块，在其范围内进行一次智能模拟点击

**原型**

```python
def find_pic_touch(target)
```
**参数解释**

`target`: 欲寻找的图片路径

**返回值**

返回一个布尔值，如果成功寻找到满足要求的区块，则返回`True`，否则返回`False`

**注意**

置信度阈值为settings配置中的`accuracy`，其余注意事项同[locate](#locate)及[touch](#touch)

<br/>

### slide

智能模拟滑动，给定向量`vector`，将以随机速度，并取向量起终点附近的某个点为目标起终点进行一次滑动

**原型**

```python
def slide(vector)
```
**参数解释**

`vector`: ，描述为一个二元组 ((x1, y1), (x2, y2))，其中第一个项是滑动起点，第二个项是滑动终点

**返回值**

无返回

**注意**

点击偏移的范围为settings配置中的`touchPosRange`（单位为像素），滑动所用时长随机范围从`slideMinVer`到`slideMaxVer`（单位为毫秒，滑屏操作不能太快，建议最小值设置在500ms以上）

<br/>

### find_pic_slide
截取屏幕，在截图中寻找`target`图片，找到满足置信度要求的且置信度最高的区块，在其范围内随机选取一点作为滑动起点，并以`pos`为滑动终点进行一次智能模拟滑动

**原型**

```python
def find_pic_slide(target,pos)
```
**参数解释**

`target`: 欲寻找的图片路径
`pos`: 滑动终止位置，描述为一个二元组 (x, y)

**返回值**

返回一个布尔值，如果成功寻找到满足要求的区块，则返回`True`，否则返回`False`

**注意**

置信度阈值为settings配置中的`accuracy`，其余注意事项同[locate](#locate)及[slide](#slide)

<br/>

## ImageProc-图片处理类
引入
```python
import ImageProc
```

<br/>

### locate
从`source`图片中寻找`wanted`图片所在的位置，返回满足置信度大于`accuracy`的要求时，置信度最大的区块的左上角坐标

**原型**

```python
def locate(source, wanted, accuracy=0.90)
```
**参数解释**

`source`: 原图片路径，被查找的图片

`wanted`: 欲查找的图片路径

`accuracy`: 置信度阈值，可空，默认为0.9；置信度阈值越大，匹配结果可信度越高

**返回值**

返回一个点坐标 (x,y)，当没有任何满足要求的结果时，返回None

**注意**

此方法不会改变欲查找的图片的大小，而是直接去比对，因此如果存在被查找图片中找不到欲识别图片的情况，请先检查分辨率是否正确，然后再调节置信度阈值以达到效果

<br/>

### locate_all
从`source`图片中寻找`wanted`图片所在的位置，返回满足置信度大于`accuracy`的要求的所有区块的左上角坐标，对识别到的邻近点自动去重

**原型**

```python
def locate_all(source, wanted, accuracy=0.90)
```
**参数解释**

`source`: 原图片路径，被查找的图片

`wanted`: 欲查找的图片路径

`accuracy`: 置信度阈值，可空，默认为0.9；置信度阈值越大，匹配结果可信度越高

**返回值**

返回一个点坐标数组 \[(x1,y1), (x2,y2), ...\]，当没有任何满足要求的结果时，返回一个空数组

**注意**

此方法不会改变欲查找的图片的大小，而是直接去比对，因此如果存在被查找图片中找不到欲识别图片的情况，请先检查分辨率是否正确，然后再调节置信度阈值以达到效果；针对某个被识别到的点坐标，如果下一个被识别到的点坐标在其为中心，半径为15个像素的范围内，将会被自动去重，不记录到结果中

<br/>

### centerOfTouchArea
给定目标尺寸大小`wantedSize`和目标左上角顶点坐标`topLeftPos`，返回目标中心的坐标

**原型**

```python
def centerOfTouchArea(wantedSize, topLeftPos)
```
**参数解释**

`wantedSize`: 目标尺寸大小，描述为一个三元组 (h_src, w_src, tongdao) 分别代表高，宽，通道数，通道数在本函数计算中不需要，可给任意值；一般这个参数传 img.shape 即可（shape方法为cv2计算图片尺寸的方法）

`topLeftPos`: 目标左上角顶点坐标，描述为一个二元组 (x, y)

**返回值**

返回一个点坐标 (x,y)

**注意**

无

<br/>

## ADBHelper-ADB助手类

引入
```python
import ADBHelper
```

> 注意：首次调用 ADBHelper 中的方法时，由于ADB要启动守护进程，因此可能会慢一些

<br/>

### getDevicesList
调用ADB命令，获取连接到当前计算机的安卓设备（支持模拟器）列表，返回一个数组，其中每一个项为一个安卓设备的deviceID

**原型**

```python
def getDevicesList()
```
**参数解释**

无入参

**返回值**

返回一个文本数组 \["did1", "did2", ...\]

**注意**

如果获取不到，请先检查设备有没有打开调试模式，并信任所连接的计算机；对于部分模拟器而言，获取到的did是一个`ip地址+端口`的形式

<br/>

### killADBServer
调用ADB命令，杀掉当前ADB的守护进程，常用于ADB的重启

**原型**

```python
def killADBServer()
```
**参数解释**

无入参

**返回值**

无返回

**注意**

无

<br/>

### screenCapture
给定设备ID`deviceID`和截图保存路径`capPath`，对指定设备进行一次屏幕截图

**原型**

```python
def screenCapture(deviceID, capPath)
```
**参数解释**

`deviceID`: 设备ID，可以通过`getDevicesList()`方法获取

`capPath`: 截图保存路径，截图完成后保存到本地的路径

**返回值**

无返回

**注意**

无

<br/>

### touch
给定设备ID`deviceID`和点击位置`pos`，对指定设备的指定点击位置进行一次模拟点击的操作

**原型**

```python
def touch(deviceID, pos)
```
**参数解释**

`deviceID`: 设备ID，可以通过`getDevicesList()`方法获取

`pos`: 点击位置，描述为一个二元组 (x, y)

**返回值**

无返回

**注意**

无

<br/>

### slide
给定设备ID`deviceID`、滑动起始位置`posStart`、滑动终止位置`posStop`和滑动所需时间`time`（单位为毫秒），对指定设备进行一次模拟滑动：花费`time`毫秒的时间从`posStart`滑动到`posStop`

**原型**

```python
def slide(deviceID, posStart, posStop, time)
```
**参数解释**

`deviceID`: 设备ID，可以通过`getDevicesList()`方法获取

`posStart`: 滑动起始位置，描述为一个二元组 (x, y)

`posStop`: 滑动终止位置，描述为一个二元组 (x, y)

`time`: 滑动所需时间，单位为毫秒

**返回值**

无返回

**注意**

无

<br/>

### longTouch
给定设备ID`deviceID`、点击位置`pos`和长按时间`time`（单位为毫秒），对指定设备的指定点击位置进行一次模拟长按的操作

**原型**

```python
def longTouch(deviceID, pos, time)
```
**参数解释**

`deviceID`: 设备ID，可以通过`getDevicesList()`方法获取

`pos`: 长按位置，描述为一个二元组 (x, y)

`time`: 长按时间，单位为毫秒

**返回值**

无返回

**注意**

无

<br/>
