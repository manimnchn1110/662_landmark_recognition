#download one image and keep a small size
import pandas as pd
import requests as req
from PIL import Image
from io import BytesIO
import os

train_df = pd.read_csv('train.csv')
test_download = train_df.head()

#suitable download size
TARGET_SIZE = 128
IMG_QUALITY = 90
NUM_WORKERS = 8
error_download = 0

def image_download(df):
    global error_download
    os.mkdir("""train""")
    try:
        for i in range(len(df)):
            filename = "./train/{}.jpeg".format(str(df.id[i]))
            print('Detect the image id and generate filename:' + filename)
            path = df.url[i]
            print('Detect the image and download from' + path)
            response = req.get(path)
            pil_image = Image.open(BytesIO(response.content))
            pil_image_rgb = pil_image.convert('RGB')
            pil_image_resize = pil_image_rgb.resize((TARGET_SIZE, TARGET_SIZE))
            pil_image_resize.save(filename, quality=IMG_QUALITY)
    except:
        print('Fail to download the image.')
        error_download += 1
        pass
    return error_download



image_download(test_download)
