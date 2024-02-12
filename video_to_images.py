import cv2

def extract_frames(video_path, output_folder, frame_interval):
    # Capture the video from the path provided
    video_capture = cv2.VideoCapture(video_path)
    
    # Initialize frame count
    count = 0
    saved_frame_count = 0
    
    # Check if video opened successfully
    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return
    
    # Loop through video frame by frame
    while video_capture.isOpened():
        # Read the frame
        ret, frame = video_capture.read()
        
        # If successfully read the frame
        if ret:
            # Check if the current frame number matches the interval
            if count % frame_interval == 0:
                # Save the current frame as an image
                cv2.imwrite(f"{output_folder}/frame_{saved_frame_count}.jpg", frame)
                saved_frame_count += 1
            count += 1
        else:
            break
    
    # When everything done, release the video capture object
    video_capture.release()
    print(f"Extracted {saved_frame_count} frames at an interval of {frame_interval} and saved to {output_folder}.")

# Specify the video file path, output folder, and the frame interval
video_path = '/path/to/your/video/file.mp4'
output_folder = '/path/to/output/folder'
frame_interval = 10 # adjust this number to change the interval

# Call the function with the frame interval
extract_frames(video_path, output_folder, frame_interval)
