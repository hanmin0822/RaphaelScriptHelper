# 请将此脚本、img文件夹和ResourceDictionary.py文件复制到项目根目录下再运行！

import ADBHelper, RaphaelScriptHelper, ResourceDictionary

deviceList = ADBHelper.getDevicesList()
i = 0
for did in deviceList:
    print(str(i) + ": " + did)
    i = i + 1
input_i = input("请输入需要执行脚本的设备编号\n")

delayTime = input("请输入关卡所耗时间（单位：秒）\n")

RaphaelScriptHelper.deviceType = 1
RaphaelScriptHelper.deviceID = deviceList[int(input_i)]

for i in range(0,100):
    j = 0
    while j < 5:
        RaphaelScriptHelper.find_pic_touch(ResourceDictionary.start)
        RaphaelScriptHelper.random_delay()
        if RaphaelScriptHelper.find_pic_touch(ResourceDictionary.start1):
            break
        j = j + 1
        RaphaelScriptHelper.random_delay()

    RaphaelScriptHelper.delay(int(delayTime))

    j = 0
    while j < 5:
        if RaphaelScriptHelper.find_pic_touch(ResourceDictionary.finish):
            break
        j = j + 1
        RaphaelScriptHelper.delay(3)

    RaphaelScriptHelper.delay(3)
    RaphaelScriptHelper.random_delay()
