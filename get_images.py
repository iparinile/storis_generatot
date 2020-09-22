from yandex_images import YandexImages
from editPic import edit_pic
import shutil


def get_images(keyword):
    img = YandexImages(1080, 1920)
    pics = img.get_images_by_keyword(keyword, 4)
    counter = 1
    list_of_img = []
    for pic in pics:
        pic = pic['image']
        pic_name = keyword + str(counter) + '.jpg'
        f = open(pic_name, 'wb')
        f.write(pic)
        f.close()
        edit_pic(pic_name, keyword)
        counter += 1
        list_of_img.append(pic_name)
        shutil.move(pic_name, 'static/images/')
    return list_of_img
