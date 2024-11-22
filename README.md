# Hand Mouse Controller

This project demonstrates a **Hand Mouse Controller** using a webcam and hand tracking. The application allows users to control the mouse cursor and perform mouse clicks with hand gestures detected in real-time.

## Features

- **Mouse Movement**: Use your hand gestures to move the cursor on the screen.
- **Left Click**: Bring the tips of your index fingers close together (if using two hands).
- **Right Click**: Pinch your thumb and middle finger together.
- **Real-time Tracking**: Uses a webcam feed to track hand gestures in real-time.

## Technologies Used

- **OpenCV**: For capturing and processing the webcam feed.
- **Mediapipe**: For robust hand tracking and gesture detection.
- **PyAutoGUI**: For controlling the mouse movements and clicks programmatically.
- **NumPy**: For efficient numerical computations.

## Requirements

Ensure you have the following Python libraries installed:

- OpenCV: `pip install opencv-python`
- Mediapipe: `pip install mediapipe`
- PyAutoGUI: `pip install pyautogui`
- NumPy: `pip install numpy`

## How to Run

1. Clone this repository or download the script file `import cv2.py`.
2. Ensure your system has a webcam connected.
3. Run the script:

   ```bash
   python import cv2.py
   ```

4. A window will open showing the webcam feed. Perform the gestures to control the mouse.

## Controls

- **Move Cursor**: Move your hand in front of the webcam.
- **Left Click**: Bring the tips of your index fingers close together (for two hands).
- **Right Click**: Pinch the thumb and middle finger together.

## Limitations

- Works best in a well-lit environment.
- May require some practice to perform gestures correctly.
- Detection might not work effectively with fast hand movements.
