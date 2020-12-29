# -*-coding:utf-8-*-
from faker import Faker
import csv
import time
import numpy as np

def women_name():
    name = fake.first_name() + fake.first_name_female()
    return name
    # 姓氏方法+女性名称方法缝合,生成完美女性名字
def man_name():
    name = fake.first_name() + fake.first_name_male()
    return name
    # 男性名称同理女性完美名称
def person_make():
    global fake
    print("<---------人员信息测试数据生成系统v1.1--------->")
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
    print("请稍等,人员生成中………")
    start_time = time.time()
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
                man = women_name()
            else:
                man = man_name()
            # 生成最小年龄为19岁，最大年龄为45岁的身份证号
            Name.append(str(man))
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
    file = open("\\Users\cpr019\Desktop\PersonData.csv", "w", newline='', encoding="UTF-8-sig")
    # newline解决空白行问题
    fwrite = csv.writer(file)
    header = ["Name", "Sex", "ID", "Phone", "Birthday"]
    # 写入变量名
    fwrite.writerow(header)
    fwrite.writerows(ALL)
    # 写入数据
    file.close()
    end_time = time.time()
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
    print('Running time: %.2f 秒' % (end_time - start_time) + '\n')
    end=input("请按任意键退出,谢谢！")

person_make()
