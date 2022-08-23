import cv2
import os

xml_path = "./haarcascade_frontalface_alt2.xml"
face_cascade = cv2.CascadeClassifier(xml_path)

path = "./data"
for folder in os.listdir(path):
    sub_path = path + "/" + folder
    for img in os.listdir(sub_path):
        image_path = sub_path + "/" + img
        img_read = cv2.imread(image_path)
        # faces = face_cascade.detectMultiScale(img_read)
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(img_read, (x, y), (x + w, y + h), (0, 0, 255), 2)
        #     faces = img_read[y:y + h, x:x + w]
        #     cv2.imwrite(image_path, faces)
        #     print(image_path)
