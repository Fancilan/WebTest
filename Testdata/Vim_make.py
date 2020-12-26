import random
import time
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

def Vin_make():
	print("<-----------汽车Vin码生成器v1.0----------->")
	num=int(input("请输入您想要生成vin码的个数："))
	time.sleep(1)
	print("请稍等，生成中……")
	file = open("VinData.txt", "w", encoding="UTF-8-sig")
	start_time = time.time()
	for n in range(num):
		if n<num:
			res = random_vin()
			file.write(res+'\n')
			# print(res)
			# time.sleep(0.5)
		else:
			break
	end_time = time.time()
	time.sleep(1)
	print("导出成功Success！")
	print('Running time: %.2f Seconds' % (end_time - start_time) + '\n')
	file.close()
	end=input("按任意键退出程序！")

Vin_make()
