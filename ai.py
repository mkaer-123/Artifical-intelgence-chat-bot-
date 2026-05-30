#!/usr/bin/env python3
"""
Local AI Chatbot - No API keys or external libraries required
A simple question-answering system using rule-based pattern matching and responses
"""

import sys
import json

class LocalAI:
    def __init__(self):
        """Initialize the local AI with knowledge base"""
        self.knowledge_base = {
            "greeting": {
                "patterns": ["hello", "hi", "hey", "greetings", "what's up", "howdy"],
                "responses": [
                    "Hello! How can I help you today?",
                    "Hi there! What would you like to know?",
                    "Hey! What's on your mind?"
                ]
            },
            "how_are_you": {
                "patterns": ["how are you", "how do you feel", "how's it going", "what's your status"],
                "responses": [
                    "I'm doing great, thanks for asking! How can I assist you?",
                    "I'm functioning well and ready to help. What do you need?",
                    "All systems operational! What would you like to discuss?"
                ]
            },
            "name": {
                "patterns": ["what is your name", "who are you", "what are you called", "your name"],
                "responses": [
                    "I'm LocalAI, a question-answering assistant running locally on your machine.",
                    "My name is LocalAI. I'm here to help answer your questions!",
                    "I'm LocalAI, your local question-answering companion."
                ]
            },
            "help": {
                "patterns": ["help", "what can you do", "capabilities", "features"],
                "responses": [
                    "I can answer questions on various topics, provide information, have conversations, and help with general knowledge. Just ask me anything!",
                    "I'm here to answer your questions on a wide range of topics. Type your question or say hello to get started!",
                    "I can help with knowledge questions, have conversations, and provide information on many subjects."
                ]
            },
            "creator": {
                "patterns": ["who created you", "who made you", "your creator", "who built you"],
                "responses": [
                    "I was created as a local AI assistant without external API dependencies.",
                    "I'm a locally-built AI that runs completely on your machine.",
                    "I was created to be a simple, offline question-answering system."
                ]
            },
            "time": {
                "patterns": ["what time is it", "tell me the time", "current time"],
                "responses": [
                    "I don't have access to real-time information, but you can check your system clock!",
                    "I can't tell the exact time, but your system clock should show the current time.",
                    "Time information isn't available to me right now."
                ]
            },
            "weather": {
                "patterns": ["what's the weather", "weather", "how's the weather"],
                "responses": [
                    "I don't have access to weather data. Check a weather service or your local weather app!",
                    "I can't provide real-time weather information. Try a weather website or app.",
                    "Weather data isn't available to me, but you can check online weather services."
                ]
            },
            "python": {
                "patterns": ["python", "programming", "code", "coding"],
                "responses": [
                    "Python is a versatile programming language known for being easy to read and learn. It's great for web development, data science, automation, and much more!",
                    "Python is a powerful language used in AI, data analysis, web development, and automation. It's beginner-friendly with a rich ecosystem.",
                    "Python is one of the most popular programming languages. It's used for everything from web apps to machine learning!"
                ]
            },
            "goodbye": {
                "patterns": ["goodbye", "bye", "see you", "farewell", "exit", "quit"],
                "responses": [
                    "Goodbye! Feel free to ask me anything anytime!",
                    "See you later! Come back if you have more questions.",
                    "Bye! It was nice chatting with you!"
                ]
            }
        }
        self.conversation_history = []
    
    def normalize_input(self, user_input):
        """Normalize user input for pattern matching"""
        return user_input.lower().strip()
    
    def find_matching_response(self, user_input):
        """Find a response based on pattern matching"""
        normalized_input = self.normalize_input(user_input)
        
        # Check each category in knowledge base
        for category, data in self.knowledge_base.items():
            patterns = data.get("patterns", [])
            responses = data.get("responses", [])
            
            # Check if any pattern matches
            for pattern in patterns:
                if pattern in normalized_input:
                    import random
                    return random.choice(responses)
        
        # Default response if no match found
        return self.get_default_response(normalized_input)
    
    def get_default_response(self, user_input):
        """Generate a default response for unmatched input"""
        responses = [
            f"That's an interesting question about '{user_input}'! I may not have specific information on that, but feel free to ask me about other topics.",
            f"I'm not entirely sure about that. Could you rephrase your question or ask about something else?",
            "I don't have information on that particular topic, but I'd be happy to help with other questions!",
            "That's beyond my current knowledge base. Try asking about Python, programming, or general topics!"
        ]
        import random
        return random.choice(responses)
    
    def add_to_history(self, user_input, response):
        """Add conversation to history"""
        self.conversation_history.append({
            "user": user_input,
            "ai": response
        })
    
    def respond(self, user_input):
        """Get AI response to user input"""
        if not user_input.strip():
            return "Please ask me a question or say something!"
        
        response = self.find_matching_response(user_input)
        self.add_to_history(user_input, response)
        return response
    
    def get_history(self):
        """Return conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []


def main():
    """Main function to run the chatbot"""
    ai = LocalAI()
    
    print("=" * 60)
    print("LocalAI - Your Offline Question-Answering Assistant")
    print("=" * 60)
    print("Type 'help' for capabilities, 'history' to see chat history")
    print("Type 'exit' or 'quit' to leave")
    print("=" * 60)
    print()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Handle special commands
            if user_input.lower() == "history":
                if ai.get_history():
                    print("\n--- Conversation History ---")
                    for i, entry in enumerate(ai.get_history(), 1):
                        print(f"{i}. You: {entry['user']}")
                        print(f"   AI: {entry['ai']}")
                    print("----------------------------\n")
                else:
                    print("No conversation history yet.\n")
                continue
            
            if user_input.lower() in ["exit", "quit", "goodbye", "bye"]:
                response = ai.respond(user_input)
                print(f"AI: {response}\n")
                break
            
            # Get and display response
            response = ai.respond(user_input)
            print(f"AI: {response}\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye! Thanks for chatting with LocalAI!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
