import os
path = input('enter the path you want to search in: ')
all_files = [os.path.join(file) for root, dir, files in os.walk(path) for file in files if file.endswith('.pdf')]

print(f'Number of files is {len(all_files)}')
for file in all_files:
    print(file)

