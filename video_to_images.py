import cv2
import os

video_name = "DIC"
video_path = f"{video_name}.MP4"
cap = cv2.VideoCapture(video_path)

# Check if the video file is valid
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get the frame rate (FPS) of the video
fps = int(cap.get(cv2.CAP_PROP_FPS))

# Calculate the total number of frames in the video
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Specify the desired number of images to capture
desired_num_images = 100
# desired_num_images = frame_count # if you don't want to skip any frame

# Calculate the skip frames based on the total frame count and desired number of images
skip_frames = max(1, frame_count // desired_num_images)

# Calculate the video duration in seconds
video_duration = frame_count / fps



print(f"Frame Rate (FPS): {fps}")
print(f"Total Frames: {frame_count}")
print(f"Video Duration (seconds): {video_duration}")

if not os.path.exists(f"{video_name}"):
    os.makedirs(f"{video_name}")

i = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        if i % skip_frames == 0:
            # Generate the image filename based on the desired pattern
            image_number = i // skip_frames
            image_filename = f"{video_name}/image_{image_number:05}.png"
            cv2.imwrite(image_filename, frame)
        i += 1
    else:
        break
    if i >= desired_num_images*skip_frames:
        break

cap.release()
cv2.destroyAllWindows()
