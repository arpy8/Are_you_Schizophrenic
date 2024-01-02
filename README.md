# Are you Schizophrenic ?
 
## Overview
This repository contains a simple app I made as a fun side project for detecting schizophrenia based on the number of people in an image or video frame. The app uses YOLOv5, a deep learning model for object detection, to count the number of people present. The user can either upload an image or use their camera for real-time detection.

## To run the app locally:
1. Clone the repository:
   ```bash
   git clone https://github.com/arpy8/Are_you_Schizophrenic.git
   cd Are_you_Schizophrenic
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run main.py
   ```

4. Choose the input source (Image or Camera) and follow the on-screen instructions.

## Dependencies
- Python 3.6+
- OpenCV
- PyTorch
- NumPy
- Streamlit
- Pillow

## App Structure
- `main.py`: The main Streamlit app script.
- `requirements.txt`: List of Python dependencies.
- `README.md`: This file providing information about the repository.
- `yolov5l.pt`: Weights for the yolo model.

## Usage Instructions
1. Choose between "Image" or "Camera" as the input source.
2. If using an image, upload the image and specify the expected number of people.
3. If using the camera, specify the expected number of people in the frame.
4. Click the "Detect" button to initiate the schizophrenia detection process.
5. The app will display processing information, and the results will be shown.

## Acknowledgments
This app utilizes the YOLOv5 model for object detection. Check out the [YOLOv5 repository](https://github.com/ultralytics/yolov5) for more details.

## Disclaimer
This app is a simplified demonstration and not a diagnostic tool. The detection mechanism is based on the number of people in the input, and its accuracy may vary. It is not a substitute for professional medical advice.

## Author
- Username: [arpy8](https://github.com/arpy8)

Feel free to contribute, report issues, or provide suggestions for improvement!
