# 1. Написать программу для распознавания лица и глаз человека.
# Для решения задачи использовать библиотеку машинного зрения OpenCV и каскады Хаара.
# Лицо и глаза человека должны быть выделены на фотоизображении прямоугольными рамками.
# Предусмотреть возможность обнаружения на фотоизображении нескольких людей.
# Фотоизображение должно быть захвачено с web-камеры.
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

for i in range(30):
    cap.read()

ret, frame = cap.read()


def viewImage(name_of_window, image):
    cv2.namedWindow(name_of_window, cv2.WINDOW_AUTOSIZE)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


face_cascade = cv2.CascadeClassifier("c:\\python_\\haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('c:\\python_\\haarcascade_eye.xml')
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(1, 1)
)
faces_detected = "Faces detected: " + format(len(faces))
print(faces_detected)

for (x, y, w, h) in faces:
    frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 0), 2)
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = frame[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
viewImage(faces_detected, frame)

cv2.imwrite('c:\\python_\\cam.png', frame)

cap.release()
cv2.destroyAllWindows()
