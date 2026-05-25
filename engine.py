import urllib.request
import json

# 1. Grab the secret key
api_key = ""
with open(".env", "r") as file:
    for line in file:
        if "GEMINI_API_KEY" in line:
            api_key = line.split("=")[1].strip().strip('"').strip("'")

# 2. Load your personal cheat sheet
try:
    with open("profile.json", "r") as profile_file:
        user_profile = json.load(profile_file)
        writing_rules = user_profile.get("writing_rules", "")
        examples = "\n".join(user_profile.get("example_past_messages", []))
except FileNotFoundError:
    writing_rules = "Write naturally."
    examples = "No examples provided."

# 3. Define our AI assistant function
def get_ai_suggestions(chat_history, mood):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    # --- THE PERSONALIZED SYSTEM PROMPT ---
    instructions = f"""
    You are an advanced AI keyboard extension ghostwriting for the user. 
    Your job is to generate 3 contextual, natural-sounding text message replies that match the requested tone.
    
    CRITICAL: You must mimic the user's personal writing style. 
    User's Writing Rules: {writing_rules}
    
    Here are examples of how the user actually texts:
    {examples}
    
    STRICT RULES:
    1. Act purely as a ghostwriter.
    2. Do NOT explain your choices or add pleasantries.
    3. Output exactly 3 distinct reply options, numbered 1, 2, and 3.
    
    CONVERSATION HISTORY TO ANALYZE:
    {chat_history}
    
    TARGET REPLY TONE: 
    {mood}
    """
    
    payload = {"contents": [{"parts": [{"text": instructions}]}]}
    request = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode("utf-8"), 
        headers={'Content-Type': 'application/json'}
    )
    
    try:
        with urllib.request.urlopen(request) as response:
            answer = json.loads(response.read().decode("utf-8"))
            return answer['candidates'][0]['content']['parts'][0]['text']
    except Exception as e:
        return "⚠️ Connection error. Please try generating again."

# Testing
if __name__ == "__main__":
    print("Engine is ready.")


    STRICT RULES:
    1. Act purely as a ghostwriter for the human user.
    2. NEVER refer to yourself as an AI, a program, or a keyboard. You are drafting text for the human to send about themselves.
    3. Do NOT explain your choices or add pleasantries.
    4. Output exactly 3 distinct reply options, numbered 1, 2, and 3.
