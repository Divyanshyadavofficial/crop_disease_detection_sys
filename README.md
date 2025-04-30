# crop_disease_detection_sys
# 🌿 Plant Disease Detection using CNN

This project is a Convolutional Neural Network (CNN)-based plant disease classification system. It detects three common rice leaf diseases — **Bacterial Blight**, **Brown Spot**, and **Leaf Smut** — using image classification techniques with TensorFlow and Keras.

---

## 📁 Dataset

The dataset is sourced from **Mendeley Data** and consists of 3 categories:

- `Bacterial Blight`
- `Brown Spot`
- `Leaf Smut`

Each category contains multiple labeled leaf images.  
You can organize the dataset as:

dataset/ ├── Bacterial Blight/ ├── Brown Spot/ └── Leaf Smut/

🧪 Model Architecture

Input: 128x128 RGB images
2 Convolutional Layers + MaxPooling
Dense Layer with Dropout
Output: 3-Class Softmax

Accuracy: ~90%+ (may vary depending on training duration and data balance)
Loss: Depends on epochs and batch size


🧠 Future Improvements

Add more disease categories
Deploy with Streamlit or Flask
Implement Mobile App version
Add Grad-CAM visualization to highlight disease areas
