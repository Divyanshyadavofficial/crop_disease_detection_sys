import streamlit as st
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from PIL import Image

# Load the trained model
@st.cache_resource
def load_trained_model():
    return load_model("rice_leaf_disease_model.h5")

model = load_trained_model()
class_labels = ['Bacterial Blight', 'Brown Spot', 'Leaf Smut']

# Prediction function
def predict(img):
    img = img.resize((128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    return class_labels[np.argmax(prediction)], prediction

# Streamlit UI
st.title("🌾 Rice Leaf Disease Detection")
st.write("Upload an image of a rice leaf to classify the disease.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Predict"):
        label, raw_preds = predict(img)
        st.success(f"Predicted Disease: **{label}**")
        st.write("Prediction Probabilities:")
        for i, prob in enumerate(raw_preds[0]):
            st.write(f"{class_labels[i]}: {prob:.4f}")
