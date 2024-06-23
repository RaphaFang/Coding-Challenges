import random
import string
import time

words = set()
while len(words) < 100000:
    word = ''.join(random.choices(string.ascii_lowercase, k=10))
    words.add(word)
    # words.append(word)

# start_time = time.time()
# list_to_set = set(words)
# set_time = time.time() - start_time

# search_word = random.choice(sett)

word_list = list(words)
# print(word_list)
word_set = set(words)
# print(word_set)
word_dict = {w:None for w in words}
# print(word_dict)

search_word = random.choice(word_list)

start_time = time.time()
found_in_list = search_word in word_list
list_time = time.time() - start_time

start_time = time.time()
found_in_set = search_word in word_set
set_time = time.time() - start_time

start_time = time.time()
found_in_dict = search_word in word_dict
dict_time = time.time() - start_time

print(f"List type searching spends: {list_time:.10f} sec")
print(f"Set type searching spends: {set_time:.10f} sec")
print(f"Dict type searching spends: {dict_time:.10f} sec")

# List type searching spends: 0.0026967525 sec
# Set type searching spends: 0.0000059605 sec
# Dict type searching spends: 0.0000019073 sec