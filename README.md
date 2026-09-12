<img width="1280" height="640" alt="git (1)" src="https://github.com/user-attachments/assets/8920b256-2ba8-4988-b824-5351134eb4bd" />



# Car eMotion 


## Basic Details
### Team Name: Audi Poyi


### Team Members
- Member 1: Vishnusree N

### Project Description
The project is a car empath which detects emotion of cars from their faces.

### The Problem (that doesn't exist)
Cars have feelings too. Humans need to be more empathetic.

### The Solution (that nobody asked for)
This application looks at the faces of cars, and translates what they feel.

## Technical Details
### Technologies/Components Used
For Software:
- Python 3.10
- Streamlit for UI
- Google GenAI API for the 
- PIL to save image and contour it
- pydantic to extract facial features


# Installation
```git clone https://github.com/vs-tries-to-code/useless_project_temp.git```
```pip install requirements.txt```


# Run
```streamlit run app.py```

### Project Documentation


```mermaid
flowchart TD
    A[User provides car image] --> A1{Input method}
    A1 -->|Upload| A2[File uploader]
    A1 -->|Live camera| A3[Camera input]
    A2 --> B[Image loaded with PIL]
    A3 --> B

    B --> C[Click 'Diagnose Car Emotions']
    C --> D[Send image + prompt to Gemini API]
    D --> E["Structured output schema (Pydantic)\nrequests 4 contours + emotion line"]
    E --> F[Gemini returns JSON:\nleft_headlight, right_headlight,\nlogo, lower_grille_mouth, emotion_diagnosis]

    F --> G[Scale each point set\nfrom 0-1000 range to actual image pixels]
    G --> H[Draw polygon outline\nfor each of the 4 features\non a copy of the image]

    H --> I[Display results]
    I --> I1[Left column: contoured car image]
    I --> I2[Right column: emotion diagnosis text]
```
# Screenshots (Add at least 3)
<img width="1178" height="850" alt="image" src="https://github.com/user-attachments/assets/35cd0658-0c86-47a5-a826-0f5de6bee673" />
Uploading car image

<img width="1018" height="507" alt="image" src="https://github.com/user-attachments/assets/b65f7d89-350a-4bca-9b5c-b4222c8d0c07" />
Emotion diagnosis


# Video
https://drive.google.com/file/d/1gstqzja9aatf7R7SEqk35XQFGAGbT02r/view?usp=drive_link
Video demonstrates the working of emotion diagnosis


## Team Contributions
Vishnusree - Idea
Google Gemini - its implementation


---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--26-26?link=https%3A%2F%2Ftinkerhub.org%2Fevents%2F1M8ORET9A1%2Fuseless-projects-3.0)



