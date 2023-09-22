# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки


from pathlib import Path

VIDEO_DIRECT = 'video'
IMAGE_DIRECT = 'images'
TEXT_DIRECT = 'documents'
AUDIO_DIRECT = 'mp3'
VIDEO_EXTENTIONS = ('.mp4', '.avi', '.mkv')
AUDIO_EXTENTIONS = ('.mp3', 'flask')
IMAGE_EXTENTIONS = ('.jpg', '.bmp')
TEXT_EXTENTIONS = ('.txt', '.doc', '.docx')

def check_directory(curr_direct):
    # print('я тут')
    # _path = pathlib.Path(curr_direct)
    list_of_dirr = [item.name for item in curr_direct.iterdir() if item.is_dir()]
    if not VIDEO_DIRECT in list_of_dirr:

        Path.mkdir(curr_direct / VIDEO_DIRECT)
    if not IMAGE_DIRECT in list_of_dirr:
        Path.mkdir(curr_direct / IMAGE_DIRECT)
    if not TEXT_DIRECT in list_of_dirr:
        Path.mkdir(curr_direct / TEXT_DIRECT)
    if not AUDIO_DIRECT in list_of_dirr:
        Path.mkdir(curr_direct / AUDIO_DIRECT)


def sort_files(direct_name: str):
    curr_direct = Path.cwd()
    direct_path = curr_direct / direct_name
    print(direct_path)
    check_directory(direct_path)

    for items in direct_path.iterdir():
        if items.suffix in VIDEO_EXTENTIONS:
            items.replace(direct_path / VIDEO_DIRECT / items.name)
        elif items.suffix in IMAGE_EXTENTIONS:
            items.replace(direct_path / IMAGE_DIRECT / items.name)
        elif items.suffix in TEXT_EXTENTIONS:
            items.replace(direct_path / TEXT_DIRECT / items.name)
        elif items.suffix in AUDIO_EXTENTIONS:
            items.replace(direct_path / AUDIO_DIRECT / items.name)


if __name__ == '__mane__':
    sort_files('mix')
