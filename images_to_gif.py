import os
import imageio.v2 as imageio

output_dir = "DIC"
# Folder path containing the images
folder_path = output_dir

# Get the list of image file names in the folder
image_files = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

# Create a list to store the image data
images = []

# Read each image and append it to the list
for file in image_files:
    image_path = os.path.join(folder_path, file)
    image = imageio.imread(image_path)
    images.append(image)

# Specify the output file path for the GIF
output_path = f'{output_dir}.gif'

# Save the images as a GIF
imageio.mimsave(output_path, images, duration=0.01) 

#duration parameter specifies the display duration of each frame in the resulting GIF
#to have same speed as video --> duration = int (video_duration / fps)

print(f"GIF created and saved as '{output_path}'")
# In this code image files are converted into gif file
