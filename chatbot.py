import nltk
import spacy
import random
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Initialize NLTK and spaCy
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()
nlp = spacy.load("en_core_web_sm")

# Predefined responses and queries
responses = {
    'greeting': ['Hello!', 'Hi there!', 'How can I assist you today?'],
    'goodbye': ['Goodbye!', 'See you later!', 'Take care!'],
    'thanks': ['You are welcome!', 'Happy to help!', 'Glad I could assist!'],
    'default': ['Sorry, I didn’t understand that.', 'Can you please rephrase?', 'I am not sure about that.']
}

# Sample questions for the bot
questions = {
    'greeting': ['hi', 'hello', 'hey', 'good morning', 'good evening'],
    'goodbye': ['bye', 'goodbye', 'see you', 'take care'],
    'thanks': ['thank you', 'thanks']
}

# Function to clean and preprocess the user input
def preprocess_input(user_input):
    # Tokenize the input
    tokens = word_tokenize(user_input.lower())
    
    # Remove stopwords and lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stopwords.words('english')]
    
    return tokens

# Function to identify intent based on user input
def identify_intent(user_input):
    preprocessed_input = preprocess_input(user_input)
    
    # Loop through the intent patterns and check if they match the user input
    for intent, patterns in questions.items():
        for pattern in patterns:
            if pattern in preprocessed_input:
                return intent
    
    return 'default'

# Main chatbot function
def chatbot():
    print("Chatbot: Hi! I am your virtual assistant. Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        
        # Exit the chatbot if user types 'exit'
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye! Have a nice day!")
            break
        
        # Identify intent and respond accordingly
        intent = identify_intent(user_input)
        
        if intent in responses:
            print("Chatbot:", random.choice(responses[intent]))
        else:
            print("Chatbot:", random.choice(responses['default']))

# Run the chatbot
if __name__ == "__main__":
    chatbot()
