#图片匹配置信度，0-1之间，默认0.93，如果匹配出错误目标则提高置信度，如果要模糊匹配或高置信度无法匹配则降低置信度
accuracy = 0.93

#缓存文件存放地址，以/结尾
cache_path = './cache/'

#事件操作完成等待范围[actionDelayMin,actionDelayMax]，单位秒
randomDelayMin = 1
randomDelayMax = 5

#点击偏移范围，[0,x]
touchPosRange = 8

#点击延迟范围，[0,x]
touchDelayRange = 30

#滑屏所需时长范围[slideMinVer,slideMaxVer]，单位毫秒 (滑屏操作不能太快，建议最小值设置在500ms以上)
slideMinVer = 500
slideMaxVer = 3000