# Tennis Analysis Project

This project is focused on analyzing tennis videos, detecting keypoints, and tracking the ball and players. It uses deep learning models and custom utility scripts to process and extract meaningful statistics from match footage.


## Folder Descriptions

- **constants/**: Contains constant values and utility functions related to court dimensions and lines.
  - `court_line_detector.py`: Responsible for detecting court lines using predefined constants.
  
- **court_line_detector/**: Includes scripts for detecting court lines in the input videos.
  
- **input_videos/**: This folder contains the input media for analysis.
  - `input_video.mp4`: The primary video file for processing.
  - `image.png`: Sample image related to the input video.
  
- **mini_court/**: Handles the logic related to the smaller representation of the tennis court.
  - `mini_court.py`: Script to handle operations on the mini-court representation.
  
- **models/**: Pre-trained models used for detecting keypoints and objects.
  - `keypoints_model.pth`: The model used for detecting keypoints on the tennis court.
  - `yolo5_last.pt`: YOLOv5 model used for object detection (e.g., tennis ball and players).
  - Both of these models are stored at drived. linked is placed in the txt file.
  
- **output_videos/**: Contains processed video outputs after analysis.
  - `output_video.mp4`: Video with analysis results in MP4 format.
  
- **tracker_stubs/**: Placeholder files for storing tracking data.
  - `ball_detections.pkl`: Stores ball detection data.
  - `player_detections.pkl`: Stores player detection data.
  
- **trackers/**: Scripts to track the ball and players throughout the video.
  - `ball_tracker.py`: Tracks the tennis ball in the video.
  - `player_tracker.py`: Tracks players' movements in the video.
  
- **training/**: Jupyter notebooks and models used for training the ball and court keypoint detectors.
  - `tennis_ball_detector_training.ipynb`: Notebook for training the tennis ball detection model.
  - `tennis_court_keypoints_training.ipynb`: Notebook for training the court keypoint model.
  
- **utils/**: Contains various utility scripts to assist with video processing, drawing, and conversions.
  - `bbox_utils.py`: Bounding box utilities for object detection.
  - `conversions.py`: Functions for converting between various formats (e.g., coordinates).
  - `player_stats_drawer_utils.py`: Handles drawing player statistics on video frames.
  - `video_utils.py`: Contains utilities for video processing.
  - `full-size-tennis-court-dimensions.png`: Image file showing the full tennis court dimensions used as reference.
  
- **main.py**: The main entry point for running the tennis analysis program.

- **yolo_inference.py**: Script for running YOLO model inference on input videos.

- **yolov8x.pt**: YOLOv8 model file used for object detection.

## Usage Instructions

1. Place your input video files in the `input_videos/` folder.
2. Run `main.py` to start the analysis on the video.
3. Output videos will be generated in the `output_videos/` folder.

## Model Training

- Use the Jupyter notebooks in the `training/` folder to retrain the ball and keypoint detection models.

## Requirements

Make sure you have installed all necessary dependencies:
- PyTorch
- OpenCV
- YOLOv5
- Supervision
- pandas
- numpy

