import PIL
from PIL import Image
from PIL import ImageFilter
import os


def main():
    # path of the folder containing the raw images
    inPath = "/home/shaiful/Downloads/Annotation/WIN_20200713_18_47_02_Pro-20200715T185959Z-001/WIN_20200713_18_47_02_Pro"

    # path of the folder that will contain the modified image
    outPath = "/home/shaiful/Downloads/Annotation/WIN_20200713_18_47_02_Pro-20200715T185959Z-001/WIN_20200713_18_47_02_Pro_output"

    for imagePath in os.listdir(inPath):
        # imagePath contains name of the image
        inputPath = os.path.join(inPath, imagePath)
        basewidth = 600
        img = Image.open(inputPath)
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)

        fullOutPath = os.path.join(outPath, '' + imagePath)
        img.save(fullOutPath)

        # # inputPath contains the full directory name
        # img = Image.open(inputPath)
        #
        #
        # # fullOutPath contains the path of the output
        # # image that needs to be generated
        # img.rotate(270, expand = True).save(fullOutPath)

        print(fullOutPath)

    # Driver Function


if __name__ == '__main__':
    main()