# 2.2 Самостоятельно изучить библиотеки и модули (Keras, ImageAI, RetinaNet и др.)
# для автоматического распознавания на изображении типовых объектов:
# автомобилей, людей, дорожных знаков, собак, кошек…
# Написать программу для автоматического распознавания на изображении
# типовых объектов на основе применения готовых библиотек Python.

from imageai.Detection import ObjectDetection
import os

exec_path = os.getcwd()

detector = ObjectDetection()

detector.setModelTypeAsRetinaNet()

detector.setModelPath(
    os.path.join(exec_path, "resnet50_coco_best_v2.0.1.h5")
)

detector.loadModel()

list = detector.detectObjectsFromImage(
    input_image=os.path.join(exec_path, "cp.jpg"),
    output_image_path=os.path.join(exec_path, "new_cp.jpg")
)