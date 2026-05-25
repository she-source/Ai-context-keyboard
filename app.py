
import tkinter as tk
from tkinter import ttk
from engine import get_ai_suggestions

def on_click():
    # Grab all text from line 1 to the end of the text box
    chat_history = chat_text.get("1.0", tk.END).strip()
    mood = mood_combobox.get()
    
    output_label.config(text="AI is analyzing context... ✨", fg="blue")
    root.update()
    
    suggestions = get_ai_suggestions(chat_history, mood)
    
    output_label.config(text=suggestions, fg="black")

# --- BUILD THE VISUAL WINDOW ---
root = tk.Tk()
root.title("AI Content Keyboard - Prototype")
root.geometry("480x480") # Made the window slightly bigger
root.configure(padx=20, pady=20)

# --- THE UPGRADED MULTI-LINE CHAT BOX ---
tk.Label(root, text="Paste recent chat history here:", font=("Arial", 10, "bold")).pack(anchor="w")
# We use tk.Text instead of tk.Entry so it supports multiple lines of context!
chat_text = tk.Text(root, height=5, width=53, font=("Arial", 10))
chat_text.pack(pady=5)

# The Dropdown Menu
tk.Label(root, text="Select your reply tone:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(10,0))
mood_options = [
    "Professional & Polite",
    "Casual & Friendly",
    "Funny & Witty",
    "Gen Z Slang",
    "De-escalating & Calm",
    "Direct & Assertive",
    "Anxious but polite",
    "Flirty"
]
mood_combobox = ttk.Combobox(root, values=mood_options, width=50, state="readonly")
mood_combobox.set("Casual & Friendly")
mood_combobox.pack(pady=5)

# The Magic Generate Button
btn = tk.Button(root, text="Generate Replies ✨", bg="black", fg="white", font=("Arial", 10, "bold"), command=on_click)
btn.pack(pady=20)

# Where the AI text will show up
output_label = tk.Label(root, text="Your suggestions will appear here.", justify="left", wraplength=420, font=("Arial", 11))
output_label.pack(pady=10)

root.mainloop()

