# utils/color_utils.py

import cv2
import numpy as np
from sklearn.cluster import KMeans
from collections import Counter

def is_grayscale(image_path):
    img = cv2.imread(image_path)
    if len(img.shape) < 3:
        return True
    b, g, r = img[:, :, 0], img[:, :, 1], img[:, :, 2]
    return np.array_equal(b, g) and np.array_equal(b, r)

def extract_dominant_colors(image_path, num_colors=5):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Resize for faster processing
    image = cv2.resize(image, (150, 150))
    pixels = image.reshape((-1, 3))

    # KMeans to find dominant colors
    kmeans = KMeans(n_clusters=num_colors, random_state=0, n_init='auto')
    kmeans.fit(pixels)

    centers = kmeans.cluster_centers_.astype(int)
    counts = Counter(kmeans.labels_)

    # Sort by frequency
    sorted_colors = [tuple(centers[i]) for i in counts.keys()]
    
    # Convert RGB to HEX
    hex_colors = ['#%02x%02x%02x' % color for color in sorted_colors]
    return hex_colors
