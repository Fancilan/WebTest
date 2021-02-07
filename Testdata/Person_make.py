# -*-coding:utf-8-*-
from faker import Faker
import csv
import time
import numpy as np
import getpass
import random


def women_name():
    name = fake.first_name() + fake.first_name_female()
    return name
    # 姓氏方法+女性名称方法缝合,生成完美女性名字
def man_name():
    name = fake.first_name() + fake.first_name_male()
    return name
    # 男性名称同理女性完美名称
def women_name_choice(first_name):
    name = first_name + fake.first_name_female()
    return name
    # 自定义姓氏+女名
def man_name_choice(first_name):
    name = first_name + fake.first_name_male()
    return name
    # 自定义姓氏+男名

def export_data(ALL,person,start_time):
    cal = str(time.strftime("%Y-%m-%d", time.localtime())) +'-' +str(''.join(random.sample('0123456789',6)))
    user_name = getpass.getuser()# 获取当前用户名
    data_name = 'C:\\Users\\' + user_name +'\\Desktop\\data_'+ cal +'.csv'
    file = open(data_name, "w", newline='', encoding="UTF-8-sig")
    # newline解决空白行问题
    fwrite = csv.writer(file)
    header = ["Name", "Sex", "ID", "Phone", "Birthday"]
    # 写入变量名
    fwrite.writerow(header)
    fwrite.writerows(ALL)
    # 写入数据嗯
    file.close()
    end_time = time.time()
    final_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    time.sleep(0.5)
    msg = str("人员采集数量:" + str(person) + "人,成功！")
    print(msg)
    time.sleep(0.5)
    print(str("导出成功Success！导出文件在根目录下"))
    time.sleep(0.5)
    print("人员信息预览:")
    print(np.array(ALL))
    print(str('\n'))
    time.sleep(1)
    print('程序开始时间：' + origin_time)
    print('程序结束时间：' + final_time)
    print('Running time: %.3f 秒' % (end_time - start_time) + '\n')
    print("文件路径:"+ data_name)
    time.sleep(1)
    end = int(input("\n请问还要继续生成人员数据么？\n1.是\n2.否\n:"))
    if end == 1:
        person_make()
    else:
        eend = input("请按任意键退出,谢谢！")

def person_make():
    global fake
    global origin_time
    # 生成fake实例
    fake = Faker(locale='zh_CN')
    '''如果要生成中文的随机数据，我们可以在实例化时给locale参数传入‘zh_CN’这个值'''
    Name = []
    Phone = []
    ID = []
    Birthday = []
    Sex = []
    while True:
        num = input("请输入您想生成人员数量:")
        # person = int(num)
        if num == 'out':
            time.sleep(1)
            print("感谢您的使用！")
            time.sleep(0.5)
            print("再见。")
            time.sleep(0.5)
            quit()
        elif num == '0':
            print("人数为0，你逗我玩呢？请重新输入！")
        elif num == '':
            print("请重新输入，再输入回车削你！")
        elif int(num) >= 1000000:
            print("人员数量超过最大生成限制，请重新输入！")
        else:
            break
    person = int(num)
    time.sleep(0.5)
    print("1.自定义姓氏模式\n2.随机姓氏模式")
    select = int(input("请选择您要生成人员的信息的模式:"))
    time.sleep(0.5)
    if select == 2:
        print("请稍等，人员数据生成中…………")
        start_time = time.time()
        origin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(person):
            if i < person:
                # man = fake.name_male()
                # 生成男人的名字，有概率生成女人的名字，这个方法其实不是很好
                phone = fake.phone_number()
                # 生成手机号码
                is_id = fake.ssn(min_age=19, max_age=45)
                date = is_id
                sex_id = date[-2]
                if int(sex_id) % 2 == 0:
                    man_A = women_name()
                    while True:
                        man_B = women_name()
                        if man_A == man_B:
                            continue
                        else:
                            Name.append(str(man_A))
                            break
                else:
                    man_c = man_name()
                    while True:
                        man_d = man_name()
                        if man_c == man_d:
                            continue
                        else:
                            Name.append(str(man_c))
                            break

                # 生成最小年龄为19岁，最大年龄为45岁的身份证号
                # Name.append(str(man))
                Phone.append(str(phone))
                ID.append(str('\n') + str(is_id))
                # \n换个行可使身份证号后几位不消失，变为文本显示
            else:
                break
    else:
        while True:
            first_name = input("请输入您自定义的姓氏:")
            if first_name == '':
                print("请重新输入，再输入回车削你！")
            else:
                break
        print("请稍等，人员数据生成中…………")
        start_time = time.time()
        origin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        for i in range(person):
            if i < person:
                # man = fake.name_male()
                # 生成男人的名字，有概率生成女人的名字，这个方法其实不是很好
                phone = fake.phone_number()
                # 生成手机号码
                is_id = fake.ssn(min_age=19, max_age=45)
                date = is_id
                sex_id = date[-2]
                if int(sex_id) % 2 == 0:
                    man1 = women_name_choice(first_name)
                    while True:
                        man2 = women_name_choice(first_name)
                        if man1 == man2:
                            continue
                        else:
                            Name.append(str(man1))
                            break
                else:
                    man3 = man_name_choice(first_name)
                    while True:
                        man4 = man_name_choice(first_name)
                        if man3 == man4:
                            continue
                        else:
                            Name.append(str(man3))
                            break
                # 生成最小年龄为19岁，最大年龄为45岁的身份证号
                Phone.append(str(phone))
                ID.append(str('\n') + str(is_id))
                # \n换个行可使身份证号后几位不消失，变为文本显示
            else:
                break
    for n in ID:
        date = n
        year = date[7:11]
        month = date[11:13]
        date = date[13:15]
        birthday = year + '-' + month + '-' + date
        Birthday.append(str('\t') + birthday)
        '''提取身份证日期，然后输出为标准格式XXXX-XX-XX
        #日期显示与身份证同理，\t'''
    for y in ID:
        date_1 = y
        se_id = date_1[-2]
        if int(se_id) % 2 == 0:  # 身份证男女校验，身份证第17位数为奇数为男，偶数为女
            sex = "女"
            Sex.append(sex)
        else:
            sex = "男"
            Sex.append(sex)
    ALL = [[] for i in range(person)]
    # 设置一个二维数组
    for x in range(person):
        ALL[x].append(Name[x])
        ALL[x].append(Sex[x])
        ALL[x].append(ID[x])
        ALL[x].append(Phone[x])
        ALL[x].append(Birthday[x])
        # 二维数组循环插入，为导出CSV数据格式作准备
    export_data(ALL,person,start_time)

def start():
    print("<---------人员信息测试数据生成系统v1.3--------->")
    person_make()

start()

