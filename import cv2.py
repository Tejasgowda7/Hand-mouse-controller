import cv2
import mediapipe as mp
import pyautogui
import numpy as np

class HandMouseController:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7, min_tracking_confidence=0.5)
        self.mp_drawing = mp.solutions.drawing_utils
        self.screen_width, self.screen_height = pyautogui.size()
        self.margin = 20  # Set a margin to avoid corners

    def run(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame from webcam.")
                break

            frame = cv2.flip(frame, 1)  # Flip the frame horizontally
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
            result = self.hands.process(rgb_frame)  # Process the frame

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
                self.handle_landmarks(result.multi_hand_landmarks, frame)

            cv2.imshow('Hand Mouse Controller', frame)
            if cv2.waitKey(1) & 0xFF == 27:  # Press 'ESC' to exit
                break

        cap.release()
        cv2.destroyAllWindows()

    def handle_landmarks(self, multi_hand_landmarks, frame):
        if len(multi_hand_landmarks) == 2:
            hand1_landmarks = multi_hand_landmarks[0].landmark
            hand2_landmarks = multi_hand_landmarks[1].landmark

            # Get landmarks for index fingers
            hand1_index_finger_tip = hand1_landmarks[8]
            hand2_index_finger_tip = hand2_landmarks[8]

            # Calculate distance between index fingers
            index_fingers_distance = ((hand1_index_finger_tip.x - hand2_index_finger_tip.x) ** 2 +
                                      (hand1_index_finger_tip.y - hand2_index_finger_tip.y) ** 2) ** 0.5

            # Perform left click if index fingers are close
            if index_fingers_distance < 0.05:
                pyautogui.mouseDown()
                pyautogui.mouseUp()

        for hand_landmarks in multi_hand_landmarks:
            index_finger_tip = hand_landmarks.landmark[8]
            middle_finger_tip = hand_landmarks.landmark[12]
            thumb_tip = hand_landmarks.landmark[4]

            # Calculate distances to determine pinch gesture
            middle_thumb_distance = ((middle_finger_tip.x - thumb_tip.x) ** 2 + (middle_finger_tip.y - thumb_tip.y) ** 2) ** 0.5

            # Move cursor when index and middle fingers are together
            x = int(index_finger_tip.x * frame.shape[1])
            y = int(index_finger_tip.y * frame.shape[0])
            screen_x = np.clip(np.interp(x, (0, frame.shape[1]), (self.margin, self.screen_width - self.margin)), self.margin, self.screen_width - self.margin)
            screen_y = np.clip(np.interp(y, (0, frame.shape[0]), (self.margin, self.screen_height - self.margin)), self.margin, self.screen_height - self.margin)
            pyautogui.moveTo(screen_x, screen_y)

            # Perform right click if middle finger and thumb are pinched
            if middle_thumb_distance < 0.05:
                pyautogui.click(button='right')

if __name__ == "__main__":
    controller = HandMouseController()
    controller.run()
