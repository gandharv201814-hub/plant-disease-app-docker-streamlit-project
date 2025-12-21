# Plant Disease Classifier

A full-stack machine learning project for **plant disease detection** using a fine-tuned MobileNetV2 model.  
This project includes **data augmentation**, a **Streamlit web app** for easy interaction, and **Docker support** for deployment.

---

## Features

- **Fine-tuned MobileNetV2**: Trained on plant leaf images for 38 disease categories.  
- **Data Augmentation**: Improves model generalization and accuracy.  
- **Streamlit Web App**: Upload leaf images and get instant disease predictions.  
- **Dockerized Deployment**: Run the app in a container anywhere without complex setup.  

---
**1. Web Application Home Page**  
Initial view of the Streamlit web application when it is first launched.

<img width="1066" height="361" alt="plant disease ss 1" src="https://github.com/user-attachments/assets/6ddd7960-5205-4664-99d5-7d0b02d6e637" />

---

**2. Image Upload Interface**  
User uploads a plant leaf image for disease prediction.

<img width="1063" height="539" alt="plant disease ss 2" src="https://github.com/user-attachments/assets/2fd4d219-de3a-48c6-aaa4-be4f9259f53f" />

---

**3. Disease Classification Result**  
Output displayed after clicking the **Classify** button, showing the predicted plant disease class.

<img width="1072" height="549" alt="plant disease ss 3" src="https://github.com/user-attachments/assets/a832f675-bd03-4b93-a22c-790a0d04a7a0" />

---

## Installation

### Clone the repository
```bash
git clone https://github.com/gandharv201814/plant-disease-app-docker-streamlit-project.git
cd plant-disease-app-docker-streamlit-project

---

plant-disease-app-docker-streamlit-project/
│
├── app.py                        # Streamlit web application
├── model/
│   └── plant_disease_prediction_model.h5   # Trained model
├── Dockerfile                     # Docker configuration
├── requirements.txt               # Project dependencies
├── data/                          # (Optional) sample images
└── README.md

