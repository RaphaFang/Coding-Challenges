import random
import string
import time

# start_time = time.time()
# words = set()
# while len(words) < 100000:
#     word = ''.join(random.choices(string.ascii_lowercase, k=10))
#     words.add(word)
# # set_time = time.time() - start_time


# word_list = list(words)

# search_word = random.choice(word_list)


# start_time = time.time()
# found_in_list = search_word in words
# set_time = time.time() - start_time

# print(f"直接生成 set 的时间: {set_time:.10f} 秒")



# words = []
# while len(words) < 100000:
#     word = ''.join(random.choices(string.ascii_lowercase, k=10))
#     words.append(word)

# sett = set(words)

# search_word = random.choice(words)

# start_time = time.time()
# found_in_list = search_word in sett
# set_time = time.time() - start_time

# print(f"将 list 转换为 set 的时间: {set_time:.10f} 秒")

# 0.2025821209 (創立set) + 0.0008018017(搜尋set)
print(0.2025821209 + 0.0008018017 )

# 0.2165329456(創立list) + 0.0106906891(轉換) + 0.0000009537(搜尋set) = 
print(0.2165329456 + 0.0106906891 + 0.0000009537)
