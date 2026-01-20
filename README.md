# 📊 Financial Data Extractor (LangChain + Streamlit)
> A mini project built while learning LangChain essentials to extract structured financial data from news articles using LLMs.


## 🔗 Live Demo

Try it live on Streamlit: [Financial Data Extractor](https://financial-data-extractor-langchain-ttk7mwvlmqlbukjbyi6y3s.streamlit.app/)

---

A simple LLM-powered web app that extracts **Revenue and EPS (Actual vs Expected)**
from financial news paragraphs using **LangChain + Groq LLM** and displays them in a table using **Streamlit**.

This project is built as part of learning **LangChain Essentials** and understanding
how to structure end-to-end LLM applications.

---

## 🚀 Features

- 📝 Input financial news paragraph
- 🤖 Uses LLM via LangChain to extract:
  - Revenue Actual
  - Revenue Expected
  - EPS Actual
  - EPS Expected
- 📊 Displays structured data in table format
- 🧩 Clean separation of UI and LLM logic

---

## 🧠 Architecture Flow
<img width="1422" height="600" alt="Untitled design (2)" src="https://github.com/user-attachments/assets/7c05be22-b4e8-4ab5-a4dd-a966f4f0705b" />

---

## 🔍 What Does This App Do?

This application extracts structured financial metrics from unstructured
news articles using an LLM.

It identifies and returns:

- Revenue (Actual vs Expected)
- EPS (Actual vs Expected)

The extracted values are displayed in a clean table format for easy comparison.

---

## ⚙️ How It Works

1. User enters a financial news paragraph in the Streamlit UI.
2. The text is passed to the LangChain pipeline.
3. A prompt template instructs the LLM to extract financial values.
4. Groq-hosted Llama 3.3 model processes the request.
5. The response is parsed using a JSON Output Parser.
6. Parsed values are converted into a Pandas DataFrame.
7. The table is rendered back in the Streamlit interface.

---

## 🧪 Example

### 📥 Input

> Apple reported quarterly revenue of $94.93 billion, beating estimates of  
> $94.58 billion. Earnings per share came in at $1.64 compared to expectations  
> of $1.60.

### 📤 Output

| Measure | Estimated | Actual |
|--------|----------|--------|
| Revenue | 94.58 billion | 94.93 billion |
| EPS | 1.60 | 1.64 |

---

## 🛠️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Keshx-3/Financial-Data-Extractor-Langchain.git
cd financial-data-extractor-langchain
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

GROQ_API_KEY=your_api_key_here


5. Run the App
```bash
streamlit run main.py
```




