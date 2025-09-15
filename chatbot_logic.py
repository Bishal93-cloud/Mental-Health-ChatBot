import json

def get_questions():
    
    questions = [
        "On a scale of 1-5, how would you describe your overall mood in the last two weeks? (1=very low, 5=very high)",
        "Have you noticed any significant changes in your sleep patterns? (yes/no)",
        "Have you experienced a change in your appetite or weight recently? (yes/no)",
        "Do you find yourself losing interest or pleasure in activities you used to enjoy? (yes/no)",
        "How would you describe your energy levels on a scale of 1-5? (1=very low, 5=very high)",
        "Do you have feelings of sadness, hopelessness, or worthlessness that don't seem to go away? (yes/no)",
        "How often do you feel anxious or worried about things? (1=rarely, 5=all the time)",
        "Are you having trouble concentrating or making decisions? (yes/no)",
        "Do you feel more irritable or easily frustrated than usual? (yes/no)",
        "Have you had any thoughts of harming yourself or others? (yes/no)",
        "How are you coping with daily stress? (1=not well, 5=very well)",
        "Have you experienced any recent traumatic or stressful events? (yes/no)",
        "How are your relationships with family and friends? (1=poor, 5=great)",
        "Do you ever feel overwhelmed by your emotions? (yes/no)",
        "What are some of your biggest challenges right now? (1=few, 5=many)",
        "Do you often find yourself overly concerned with your body weight, shape, or appearance? (yes/no)",
        "Have you recently engaged in extreme dieting, binge eating, or forced vomiting? (yes/no)",
        "Do you feel a strong fear of being judged or scrutinized by others in social situations? (yes/no)",
        "Do you avoid social gatherings or public speaking because of intense anxiety? (yes/no)"
    ]
    return questions

def analyze_user_input(answers):
    """
    Analyzes the user's answers to determine potential symptom clusters.
    
    Args:
        answers (dict): A dictionary mapping question number to user's response.
        Example: {1: "4", 2: "yes", 3: "no", ...}
    
    Returns:
        dict: A dictionary containing the most likely symptom clusters and a final message.
    """
    symptom_scores = {
        "Major Depressive Disorder": 0,
        "Generalized Anxiety Disorder": 0,
        "Eating Disorders": 0,
        "Social Anxiety Disorder": 0,
        "Post-Traumatic Stress Disorder": 0,
    }
    
    # --- Scoring Logic ---
    
    # Major Depressive Disorder Symptoms
    if "1" in answers and int(answers["1"]) < 3:
        symptom_scores["Major Depressive Disorder"] += 2
    if "4" in answers and answers["4"].lower() in ["yes", "y"]:
        symptom_scores["Major Depressive Disorder"] += 3
    if "6" in answers and answers["6"].lower() in ["yes", "y"]:
        symptom_scores["Major Depressive Disorder"] += 3
    if "5" in answers and int(answers["5"]) < 3:
        symptom_scores["Major Depressive Disorder"] += 2
    if "2" in answers and answers["2"].lower() in ["yes", "y"]:
        symptom_scores["Major Depressive Disorder"] += 1
        
    # Generalized Anxiety Disorder Symptoms
    if "7" in answers and int(answers["7"]) > 3:
        symptom_scores["Generalized Anxiety Disorder"] += 3
    if "8" in answers and answers["8"].lower() in ["yes", "y"]:
        symptom_scores["Generalized Anxiety Disorder"] += 2
    if "9" in answers and answers["9"].lower() in ["yes", "y"]:
        symptom_scores["Generalized Anxiety Disorder"] += 1
    if "5" in answers and int(answers["5"]) > 3:
        symptom_scores["Generalized Anxiety Disorder"] += 1

    # Eating Disorder Symptoms
    if "16" in answers and answers["16"].lower() in ["yes", "y"]:
        symptom_scores["Eating Disorders"] += 3
    if "17" in answers and answers["17"].lower() in ["yes", "y"]:
        symptom_scores["Eating Disorders"] += 3

    # Social Anxiety Disorder Symptoms
    if "18" in answers and answers["18"].lower() in ["yes", "y"]:
        symptom_scores["Social Anxiety Disorder"] += 3
    if "19" in answers and answers["19"].lower() in ["yes", "y"]:
        symptom_scores["Social Anxiety Disorder"] += 3
    
    # Post-Traumatic Stress Disorder Symptoms
    if "12" in answers and answers["12"].lower() in ["yes", "y"]:
        symptom_scores["Post-Traumatic Stress Disorder"] += 3
    
    # --- Evaluation ---
    threshold = 4
    potential_conditions = {
        condition: score for condition, score in symptom_scores.items() if score >= threshold
    }
    
    # --- Generate the Final Response with Elaborations ---
    if not potential_conditions:
        response_message = "Thank you for sharing. Your responses do not indicate any major symptom clusters. If you're feeling low, remember it's always helpful to talk to someone."
        return {"result": "safe", "message": response_message, "conditions": []}
    
    sorted_conditions = sorted(potential_conditions.items(), key=lambda item: item[1], reverse=True)
    condition_names = [condition[0] for condition in sorted_conditions]
    
    elaboration = ""
    for condition in condition_names:
        if condition == "Major Depressive Disorder":
            elaboration += "The analysis showed a pattern of low mood, loss of interest in activities, and feelings of sadness, which are key indicators of depression.\n\n"
        elif condition == "Generalized Anxiety Disorder":
            elaboration += "Your responses indicated frequent worry, difficulty concentrating, and feelings of restlessness, which are common signs of generalized anxiety.\n\n"
        elif condition == "Eating Disorders":
            elaboration += "Your concerns about body image and changes in eating habits were noted, which are significant symptoms of an eating disorder.\n\n"
        elif condition == "Social Anxiety Disorder":
            elaboration += "The analysis indicated a fear of social situations and a tendency to avoid them, which are primary symptoms of social anxiety.\n\n"
        elif condition == "Post-Traumatic Stress Disorder":
            elaboration += "Your response about a traumatic event is a key factor in the symptoms of PTSD.\n\n"

    response_message = (
        "Based on your responses, you are experiencing symptom clusters related to the following conditions:\n\n"
        + elaboration
        + "It is very important to remember that this chatbot is not a substitute for a medical professional. Please consider speaking with a qualified therapist or doctor for a proper diagnosis and personalized treatment plan."
    )
    
    return {"result": "symptom_detected", "message": response_message, "conditions": condition_names}


if __name__ == '__main__':
    print("Welcome to the mental health chatbot. Please answer the following questions.")
    
    questions = get_questions()
    user_answers = {}
    
    for i, question in enumerate(questions, 1):
        print(f"\nQ{i}: {question}")
        answer = input("Your answer: ")
        
        # --- Input Validation ---
        if i in [2, 3, 4, 6, 8, 9, 10, 12, 14, 16, 17, 18, 19]:
            while answer.lower() not in ['yes', 'y', 'no', 'n']:
                print("Invalid input. Please answer with 'yes' or 'no'.")
                answer = input("Your answer: ")
        else: # For numerical answers
            while True:
                try:
                    num = int(answer)
                    if 1 <= num <= 5:
                        break
                    else:
                        print("Invalid input. Please enter a number from 1 to 5.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
                answer = input("Your answer: ")
        
        user_answers[str(i)] = answer.strip().lower()
    
    print("\nThank you for your answers. Let me analyze your responses.")
    
    final_result = analyze_user_input(user_answers)
    
    print("\n--- Analysis Result ---")
    print(final_result["message"]) # Print only the message for a cleaner output