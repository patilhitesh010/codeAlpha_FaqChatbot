from chatbot_engine import FAQChatbot

def main():
    print("--- FAQ Chatbot (CLI) ---")
    print("Type your question below. Type 'exit' to quit.")
    
    bot = FAQChatbot()
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        if not user_input:
            continue
            
        response = bot.get_response(user_input)
        
        if response["matched_question"]:
            print(f"Matched FAQ: {response['matched_question']}")
            print(f"Similarity Score: {response['score']}")
        
        print(f"Chatbot: {response['answer']}")

if __name__ == "__main__":
    main()