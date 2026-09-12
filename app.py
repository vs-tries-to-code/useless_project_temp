import os
import streamlit as st
from PIL import Image, ImageDraw
from google import genai
from google.genai import types
from pydantic import BaseModel, Field
from typing import List
from dotenv import load_dotenv
import json

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

st.title("Car eMotion")
st.write("Diagnose a car's emotional state and trace its facial features via upload or live camera.")

# Add a selection method for the user
input_method = st.radio("Choose input method:", ["Upload Image", "Use Live Camera"])

uploaded_file = None

if input_method == "Upload Image":
    uploaded_file = st.file_uploader("Choose a car image", type=["jpg", "jpeg", "png"])
else:
    uploaded_file = st.camera_input("Point your camera at a car (or a toy car/photo!)")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Selected Car", use_container_width=True)
    
if st.button("Diagnose Car Emotions") and uploaded_file is not None:
    with st.spinner("Analyzing headlights, grille, and existential dread..."):
        
        class Point(BaseModel):
            x: int = Field(description="X coordinate scaled 0 to 1000")
            y: int = Field(description="Y coordinate scaled 0 to 1000")

        class CarFacePolygons(BaseModel):
            left_headlight: List[Point] = Field(description="Contour points tracing the left headlight shape")
            right_headlight: List[Point] = Field(description="Contour points tracing the right headlight shape")
            logo: List[Point] = Field(description="Contour points tracing the car brand logo/nose")
            lower_grille_mouth: List[Point] = Field(description="Contour points tracing strictly the LOWER bumper air intake grille. DO NOT use the upper grille where the logo sits.")
            emotion_diagnosis: str = Field(description="What is this car feeling?")

        response = client.models.generate_content(
            model='gemini-3.6-flash',
            contents=[
                image, 
                (
                    "Trace the car face for a cartoon effect. "
                    "1. Left and right headlights (eyes). "
                    "2. Brand logo (nose). "
                    "3. LOWER bumper grille (mouth). IMPORTANT: Ignore the upper grille containing the logo; "
                    "the mouth must be the lower air intake grille closer to the bottom. "
                    "Provide a sequence of ordered polygon points (0-1000 scale) tracing the contour of each feature, "
                    "and give a hilarious translation of its expression, based on human experience. Keep the response as a funny one-liner."
                    "Example: This car just realised it was a second-hand."
                )
            ],
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=CarFacePolygons,
            ),
        )
        
        result_data = json.loads(response.text)
        img_width, img_height = image.size

        draw_image = image.copy()
        draw = ImageDraw.Draw(draw_image)

        def draw_organic_shape(point_list):
            pixel_points = [
                ((pt["x"] / 1000) * img_width, (pt["y"] / 1000) * img_height) 
                for pt in point_list
            ]
            
            draw.polygon(pixel_points, outline="white", width=9)
            
            draw.polygon(pixel_points, outline="#00FFFF", width=5)

        features = ["left_headlight", "right_headlight", "logo", "lower_grille_mouth"]
        for feature in features:
            if feature in result_data:
                draw_organic_shape(result_data[feature])

        # Display results side by side
        col1, col2 = st.columns(2)
        with col1:
            st.image(draw_image, caption="Contoured Car Face", use_container_width=True)
        with col2:
            st.subheader("Emotion Diagnosis")
            st.markdown(f"## {result_data['emotion_diagnosis']}")