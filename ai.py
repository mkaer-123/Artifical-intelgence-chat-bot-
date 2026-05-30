#!/usr/bin/env python3
"""
Local AI Chatbot with Probability and Learning
No API keys or external libraries required
A question-answering system with pattern matching, probability scoring, and learning capabilities
"""

import sys
import json

class LocalAI:
    def __init__(self):
        """Initialize the local AI with knowledge base, probability scoring, and learning"""
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
        
        # Probability and learning tracking
        self.response_ratings = {}  # Track user satisfaction with responses
        self.pattern_frequency = {}  # Track which patterns are matched most
        self.learned_patterns = {}   # Dynamically learned patterns from user feedback
        self.conversation_count = 0  # Total conversations
        self.pattern_match_history = {}  # Track successful pattern matches
    
    def normalize_input(self, user_input):
        """Normalize user input for pattern matching"""
        return user_input.lower().strip()
    
    def calculate_pattern_probability(self, pattern, normalized_input):
        """Calculate probability that a pattern matches the input"""
        # Basic probability: how much of the pattern is in the input
        pattern_length = len(pattern)
        input_length = len(normalized_input)
        
        if pattern in normalized_input:
            # Get position and calculate probability based on position and length
            position = normalized_input.find(pattern)
            probability = (pattern_length / input_length) * 0.8  # Base score of 0.8 for match
            
            # Boost probability if pattern is at the start
            if position == 0:
                probability += 0.2
            
            # Apply learned frequency bonus
            frequency_bonus = self.pattern_frequency.get(pattern, 0) * 0.05
            probability = min(probability + frequency_bonus, 1.0)
            
            return probability
        
        return 0.0
    
    def find_best_matching_category(self, user_input):
        """Find the best matching category using probability scoring"""
        normalized_input = self.normalize_input(user_input)
        best_category = None
        best_probability = 0.0
        best_pattern = None
        
        # Check each category in knowledge base
        for category, data in self.knowledge_base.items():
            patterns = data.get("patterns", [])
            
            # Calculate probability for each pattern
            for pattern in patterns:
                probability = self.calculate_pattern_probability(pattern, normalized_input)
                
                if probability > best_probability:
                    best_probability = probability
                    best_category = category
                    best_pattern = pattern
        
        return best_category, best_probability, best_pattern
    
    def find_matching_response(self, user_input):
        """Find a response based on probability-weighted pattern matching"""
        best_category, best_probability, best_pattern = self.find_best_matching_category(user_input)
        
        # If we have a good match (probability > 0.3)
        if best_probability > 0.3 and best_category:
            responses = self.knowledge_base[best_category].get("responses", [])
            
            # Select best response based on ratings
            response = self._select_best_response(best_category, responses)
            
            # Track the successful match
            self.pattern_match_history[best_pattern] = self.pattern_match_history.get(best_pattern, 0) + 1
            self.pattern_frequency[best_pattern] = self.pattern_frequency.get(best_pattern, 0) + 1
            
            return response, best_category, best_probability
        
        # Check learned patterns for low-probability matches
        for learned_pattern, learned_response in self.learned_patterns.items():
            if learned_pattern in self.normalize_input(user_input):
                return learned_response, "learned", 0.75
        
        # Default response if no match found
        return self.get_default_response(self.normalize_input(user_input)), None, 0.0
    
    def _select_best_response(self, category, responses):
        """Select response based on user ratings"""
        import random
        
        # If no ratings yet, return random
        if category not in self.response_ratings:
            return random.choice(responses)
        
        ratings = self.response_ratings[category]
        
        # Find highest rated response
        best_response = max(responses, 
                           key=lambda r: ratings.get(r, 0))
        
        return best_response
    
    def rate_response(self, response, rating):
        """Allow user to rate AI responses for learning"""
        # This will be called after each response
        # Rating: 1-5 stars
        pass
    
    def learn_new_pattern(self, pattern, response, category=None):
        """Learn new pattern-response mapping from user feedback"""
        if pattern and response:
            self.learned_patterns[pattern] = response
            print(f"✓ Learned new pattern: '{pattern}'")
    
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
    
    def add_to_history(self, user_input, response, probability=0.0, category=None):
        """Add conversation to history with metadata"""
        self.conversation_history.append({
            "user": user_input,
            "ai": response,
            "probability": probability,
            "category": category,
            "rating": None
        })
    
    def respond(self, user_input):
        """Get AI response to user input"""
        if not user_input.strip():
            return "Please ask me a question or say something!", None, 0.0
        
        response, category, probability = self.find_matching_response(user_input)
        self.conversation_count += 1
        self.add_to_history(user_input, response, probability, category)
        
        return response, category, probability
    
    def get_stats(self):
        """Get learning and probability statistics"""
        return {
            "total_conversations": self.conversation_count,
            "history_size": len(self.conversation_history),
            "learned_patterns": len(self.learned_patterns),
            "total_patterns_learned": len(self.pattern_frequency),
            "top_patterns": sorted(self.pattern_frequency.items(), 
                                  key=lambda x: x[1], reverse=True)[:5],
            "conversation_history": self.conversation_history
        }
    
    def get_history(self):
        """Return conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []


def main():
    """Main function to run the chatbot"""
    ai = LocalAI()
    
    print("=" * 70)
    print("LocalAI - Offline QA Assistant with Probability & Learning")
    print("=" * 70)
    print("Commands:")
    print("  'help'     - See what I can do")
    print("  'history'  - View conversation history")
    print("  'stats'    - View learning statistics")
    print("  'learn'    - Teach me a new pattern-response")
    print("  'exit'     - Leave the chatbot")
    print("=" * 70)
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
                        prob_str = f" [Confidence: {entry['probability']:.0%}]" if entry['probability'] else ""
                        category_str = f" [{entry['category']}]" if entry['category'] else ""
                        print(f"{i}. You: {entry['user']}")
                        print(f"   AI: {entry['ai']}{prob_str}{category_str}")
                    print("----------------------------\n")
                else:
                    print("No conversation history yet.\n")
                continue
            
            elif user_input.lower() == "stats":
                stats = ai.get_stats()
                print("\n--- Learning Statistics ---")
                print(f"Total Conversations: {stats['total_conversations']}")
                print(f"Learned Patterns: {stats['learned_patterns']}")
                print(f"Unique Patterns: {stats['total_patterns_learned']}")
                print("\nTop 5 Most Matched Patterns:")
                for pattern, count in stats['top_patterns']:
                    print(f"  - '{pattern}': {count} matches")
                print("----------------------------\n")
                continue
            
            elif user_input.lower() == "learn":
                print("\n--- Teach LocalAI ---")
                pattern = input("Enter a new pattern (e.g., 'machine learning'): ").strip()
                response = input("Enter the response you'd like: ").strip()
                if pattern and response:
                    ai.learn_new_pattern(pattern, response)
                print()
                continue
            
            elif user_input.lower() in ["exit", "quit", "goodbye", "bye"]:
                response, _, _ = ai.respond(user_input)
                print(f"AI: {response}\n")
                break
            
            # Get and display response
            response, category, probability = ai.respond(user_input)
            confidence = f" [Confidence: {probability:.0%}]" if probability else ""
            print(f"AI: {response}{confidence}\n")
        
        except KeyboardInterrupt:
            print("\n\nGoodbye! Thanks for chatting with LocalAI!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.\n")


if __name__ == "__main__":
    main()
