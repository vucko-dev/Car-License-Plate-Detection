import os
import shutil
import random

# Paths
dataset_path = "./data/"
images_path = os.path.join(dataset_path, "images")
annotations_path = os.path.join(dataset_path, "annotations")

# Output directories
output_dirs = {
    "train": "dataset/train",
    "valid": "dataset/valid",
    "test": "dataset/test"
}

# Create directories
for split in output_dirs.values():
    os.makedirs(os.path.join(split, "images"), exist_ok=True)
    os.makedirs(os.path.join(split, "annotations"), exist_ok=True)

# Get all image filenames
image_files = [f for f in os.listdir(images_path) if f.endswith(".png")]
random.shuffle(image_files)

# Split ratios
train_ratio = 0.7
valid_ratio = 0.2
test_ratio = 0.1

# Compute split indices
total = len(image_files)
train_idx = int(total * train_ratio)
valid_idx = train_idx + int(total * valid_ratio)

# Assign files
splits = {
    "train": image_files[:train_idx],
    "valid": image_files[train_idx:valid_idx],
    "test": image_files[valid_idx:]
}

# Move files
for split, files in splits.items():
    for file in files:
        shutil.copy(os.path.join(images_path, file), os.path.join(output_dirs[split], "images", file))
        shutil.copy(os.path.join(annotations_path, file.replace(".png", ".xml")), os.path.join(output_dirs[split], "annotations", file.replace(".png", ".xml")))

print("Dataset split complete!")
