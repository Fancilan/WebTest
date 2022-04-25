# -*- coding: UTF-8 -*-
# @Time:2021/1/29 14:37
# @Name:common.py

import random
# from faker import Faker

class Name():

    def random_firstname(self):
        smaple = '''赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜
                    戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐
                    费廉岑薛雷贺倪汤滕殷罗毕邬安常乐于时傅皮卞齐康伍余元卜顾孟平黄
                    和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董梁
                    杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍
                    虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮龚
                    程嵇邢滑裴陆荣翁荀羊於惠甄曲家封芮羿储靳汲邴糜松井段富巫乌焦巴弓
                    牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙
                    叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴鬱胥能苍双
                    闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍卻璩桑桂濮牛寿通边扈燕冀郏浦尚农
                    温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘
                    匡国文寇广禄阙东欧殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空
                    曾毋沙乜养鞠须丰巢关蒯相查后荆红游竺权逯盖益桓公万俟司马上官欧阳
                    夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠
                    公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空丌官司寇仉督子车
                    颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁晋楚闫法汝鄢涂钦
                    段干百里东郭南门呼延归海羊舌微生岳帅缑亢况郈有琴梁丘左丘东门西门
                    商牟佘佴伯赏南宫墨哈谯笪年爱阳佟第五言福百家姓终'''
        first_name_A = random.choice(smaple)
        return str(first_name_A)
    def random_class(self):
        data_1 = random.choice('一二三四五六')
        data_2 = '年级'
        data = data_1 + data_2
        return data

    def random_email(self):
        # fake = Faker()
        # data = fake.free_email()
        data = "123456789@qq.com"
        return data

    def random_province(self):
        # fake = Faker(locale='zh_CN')
        # data = fake.province()
        data = "湖北省"
        return data

    def random_school(self):
        # fake = Faker(locale='zh_CN')
        # data_1 = fake.city_name()
        # data_2 = random.choice(['第一','第二','重点'])
        # data = data_1 + '市' +data_2 +'实验小学'
        data = "实验小学"
        return data

fake_data = Name()

if __name__ == '__main__':
    a= Name()
    b = a.random_email()



