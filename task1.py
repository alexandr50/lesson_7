import os

pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'существует')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)
