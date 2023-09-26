import os
import json
import csv
import pickle

root_path = 'C:/Users/Ruslan/Desktop/myrep/OsnoviCompSetey/Dz2'

file_list = []
dir_list = []

def walk_through_dir(root_path):
    for root, dirs, files in os.walk(root_path):
        for _dir in dirs:
            dir_path = os.path.join(root, _dir)
            dir_list.append({
                'dir': dir_path.split('\\')[-2].split('/')[-1],
                'name': _dir,
                'type': 'directory',
                'size': os.path.getsize(dir_path)
            }
            )

        for file in files:
            file_path = os.path.join(root, file)
            file_list.append({
                'dir': file_path.split('\\')[-2].split('/')[-1],
                'name': file,
                'type': 'file',
                'size': os.path.getsize(file_path)
            }
            )

        return file_list + dir_list


def save_to_json(info_list: list[dict[str, str | int]]):
    with open('info_to_json.json', 'w', encoding='utf-8') as js_file:
        json.dump(info_list, js_file, indent=4, ensure_ascii=False)


def save_to_csv(df_list: list[dict[str, str | int]]):
    with open('info_to_csv.csv', 'w', newline='', encoding='utf-8') as csv_file:
        columns = ['dir', 'name', 'type', 'size']
        csv_writer = csv.DictWriter(csv_file, dialect='excel', fieldnames=columns)
        csv_writer.writeheader()
        csv_writer.writerows(df_list)


def save_to_pickle(data_lst: list[dict[str, str | int]]):
    with open('info_to_pickle.pickle', 'wb') as pickle_file:
        pickle.dump(data_lst, pickle_file)

# print(dir_list)
# print(file_list)
info_file = walk_through_dir(root_path)
save_to_json(info_file)
save_to_csv(info_file)
save_to_pickle(info_file)
print(info_file)