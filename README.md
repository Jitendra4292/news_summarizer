# Personal News Summarizer & Sentiment Tracker

A simple Python web app that fetches news articles from URLs, summarizes their content, and shows sentiment analysis (Positive, Neutral, Negative). Built with Streamlit, Newspaper3k, HuggingFace Transformers, and TextBlob.

## Features

- Input a news article URL.
- Fetch and display the article’s full text and title.
- Generate a concise summary using state-of-the-art NLP summarization.
- Show sentiment of the article content.
- Beginner-friendly and easy to run locally.

## Prerequisites

- Python 3.7 or higher installed on your computer.
- Internet connection to download article content and model weights.
- (Optional but recommended) Git for cloning the repo.

## Step-by-Step Setup & Running Instructions

### 1. Clone the Repository (or Download the Project Folder)

If you have Git installed, open your terminal (Command Prompt / PowerShell / VS Code Terminal) and run:


Or simply download the ZIP from GitHub and extract it, then open the folder in your terminal.

*(Replace `YOUR-USERNAME` and `news-summarizer-tracker` with your actual repo details.)*

### 2. Create & Activate a Python Virtual Environment

To keep dependencies isolated, create a virtual environment and activate it:

**On Windows:**


**On Mac/Linux:**


You should see your terminal prompt change to indicate the environment is active (e.g., `(venv)`).

### 3. Install Required Python Packages

Make sure you're inside your activated virtual environment, then run:


- This installs the web framework, article fetching, NLP models, and sentiment analysis tools.
- The `lxml[html_clean]` fixes some parsing issues with Newspaper3k.

### 4. Run the Streamlit App

Start the app by running:


This will launch a local web server and open your default browser displaying the app interface.

### 5. Use the App

- Paste a valid news article URL into the input box.
- The app fetches and displays the full article title and content.
- It automatically summarizes the article and shows the summary.
- Displays the sentiment score and label for the article content.

### 6. (Optional) Deactivate Virtual Environment

When you're done, you can exit the environment by typing:


## Troubleshooting & Tips

- If you get errors about missing packages, double-check you activated the virtual environment.
- For slow startup, first run might download large NLP models.
- Not all news URLs are parseable; try reliable sources like BBC, CNN, Reuters.
- If `git` is not installed, you can download the project ZIP instead.
- If Newspaper3k gives errors about lxml, make sure to run:


- To update dependencies later:


## Project Files

- **app.py** — Main Streamlit application code.
- **requirements.txt** — List of all Python packages used.
- **.gitignore** — Specifies files/folders to ignore in Git (e.g., `.venv`).
- **README.md** — This file.

## License & Contact

- Licensed under MIT.
- Created by [Your Name].
- Questions? Feel free to open issues on the GitHub repo.

