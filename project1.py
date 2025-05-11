# PROJECT 1 : EMOJI MOOD RESPONDER

# Dictionary of moods
mood_emoji_dict = {
    "happy": ("😊", "Keep smiling!"),
    "sad": ("😢", "It's okay to feel sad. Better days will come."),
    "angry": ("😠", "Take a deep breath. Everything will be okay."),
    "excited": ("😄", "That's awesome! Enjoy the moment!"),
    "tired": ("😴", "Get some rest, you'll feel better."),
    "bored": ("😐", "Find something you love doing or learn something new!"),
    "nervous": ("😰", "You're doing better than you think. Stay calm and carry on."),
    "confused": ("😕", "It's okay not to have all the answers. Clarity will come."),
    "grateful": ("🥰", "Gratitude turns what we have into enough. Stay blessed."),
    "motivated": ("🔥", "You’re on fire! Keep chasing your goals with passion!")
}

# user input
user_mood = input("How are you feeling today? ").strip().lower()

if user_mood in mood_emoji_dict:
    emoji, message = mood_emoji_dict[user_mood]
    print(f"{emoji} {message}")
else:
    print("🤔 Sorry, I couldn't recognize your mood, but I hope you have a great day!")