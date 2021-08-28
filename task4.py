import os
files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append(os.stat(file_path).st_size)
max_size = max(files)
i = 1
dict_1 = {}
for _ in range(len(str(max_size))):
    i *= 10
    dict_1[i] = 0
print(dict_1)
for file in files:
    dict_1[10 ** len(str(file))] += 1
print(dict_1)

