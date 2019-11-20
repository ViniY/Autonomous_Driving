from PIL import Image
import os
import pandas as pd
from matplotlib import pyplot as plt
from pandas._libs.parsers import CParserError

PATH = '/Users/vini/Desktop/Autonomous_Driving'


def load_csv(path):
    df = pd.DataFrame
    # try:
    #     csv_path = path + "/train.csv"
    #     print(csv_path)
    #     df = pd.read_csv(path,sep=',')
    #     print(df.head(10))
    # except CParserError:
    #     print("Something wrong the file")
    # return df

    csv_path = path + '/train.csv'
    print(csv_path)
    df = pd.read_csv(csv_path,engine='python')
    print(df.head(10))


def load_image():
    img_dict= {}
    img_list = []
    image_fold = PATH + '/train_images'
    entries = os.listdir(image_fold)
    print(entries)

    for name in entries:
        # print(name)
        # print("--"*80)
        if ".DS_Store" in name:
            continue
        img_address = image_fold + "/" + name
        img = Image.open(img_address)
        img_list.append(img)
        img_dict[name] = img
        # imgplot = plt.imshow(img)
        # plt.show()
    print(len(img_list))
    print("*" * 40)
    img = img_list[100]

    width = 374
    height = 300

    img = img.resize((width, height), Image.LANCZOS)  # best down-sizing filter
    area = (0, height*1/3, width, height)  # left upper right lower
    print(area)
    cropped_img = img.crop(area)
    # print(type(cropped_img))
    # print("=="*40)
    # width, height = img.size
    # print("width = " + str(width))
    # print("height = " + str(height))
    # imgplot = plt.imshow(img)

    # imgplot = plt.imshow(cropped_img)

    cropped_img.show()

    print("--" * 40)
    print(len(img_dict))


# def cut_img(img_list):



    return
# def load_img(path):
#     img_dict = {}
#     entries = os.listdir(path)
#     print(entries)
#
#     img_list = []
#     for name in entries:
#         address = "E:\Kaggle\\train\\" + name
#         # img = cv2.imread(address, 0)
#
#         img = Image.open(address)
#         img = img.resize((width, height), Image.LANCZOS)  # best down-sizing filter
#         img_list.append(img)
#         img_dict[name] = img
#         # imgplot = plt.imshow(img)
#         # plt.show()
#     print("--" * 40)
#     print(len(img_dict))



def main():
    load_csv(PATH)
    load_image()

if __name__ == '__main__':
    print(os.listdir(PATH))
    main()
    # PATH = '/Users/vini/Desktop/Autonomous Driving'

