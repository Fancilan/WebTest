from faker import Faker
import csv
import time
import numpy as np
#生成fake实例
fake = Faker(locale='zh_CN')
'''如果要生成中文的随机数据，我们可以在实例化时给locale参数传入‘zh_CN’这个值'''
Name=[]
Phone=[]
ID=[]
Birthday=[]
Sex=[]
print("<==========人员信息随机生成系统v1.0============>")
def Person_make():
    num=int(input("请输入您想生成人员采集的数量:"))
    Person=num
    time.sleep(1.5)
    print("请稍等,人员生成中………")
    time.sleep(1.5)
    start_time=time.time()
    for i in range(Person):
        if i<Person:
            man = fake.name()
            #生成男人的名字
            phone = fake.phone_number()
            #生成手机号码
            is_id = fake.ssn(min_age=19, max_age=45)
            #生成最小年龄为19岁，最大年龄为45岁的省份证号
            Name.append(str(man))
            Phone.append(str(phone))
            ID.append(str('\n')+str(is_id))

            #\n换个行可使身份证号后几位不消失，变为文本显示
        else:
            break
    for n in ID:
        date= n
        year = date[7:11]
        month = date[11:13]
        date = date[13:15]
        birthday = year + '-' + month + '-' + date
        Birthday.append(str('\t')+birthday)
        #提取身份证日期，然后输出为标准格式XXXX-XX-XX
        #日期显示与身份证同理，\t
    for y in ID:
        Date = y
        Sex_id = Date[17:18]
        if int(Sex_id) % 2 == 0:    #身份证男女校验，身份证第17位数为奇数为男，偶数为女
            sex="女"
            Sex.append(sex)
        else:
            sex="男"
            Sex.append(sex)

    All=[[] for i in range(Person)]
    #设置一个二维数组
    for x in  range(0,Person):
        All[x].append(Name[x])
        All[x].append(Sex[x])
        All[x].append(ID[x])
        All[x].append(Phone[x])
        All[x].append(Birthday[x])
    #二维数组循环插入，为导出CSV数据格式作准备

    file=open("PersonData.csv", "w", newline='', encoding="UTF-8-sig")
    #newline解决空白行问题
    fwrite=csv.writer(file)
    header=["Name","Sex","ID","Phone","Birthday"]
    #写入变量名
    fwrite.writerow(header)
    fwrite.writerows(All)
    #写入数据
    file.close()
    end_time=time.time()
    time.sleep(1.5)
    msg=str("人员采集数量设置成功:" +str(Person)+"人")
    print(msg)
    time.sleep(0.5)
    print(str("导出成功！"))
    time.sleep(1)
    print("人员信息预览:")
    print(np.array(All))
    print(str('\n'))
    time.sleep(1)
    print('Running time: %.2f Seconds'%(end_time-start_time) + '\n')
    input("请按任意键退出,谢谢！")
Person_make()