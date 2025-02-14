import subprocess
import os

def create_virtcam(video_nr):
    device_path = f'/dev/video{video_nr}'
    if not os.path.exists(device_path):
        print(f"Creating it at {device_path}...")
        try:
            subprocess.run([
                'sudo', 'modprobe', '-v', 'v4l2loopback', 
                f'video_nr={video_nr}', 
                'card_label="Virtual"', 
                'exclusive_caps=1'
            ], check=True)
            print("Virtual Camera created successfully.")
            return True
        except subprocess.CalledProcessError as e:
            print(f"Error: {e}")
            return False
    else:
        print(f"Virtual Camera already exists at {device_path}.")
        return True
