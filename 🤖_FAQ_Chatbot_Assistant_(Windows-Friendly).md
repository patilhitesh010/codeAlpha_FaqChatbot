# 🤖 FAQ Chatbot Assistant (Windows-Friendly)

A beginner-friendly FAQ Chatbot built with Python. This version is designed to be lightweight, using built-in libraries for a smooth experience on Windows without needing complex setups like NLTK or Streamlit.

## 🌟 Features
- **Desktop UI**: A professional-looking chat window built with **Tkinter**.
- **Smart Matching**: Uses **TF-IDF Vectorization** to understand the intent behind your questions.
- **Robust Preprocessing**: Uses **Regex** to clean and normalize text (lowercase, punctuation removal, stopword filtering).
- **Auto-Pathing**: Automatically finds your data files, even if you run the script from a different folder.

## 📂 Project Structure
- `chatbot_engine.py`: The "brain" of the bot (Preprocessing & Similarity Matching).
- `gui_chat.py`: The desktop application interface.
- `cli_chat.py`: A terminal-based version of the chatbot.
- `faqs.json`: The knowledge base containing your question-answer pairs.

## 🚀 Installation

1. **Install Python**: Ensure you have Python installed from [python.org](https://www.python.org/).
2. **Install Required Libraries**:
   Open your **Command Prompt** or **PowerShell** and run:
   ```bash
   pip install scikit-learn pandas
   ```

## 🛠️ How to Run

### Option 1: Desktop Interface (Recommended)
Double-click `gui_chat.py` or run this command:
```bash
python gui_chat.py
```

### Option 2: Command Line Interface
If you prefer the terminal, run:
```bash
python cli_chat.py
```

## 🧠 How it Works

### 1. Cleaning the Text (Preprocessing)
When you type a message, the bot:
- Converts it to **lowercase**.
- Removes **punctuation** (like `?`, `!`, `.`).
- Removes **stop words** (common words like "the", "is", "at") that don't help with matching.

### 2. Finding the Best Match
The bot turns your question into a mathematical "vector" using **TF-IDF**. It then compares your vector against all the questions in `faqs.json` using **Cosine Similarity**. 
- If the similarity score is high (e.g., > 0.25), it gives you the answer.
- If the score is too low, it politely asks you to rephrase.

## 📝 Example
**User Input:** "How can I pay for courses?"  
**Matched FAQ:** "What payment methods do you accept?"  
**Bot Answer:** "We accept all major credit cards, PayPal, and Apple Pay."
