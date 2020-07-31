# -*- coding: utf-8 -*-
import logging
import sys
import pandas as pd 
import numpy as np 
# reload(sys)
# sys.setdefaultencoding('utf8')
logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO)

def draftScore(Score):
    #阵容得分
    return sum(Score)/len(Score)

#def getScore(hero):

def friendRate(draft,hero,pr):
    path = './friend/' + hero + '.txt'
    data = pd.read_csv(path,names=['hero_name','english_name','win_rate','times'],sep=' ', encoding = 'utf-8')
    data=data.reset_index(drop=True)
    data=data.set_index(['english_name'])
    # 将该英雄的friend数据读进来
    timesMin = np.min(data['times'])
    timesMax = np.max(data['times'])
    timesMean = np.mean(data['times'])
    FR = 0
    for i in range(len(draft)):
        if(draft[i] != hero):
            confidence = 1
            fr_i = (float(data.loc[draft[i]]['win_rate'].strip('%'))/100)/pr
            confidence = np.log10(data.loc[draft[i]]['times']+timesMean)/np.log10(timesMean+timesMean)
            if(fr_i > 1):
                fr_i = fr_i * confidence
            elif(fr_i < 1):
                fr_i = fr_i / confidence
            else:
                fr_i = fr_i
            FR = FR + fr_i
    return FR/(len(draft)-1)
    # print(np.min(data['times']))
    # print(np.mean(data['times']))

def eneRate(draft,hero,pr):
    path = './ene/' + hero + '.txt'
    data = pd.read_csv(path,names=['hero_name','english_name','win_rate','times'],sep=' ', encoding = 'utf-8')
    data=data.reset_index(drop=True)
    data=data.set_index(['english_name'])
    # 将该英雄的ene数据读进来
    timesMin = np.min(data['times'])
    timesMax = np.max(data['times'])
    timesMean = np.mean(data['times'])
    ER = 0
    for i in range(len(draft)):
        if(draft[i] != hero):
            confidence = 1
            er_i = (float(data.loc[draft[i]]['win_rate'].strip('%'))/100)/pr
            confidence = np.log10(data.loc[draft[i]]['times']+timesMean)/np.log10(timesMean+timesMean)
            if(er_i > 1):
                er_i = er_i * confidence
            elif(er_i < 1):
                er_i = er_i / confidence
            else:
                er_i = er_i
            ER = ER + er_i
    return ER/(len(draft))
    # print(np.min(data['times']))
    # print(np.mean(data['times']))

def check(draft):
    pure_rate = []
    en_name = []
    path = './hero.txt'
    data = pd.read_csv(path,names=['hero_name','english_name','win_rate','times'],sep=' ', encoding = 'utf-8')
    data=data.reset_index(drop=True)
    data=data.set_index(['hero_name'])
    # 将该英雄的数据读进来
    timesMin = np.min(data['times'])
    timesMax = np.max(data['times'])
    timesMean = np.mean(data['times'])
    for i in range(len(draft)):
        try:
            # rate = (float(data.loc[draft[i]]['win_rate'].strip('%'))/100) * (np.log(timesMean+data.loc[draft[i]]['times'])/np.log(timesMean+timesMean))
            rate = (float(data.loc[draft[i]]['win_rate'].strip('%'))/100) 
            pure_rate.append(rate)
            en_name.append(data.loc[draft[i]]['english_name'])
        except:
            sttr = 'can\'t find hero called' + draft[i]
            logging.error(sttr)
    return pure_rate,en_name

if __name__ == '__main__':
    #eg vs nigma  gmae1 :天辉： 0.479676912369738 夜魇 0.5307449309503159
    # draftRadient = ['斯拉克','风暴之灵','水晶室女','孽主','撼地者']
    # draftDire = ['巫妖','幻影长矛手','末日使者','瘟疫法师','天涯墨客']
    
    #eg vs nigma  gmae2 : 天辉： 0.5006038421417761 夜魇 0.4947910494764101
    # draftRadient = ['灰烬之灵','黑暗贤者','巫妖','撼地者','哈斯卡']
    # draftDire = ['娜迦海妖','风暴之灵','干扰者','司夜刺客','魅惑魔女']
    
    #vg vs ig  gmae2 :  0.4986979476181192 夜魇 0.49493205012589436
    # draftRadient = ['剃刀','黑暗贤者','孽主','昆卡','寒冬飞龙']
    # draftDire = ['撼地者','齐天大圣','天穹守望者','末日使者','祸乱之源']

    #aster vs chaos game1：
    draftRadient = ['半人马战行者','卓尔游侠','影魔','复仇之魂','拉比克']
    draftDire = ['斯拉克','帕克','干扰者','树精卫士','孽主']
    PR_radient , en_name_radient= check(draftRadient)
    PR_dire , en_name_dire= check(draftDire)
    Score = []
    for i in range(len(draftRadient)):
        print(draftRadient[i],PR_radient[i])
        friend = friendRate(en_name_radient,en_name_radient[i],PR_radient[i])
        ene = eneRate(en_name_dire,en_name_radient[i],PR_radient[i])
        # Score.append(PR_radient[i]*friend*ene)
        Score.append(0.5*friend*ene)
        print(friend,ene,Score[i])
    radient = draftScore(Score)
    Score = []
    for i in range(len(draftDire)):
        print(draftDire[i],PR_dire[i])
        friend = friendRate(en_name_dire,en_name_dire[i],PR_dire[i])
        ene = eneRate(en_name_radient,en_name_dire[i],PR_dire[i])
        # Score.append(PR_dire[i]*friend*ene)
        Score.append(0.5*friend*ene)
        print(friend,ene,Score[i])
    dire = draftScore(Score)
    print('天辉：',radient,'夜魇',dire)
    # friendRate(draft,'pudge',0.45)
