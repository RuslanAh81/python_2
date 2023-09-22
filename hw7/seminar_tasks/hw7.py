import os

def group_rename(wanted_name: str, count_nums, extention_old: str, extention_new: str, _range: list[int], my_path : str ='.'):
    count = 1
    file_list = os.listdir(my_path)
    print(file_list)
    for file_name in os.listdir(my_path):
        # print(my_path, file_name)
        if file_name.endswith(extention_old):
            last_name = os.path.splitext(file_name)[0]
            last_name = last_name[_range[0]:_range[1] + 1] if _range else ''
            print(last_name)
            new_name = f'{last_name}{wanted_name}{str(count).zfill(count_nums)}{extention_new}'
            count += 1
            os.rename(os.path.join(my_path, file_name), os.path.join(my_path, new_name))


if __name__ == '__main__':
    group_rename('YOGA', 3, '.bmp', '.txt', [1, 3], 'mix')