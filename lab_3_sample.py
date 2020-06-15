from tkinter import messagebox
import cv2 as cv22
import time


# time.sleep(5)
def viewImage(image, name_of_window):
    cv22.namedWindow(name_of_window, cv22.WINDOW_AUTOSIZE)
    cv22.imshow(name_of_window, image)
    cv22.waitKey(0)
    cv22.destroyAllWindows()


# messagebox.showinfo("1", "2")
image = cv22.imread("C:\\python_\\kras.jpg")
viewImage(image, "")
h, w, channels = image.shape
print("{0}, {1}, {2}".format(w, h, channels))
image2 = image[50:h - 50, 50:w - 50]
# viewImage(image2, "")
# print(image2)
scale_percent = 250  # изменение размера изображения. в процентах
w2 = int(image.shape[1] * scale_percent / 100)
h2 = int(image.shape[0] * scale_percent / 100)
dim = (w2, h2)
image3 = cv22.resize(image, dim)
# viewImage(image3, "")
image5 = cv22.transpose(image)  # поворот на 90 градусов
# viewImage(image5, "")
# cv22.imwrite("C:\\python_\\cat3.png", image5)
image5 = cv22.flip(image, 1)  # зеркальное отражение по горизонтали
# viewImage(image5, "")
image5 = cv22.flip(image, 0)  # зеркальное отражение по вертикали
# viewImage(image5, "")
center = (w // 2, h // 2)
M = cv22.getRotationMatrix2D(center, 180, 1.0)
image4 = cv22.warpAffine(image, M, (w, h))
# viewImage(image4, "")
image7 = cv22.cvtColor(image, cv22.COLOR_BGR2GRAY)  # серое
# viewImage(image7, "")
try:
    h, w, channels = image7.shape
    print(image7.shape)
except:
    h, w = image7.shape
    print(image7.shape)

ret, image7 = cv22.threshold(image7, 127, 255, 0)  # черно-белое
# viewImage(image7, "")
image8 = image.copy()
cv22.rectangle(image8, (10, 10), (150, 70), (0, 0, 255), 2)  # (w, h) схема не RGB, а BGR. 2 - толщина
cv22.line(image8, (10, 10), (150, 70), (0, 0, 255), 2)  # (w, h) схема не RGB, а BGR. 2 - толщина
cv22.putText(image8, "my cat", (150, 70), cv22.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
# (w, h)  - левый нижний угол, 1 - размер, 3 - толщина букв
image8[70:h - 10, 150:150 + 20] = (255, 0, 0)  # [h1:h2, x1:x2]


# print(image8[70, 150])
# viewImage(image8, "")
def drawTarget2():
    st.remove(1)


def drawTarget(img, x, y, radius):
    # print(1)
    if (st.count(1) == 0):
        st.append(1)
    if (x > 100):
        cv22.circle(img, (x, y), radius, mycolor, -1)  # -1 сплошная заливка
        print(st)
    else:
        b = str(img[y, x][0])
        g = str(img[y, x][1])
        r = str(img[y, x][2])
        mycolor_temp = (int(b), int(g), int(r))
        cv22.rectangle(img, (0, 0), (15, 15), mycolor_temp, -1)


def myMouseCallback(event, x, y, flags, img):
    if event == cv22.EVENT_LBUTTONDOWN:
        print("{} * {}".format(x, y))
        drawTarget(img[0], x, y, 5)
        print(img[1])
    if event == cv22.EVENT_MOUSEMOVE:
        if (st.count(1) > 0):
            drawTarget(img[0], x, y, 5)
    if event == cv22.EVENT_LBUTTONUP:
        drawTarget2()


image = cv22.imread("C:\\python_\\kras.jpg")
image2 = image.copy()
# 0..15 - текущий цвет. 20..35 - пипетка. 40-... другие цвета
mycolor = (255, 0, 0)
cv22.rectangle(image, (0, 0), (15, 15), mycolor, -1)  # -1 закрашенный
st = []

wy_color_rect_size = 15
y_start = 40
w_start = 0
mycolor_temp_b = 0
mycolor_temp_g = 0
mycolor_temp_r = 0
for mycolor_temp_b in range(0, 256, 127):
    for mycolor_temp_g in range(0, 256, 127):
        for mycolor_temp_r in range(0, 256, 127):
            mycolor_temp = (mycolor_temp_b, mycolor_temp_g, mycolor_temp_r)
            cv22.rectangle(image, (w_start, y_start), (w_start + wy_color_rect_size, y_start + wy_color_rect_size),
                           mycolor_temp, -1)  # -1 закрашенный
            y_start = y_start + wy_color_rect_size + 5
    w_start = w_start + wy_color_rect_size + 5
    y_start = 40
cv22.namedWindow("cat", cv22.WINDOW_AUTOSIZE)
cv22.setMouseCallback("cat", myMouseCallback, (image, st))
while True:
    image2 = image.copy()
    cv22.imshow("cat", image2)
    c = cv22.waitKey(33)  # 33 мс будет держаться изображение. 30 кадров в секунду
    if (c == 27):
        # если нажата ESC - выходим
        break
    if (c != -1):
        print(c)
    mycolor = (int(str(image[5, 5][0])), int(str(image[5, 5][1])), int(str(image[5, 5][2])))
    # print(st)

    if (c == ord('R')) or (c == ord('r')):
        mycolor = (0, 0, 255)
        cv22.rectangle(image, (0, 0), (15, 15), mycolor, -1)
    if (c == ord('G')) or (c == ord('g')):
        mycolor = (0, 255, 0)
        cv22.rectangle(image, (0, 0), (15, 15), mycolor, -1)
    if (c == ord('B')) or (c == ord('b')):
        mycolor = (255, 0, 0)
        cv22.rectangle(image, (0, 0), (15, 15), mycolor, -1)

cv22.destroyWindow("cat")

cv22.namedWindow("my", cv22.WINDOW_AUTOSIZE)
cap = cv22.VideoCapture("C:\\python_\\sber.mp4")

for i in range(0, 10):
    print(i, ' ', cap.get(i))
'''
3   640.0
4   240.0
5   25.0
'''
while True:
    # получаем следующий кадр
    ret, frame = cap.read()

    cv22.imshow("my", frame)
    c = cv22.waitKey(33)
    if (c == 27):  # если нажата ESC - выходим
        break

# освобождаем ресурсы
cap.release()
# удаляем окно
cv22.destroyWindow("my")
