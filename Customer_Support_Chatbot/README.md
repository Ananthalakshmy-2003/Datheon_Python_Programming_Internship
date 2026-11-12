# Customer Support Chatbot

## Project Description

The Customer Support Chatbot is a rule-based conversational application developed using Python.

It interacts with users by identifying keywords and patterns in their messages using regular expressions. Based on the detected intent, the chatbot provides relevant responses to questions about business hours, product information, prices, delivery, returns, and customer support.

The chatbot also supports multiple-intent matching, fallback responses for unknown queries, and clean exit commands.

## Features

- Interactive text-based conversation.
- Greeting message detection.
- Business hours information.
- Product-related FAQs.
- Product price inquiries.
- Delivery and shipping information.
- Return and refund information.
- Customer support contact information.
- Multiple-intent matching.
- Regular expression-based keyword detection.
- Fallback responses for unrecognized queries.
- Handles empty user input.
- Supports exit commands such as `bye`, `exit`, and `quit`.
- Handles keyboard interruption and input errors gracefully.

## Technologies Used

- **Python 3** – Programming language.
- **re module** – Identifies keywords and patterns using regular expressions.
- **Dictionary** – Stores chatbot intents, patterns, and responses.
- **Functions** – Organizes chatbot operations into reusable sections.

## Project Structure

```text
Customer_Support_Chatbot/
│
├── chatbot.py
│
└── README.md
```

## Requirements

- Python 3.x
- Visual Studio Code (recommended)

No external Python packages are required.

## How to Run

**Step 1:** Download or clone the project.

**Step 2:** Open the project folder in Visual Studio Code.

**Step 3:** Open the terminal.

**Step 4:** Execute the following command:

```bash
python chatbot.py
```

**Step 5:** Start interacting with the chatbot by entering your questions.

## Sample Conversation

```text
======================================
     CUSTOMER SUPPORT CHATBOT
======================================

Bot: Hello! Welcome to Customer Support.
Bot: How can I help you today?
Bot: Type 'bye', 'exit', or 'quit' to end the chat.

You: hello

Bot: Hello! Welcome to Customer Support.
How can I help you?

You: What are your business hours?

Bot: Our business hours are Monday to Saturday,
9:00 AM to 6:00 PM. We are closed on Sundays.

You: Tell me about products and delivery.

Bot: We offer electronics, accessories, and home products.
Please contact our sales team for more details.

Standard delivery usually takes 3 to 5 business days.

You: bye

Bot: Thank you for contacting us. Goodbye!
```

## Working Methodology

1. The chatbot receives a message from the user.
2. The input is converted into lowercase and unnecessary spaces are removed.
3. Regular expressions identify matching keywords and patterns.
4. The chatbot identifies the corresponding user intent.
5. Relevant responses are generated.
6. If multiple intents are detected, multiple responses are returned.
7. If no matching intent is found, a fallback response is displayed.
8. The conversation ends when the user enters `bye`, `exit`, or `quit`.

## Learning Outcomes

Through this project, I learned:

- Python regular expressions.
- String normalization and processing.
- Dictionary-based data management.
- Functions and loops.
- Rule-based chatbot development.
- Pattern matching and intent identification.
- Multiple-intent handling.
- Exception handling.
- Building interactive command-line applications.

## Limitations

- The chatbot uses predefined rules and responses.
- It does not understand complex natural language like an AI chatbot.
- It does not connect to a live product database.
- Product and business information must be updated manually.

## Future Enhancements

- Integrate an AI-based response system.
- Load FAQs from an external JSON dataset.
- Add a graphical user interface.
- Connect to a real product database.
- Support more user queries and languages.

## Author

Python Beginner Project

## License

This project is created for educational and learning purposes.