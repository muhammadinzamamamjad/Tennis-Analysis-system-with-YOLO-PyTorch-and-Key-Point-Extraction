import cv2
import supervision as sv

def read_video(video_path):
    cap = cv2.VideoCapture(video_path)
    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(frame)
    cap.release()
    return frames

def save_video(output_video_frames, output_video_path, input_video_path):
    video_info = sv.VideoInfo.from_video_path(video_path=input_video_path)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Correct codec for MP4
    out = cv2.VideoWriter(output_video_path, fourcc, video_info.fps, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
    
    for frame in output_video_frames:
        out.write(frame)
    
    out.release()