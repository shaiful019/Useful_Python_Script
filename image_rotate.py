from PIL import Image
from PIL import ImageFilter
import os


def main():
    # path of the folder containing the raw images
    inPath = "/home/shaiful/Downloads/test/image-20200706T132248Z-001/image/IMG_7447"

    # path of the folder that will contain the modified image
    outPath = "/home/shaiful/Downloads/test/image-20200706T132248Z-001/image/IMG_7447_output"

    for imagePath in os.listdir(inPath):
        # imagePath contains name of the image
        inputPath = os.path.join(inPath, imagePath)

        # inputPath contains the full directory name
        img = Image.open(inputPath)

        fullOutPath = os.path.join(outPath, ''+ imagePath)
        # fullOutPath contains the path of the output
        # image that needs to be generated
        img.rotate(270, expand = True).save(fullOutPath)

        print(fullOutPath)

    # Driver Function


if __name__ == '__main__':
    main()