import cv2
import tensorflow as tf
# from tflite_runtime.interpreter import Interpreter
import numpy as np
import sys
import matplotlib.pyplot as plt

modelPath = sys.argv[1]
imagePath = sys.argv[2]

interpreter = tf.lite.Interpreter(model_path = modelPath)
# from tflite_runtime.interpreter import Interpreter
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

image = cv2.imread(imagePath, cv2.IMREAD_COLOR)

heightAndWidth = 300

image = image[0:300, 0:300]
input_data = image.reshape((1, 300, 300, 3)).astype(np.float32)
input_data = cv2.normalize(input_data, None, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
# print(input_data)
interpreter.set_tensor(input_details[0]['index'], input_data)
# plt.imshow(image)
# plt.show()
interpreter.invoke()

detection_boxes = interpreter.get_tensor(output_details[0]['index'])[0]
detection_classes = interpreter.get_tensor(output_details[1]['index'])[0].astype(np.uint8) + 1
detection_scores = interpreter.get_tensor(output_details[2]['index'])[0]
boxCount = int(interpreter.get_tensor(output_details[3]['index'])[0])
print(detection_boxes)
print(detection_classes)
print(detection_scores)
print(boxCount)

for i in range(boxCount) :
    if (detection_scores[i] > 0.5) :

        yUp = int(heightAndWidth * detection_boxes[i][0])
        xLeft = int(heightAndWidth * detection_boxes[i][1])
        yDown = int(heightAndWidth * detection_boxes[i][2])
        xRight = int(heightAndWidth * detection_boxes[i][3])

        # print(f"f{yUp}, {xLeft}, {yDown}, {xRight}")
        # print(f"({xLeft}, {xRight}) ({yUp}, {yDown})")

        cv2.rectangle(image, (xLeft, yUp), (xRight, yDown), (0, 255, 0), 2)

        text = f"{detection_scores[0]: .2f}"
        cv2.putText(image, text, (xLeft, yUp), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.8, (0, 0, 255), 1, cv2.LINE_4)

plt.imshow(image)
plt.show()