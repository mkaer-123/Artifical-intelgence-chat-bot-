# LocalAI - Offline Question-Answering Assistant

A lightweight, local AI chatbot that runs entirely on your machine without requiring API keys, external libraries, or internet connectivity.

## Features

- **No API Keys Required** - Runs completely offline on your machine
- **No External Dependencies** - Uses only Python standard library
- **Easy to Use** - Simple command-line interface
- **Extensible** - Easy to add more questions and responses
- **Conversation History** - Keep track of your chat history
- **Python 3 Compatible** - Works with Python 3.6+

## Installation

1. Clone or download this repository:
```bash
git clone https://github.com/mkaer-123/ai.git
cd ai
```

2. No dependencies to install! Just Python 3.

## Usage

### Running the Chatbot

```bash
python3 ai.py
```

You'll see:
```
============================================================
LocalAI - Your Offline Question-Answering Assistant
============================================================
Type 'help' for capabilities, 'history' to see chat history
Type 'exit' or 'quit' to leave
============================================================

You: 
```

### Example Interactions

```
You: Hello!
AI: Hi there! What would you like to know?

You: What's your name?
AI: I'm LocalAI, a question-answering assistant running locally on your machine.

You: What can you do?
AI: I can answer questions on various topics, provide information, have conversations, and help with general knowledge. Just ask me anything!

You: Tell me about Python
AI: Python is a versatile programming language known for being easy to read and learn. It's great for web development, data science, automation, and much more!

You: history
--- Conversation History ---
1. You: Hello!
   AI: Hi there! What would you like to know?
2. You: What's your name?
   AI: I'm LocalAI, a question-answering assistant running locally on your machine.
...

You: exit
AI: Goodbye! Feel free to ask me anything anytime!
```

### Commands

- **Regular questions** - Ask anything and LocalAI will respond
- **`help`** - See what LocalAI can do
- **`history`** - View your conversation history
- **`exit` or `quit`** - Leave the chatbot

## How It Works

LocalAI uses a simple pattern-matching system:

1. **Input Normalization** - Converts user input to lowercase and removes extra whitespace
2. **Pattern Matching** - Looks for keywords in a knowledge base
3. **Response Generation** - Randomly selects from a list of appropriate responses
4. **History Tracking** - Keeps a record of the conversation

## Knowledge Base

The chatbot comes with knowledge about:

- **Greetings** - Hello, hi, hey, etc.
- **Status** - How are you, how do you feel
- **Identity** - Who are you, what's your name
- **Capabilities** - What can you do, help
- **Creator Info** - Who made you, who created you
- **Python & Programming** - Questions about Python and coding
- **Weather & Time** - Honest responses that data isn't available
- **Goodbyes** - Farewell interactions

## Adding More Knowledge

Edit the `LocalAI` class's `knowledge_base` dictionary to add more topics:

```python
"new_topic": {
    "patterns": ["keyword1", "keyword2", "keyword3"],
    "responses": [
        "Response option 1",
        "Response option 2",
        "Response option 3"
    ]
}
```

Example:
```python
"jokes": {
    "patterns": ["joke", "make me laugh", "funny"],
    "responses": [
        "Why did the Python go to the gym? To get more Pythons!",
        "How many developers does it take to change a lightbulb? None, that's a DevOps problem!",
        "Why do Java developers always wear glasses? Because they can't C#!"
    ]
}
```

## Requirements

- Python 3.6 or higher
- No additional packages needed!

## Customization

### Change Responses
Edit the `responses` lists in the `knowledge_base` dictionary

### Add New Topics
Add new categories with `patterns` and `responses` to the `knowledge_base`

### Modify Behavior
Edit the `respond()`, `find_matching_response()`, or other methods

## Limitations

- Pattern matching only (no deep learning or neural networks)
- Responses are pre-defined
- No internet access or real-time data
- Limited to knowledge base topics
- No memory between sessions (unless you implement file storage)

## Future Enhancements

Possible improvements:
- Save conversation history to file
- Load custom knowledge bases from JSON
- Fuzzy matching for typo tolerance
- Sentiment analysis
- Multi-language support
- File-based knowledge base configuration

## License

MIT License - Feel free to use and modify!

## Author

Created by mkaer-123 - A simple, lightweight AI for everyone!

## Support

For issues or suggestions, open an issue on GitHub or modify the code yourself - it's simple Python!

---

**Enjoy using LocalAI!** 🤖
