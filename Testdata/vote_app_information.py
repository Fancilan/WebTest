# -*-coding:utf-8-*-
import csv
import getpass
import random
import time
import numpy as np
from faker import Faker
import RandomName
from Testdata.common import fake_data
from tqdm import tqdm

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
def women_name_random():
    name = fake_data.random_firstname() + fake.first_name_female()
    return name
    # 自定义姓氏+女名
def man_name_random():
    name = fake_data.random_firstname() + fake.first_name_male()
    return name
    # 百家姓+男名

def export_data(ALL,person,start_time):
    cal = str(time.strftime("%Y-%m-%d", time.localtime())) +'-' +str(''.join(random.sample('0123456789',6)))
    user_name = getpass.getuser()# 获取当前用户名
    data_name = 'C:\\Users\\' + user_name +'\\Desktop\\data_'+ cal +'.csv'
    file = open(data_name, "w", newline='', encoding="UTF-8-sig")
    # newline解决空白行问题
    fwrite = csv.writer(file)
    header = ["province", "school", "grade", "name", "email"]   #["province", "school", "grade", "name", "email"]
    fwrite.writerow(header)
    print("第二阶段数据写入中………")
    time.sleep(1)
    for o in tqdm(range(1)):
        fwrite.writerows(ALL)
        time.sleep(0.01)
    end_time = time.time()
    final_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    file.close()
    time.sleep(0.5)
    msg = str("人员数量:" + str(person) + "人,写入完成！")
    print(msg)
    time.sleep(0.5)
    # print("人员信息预览:")
    # print(np.array(ALL))
    # print(str('\n'))
    # time.sleep(1)
    print('开始时间：' + origin_time)
    print('结束时间：' + final_time)
    print('总耗时长: %.3f 秒' % (end_time - start_time) + '\n')
    time.sleep(0.5)
    print(str("导出成功Success!"))
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
    global Name,Phone,Birthday,Sex,ID,Province,School,Grade,Mail,person
    # 生成fake实例
    fake = Faker(locale='zh_CN')
    '''如果要生成中文的随机数据，我们可以在实例化时给locale参数传入‘zh_CN’这个值'''
    Name = []
    Phone = []
    ID = []
    Birthday = []
    Sex = []
    Province = []
    School = []
    Grade = []
    Mail = []
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
        elif int(num) >= 100000:
            print("人员数量超过最大生成限制，请重新输入！")
        else:
            break
    person = int(num)
    time.sleep(0.5)
    print("1.自定义姓氏模式\n2.百家姓模式")
    select = int(input("请选择您要生成人员的信息的模式:"))
    time.sleep(0.5)
    if select == 2:
        start_time = time.time()
        origin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print("请稍后，人员数据生成中…………")
        for o in tqdm(range(person)):
            for i in range(person):
                if i < person:
                    man = man_name_random()
                    # 生成男人的名字，有概率生成女人的名字，这个方法其实不是很好
                    Name.append(man)
                    pro = fake_data.random_province()
                    Province.append(pro)  # 省份
                    sch = fake_data.random_school()
                    School.append(sch)
                    gra = fake_data.random_class()
                    Grade.append(gra)
                    email = fake_data.random_email()
                    Mail.append(email)
                    # \n换个行可使身份证号后几位不消失，变为文本显示
                else:
                    break
            time.sleep(0.01)
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
    ALL = [[] for i in range(person)]
    # 设置一个二维数组
    for x in range(person):
        ALL[x].append(Province[x])
        ALL[x].append(School[x])
        ALL[x].append(Grade[x])
        ALL[x].append(Name[x])
        ALL[x].append(Mail[x])
    print("第一阶段数据生成完成！")
    time.sleep(0.5)
    export_data(ALL,person,start_time)

if __name__ == '__main__':
    print("<--------人员信息测试数据生成系统--------->")
    person_make()



