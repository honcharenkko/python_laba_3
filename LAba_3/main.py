import face_recognition
import cv2

# Функція для розпізнавання облич з камери
def recognize_faces():
    # Використання першої доступної камери (0)
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("Error: Could not open video capture.")
        return

    while True:
        # Зчитування кадру з камери
        ret, frame = video_capture.read()

        if not ret:
            print("Error: Could not read frame from video capture.")
            break

        # Конвертація кольорового простору з BGR (OpenCV) в RGB (face_recognition)
        rgb_frame = frame[:, :, ::-1]

        # Отримання координат облич на кадрі
        face_locations = face_recognition.face_locations(rgb_frame)

        # Виведення кількості розпізнаних облич
        print(f"Number of faces detected: {len(face_locations)}")

        # Відображення кадру (без нанесення рамок)
        cv2.imshow('Video', frame)

        # Вихід з циклу при натисканні клавіші 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Закриття відеопотоку та вікна з відеопотоком
    video_capture.release()
    cv2.destroyAllWindows()

# Виклик функції для розпізнавання облич з камери
recognize_faces()

