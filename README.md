# GazeCam

GazeCam is a Python-based application using OpenCV and dlib for gaze-controlled interaction using your webcam. This project enables basic eye tracking and blinking detection using facial landmarks.

## Features

- **Blink Detection:** Detects blinking using the ratio of eye landmarks.
- **Gaze Detection:** Provides basic gaze direction estimation by tracking the position of the eye.

## Requirements

- Python 3.x
- OpenCV
- dlib
- NumPy

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/parth-nikam/GazeCam.git
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download dlib's pre-trained facial landmark predictor:**
   You can obtain the `shape_predictor_68_face_landmarks.dat` file from the [dlib website](http://dlib.net/files/). Place it in the root directory of the project.

## Usage

1. Run the `main.py` file:
    ```bash
    python main.py
    ```

2. Ensure proper lighting and position yourself in front of the webcam.
3. The application will display your webcam feed with overlaid visualizations for eye detection and blinking.

## Acknowledgments

The project utilizes the following libraries:
- [OpenCV](https://opencv.org/)
- [dlib](http://dlib.net/)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance the functionality or fix any bugs.

## License

This project is licensed under the [MIT License](LICENSE).
