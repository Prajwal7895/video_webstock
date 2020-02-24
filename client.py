import cv2
import zmq
import base64
import numpy as np

context = zmq.Context()
video_socket = context.socket(zmq.SUB)
video_socket.bind('ws://1.2.3.4:8888')
video_socket.setsockopt_string(zmq.SUBSCRIBE, np.unicode(''))

while True:
    try:
        frame = video_socket.recv_string()
        img = base64.b64decode(frame)
        npimg = np.fromstring(img, dtype=np.uint8)
        source = cv2.imdecode(npimg, 1)
        cv2.imshow("Stream", source)
        cv2.waitKey(1)

    except KeyboardInterrupt:
        cv2.destroyAllWindows()
        break
