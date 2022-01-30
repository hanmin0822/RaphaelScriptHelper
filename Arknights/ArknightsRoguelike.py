# 请参考视频教程 https://www.bilibili.com/video/BV1u3411E7KD/ 改写此脚本后再运行
# 请注意视频教程或文字教程中的相关注意事项

import RaphaelScriptHelper as gamer
import multiprocessing
import ResourceDictionary as rd
import settings
from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

# 请在跑脚本之前参考教程修改这一部分
# =======================================================================

# 安卓设备的DID
gamer.deviceID = "127.0.0.1:62001"

# 从点击开始以后到进入正式游戏界面之前的前期准备部分
def init_front():
    # 选择分队
    gamer.touch(rd.zhihuifendui)
    gamer.random_delay()
    gamer.touch(rd.zhihuifendui)
    gamer.random_delay()

    # 选择招募组合
    gamer.touch(rd.wenzhawenda)
    gamer.random_delay()
    gamer.touch(rd.wenzhawenda)
    gamer.random_delay()

    #选择第一个职业和干员
    gamer.touch(rd.zhongzhuang)
    gamer.random_delay()
    gamer.touch(rd.linguang)
    gamer.random_delay()
    gamer.touch(rd.querenganyuan)
    gamer.random_delay()
    gamer.touch(rd.skip)
    gamer.delay(1)
    gamer.touch(rd.skip)
    gamer.delay(1)
    gamer.touch(rd.skip)
    gamer.random_delay()
    gamer.delay(3)

    #选择第二个职业和干员
    gamer.touch(rd.juji)
    gamer.random_delay()
    gamer.touch(rd.landu)
    gamer.random_delay()
    gamer.touch(rd.querenganyuan)
    gamer.random_delay()
    gamer.touch(rd.skip)
    gamer.delay(1)
    gamer.touch(rd.skip)
    gamer.delay(1)
    gamer.touch(rd.skip)
    gamer.random_delay()
    gamer.delay(3)

    #选择第三个职业和干员
    gamer.touch(rd.shushi)
    gamer.random_delay()
    gamer.touch(rd.yanrong)
    gamer.random_delay()
    gamer.touch(rd.querenganyuan)
    gamer.random_delay()
    gamer.delay(3)
    gamer.touch(rd.skip)
    

# 与虫为伴关卡所需时间，单位为秒
fight_yu_chong_wei_ban_duration = 80

# 与虫为伴打法 在此定义 请参考这个方法内的注释来编写
def fight_yu_chong_wei_ban():
    for i in range(4): # 循环做4次，以防中途有干员被打死然后就不部署了
        # 刚进游戏画面时的延时，这里不需要设置太高，因为此时已经是二倍速状态，如果一开始使用的干员费用较高可以适当增大此值
        gamer.delay(4)

        # 这一行代码的意思是将临光放在指定位置，朝向向上，下同，这些都可以自己替换掉
        fight_agent_arrange(rd.fight_icon_linguang, rd.yuchongweiban_linguang, Direction.UP)
        # 放完临光后延时5秒再放下一个干员（注意费用回复时间）
        gamer.delay(5)

        fight_agent_arrange(rd.fight_icon_landu, rd.yuchongweiban_landu, Direction.LEFT)
        gamer.delay(8)

        fight_agent_arrange(rd.fight_icon_yanrong, rd.yuchongweiban_yanrong, Direction.UP)
        gamer.delay(10)


# 驯兽小屋关卡所需时间，单位为秒
fight_xun_shou_xiao_wu_duration = 80

# 驯兽小屋打法 在此定义 参考 与虫为伴的注释
def fight_xun_shou_xiao_wu():
    for i in range(4):
        gamer.delay(4)

        fight_agent_arrange(rd.fight_icon_linguang, rd.xunshouxiaowu_linguang, Direction.Right)
        gamer.delay(5)

        fight_agent_arrange(rd.fight_icon_landu, rd.xunshouxiaowu_landu, Direction.LEFT)
        gamer.delay(8)

        fight_agent_arrange(rd.fight_icon_yanrong, rd.xunshouxiaowu_yanrong, Direction.LEFT)
        gamer.delay(10)

# 礼炮小队关卡所需时间，单位为秒
fight_li_pao_xiao_dui_duration = 80

# 礼炮小队打法 在此定义 参考 与虫为伴的注释
def fight_li_pao_xiao_dui():
    for i in range(4):
        gamer.delay(4)

        fight_agent_arrange(rd.fight_icon_linguang, rd.lipaoxiaodui_linguang, Direction.RIGHT)
        gamer.delay(5)

        fight_agent_arrange(rd.fight_icon_landu, rd.lipaoxiaodui_landu, Direction.RIGHT)
        gamer.delay(8)

        fight_agent_arrange(rd.fight_icon_yanrong, rd.lipaoxiaodui_yanrong, Direction.RIGHT)
        gamer.delay(10)

