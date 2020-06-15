# 2.1 Написать программу на языке Python для ручного выделения
# (прямоугольной рамкой разных цветов) на изображении различных объектов: машин, людей, фонарей…

import cv2 as cv22

def click_event(event, x, y, flag, param):
    if event == cv22.EVENT_LBUTTONDOWN:
        print(x, ', ', y)
        font = cv22.FONT_HERSHEY_SIMPLEX
        strXY = str(x) + ', ' + str(y)
        cv22.rectangle('image', (x, y), (15, 15), (222, 255, 0), -1)
        #cv22.putText(img, strXY, (x, y), font, 1, (222, 255, 0), 2)
        cv22.imshow('image', img)


img = cv22.imread("C:\\python_\\cp.jpg")
cv22.imshow('image', img)

cv22.setMouseCallback('image', click_event)

cv22.waitKey(0)

cv22.destroyAllWindows()