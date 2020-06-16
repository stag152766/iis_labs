# Работа с веб камерой

import cv2

cap = cv2.VideoCapture(0)

# прогрев камеры
for i in range(30):
    cap.read()

# делаем снимок
ret, frame = cap.read()

cv2.imshow("", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()

frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow("", frame2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# записываем в файл
cv2.imwrite('c:\\python_\\cam.png', frame)

cap.release()
