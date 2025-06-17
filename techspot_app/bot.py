from .prompt import *


def get_bot_response(user_input):
    user_input = user_input.strip().lower()


    ecommerce_reply = ecommerce_prompts(user_input)
    if ecommerce_reply:
        return ecommerce_reply
    

    # Default fallback
    return "Sorry, I didn’t understand that. Try saying 'joke', 'date', 'time', or 'greet' 👋"
