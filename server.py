import base64
import cv2
import zmq

context = zmq.Context()
video_socket = context.socket(zmq.PUB)
video_socket.connect('ws://1.2.3.4:8888')

camera = cv2.VideoCapture(0)  # init the camera

while True:
    try:
        grabbed, frame = camera.read()  # grab the current frame
        frame = cv2.resize(frame, (640, 480))  # frame resizing
        encoded, buffer = cv2.imencode('.jpg', frame)
        img_as_text = base64.b64encode(buffer)
        video_socket.send(img_as_text)

    except KeyboardInterrupt:
        camera.release()
        cv2.destroyAllWindows()
        break
