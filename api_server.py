from flask import Flask, request, jsonify, session
from chatbot_logic import analyze_user_input, provide_emotional_first_aid

# You'll now define the questions directly in this file
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

# Initialize the Flask application
app = Flask(__name__)
# The secret key is essential for enabling sessions
app.secret_key = 'your_super_secret_key'

@app.route('/start', methods=['GET'])
def start_chat():
    """Starts a new chat session and sends the initial greeting."""
    session.clear() # Clear any previous session data
    session['state'] = 'initial_greeting'
    session['answers'] = {}
    return jsonify({
        "message": "Hi there! I'm a mental health assistant. Are you facing any psychological issues or mind-related problems?",
        "status": "continue"
    })

@app.route('/chat', methods=['POST'])
def chat():
    """Handles the full conversational flow, from questions to analysis."""
    user_input = request.json.get('message', '').strip().lower()
    current_state = session.get('state', 'initial_greeting')
    
    if current_state == 'initial_greeting':
        if user_input in ["yes", "y", "i am", "yeah"]:
            session['state'] = 'in_conversation'
            session['question_number'] = 1
            return jsonify({
                "message": "I'm sorry to hear that. I can ask you a few questions to understand how you are feeling. Let's begin. \n\nQ1: " + questions[0],
                "status": "continue_with_questions"
            })
        elif user_input in ["hello", "hi", "hey"]:
            return jsonify({
                "message": "Hi there! Are you facing any psychological issues or mind-related problems?",
                "status": "continue"
            })
        else:
            return jsonify({
                "message": "I'm sorry, I didn't get that. To begin, please tell me if you are facing any psychological issues.",
                "status": "continue"
            })
    
    elif current_state == 'in_conversation':
        q_num = session.get('question_number')
        user_answers = session.get('answers', {})
        
        # Save the answer to the current question
        user_answers[str(q_num)] = user_input
        session['answers'] = user_answers
        
        next_q_num = q_num + 1
        
        if next_q_num <= len(questions):
            # Send the next question
            session['question_number'] = next_q_num
            return jsonify({
                "message": f"Q{next_q_num}: {questions[next_q_num - 1]}",
                "status": "continue_with_questions"
            })
        else:
            # All questions have been answered, time to analyze
            result = analyze_user_input(user_answers)
            session.clear() # Clear the session after the conversation is complete
            return jsonify(result)

    return jsonify({"message": "Something went wrong with the chat state.", "status": "error"})

if __name__ == '__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', port=5000, debug=True)