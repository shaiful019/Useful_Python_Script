import glob
import os

import cv2


save_path = 'cropped_data'
os.makedirs(save_path, exist_ok=True)
files_list = glob.glob('*.jpg')

for f in files_list:
    img = cv2.imread(f)
    f_name = f.split('.')[0]

    print(img.shape)

    with open(f'{f_name}.txt', 'r') as t:
        lines = t.readlines()
        print(lines)

        for idx, line in enumerate(lines):
            line = line.strip()
            yolo_list = line.split(' ')
            x, y, w, h = float(yolo_list[1]), float(yolo_list[2]), float(yolo_list[3]), float(yolo_list[4])
            x = int(x * img.shape[1])
            y = int(y * img.shape[0])
            w = int(w * img.shape[1]) // 2
            h = int(h * img.shape[0]) // 2

            # cv2.rectangle(img, (x - w, y - h), (x + w, y + h), (0, 255, 255), 3)
            cropped_img = img[y - h: y + h, x - w: x + w]
            cv2.imwrite(os.path.join(save_path, f'{f_name}_{idx}.jpg'), cropped_img)
