# 2.1 Написать программу на языке Python для ручного выделения
# (прямоугольной рамкой разных цветов) на изображении различных объектов: машин, людей, фонарей…
import cv2

st = []
image = cv2.imread("C:\\python_\\cp.jpg")
cv2.imshow('image', image)


def click_event(event, x, y, flag, param):
    global st
    if event == cv2.EVENT_LBUTTONDOWN:
        st = [(x, y)]
    if event == cv2.EVENT_LBUTTONUP:
        st.append((x, y))
        cv2.rectangle(image, st[0], st[1], (222, 255, 0), 2)
        cv2.imshow('image', image)


cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()
