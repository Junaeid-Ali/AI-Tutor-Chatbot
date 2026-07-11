# 🎓 AI Tutor Chatbot

An intelligent AI Tutor built with **LangChain**, **Mistral AI**, and **Streamlit** that helps students understand concepts through clear, step-by-step explanations instead of simply providing answers.

---

## 📌 Features

* 💬 Interactive chatbot interface
* 📚 Step-by-step explanations
* 🧠 Encourages critical thinking
* 💻 Programming and coding assistance
* ➗ Mathematical problem solving with detailed calculations
* 📝 Uses prompt engineering for educational responses
* ⚡ Built using LangChain and Mistral AI
* 🎨 Simple and user-friendly Streamlit interface

---

## 🛠️ Tech Stack

* Python
* LangChain
* Mistral AI
* Streamlit
* python-dotenv

---

## 📂 Project Structure

```text
AI-Tutor/
│
├── app.py                 # Streamlit application
├── requirements.txt       # Project dependencies
├── .env                   # API key (not included in GitHub)
├── README.md
└── assets/                # Images or other static files (optional)
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Junaeid-Ali/AI-Tutor-Chatbot.git
cd AI-Tutor-Chatbot
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```env
MISTRAL_API_KEY=YOUR_API_KEY
```

Replace `YOUR_API_KEY` with your own Mistral API key.

### 5. Run the application

```bash
streamlit run app.py
```

---

## 📖 How It Works

1. The user enters a question.
2. LangChain formats the question using a custom educational prompt template.
3. The prompt is sent to the Mistral AI language model.
4. The model generates a student-friendly response.
5. The answer is displayed in the Streamlit chat interface.

---

## 🎯 Educational Prompt Design

The AI Tutor is instructed to:

* Explain concepts using simple language.
* Teach step by step.
* Encourage critical thinking.
* Correct mistakes politely.
* Provide examples whenever possible.
* Explain programming logic before code.
* Show complete mathematical calculations.
* End responses with a follow-up question to reinforce learning.

---

## 📷 Screenshot

Add a screenshot of your application here.

```
assets/screenshot.png
```

---

## 🔮 Future Improvements

* 📄 PDF Question Answering (RAG)
* 🧠 Conversation memory
* 📚 Multiple subject selection
* 📝 Quiz generation
* 📊 Learning progress dashboard
* 🌙 Dark mode
* 🔊 Text-to-speech
* 🌐 Multi-language support
* 📂 Document upload

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Md. Junaeid Ali**

If you found this project helpful, consider giving it a ⭐ on GitHub!
