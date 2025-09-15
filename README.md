# Mental Health Chatbot API

This repository contains the core AI logic and API for a mental health support chatbot. The chatbot analyzes user-provided symptoms and suggests potential symptom clusters (e.g., depression, anxiety) in a safe and non-diagnostic manner. It is designed to be integrated into a larger application backend.

---

### Features
- **Symptom Analysis**: Analyzes user responses to identify patterns associated with common psychological conditions.
- **Rule-Based System**: Uses a simple, robust rule-based scoring system.
- **API Endpoint**: Exposes the analysis logic through a RESTful API for easy integration.
- **Educational Output**: Provides elaborate, non-diagnostic feedback and encourages users to seek professional help.

---

### Prerequisites
- Python 3.x
- pip (Python package installer)
- virtualenv (recommended for environment isolation)

---

### Setup and Installation
1.  **Clone the Repository**:
    ```bash
    git clone [https://github.com/Bishal93-cloud/Mental-Health-ChatBot.git](https://github.com/Bishal93-cloud/Mental-Health-ChatBot.git)
    cd Mental-Health-ChatBot
    ```

2.  **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment**:
    - On Windows:
    ```bash
    .\venv\Scripts\activate
    ```
    - On macOS/Linux:
    ```bash
    source venv/bin/activate
    ```

4.  **Install Dependencies**:
    ```bash
    pip install flask
    ```

---

### Running the Server
To start the API, run the following command from the root directory of the project:

```bash
python api_server.py
```

---

### API Usage
The chatbot's logic is exposed via a RESTful API endpoint. Your backend should make a `POST` request to this endpoint.

- **Endpoint**: `/analyze_symptoms`
- **Method**: `POST`
- **URL**: `http://localhost:5000/analyze_symptoms` (when running locally)

#### Request Body
The endpoint expects a JSON object with the user's answers. The keys are question numbers (as strings, "1" to "19") and the values are the user's responses.

**Example Request:**
```json
{
    "1": "4",
    "2": "no",
    "3": "yes",
    "4": "yes",
    "5": "2",
    "6": "yes",
    "7": "4",
    "8": "yes",
    "9": "no",
    "10": "no",
    "11": "3",
    "12": "yes",
    "13": "4",
    "14": "yes",
    "15": "5",
    "16": "yes",
    "17": "no",
    "18": "yes",
    "19": "yes"
}
```

---

#### Response Body
The API will return a JSON object with the analysis result.

**Example Response:**
```json
{
    "conditions": [
        "Generalized Anxiety Disorder",
        "Major Depressive Disorder"
    ],
    "message": "Based on your responses, you are experiencing symptom clusters related to the following conditions:\n\nYour responses indicated frequent worry, difficulty concentrating, and feelings of restlessness, which are common signs of generalized anxiety.\n\nYour responses indicated a pattern of low mood, loss of interest in activities, and feelings of sadness, which are key indicators of depression.\n\nIt is very important to remember that this chatbot is not a substitute for a medical professional. Please consider speaking with a qualified therapist or doctor for a proper diagnosis and personalized treatment plan.",
    "result": "symptom_detected"
}
```

---

### Frontend Questions
Your friend can use the following questions for the frontend. The questions are numbered to correspond with the keys in the API request body.

1.  On a scale of 1-5, how would you describe your overall mood in the last two weeks? (1=very low, 5=very high)
2.  Have you noticed any significant changes in your sleep patterns? (yes/no)
3.  Have you experienced a change in your appetite or weight recently? (yes/no)
4.  Do you find yourself losing interest or pleasure in activities you used to enjoy? (yes/no)
5.  How would you describe your energy levels on a scale of 1-5? (1=very low, 5=very high)
6.  Do you have feelings of sadness, hopelessness, or worthlessness that don't seem to go away? (yes/no)
7.  How often do you feel anxious or worried about things? (1=rarely, 5=all the time)
8.  Are you having trouble concentrating or making decisions? (yes/no)
9.  Do you feel more irritable or easily frustrated than usual? (yes/no)
10. Have you had any thoughts of harming yourself or others? (yes/no)
11. How are you coping with daily stress? (1=not well, 5=very well)
12. Have you experienced any recent traumatic or stressful events? (yes/no)
13. How are your relationships with family and friends? (1=poor, 5=great)
14. Do you ever feel overwhelmed by your emotions? (yes/no)
15. What are some of your biggest challenges right now? (1=few, 5=many)
16. Do you often find yourself overly concerned with your body weight, shape, or appearance? (yes/no)
17. Have you recently engaged in extreme dieting, binge eating, or forced vomiting? (yes/no)
18. Do you feel a strong fear of being judged or scrutinized by others in social situations? (yes/no)
19. Do you avoid social gatherings or public speaking because of intense anxiety? (yes/no)
