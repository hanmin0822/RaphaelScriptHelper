<h1 align="center">
  RaphaelScriptHelper 拉斐尔脚本助手
  <br>
</h1>

<p align="center">
  <b>～轻松编写更智能的游戏脚本～</b>
  <br>
  <br>
</p>

> **警告：本项目仅作学习交流用途，禁止将本项目中的任何脚本、工具用于任何非法用途，如果使用本项目中的任何脚本、工具造成游戏被封号、处罚等一切损失需自行承担后果，本项目对此概不负责！**

> 请注意：使用脚本会在一定程度上影响游戏体验，请根据自身需求使用。


本项目的命名取自轻小说[《关于我转生变成史莱姆这档事》](https://mzh.moegirl.org.cn/%E5%85%B3%E4%BA%8E%E6%88%91%E8%BD%AC%E7%94%9F%E5%8F%98%E6%88%90%E5%8F%B2%E8%8E%B1%E5%A7%86%E8%BF%99%E6%A1%A3%E4%BA%8B)中主角 <ruby><rt></rt>利姆鲁·特恩佩斯特<rp>（</rp><rt>リムル・テンペスト</rt><rp>）</rp></ruby> 进化成魔王后持有的究极技能之一 <ruby><rt></rt>智慧之王<rp>（</rp><rt>拉斐尔</rt><rp>）</rp></ruby> ，拉斐尔具有接管主角意识并代打的能力，这很像使用本项目来帮助我们完成一些重复繁琐的流程。~~所以说本项目也可以帮助你成为萌王？(误)~~

[演示视频](https://www.bilibili.com/video/BV1RZ4y1f76m/)

## 简介
RaphaelScriptHelper (拉斐尔脚本助手/拉斐尔模块) 是一个基于openCV图像处理、OCR、ADB等技术的Python框架，可以让脚本编写者在短时间内编写出一个实用的游戏脚本，适用于可以支持脚本运行的各种系统及模拟器，支持诸如识图、点击、按键、滑动、文字识别、随机操作等功能。一个实用的例子是几行代码编写一个简单的明日方舟日常刷图脚本（见演示视频）。

## 目前可以直接使用的脚本
* [明日方舟集成战略模式（肉鸽）脚本](https://github.com/hanmin0822/RaphaelScriptHelper/blob/master/Arknights/ArknightsRoguelike.py)
* [明日方舟日常刷图脚本](https://github.com/hanmin0822/RaphaelScriptHelper/blob/master/Arknights/Arknights_default.py)

> 请注意：请仔细阅读各脚本最上方的注释说明再使用。

欢迎大家编写更多好用的脚本并提PR到本项目中来哦～

## 环境配置

Python 3.7

使用到的Python库

```
numpy=1.19.5
opencv-python=4.5.1.48
```

ADB套件请在[这里](https://pan.baidu.com/s/15dpjviyIHezaT56knux2xQ?pwd=mr5p)下载并解压放置到脚本框架根目录

## 快速上手
使用一行代码来引入 RaphaelScriptHelper
```python
import RaphaelScriptHelper as rsh
```
使用一至两行代码来指定脚本运行的设备
```python
rsh.deviceType = 1 #0为PC环境，1为安卓设备
rsh.deviceID = "安卓设备ID" #如使用安卓设备，请填写
```
使用一行代码来模拟点击屏幕，会自动在一定范围内随机偏移、随机时长（防作弊检测）来点击一次
```python
rsh.touch(pos)
```
使用一行代码来模拟点击屏幕上指定区域，先使用[选择工具](https://github.com/hanmin0822/RaphaelScriptHelper/blob/master/FunctionDoc.md#%E6%A0%87%E7%82%B9%E6%88%AA%E5%8F%96%E5%B7%A5%E5%85%B7%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E)来指定区域并保存，方便后续识别，会自动在识别区域内任意点、随机时长（防作弊检测）来点击一次
```python
rsh.find_pic_touch("./test.png")
```
## 详细功能
请参阅[详细功能使用手册](https://github.com/hanmin0822/RaphaelScriptHelper/blob/master/FunctionDoc.md)

## 注意事项
* 本项目仅作学习交流用途，禁止将本项目中的任何脚本、工具用于任何非法用途，如果使用本项目中的工具造成游戏被封号、处罚等概不负责
* 针对识图功能，不会改变欲识别图片的大小，而是直接用这张图片去比对，因此如果存在被查找图片中找不到欲识别图片的情况，请先检查分辨率是否正确，然后再调节可信度阈值以达到效果

## TODO
* 支持PC端截图、键盘鼠标智能模拟
* 支持在线/离线OCR
* 增加GUI界面支持可视化编写流程
