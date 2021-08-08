
import cv2
from pathlib import Path
import time
import glob
import re
import subprocess

IMAGE_PATH = "Data"


def main():
    files = Path(IMAGE_PATH).glob("*.jpg")
    procs = []
    N = 20
    for file in files:
        proc = subprocess.Popen(["python", "sub.py", str(file), file.name, IMAGE_PATH])
        procs.append(proc)

        if len(procs) == N:
            for proc in procs:
                proc.communicate()
            procs.clear()
    for proc in procs:
        proc.communicate()


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print("Finished in {} seconds.".format(end-start))