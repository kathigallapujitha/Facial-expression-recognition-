# Facial Expression Recognition in Google Colab

# Step 1: Install required libraries
!pip install fer opencv-python-headless

# Step 2: Import libraries
import cv2
import matplotlib.pyplot as plt
from fer import FER
from google.colab import files

# Step 3: Upload image
uploaded = files.upload()

# Get uploaded file name
for filename in uploaded.keys():
    img_path = filename

# Step 4: Load image
img = cv2.imread(img_path)

# Convert BGR (OpenCV) to RGB (matplotlib)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 5: Initialize detector
detector = FER(mtcnn=True)  # mtcnn=True -> better face detection

# Step 6: Detect emotions
result = detector.detect_emotions(img_rgb)

# Show result
plt.imshow(img_rgb)
plt.axis("off")
plt.show()

if result:
    for face in result:
        emotions = face["emotions"]
        top_emotion = max(emotions, key=emotions.get)
        print("Predicted Expression:", top_emotion)
        print("All Emotions:", emotions)
else:
    print("No face detected!")
