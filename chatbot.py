import random
import nltk
import spacy
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from termcolor import colored
import time

# Initialize spaCy model for NLP
nlp = spacy.load ( 'en_core_web_sm' )

# Download necessary NLTK data
nltk.download ( 'punkt' )
nltk.download ( 'wordnet' )
nltk.download ( 'stopwords' )

# Initialize NLTK objects
lemmatizer = WordNetLemmatizer ( )
stop_words = set ( stopwords.words ( 'english' ) )


# Aesthetic Print Functions
def type_writer_effect(text , delay=0.05 , color='cyan') :
    """Simulates typewriter effect with color"""
    for char in text :
        print ( colored ( char , color ) , end='' , flush=True )
        time.sleep ( delay )
    print ( '' )


# Function to preprocess the user input
def preprocess(text) :
    # Tokenize and normalize text
    tokens = word_tokenize ( text.lower ( ) )
    # Lemmatize and remove stopwords
    return [ lemmatizer.lemmatize ( word ) for word in tokens if word.isalnum ( ) and word not in stop_words ]


# Chatbot Responses
responses = {
    "greeting" : [ "Hello, it's wonderful to meet you! How can I assist you today?" ,
                   "Hi there! What can I help you with today?" ] ,
    "farewell" : [ "Goodbye, have a fantastic day ahead!" , "See you soon, take care!" ] ,
    "unknown" : [ "I'm not quite sure what you mean. Could you clarify?" ,
                  "Hmm, I don't understand. Could you rephrase that for me?" ]
}


# Function to generate a response based on user input
def get_response(user_input) :
    tokens = preprocess ( user_input )

    if any ( greet in tokens for greet in [ 'hello' , 'hi' , 'hey' ] ) :
        return random.choice ( responses [ "greeting" ] )
    elif any ( farewell in tokens for farewell in [ 'bye' , 'goodbye' , 'see you' ] ) :
        return random.choice ( responses [ "farewell" ] )
    else :
        return random.choice ( responses [ "unknown" ] )


# Main chatbot interaction loop with a beautiful interface
def chatbot() :
    type_writer_effect ( "Chatbot: ✨ Welcome to the world of conversations! ✨" , color='green' )
    type_writer_effect ( "Chatbot: How may I assist you today? Type 'exit' to leave the chat." , color='green' )

    while True :
        user_input = input ( colored ( "You: " , 'yellow' ) )

        if user_input.lower ( ) == 'exit' :
            type_writer_effect ( "Chatbot: It was nice chatting with you. Take care! 💫" , color='green' )
            break

        response = get_response ( user_input )
        type_writer_effect ( f"Chatbot: {response}" , color='cyan' )


# Entry point
if __name__ == "__main__" :
    chatbot ( )
