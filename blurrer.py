import cv2
from os import listdir
from os.path import isfile, join

data_in = "in/"
data_out = "out/"

images = [f for f in listdir(data_in) if isfile(join(data_in, f))]

index = 0
for image in images:
    img = cv2.imread(data_in + image)

    size = img.shape
    padding = int(size[1] / 20)
    blurred_img = img[padding : size[0] - padding, padding : size[1] - padding]

    blurred_size = blurred_img.shape
    blurred_img = cv2.GaussianBlur(blurred_img, (201, 201), 50)

    img[padding : blurred_size[0] + padding, padding : blurred_size[1] + padding] = blurred_img

    cv2.imwrite(data_out + str(index) + ".jpg", img)
    index += 1
