import os
import subprocess
import glob

# Setup paths
SRC_DIR = 'assets/gallery'
DEST_DIR = 'assets/processed'

# Ensure destination exists
os.makedirs(DEST_DIR, exist_ok=True)

# Get all HEIC files and sort them
files = sorted(glob.glob(os.path.join(SRC_DIR, '*.HEIC')))

print(f"Found {len(files)} files.")

# Define series mapping (3 images per series for 5 series)
# We have exactly 15 files, so 15 / 5 = 3 images per series.
images_per_series = 3

for i, input_path in enumerate(files):
    series_index = (i // images_per_series) + 1
    image_index = (i % images_per_series) + 1
    
    output_filename = f"series{series_index}_{image_index}.jpg"
    output_path = os.path.join(DEST_DIR, output_filename)
    
    print(f"Processing {input_path} -> {output_path}...")
    
    # Run sips command
    # sips -Z 1200 -s format jpeg input --out output
    # -Z 1200 maintains aspect ratio with max dimension 1200
    cmd = [
        'sips',
        '-Z', '1200',
        '-s', 'format', 'jpeg',
        input_path,
        '--out', output_path
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error converting {input_path}: {result.stderr}")
    else:
        print("Done.")

print("All images processed.")
