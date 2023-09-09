f = open('mobydick.txt', 'r', encoding='utf-8')
mobydick_lines = f.readlines()
f.close()

f = open('middlemarch.txt', 'r', encoding='utf-8')
middlemarch_lines = f.readlines()
f.close()

# creates the small dataset - 1.46 GB
with open('small_dataset.txt', 'w', encoding='utf-8') as output_file:
    for i in range(500):
        output_file.writelines(middlemarch_lines)
        output_file.writelines(mobydick_lines)

# creates the 10x smaller dataset 149 MB
with open('smaller_dataset.txt', 'w', encoding='utf-8') as output_file:
    for i in range(50):
        output_file.writelines(middlemarch_lines)
        output_file.writelines(mobydick_lines)