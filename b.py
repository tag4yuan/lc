import time
import random
import string

# 生成所有大写字母的列表
letters = string.ascii_uppercase  # 'A' 到 'Z'

# 使用 for 循环输出随机字母，每隔5秒输出一次
for _ in range(3):  # 假设我们输出5个随机字母
    random_letter = random.choice(letters)  # 从字母表中随机选择一个字母
    print(random_letter)  # 输出随机字母
    time.sleep(5)  # 等待5秒钟,
