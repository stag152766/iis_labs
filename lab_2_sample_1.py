# Распознование лиц

import cv2


def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindow()


image_path = "c:\\python_\\ppp.png"
face_cascade = cv2.CascadeClassifier("c:\\python_\\haarcascade_frontalface_default.xml")  # ???
image = cv2.imread(image_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(1, 1)
)
faces_detected = "Лиц обнаружено: " + format(len(faces))
print(faces_detected)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
viewImage(image, faces_detected)