# 意外关卡所需时间，单位为秒
fight_yi_wai_duration = 80

# 意外打法 在此定义 参考 与虫为伴的注释
def fight_yi_wai():
    for i in range(4):
        gamer.delay(4)

        fight_agent_arrange(rd.fight_icon_landu, rd.yiwai_landu, Direction.DOWN)
        gamer.delay(5)

        fight_agent_arrange(rd.fight_icon_linguang, rd.yiwai_linguang, Direction.LEFT)
        gamer.delay(8)

        fight_agent_arrange(rd.fight_icon_yanrong, rd.yiwai_yanrong, Direction.DOWN)
        gamer.delay(10)


# =======================================================================
# 以下部分请不要随意修改

# ADB运行
gamer.deviceType = 1

# 全局标志位 勿改动
isFightLose = False

#屏幕分辨率 勿改动 请与此保持对齐
screen_size = (2340, 1080)

#战斗界面干员部署通用方法 三个参数分别是 干员 站位 朝向(0-3分别代表上下左右)
def fight_agent_arrange(agent, pos, direction):
    screen_w, screen_h = screen_size
    x, y = pos
    shift = settings.touchPosRange

    if direction == Direction.UP:
        _y = y - 400
        if (_y < shift):
            _y = shift
        slide_final_pos = (x, _y)
    elif direction == Direction.DOWN:
        _y = y + 400
        if (_y > screen_h - shift):
            _y = screen_h - shift
        slide_final_pos = (x, _y)
    elif direction == Direction.LEFT:
        _x = x - 400
        if (_x < shift):
            _x = shift
        slide_final_pos = (_x, y)
    elif direction == Direction.RIGHT:
        _x = x + 400
        if (_x > screen_w - shift):
            _x = screen_w - shift
        slide_final_pos = (_x, y)
    else:
        return False

    if gamer.find_pic_slide(agent, pos):
        gamer.delay(0.5)
        gamer.slide((pos, slide_final_pos))
        gamer.delay(0.5)
        return True

    return False

# 跳过结算画面
def skip_ending():
    gamer.random_delay()
    gamer.touch(rd.bottom)
    gamer.delay(0.5)
    gamer.touch(rd.bottom)
    gamer.delay(0.5)
    gamer.touch(rd.bottom)
    gamer.delay(0.5)
    gamer.touch(rd.bottom)
    gamer.random_delay()
    gamer.touch(rd.bottom)

# 战斗后处理
def process_after_fight():
    for i in range(5): # 避免某些关卡有特殊怪，打得比较慢，重试五次检查结果状态，每次间隔10s
        if gamer.find_pic_touch(rd.success_pass):
            gamer.random_delay()
            gamer.find_pic_touch(rd.nazou)
            gamer.delay(1)
            gamer.find_pic_touch(rd.exit)
            gamer.delay(0.5)
            if gamer.find_pic_touch(rd.exit_confirm):
                return True
            else:
                return False
        # 失败的情况考虑一下
        elif gamer.find_pic_touch(rd.signal_lost):
            gamer.random_delay()
            gamer.delay(5)
            skip_ending()
            global isFightLose
            isFightLose = True
        else:
            if i == 4:
                return False
        gamer.delay(10)

# 战斗前处理
def process_before_fight():
    gamer.random_delay()
    gamer.find_pic_touch(rd.enter)
    gamer.random_delay()
    gamer.find_pic_touch(rd.kaishixingdong)
    gamer.delay(9) # 从点击开始行动按钮以后到进入游戏的延时9秒
    gamer.find_pic_touch(rd.speed_1x) # 二倍速

# 普通战斗关卡
def fight():
    global isFightLose
    isFightLose = False
    if gamer.find_pic_touch(rd.fight_lipaoxiaodui):
        process_before_fight()
        t = multiprocessing.Process(target=fight_li_pao_xiao_dui)
        t.start()
        gamer.delay(fight_li_pao_xiao_dui_duration)
        t.terminate()
    elif gamer.find_pic_touch(rd.fight_yuchongweiban):
        process_before_fight()
        t = multiprocessing.Process(target=fight_yu_chong_wei_ban)
        t.start()
        gamer.delay(fight_yu_chong_wei_ban_duration)
        t.terminate()
    elif gamer.find_pic_touch(rd.fight_xunshouxiaowu):
        process_before_fight()
        t = multiprocessing.Process(target=fight_xun_shou_xiao_wu)
        t.start()
        gamer.delay(fight_xun_shou_xiao_wu_duration)
        t.terminate()
    elif gamer.find_pic_touch(rd.fight_yiwai):
        process_before_fight()
        t = multiprocessing.Process(target=fight_yi_wai)
        t.start()
        gamer.delay(fight_yi_wai_duration)
        t.terminate()
    else:
        return False

    process_after_fight()
    return True

