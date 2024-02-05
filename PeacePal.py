import tkinter as tk
import pygame
from tkinter import scrolledtext
from tkinter import ttk
import random
import json
import requests
from PIL import Image, ImageTk, ImageDraw
import webbrowser


# Define theme colors
LIGHT_THEME_BG = "#FFFFFF"
LIGHT_THEME_FG = "#000000"
DARK_THEME_BG = "#333333"  # Adjusted to a lighter tone of black
DARK_THEME_FG = "#FFFFFF"

# Define avatar image paths
USER_AVATAR_PATH = "user_avatar.jpg"
BOT_AVATAR_PATH = "bot_avatar.jpg"

def load_intents(file_path):
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents["intents"]

# Load intents from JSON file
intents = load_intents("intents1.json")

# Stack AI API details
API_URL = "https://www.stack-inference.com/run_deployed_flow?flow_id=65c08965ff9effac5e3fd73e&org=a7beee58-f011-4ddb-8c9a-4e298d53a3a3"
headers = {'Authorization':
			 'Bearer 5fd985e6-bdc6-4b42-82e4-11fcc800823e',
			 'Content-Type': 'application/json'
		}


def query_stack_ai(user_input):
    payload = {"in-0": user_input, "user_id": "<USER or Conversation ID>"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()["out-0"]  # Assuming a single output

def get_response(intents, user_input):
    for intent in intents:
        for pattern in intent["patterns"]:
            if pattern.lower() in user_input.lower():
                return random.choice(intent["responses"])

    # If no match in JSON intents, call Stack AI
    stack_ai_response = query_stack_ai(user_input)
    return stack_ai_response

def send_message(event=None):
    message = message_entry.get()
    message_entry.delete(0, "end")

    if message.lower() == "bye":
        chat_text.delete("1.0", tk.END)  # Clear all text from chat_text widget
        chat_text.insert("end", "Goodbye! Have a great day!\nYou can restart conversation by saying Hi\n", "bot")
        return  # Don't proceed with generating a response for "bye"
    else:
        response = get_response(intents, message)

    # Insert user avatar and message
    chat_text.image_create(tk.END, image=user_avatar, padx=5)
    chat_text.insert(tk.END, "You: " + message + "\n", "user")

    # Insert bot avatar and response
    chat_text.image_create(tk.END, image=bot_avatar, padx=5)
    chat_text.insert(tk.END, "Bot: " + response + "\n", "bot")

    chat_text.see("end")  # Scroll to the bottom

def toggle_theme():
    """Toggle between light and dark themes"""
    global current_theme
    if current_theme == "light":
        apply_dark_theme()
    else:
        apply_light_theme()

        
def apply_light_theme():
    """Apply light theme colors and font"""
    global current_theme
    current_theme = "light"
    window.config(bg=LIGHT_THEME_BG)
    chat_text.config(bg=LIGHT_THEME_BG, fg=LIGHT_THEME_FG, font=("Angsana New", 14))  # Set the font here
    #chat_input.configure(style="Light.TEntry")
    dashboard_frame.configure(style="Light.TFrame", width=int(window.winfo_width() * 0.2))
    theme_button.config(text="Dark Mode", style="Light.TButton")
    chat_text.tag_configure("user", foreground="brown", justify="right", spacing3=2, font=("Angsana New", 14))
    chat_text.tag_configure("bot", foreground="black", justify="left", spacing3=2, font=("Angsana New", 14))

def apply_dark_theme():
    """Apply dark theme colors and font"""
    global current_theme
    current_theme = "dark"
    window.config(bg=DARK_THEME_BG)
    chat_text.config(bg=DARK_THEME_BG, fg=DARK_THEME_FG, font=("Angsana New", 14))  # Set the font here
    #chat_input.configure(style="Dark.TEntry")
    dashboard_frame.configure(style="Dark.TFrame", width=int(window.winfo_width() * 0.2))
    theme_button.config(text="Light Mode", style="Dark.TButton")
    chat_text.tag_configure("user", foreground="sky blue", justify="right", spacing3=2, font=("Angsana New", 14))
    chat_text.tag_configure("bot", foreground="white", justify="left", spacing3=2, font=("Angsana New", 14))


def load_avatar(image_path, size):
    """Load user avatar and apply circular mask"""
    avatar_image = Image.open(image_path)
    avatar_image = avatar_image.resize((size, size), Image.BILINEAR)
    
    # Create circular mask
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    # Apply mask to avatar
    avatar_image.putalpha(mask)

    # Convert Image object to PhotoImage for tkinter
    avatar_photo = ImageTk.PhotoImage(avatar_image)
    return avatar_photo

def toggle_music():
    """Toggle between playing and stopping the background music"""
    global is_music_playing
    if is_music_playing:
        pygame.mixer.music.pause()
        is_music_playing = False
        music_button.config(text="Play Music")
    else:
        pygame.mixer.music.unpause()
        is_music_playing = True
        music_button.config(text="Pause Music")


# Initialize pygame
pygame.init()

# Load background music
pygame.mixer.music.load("music.mp3")

# Create the GUI
window = tk.Tk()
window.title("Mental Health Chatbot")
window.geometry("800x600")  # Set size of the window

# Title label
title_label = tk.Label(window, text="Peace Pal", font=("Helvetica", 25, "bold"), bg="light green", fg="#000000")
title_label.grid(row=0, column=0, columnspan=2, pady=5, sticky="ew")

# Chat area
chat_text = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=22)
chat_text.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
chat_text.tag_configure("user", foreground="blue", justify="right", spacing3=2)
chat_text.tag_configure("bot", foreground="black", justify="left", spacing3=2)


# Display welcome message on startup
chat_text.insert("end", "Welcome to Peace Pal!\nSay 'Hey' to start or 'Bye' to exit\n", "bot")  # Display welcome message
chat_text.see("end")  # Scroll to the bottom

# Dashboard section
dashboard_frame_style = ttk.Style()
dashboard_frame_style.configure("Light.TFrame", background="#C4C4C4")
dashboard_frame_style.configure("Dark.TFrame", background="#666666")  # Adjusted to a lighter tone of black

dashboard_frame = ttk.Frame(window, width=int(window.winfo_width() * 0.2), height=23, style="Light.TFrame")
dashboard_frame.grid(row=1, column=1, padx=10, pady=10, sticky="ns")

# Theme toggle button
theme_button = ttk.Button(dashboard_frame, text="Dark Mode", style="Light.TButton", command=toggle_theme)
theme_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

# Community button
community_button = ttk.Button(dashboard_frame, text="Community", command=lambda: webbrowser.open("https://discord.com/invite/VCMckaU3"))
community_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Music button
is_music_playing = True
music_button = ttk.Button(dashboard_frame, text="Pause Music", command=toggle_music)
music_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

# Set initial theme
current_theme = "light"
apply_light_theme()

# Load user avatars
user_avatar = load_avatar(USER_AVATAR_PATH, 50)
bot_avatar = load_avatar(BOT_AVATAR_PATH, 50)

# Create message entry with Send button
message_entry = tk.Entry(window, width=30, font=("Angsana New", 12))
message_entry.grid(row=2, column=0, padx=10, pady=10, sticky="ew")
message_entry.bind('<Return>', send_message)  # Bind Enter key to send_message function

send_button = tk.Button(window, text="Send", command=send_message)
send_button.grid(row=2, column=1, padx=10, pady=10, sticky="ew")

# Configure resizing behavior
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=0)

# Start background music
pygame.mixer.music.play(-1)  # -1 means loop indefinitely

# Main loop
window.mainloop()
