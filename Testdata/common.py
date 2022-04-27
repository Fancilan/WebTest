# -*- coding: UTF-8 -*-
# @Time:2021/1/29 14:37
# @Name:common.py

import random
# from faker import Faker

class Name_s():

    def random_firstname(self):
        smaple = '赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜'
        first_name_A = str(random.choice(smaple))
        return first_name_A
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

fake_data = Name_s()

if __name__ == '__main__':
    a= Name_s()
    b = a.random_firstname()
    print(b)