# 不期而遇节点处理
def buqieryu():
    if gamer.find_pic_touch(rd.buqieryu):
        gamer.random_delay()
        gamer.find_pic_touch(rd.enter_buqieryu)
        gamer.delay(8) #等待展示文本时间
        gamer.random_delay()

        for i in range(2):
            if gamer.find_pic_touch(rd.taopao):
                gamer.delay(1)
                gamer.find_pic_touch(rd.choose_confirm)
                break
            elif gamer.find_pic_touch(rd.xiwang):
                gamer.delay(1)
                gamer.find_pic_touch(rd.choose_confirm)
                break
            elif gamer.find_pic_touch(rd.shengming):
                gamer.delay(1)
                gamer.find_pic_touch(rd.choose_confirm)
                break
            elif gamer.find_pic_touch(rd.yuanshiding):
                gamer.delay(1)
                gamer.find_pic_touch(rd.choose_confirm)
                break
            else:
                #下滑一点然后重试一次，防止展示不完全
                gamer.slide(rd.right_slide_down)
        gamer.delay(3)
        gamer.touch(rd.bottom)
        gamer.random_delay()
        return True
    else:
        return False

# 诡异行商节点处理(刷投资)
def guiyixingshang():
    if gamer.find_pic_touch(rd.guiyixingshang):
        gamer.random_delay()
        gamer.find_pic_touch(rd.enter_guiyixingshang)
        gamer.delay(3)
        gamer.random_delay()
        if gamer.find_pic_touch(rd.touzi_enter):
            gamer.find_pic_touch(rd.touzirukou)
            gamer.random_delay()
            pos = gamer.find_pic(rd.touzi_confirm, True)
            for i in range(0,20): #点20次 投资确认
                gamer.touch(pos)
                gamer.delay(0.5)
            gamer.find_pic_touch(rd.suanle)
            gamer.random_delay()
            gamer.find_pic_touch(rd.suanle2)
            gamer.random_delay()
            pos = gamer.find_pic(rd.exit_shop)
            gamer.touch(pos)
            gamer.random_delay()
            gamer.touch(pos)
        else:
            pos = gamer.find_pic(rd.exit_shop)
            gamer.touch(pos)
            gamer.random_delay()
            gamer.touch(pos)
        return True
    else:
        return False

# 幕间余兴 这里直接选退出选项
def mujianyuxing():
    if gamer.find_pic_touch(rd.mujianyuxing):
        gamer.random_delay()
        gamer.find_pic_touch(rd.enter_buqieryu)
        gamer.delay(8) #等待展示文本时间
        gamer.random_delay()
        for i in range(2):
            if gamer.find_pic_touch(rd.taopao):
                gamer.delay(1)
                gamer.find_pic_touch(rd.choose_confirm)
                break
            else:
                #下滑一点然后重试一次，防止展示不完全
                gamer.slide(rd.right_slide_down)
        gamer.delay(3)
        gamer.touch(rd.bottom)
        gamer.random_delay()
        return True
    else:
        return False

# 退出到主界面并放弃当前进度，重开
def exit_game():
    gamer.find_pic_touch(rd.exit_all)
    gamer.delay(2)
    gamer.random_delay()
    gamer.find_pic_touch(rd.giveup)
    gamer.random_delay()
    gamer.find_pic_touch(rd.giveup_confirm)
    skip_ending()

# 干员编队部分，这里只要分辨率不变，操作是固定的
def gan_yuan_bian_dui():
    gamer.touch((2076,1026))
    gamer.random_delay()
    gamer.touch((1846, 60))
    gamer.random_delay()
    gamer.touch((987,242))
    gamer.random_delay()
    gamer.touch((987, 446))
    gamer.random_delay()
    gamer.touch((987, 656))
    gamer.random_delay()
    gamer.touch((2078, 1022))
    gamer.random_delay()
    gamer.touch((195, 52))



# 脚本从这里开始运行
gamer.deviceType = 1

while True:
    if gamer.find_pic_touch(rd.rg_start):
        gamer.random_delay()
        init_front()
        gamer.random_delay()
        if gamer.find_pic_touch(rd.enter_game):
            gamer.delay(5)
            gan_yuan_bian_dui()

            # 第一层只有四关，且第一关只能是战斗节点
            # 1
            fight()

            # TODO:可以考虑更智能的寻路算法，当前只支持按照固定优先级
            # 2
            gamer.random_delay()
            if buqieryu() is False:
                if fight() is False:
                    if mujianyuxing() is False:
                        exit_game()
                        continue
            if isFightLose:
                continue

            # 中场滑屏到后面，避免重复识别
            gamer.slide(rd.bottom_slide_left)

            # 3
            gamer.random_delay()
            if buqieryu() is False:
                if fight() is False:
                    if mujianyuxing() is False:
                        exit_game()
                        continue

            if isFightLose:
                continue

            # 第四关只能是诡异行商
            # 4
            guiyixingshang()
            gamer.delay(5)
            gamer.random_delay()
            exit_game()
    else:
        break
