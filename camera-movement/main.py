import cv2

cap = cv2.VideoCapture(0)

previous_frame = None
movement_threshold = 1000

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('movements.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if previous_frame is None:
        previous_frame = gray
        continue

    frame_delta = cv2.absdiff(previous_frame, gray)

    _, threshold = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)

    threshold = cv2.dilate(threshold, None, iterations=2)

    contours, _ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    movements_detected = False
    for contour in contours:
        if cv2.contourArea(contour) > movement_threshold:
            movements_detected = True
            break

    if movements_detected:
        out.write(frame)

    cv2.imshow('Webcam Movements', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()

cv2.destroyAllWindows()