import tkinter as tk
from tkinter import scrolledtext
from chatbot_engine import FAQChatbot

class ChatGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FAQ Chatbot Assistant")
        self.root.geometry("500x600")
        
        # Initialize Chatbot
        self.bot = FAQChatbot()
        
        # UI Components
        self.create_widgets()
        
        # Welcome message
        self.display_message("Bot: Hello! I'm your FAQ assistant. How can I help you today?\n", "bot")

    def create_widgets(self):
        # Chat Display Area
        self.chat_display = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, state='disabled', font=("Arial", 10))
        self.chat_display.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Message Entry Area
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.user_input = tk.Entry(self.entry_frame, font=("Arial", 11))
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        self.user_input.bind("<Return>", lambda event: self.handle_send())
        
        self.send_button = tk.Button(self.entry_frame, text="Send", command=self.handle_send, bg="#4CAF50", fg="white")
        self.send_button.pack(side=tk.RIGHT)

    def handle_send(self):
        query = self.user_input.get().strip()
        if not query:
            return
            
        # Display user message
        self.display_message(f"You: {query}\n", "user")
        self.user_input.delete(0, tk.END)
        
        # Get bot response
        response = self.bot.get_response(query)
        
        # Display bot response
        bot_text = f"Bot: {response['answer']}\n"
        if response['matched_question']:
            bot_text += f"(Matched: {response['matched_question']} | Score: {response['score']})\n"
        
        self.display_message(bot_text + "\n", "bot")

    def display_message(self, message, sender):
        self.chat_display.config(state='normal')
        self.chat_display.insert(tk.END, message)
        
        # Simple coloring
        if sender == "user":
            self.chat_display.tag_add("user_tag", "end-2c linestart", "end-2c")
            self.chat_display.tag_config("user_tag", foreground="blue")
        else:
            self.chat_display.tag_add("bot_tag", "end-2c linestart", "end-2c")
            self.chat_display.tag_config("bot_tag", foreground="green")
            
        self.chat_display.config(state='disabled')
        self.chat_display.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatGUI(root)
    root.mainloop()