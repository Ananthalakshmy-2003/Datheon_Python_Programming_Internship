
import re



INTENTS = {

    "greeting": {
        "patterns": [r"\bhello\b", r"\bhi\b", r"\bhey\b"],
        "response": "Hello! Welcome to Customer Support. How can I help you?"
    },

    "business_hours": {
        "patterns": [
            r"\bbusiness hours\b",
            r"\bworking hours\b",
            r"\bopening time\b",
            r"\bclosing time\b",
            r"\bwhen.*open\b",
            r"\bwhen.*close\b"
        ],
        "response": "Our business hours are Monday to Saturday, 9:00 AM to 6:00 PM. We are closed on Sundays."
    },

    "product_info": {
        "patterns": [
            r"\bproduct details\b",
            r"\bproducts\b",
            r"\bproduct information\b",
            r"\bwhat do you sell\b"
        ],
        "response": "We offer electronics, accessories, and home products. Please contact our sales team for more details."
    },

    "price": {
        "patterns": [
            r"\bprice\b",
            r"\bcost\b",
            r"\bhow much\b"
        ],
        "response": "Product prices depend on the item. Please provide the product name to know its price."
    },

    "delivery": {
        "patterns": [
            r"\bdelivery\b",
            r"\bshipping\b",
            r"\bdeliver\b"
        ],
        "response": "Standard delivery usually takes 3 to 5 business days."
    },

    "return": {
        "patterns": [
            r"\breturn\b",
            r"\brefund\b",
            r"\breplace\b",
            r"\breplacement\b"
        ],
        "response": "Products can be returned within 7 days of delivery if they meet our return conditions."
    },

    "contact": {
        "patterns": [
            r"\bcontact\b",
            r"\bphone number\b",
            r"\bcustomer care\b",
            r"\bsupport number\b"
        ],
        "response": "You can contact our customer support team at support@example.com."
    },

    "thanks": {
        "patterns": [
            r"\bthank you\b",
            r"\bthanks\b"
        ],
        "response": "You're welcome! I'm happy to help."
    }
}



def identify_intents(user_input):

    matched_responses = []

    for intent, details in INTENTS.items():

        for pattern in details["patterns"]:

            if re.search(pattern, user_input):
                matched_responses.append(details["response"])
                break

    return matched_responses



def chatbot_response(user_input):

    user_input = user_input.lower().strip()

    if not user_input:
        return "Please enter a message."

  
    if user_input in ["bye", "exit", "quit"]:
        return "Thank you for contacting us. Goodbye!"

  
    responses = identify_intents(user_input)

   
    if responses:
        return "\n".join(responses)

    return "Sorry, I didn't understand your question. Please ask about business hours, products, prices, delivery, or returns."



def main():

    print("======================================")
    print("     CUSTOMER SUPPORT CHATBOT")
    print("======================================")

    print("Bot: Hello! Welcome to Customer Support.")
    print("Bot: How can I help you today?")
    print("Bot: Type 'bye', 'exit', or 'quit' to end the chat.")

    while True:

        try:
            user_input = input("\nYou: ")

            response = chatbot_response(user_input)

            print("\nBot:", response)

            if user_input.lower().strip() in ["bye", "exit", "quit"]:
                break

        except (KeyboardInterrupt, EOFError):
            print("\nBot: Chat ended. Thank you for contacting us!")
            break



if __name__ == "__main__":
    main()
