# Chatbot_Test
This is just a test. Encountered many issues with this project.
An AI-powered chatbot using Natural Language Processing and Machine Learning.

# Features

- Handles basic conversations
- Learns from user interactions
- Extensible with new intents and responses

# Installation
pip install -r requirements.txt

requirements.txt
numpy
tensorflow
pandas
matplotlib

# To train the model:
jupyter notebook notebooks/train_model.ipynb

# Run the Flask server (chatbot.py)

and

# Send a post request to the '/chatbot' endpoint with:
curl -X POST -H "Content-Type: application/json" -d '{"message": "Hi"}' http://localhost:5000/chatbot

# Common issues encountered:
Check Python Interpreter in IDE (e.g., VSCode)
If you are using an Integrated Development Environment (IDE) like Visual Studio Code (VSCode), ensure that it is using the correct Python interpreter.

Open Command Palette:
Press Ctrl+Shift+P (or Cmd+Shift+P on macOS) to open the command palette.

Select Interpreter:
Type Python: Select Interpreter and select it. Then choose the correct Python interpreter from the list. This should be the interpreter where Flask is installed.

Reload Window:
Sometimes you may need to reload the window for changes to take effect. You can do this by typing Reload Window in the command palette and selecting it.

# Or try creating a virtual environment

Any inputs from the community will be appreciated.
