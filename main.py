from PIL import Image
from PIL import ImageFilter
import numpy as np
import os


folder = "bst img/1"; #1 or 2
files = os.listdir(folder);

images = list();

for f in files:
    img = Image.open(folder + "/" + f, mode="r");
    img = img.filter(ImageFilter.SHARPEN);
    img = img.filter(ImageFilter.SHARPEN);
    img = img.filter(ImageFilter.DETAIL);
    img = img.filter(ImageFilter.DETAIL);
    images.append(img);

IMG = images[0];
IMG.putalpha(255);
for i, img in enumerate(images[1:]):
    img.putalpha(255-i*5);
    IMG.paste(img);
IMG.show()
images[0].show()