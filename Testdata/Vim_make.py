import random
import time
import getpass
def random_vin():
# 内容的权值
	content_map = {
	    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
	    'F': 6, 'G': 7, 'H': 8, 'I': 0, 'J': 1, 'K': 2, 'L': 3,
	    'M': 4, 'N': 5, 'O': 0, 'P': 7, 'Q': 8, 'R': 9, 'S': 2, 'T': 3,
	    'U': 4, 'V': 5, 'W': 6, 'X': 7, 'Y': 8, 'Z': 9, "0": 0, "1": 1,
	    "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9
	}
	# 位置的全值
	location_map = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]
	vin = ''.join(random.sample('0123456789ABCDEFGHJKLMPRSTUVWXYZ', 17))
	num = 0
	for i in range(len(vin)):
	    num = num + content_map[vin[i]] * location_map[i]
	vin9 = num % 11
	if vin9 == 10:
	    vin9 = "X"
	list1 = list(vin)
	list1[8] = str(vin9)
	vin = ''.join(list1)
	return vin

def vin_make():
	num=int(input("请输入您想要生成vin码的个数："))
	time.sleep(1)
	print("请稍等，生成中……")
	cal = str(time.strftime("%Y-%m-%d", time.localtime())) + '-' + str(''.join(random.sample('0123456789', 5)))
	user_name = getpass.getuser()  # 获取当前用户名
	data_name = 'C:\\Users\\' + user_name + '\\Desktop\\vim_data_' + cal + '.txt'
	file = open(data_name, "w", encoding="UTF-8-sig")
	start_time = time.time()
	origin_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	for n in range(num):
		if n<num:
			res = random_vin()
			file.write(res+'\n')
			# print(res)
			# time.sleep(0.5)
		else:
			break
	end_time = time.time()
	final_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
	time.sleep(1)
	print("导出成功Success！导出文件在根目录下")
	print('Running time: %.2f Seconds' % (end_time - start_time) + '\n')
	print('程序开始时间：' + origin_time)
	print('程序结束时间：' + final_time)
	file.close()
	time.sleep(1)
	print("文件路径:" + data_name)
	time.sleep(1.5)
	end = int(input("请问还要继续生成VIN数据么？\n1.是\n2.否\n:"))
	if end == 1:
		vin_make()
	else:
		eend = input("请按任意键退出,谢谢！")

def start():
	print("<-----------汽车Vin码生成器v1.1----------->")
	vin_make()



start()