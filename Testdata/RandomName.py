# -*- coding: UTF-8 -*-
# @Time:2021/1/29 14:37
# @Name:RandomName.py
import random
# import time

class Names():


    def random_first_name(self):
        sample_0 = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        sample_1 = '戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐'
        sample_2 = '费廉岑薛雷贺倪汤滕殷罗毕邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄'
        sample_3 = '和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁'
        sample_4 = '杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍'
        sample_5 = '虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚'
        sample_6 = '程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓'
        sample_7 = '牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙'
        sample_8 = '叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双'
        sample_9 = '闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍卻璩桑桂濮牛寿通边扈燕冀郏浦尚农'
        sample_10 ='温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘'
        sample_11 ='匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空'
        sample_12 ='曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逯盖益桓公万俟司马上官欧阳'
        sample_13 ='夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠'
        sample_14 ='公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车'
        sample_15 ='颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁晋楚闫法汝鄢涂钦'
        sample_16 ='段干百里东郭南门呼延归海羊舌微生岳帅缑亢况郈有琴梁丘左丘东门西门'
        sample_17 ='商牟佘佴伯赏南宫墨哈谯笪年爱阳佟第五言福百家姓终'

        # for i in range(18):
        #     word = locals()['sample_' + str(i)]
        sum_1 = sample_0+sample_1+sample_2+sample_3+sample_4+sample_5+sample_6+sample_7+sample_8+sample_9
        sum_2 = sample_10+sample_11+sample_12+sample_13+sample_14+sample_15+sample_16+sample_17
        sum_sample = sum_1 + sum_2
        first_name_A = random.choice(str(sum_sample))

        return first_name_A





