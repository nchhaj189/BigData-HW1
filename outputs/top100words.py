import time

# 20 file dataset top 100 calculation
word_counter = {}
start_time = time.time()
with open('20files_wordcount_output.txt', 'r', encoding='utf-8') as output_file:
    lines = output_file.readlines()
    for line in lines:
        word, count = line.split('\t', 1)
        word_counter[word] = int(count)

sorted_word_count = sorted(word_counter.items(), key=lambda x: (-x[1], x[0]))

with open('20files_top100.txt', 'w', encoding='utf-8') as output_file:
    for i in range(100):
        output_file.write(f"{sorted_word_count[i][0]}\t{sorted_word_count[i][1]}\n")
    final_time = time.time() - start_time
    output_file.write(f"20 file top 100 calculation runtime: {final_time} seconds")
    print(f"20 file top 100 calculation runtime: {final_time} seconds")


# 40 file dataset top 100 calculation
word_counter = {}
start_time = time.time()
with open('40files_wordcount_output.txt', 'r', encoding='utf-8') as output_file:
    lines = output_file.readlines()
    for line in lines:
        word, count = line.split('\t', 1)
        word_counter[word] = int(count)

sorted_word_count = sorted(word_counter.items(), key=lambda x: (-x[1], x[0]))

with open('40files_top100.txt', 'w', encoding='utf-8') as output_file:
    for i in range(100):
        output_file.write(f"{sorted_word_count[i][0]}\t{sorted_word_count[i][1]}\n")
    final_time = time.time() - start_time
    output_file.write(f"40 file top 100 calculation runtime: {final_time} seconds")
    print(f"40 file top 100 calculation runtime: {final_time} seconds")


# 95 file dataset top 100 calculation
word_counter = {}
start_time = time.time()
with open('95files_wordcount_output.txt', 'r', encoding='utf-8') as output_file:
    lines = output_file.readlines()
    for line in lines:
        word, count = line.split('\t', 1)
        word_counter[word] = int(count)

sorted_word_count = sorted(word_counter.items(), key=lambda x: (-x[1], x[0]))

with open('95files_top100.txt', 'w', encoding='utf-8') as output_file:
    for i in range(100):
        output_file.write(f"{sorted_word_count[i][0]}\t{sorted_word_count[i][1]}\n")
    final_time = time.time() - start_time
    output_file.write(f"95 file top 100 calculation runtime: {final_time} seconds")
    print(f"95 file top 100 calculation runtime: {final_time} seconds")