# GazeCam 2.0

GazeCam 2.0 is an enhanced Python-based application utilizing OpenCV, dlib, and Pyglet for gaze-controlled interaction using a webcam. This version includes features such as blink detection, gaze tracking, and virtual keyboard interaction.

## Features

- **Blink Detection:** Detects blinking using the ratio of eye landmarks.
- **Gaze Detection:** Provides basic gaze direction estimation by tracking the position of the eye.
- **Virtual Keyboard Interaction:** Enables typing using gaze and blink actions on a virtual keyboard overlay.

## Requirements

- Python 3.x
- OpenCV
- dlib
- NumPy
- Pyglet

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
   Obtain the `shape_predictor_68_face_landmarks.dat` file from the [dlib website](http://dlib.net/files/). Place it in the root directory of the project.

4. **Prepare sound files:**
   Include `sound.wav`, `left.wav`, and `right.wav` for auditory feedback during interaction.

## Usage

1. Run the `main.py` file:
    ```bash
    python main.py
    ```

2. Ensure proper lighting and position yourself in front of the webcam.
3. Use gaze and blink actions to interact with the virtual keyboard.
4. See the overlaid visualizations on the webcam feed for eye detection and blinking.

## Acknowledgments

The project utilizes the following libraries:
- [OpenCV](https://opencv.org/)
- [dlib](http://dlib.net/)
- [Pyglet](https://pyglet.readthedocs.io/en/latest/)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests to enhance functionality or fix any bugs.

## License

This project is licensed under the [MIT License](LICENSE).
