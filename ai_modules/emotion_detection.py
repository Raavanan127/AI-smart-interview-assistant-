import cv2

def detect_emotion():
    cam = cv2.VideoCapture(0)
    face = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face.detectMultiScale(gray, 1.3, 5)
    cam.release()

    if len(faces) > 0:
        return "🙂 Neutral/Focused"
    return "😐 No face detected"