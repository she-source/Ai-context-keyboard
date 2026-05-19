import tkinter as tk
from engine import get_ai_suggestions

def on_click():
    chat_history = chat_entry.get()
    mood = mood_entry.get()
    
    # Update the screen to show it's loading
    output_label.config(text="AI is thinking... ✨", fg="blue")
    root.update()
    
    # Call YOUR engine to get the answers
    suggestions = get_ai_suggestions(chat_history, mood)
    
    # Display the answers on the screen
    output_label.config(text=suggestions, fg="black")

# --- BUILD THE VISUAL WINDOW ---
root = tk.Tk()
root.title("AI Content Keyboard - Prototype")
root.geometry("450x350")
root.configure(padx=20, pady=20)

# Chat Input Box
tk.Label(root, text="What did the other person say?", font=("Arial", 10, "bold")).pack(anchor="w")
chat_entry = tk.Entry(root, width=50)
chat_entry.pack(pady=5)

# Mood Input Box
tk.Label(root, text="How do you want to sound? (e.g. Professional, Funny)", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
mood_entry = tk.Entry(root, width=50)
mood_entry.pack(pady=5)

# The Magic Generate Button
btn = tk.Button(root, text="Generate Replies ✨", bg="black", fg="white", font=("Arial", 10, "bold"), command=on_click)
btn.pack(pady=15)

# Where the AI text will show up
output_label = tk.Label(root, text="Your suggestions will appear here.", justify="left", wraplength=400, font=("Arial", 11))
output_label.pack(pady=10)

# Start the application!
root.mainloop()
