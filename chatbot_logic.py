import json

def provide_emotional_first_aid(condition_names):
    """
    Provides a list of coping strategies and emotional first aid based on detected symptom clusters.
    """
    strategies = []
    
    for condition in condition_names:
        if condition == "Major Depressive Disorder":
            strategies.append(
                {
                    "title": "Coping with Low Mood",
                    "description": "It's okay to feel overwhelmed. Try to take a short walk outside or listen to some music. Even a small change in environment can help. Consider reaching out to a friend or family member for a brief chat."
                }
            )
        elif condition == "Generalized Anxiety Disorder":
            strategies.append(
                {
                    "title": "Managing Anxiety",
                    "description": "When you feel anxious, focus on your breathing. Try the '4-7-8' technique: inhale for 4 seconds, hold for 7, and exhale for 8. This can help calm your nervous system. Also, try to ground yourself by focusing on your five senses."
                }
            )
        elif condition == "Eating Disorders":
            strategies.append(
                {
                    "title": "Support for Eating-Related Challenges",
                    "description": "The relationship with food can be very difficult. Please reach out to a professional who can help you develop a healthier mindset. Focus on small, consistent habits rather than drastic changes."
                }
            )
        elif condition == "Social Anxiety Disorder":
            strategies.append(
                {
                    "title": "Handling Social Stress",
                    "description": "Take things one step at a time. If a social situation feels overwhelming, give yourself permission to step away for a moment. Remind yourself that you are safe and your feelings are valid. You can try practicing a short conversation with someone you trust first."
                }
            )
        elif condition == "Post-Traumatic Stress Disorder":
            strategies.append(
                {
                    "title": "Dealing with Traumatic Memories",
                    "description": "If you are having a difficult memory or flashback, try to focus on an object around you. Notice its color, shape, and texture. This can help bring you back to the present moment. Remember, it's not a sign of weakness to seek help."
                }
            )
    
    return strategies

def analyze_user_input(answers):
    """
    Analyzes the user's answers to determine potential symptom clusters and provides coping strategies.
    
    Args:
        answers (dict): A dictionary mapping question number to user's response.
    
    Returns:
        dict: A dictionary containing the most likely symptom clusters, a final message, and coping strategies.
    """
    symptom_scores = {
        "Major Depressive Disorder": 0,
        "Generalized Anxiety Disorder": 0,
        "Eating Disorders": 0,
        "Social Anxiety Disorder": 0,
        "Post-Traumatic Stress Disorder": 0,
    }
    
    # --- Scoring Logic (same as before) ---
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
        
    if "7" in answers and int(answers["7"]) > 3:
        symptom_scores["Generalized Anxiety Disorder"] += 3
    if "8" in answers and answers["8"].lower() in ["yes", "y"]:
        symptom_scores["Generalized Anxiety Disorder"] += 2
    if "9" in answers and answers["9"].lower() in ["yes", "y"]:
        symptom_scores["Generalized Anxiety Disorder"] += 1
    if "5" in answers and int(answers["5"]) > 3:
        symptom_scores["Generalized Anxiety Disorder"] += 1

    if "16" in answers and answers["16"].lower() in ["yes", "y"]:
        symptom_scores["Eating Disorders"] += 3
    if "17" in answers and answers["17"].lower() in ["yes", "y"]:
        symptom_scores["Eating Disorders"] += 3

    if "18" in answers and answers["18"].lower() in ["yes", "y"]:
        symptom_scores["Social Anxiety Disorder"] += 3
    if "19" in answers and answers["19"].lower() in ["yes", "y"]:
        symptom_scores["Social Anxiety Disorder"] += 3
    
    if "12" in answers and answers["12"].lower() in ["yes", "y"]:
        symptom_scores["Post-Traumatic Stress Disorder"] += 3
    
    # --- Evaluation ---
    threshold = 4
    potential_conditions = {
        condition: score for condition, score in symptom_scores.items() if score >= threshold
    }
    
    if not potential_conditions:
        response_message = "Thank you for sharing. Your responses do not indicate any major symptom clusters. If you're feeling low, remember it's always helpful to talk to someone."
        return {"result": "safe", "message": response_message, "conditions": [], "coping_strategies": []}
    
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
    
    # Get the coping strategies for the detected conditions
    coping_strategies = provide_emotional_first_aid(condition_names)
    
    return {
        "result": "symptom_detected",
        "message": response_message,
        "conditions": condition_names,
        "coping_strategies": coping_strategies
    }