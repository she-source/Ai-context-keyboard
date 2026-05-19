import urllib.request
import json

# 1. Open the .env file and grab the secret key
api_key = ""
with open(".env", "r") as file:
    for line in file:
        if "GEMINI_API_KEY" in line:
            # Clean up the text to extract just the key itself
            api_key = line.split("=")[1].strip().strip('"').strip("'")

# 2. Define our AI assistant function
def get_ai_suggestions(chat_history, mood):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"
    
    # The instructions we give to the AI
    instructions = f"""
    You are a smart keyboard assistant. 
    Conversation history: {chat_history}
    User wants to sound: {mood}
    
    Provide 3 short, natural reply options. Do not explain them.
    """
    
    # Format the request for Google
    payload = {"contents": [{"parts": [{"text": instructions}]}]}
    request = urllib.request.Request(
        url, 
        data=json.dumps(payload).encode("utf-8"), 
        headers={'Content-Type': 'application/json'}
    )
    
    # Send the request and return the answer
    with urllib.request.urlopen(request) as response:
        answer = json.loads(response.read().decode("utf-8"))
        return answer['candidates'][0]['content']['parts'][0]['text']

# 3. Test the code
if __name__ == "__main__":
    test_chat = "Client: We need the project delivered by Friday."
    test_mood = "Professional and reassuring"
    
    print("Asking AI for suggestions...")
    print("----------------------------")
    result = get_ai_suggestions(test_chat, test_mood)
    print(result)
