# PeacePal - Mental Health Chatbot
Welcome to PeacePal, your empathetic therapist and companion for mental well-being.

# Overview
PeacePal is a nostalgic journey back to the 90s, offering a unique interface reminiscent of classic games from that era. Designed to evoke a sense of nostalgia and connection to one's childhood. PeacePal aims to provide guidance and support for users dealing with mental health challenges. The chatbot offers empathetic conversations, soothing music, and helpful advice, all within a retro-inspired graphical user interface. So, take a step back in time, relive your childhood memories, and embark on a journey towards mental well-being and calmness with PeacePal.

## Features
- **Empathetic Conversations:** PeacePal engages users in empathetic conversations, offering a supportive and understanding environment.

- **Discord Community:** Join our Discord community to connect with others, share experiences, and find additional support.

- **Soothing Music:** PeacePal can play soothing music to create a calming atmosphere whenever you open the chatbot.

- **Dark and Light Themes:** Tailor your experience with the option to choose between dark and light themes for better usability.

- **Avatars:** Personalize your interaction with avatars for both the user and the bot, enhancing the user experience.

## Technology Stack
This code uses several libraries and technologies for building a chat application with a graphical user interface (GUI). Here are the main tech stacks used:

1. **Tkinter:**
   - Tkinter is a standard GUI (Graphical User Interface) library for Python.
   - It is used for creating windows, labels, buttons, and other GUI elements in the code.

2. **Pygame:**
   - Pygame is a set of Python modules designed for writing video games.
   - In this code, Pygame is used for playing background music.

3. **PIL (Python Imaging Library) / Pillow:**
   - PIL, now known as Pillow, is used for image processing tasks.
   - In this code, it is used to load and manipulate avatar images.

4. **Requests:**
   - The requests library is used for making HTTP requests.
   - It is utilized here to interact with Stack AI's API for natural language processing.

5. **JSON:**
   - The json library is used for working with JSON data.
   - It loads intents from a JSON file containing patterns and responses for the chatbot.

These are the primary technologies and libraries employed in the provided code for creating a chat application with a GUI, background music, and interaction with a natural language processing API.
## Challenges we ran into
- **Intents and Schema-Free Responses:** Our quest for a suitable JSON file posed a challenge, as we aimed for a chatbot capable of dynamic responses without imposing a specific user schema.
- **Precision in Mental Health Dataset:** Acquiring an accurate mental health dataset became crucial for practical model training, presenting its own hurdles.
- **Timeline Pressures and OpenAI Pivot:** The hackathon's tight timeline led us to opt for OpenAI initially. However, due to constraints with the premium version, we pivoted to Stack AI, a no-code generative AI platform, to expedite development. 
- **Frontend Integration Challenges:** Integrating the React frontend proved challenging, prompting a shift to Tkinter, Python's GUI library, for a seamless fusion of backend and frontend elements.
- **Music Integration and Library Choosing:** Selecting the appropriate library for integrating music functionality added complexity, requiring careful consideration of factors such as compatibility, features, and ease of integration.

## Feedback
We value your feedback! If you have suggestions, encounter issues, or want to share your experience, please reach out through our Discord community or open an issue on GitHub.

Note: PeacePal is not a substitute for professional mental health care. If you are experiencing a mental health crisis, please seek help from a licensed professional.
