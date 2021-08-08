import cv2
from pathlib import Path
import time
import sys

IMAGE_PATH = "imageData"
def mosaic(src, ratio=0.1):
    small = cv2.resize(src, None, fx=ratio, fy=ratio, interpolation=cv2.INTER_NEAREST)
    return cv2.resize(small, src.shape[:2][::-1], interpolation=cv2.INTER_NEAREST)

def mosaic_area(src, x, y, width, height, ratio=0.1):
    dst = src.copy()
    dst[y:y + height, x:x + width] = mosaic(dst[y:y + height, x:x + width], ratio)
    return dst

def img2mosaic(src, ratio=0.1):
    cascade_path = '/Users/e185746/OpenCV/opencv-4.5.1/data/haarcascades/haarcascade_frontalface_default.xml'
    cascade = cv2.CascadeClassifier(cascade_path)

    src_gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(src_gray)

    for x, y, w, h in faces:
        dst = mosaic_area(src, x, y, w, h, ratio)

    return dst

def main(fullpath, filename, image_path):
    print(filename)
    src = cv2.imread(fullpath)
    dst = img2mosaic(src, ratio=0.01)
    cv2.imwrite('mosaicData2/mosaic'+filename, dst)

if __name__ == "__main__":
    _, fullpath, filename, image_path = sys.argv
    main(fullpath, filename, image_path)