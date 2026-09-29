# 🎓 College & University FAQ Chatbot

An NLP-based FAQ chatbot designed to answer common college and university-related questions. The chatbot uses **Natural Language Processing (NLP)**, **TF-IDF vectorization**, and **Cosine Similarity** to identify the FAQ that most closely matches the user's question.

## 📌 Project Overview

Students often have questions about admission, fees, hostel facilities, library timings, examinations, scholarships, and other college services.

This project provides a simple chatbot that automatically finds the most relevant FAQ from a predefined dataset and displays the corresponding answer.

## ✨ Features

* 📚 College and university FAQ dataset
* 🧹 Text preprocessing using NLTK
* 🔤 Tokenization
* 🚫 Stopword removal
* 🌱 Stemming
* 📊 TF-IDF vectorization
* 🔎 Cosine similarity matching
* 🤖 Automatic FAQ answer retrieval
* 📈 Similarity score display
* 💻 Simple Python-based chatbot

## 🛠️ Technologies Used

| Technology   | Purpose                            |
| ------------ | ---------------------------------- |
| Python       | Main programming language          |
| Pandas       | Reading and processing FAQ dataset |
| NLTK         | Natural Language Processing        |
| Scikit-learn | TF-IDF and cosine similarity       |
| CSV          | FAQ dataset storage                |

## 📂 Project Structure

```text
College_FAQ_Chatbot/
│
├── faq_data.csv          # FAQ questions and answers
├── preprocess.py         # NLP preprocessing
├── chatbot.py            # Main chatbot program
├── read_faq.py           # Reads and displays FAQ dataset
├── test.py               # Initial Python testing
├── README.md             # Project documentation
└── .gitignore            # Files excluded from GitHub
```

## ⚙️ How It Works

```text
              User Question
                    ↓
            Text Preprocessing
                    ↓
        Tokenization & Cleaning
                    ↓
           Stopword Removal
                    ↓
                Stemming
                    ↓
          TF-IDF Vectorization
                    ↓
          Cosine Similarity
                    ↓
        Find Best Matching FAQ
                    ↓
           Display Answer
```

## 🔧 Installation

### 1. Install Python

Make sure Python 3.x is installed.

Check your Python version:

```bash
python --version
```

### 2. Install Required Libraries

Open the terminal inside the project folder and run:

```bash
pip install pandas nltk scikit-learn
```

### 3. Download NLTK Resources

Open Python:

```bash
python
```

Then run:

```python
import nltk

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
```

Exit Python:

```python
exit()
```

## ▶️ Run the Chatbot

Navigate to the project directory:

```bash
cd College_FAQ_Chatbot
```

Run:

```bash
python chatbot.py
```

The chatbot will ask:

```text
Ask your question:
```

Enter a question such as:

```text
what are the college timings?
```

## 💬 Example

### User

```text
what are the college timings?
```

### Chatbot

```text
Best Matching FAQ:
What are the college timings?

Similarity Score:
0.xx

Chatbot:
The college is open from 9:00 AM to 4:30 PM.
```

## 📊 FAQ Dataset

The chatbot currently contains FAQs related to:

* Admission
* Admission process
* Required documents
* College timings
* Academic year
* College fees
* Courses
* Admission status
* Hostel facilities
* Hostel application
* Library
* Library timings
* Contact information
* College location
* Semester examinations
* Exam timetable
* Scholarships
* Scholarship application
* Student ID card
* Course-related problems

## 🧠 NLP Pipeline

The chatbot preprocesses the FAQ questions and user input using the following steps:

1. Convert text to lowercase
2. Remove punctuation
3. Tokenize the text
4. Remove English stopwords
5. Apply stemming
6. Convert processed text into TF-IDF vectors
7. Calculate cosine similarity
8. Select the most similar FAQ
9. Return the corresponding answer

## 🔍 Cosine Similarity

Cosine similarity is used to measure how similar the user's question is to each FAQ question.

The FAQ with the highest similarity score is selected as the potential answer.

## 🎯 Project Objective

The main objective of this project is to demonstrate how NLP and machine-learning techniques can be used to build a simple automated FAQ chatbot for educational institutions.

## 🚀 Future Improvements

Possible improvements include:

* 🌐 Streamlit web interface
* 💬 Chat history
* 🎤 Voice input
* 🔊 Text-to-speech responses
* 🗄️ Database integration
* 🔐 Admin panel for updating FAQs
* 🌍 Support for multiple languages
* 🤖 Advanced transformer-based NLP models

## 📸 Project Output

Add screenshots of your chatbot output here after running the project.

Example:

```text
User:
what are the college timings?

Chatbot:
The college is open from 9:00 AM to 4:30 PM.
```

## 👨‍💻 Author

**Nagatarun**

## 📄 License

This project is created for educational and internship purposes.
