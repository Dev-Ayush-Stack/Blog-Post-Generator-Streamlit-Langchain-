# 📝 Blog Post Generator

A simple and interactive **Streamlit-based web application** that generates well-structured blog posts from a given topic using LLM-powered text generation.

---

## 🚀 Features

* 🔹 Generate blog content from any topic
* 🔹 Clean and minimal Streamlit UI
* 🔹 Customizable tone and style (if implemented)
* 🔹 Fast and lightweight app structure
* 🔹 Easy to run locally using Poetry or pip

---

## 📂 Project Structure

```
Blog-Post-Generator/
│── blog-app.py          # Main Streamlit application
│── pyproject.toml       # Dependency management (Poetry)
│── requirements.txt     # Converted dependencies for pip users
│── README.md            # Project documentation
```

---

## ⚙️ Installation & Setup

### 🔹 Option 1: Using Poetry (Recommended)

1. Install Poetry (if not installed):

```bash
pip install poetry
```

2. Install dependencies:

```bash
poetry install
```

3. Run the app:

```bash
poetry run streamlit run blog-app.py
```

---

### 🔹 Option 2: Using requirements.txt (pip)

If you prefer pip, you can use the exported dependencies:

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run the app:

```bash
streamlit run blog-app.py
```

---

## 🔄 Converting `pyproject.toml` → `requirements.txt`

This project uses **Poetry** for dependency management, but also supports pip.

To generate `requirements.txt` from `pyproject.toml`:

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

---

## 🧠 How It Works

1. User enters a topic in the input field
2. The app sends the prompt to an LLM
3. The model generates a structured blog post
4. Output is displayed instantly on the UI

---

## 📸 UI Overview

* Centered heading
* Topic input box
* Generate button
* Output blog section

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain / LLM APIs**
* **Poetry (Dependency Management)**

---

## 📌 Future Improvements

* Add tone/style selector
* Export blog as PDF/Markdown
* Add history of generated blogs
* Improve UI/UX styling

---

## 👨‍💻 Author

**Ayush Pandey**
AI/ML & Generative AI Enthusiast

---

## ⭐ Contribute

Feel free to fork this repository and enhance the project!

---

## 📜 License

This project is open-source and available under the MIT License.
