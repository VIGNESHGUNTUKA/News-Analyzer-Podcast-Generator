# 🎙️ NewsPod – Powered News Podcast Generator

**NewsPod** is a multilingual news analysis and podcast generation application that collects news, analyzes and summarizes articles, translates the generated summary into the user's selected language, and converts the final content into an audio podcast using AI voices.

The application supports both **manual news input** and **automatic news collection**.

---

## 🚀 Features

### 📰 News Collection

* Manual news input through pasted article text.
* Automatic news collection using the **GNews API**.
* Supports India-focused news collection.
* Category-based news selection:

  * Sports
  * Health
  * Technology
  * General
* Retrieves multiple articles for the selected category.
* Removes duplicate articles before processing.

### 🧠 News Analysis

The project processes the collected articles using:

* Text cleaning
* Stop-word removal
* Keyword extraction
* Frequency analysis
* Category-based processing
* Extractive summarization
* Title and description processing

The generated summary combines the most relevant information from the selected articles.

### 🌍 Multilingual Support

News can be generated in multiple languages:

* English
* Telugu
* Hindi
* Tamil

The application translates the generated English summary into the selected language before generating the podcast.

### 🎙️ AI Voice Selection

Users can choose between male and female AI voices.

Currently supported voices include:

| Language | Male Voice  | Female Voice |
| -------- | ----------- | ------------ |
| English  | Christopher | Aria         |
| Telugu   | Mohan       | Shruti       |
| Hindi    | Madhur      | Swara        |
| Tamil    | Valluvar    | Pallavi      |

Voice generation is implemented using **Microsoft Edge TTS**.

### 🎧 Podcast Generation

The application converts the translated summary into an MP3 podcast.

Generated podcasts include:

* Selected category
* Selected language
* Selected voice
* Timestamp

Example:

```text
SportsPodcast_14082026_160006.mp3
```

### 📄 Report Generation

A text report is generated for each podcast.

Reports contain:

* Category
* Language
* Number of articles
* Generated summary
* Podcast filename

Example:

```text
SportsNewsreport_Telugu_14082026_160006.txt
```

### 🌐 Web Application

The project is being developed as a web application with:

* Frontend UI
* FastAPI backend
* REST API endpoints
* Podcast generation
* Audio playback
* Podcast listing
* CORS support

---

# 🏗️ Project Architecture

```text
                    ┌─────────────────────┐
                    │       NewsPod       │
                    │    Web Interface    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │    FastAPI Backend  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┴────────────────┐
              │                                 │
              ▼                                 ▼
      ┌───────────────┐                 ┌───────────────┐
      │  Manual News  │                 │ Automatic News│
      └───────┬───────┘                 └───────┬───────┘
              │                                 │
              │                                 ▼
              │                           ┌────────────┐
              │                           │  GNews API │
              │                           └─────┬──────┘
              │                                 │
              └──────────────┬──────────────────┘
                             ▼
                    ┌─────────────────┐
                    │ Text Processing │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │   Summarization │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │   Translation   │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │    Edge TTS     │
                    └────────┬────────┘
                             ▼
                    ┌─────────────────┐
                    │   MP3 Podcast   │
                    └─────────────────┘
```

---

# 📁 Project Structure

```text
News_Podcast/
│
├── BackEnd/
│   │
│   ├── data/
│   │   └── sports_news.json
│   │
│   ├── output/
│   │   ├── Podcast/
│   │   └── Report/
│   │
│   └── src/
│       ├── app.py
│       ├── main.py
│       ├── newscollector.py
│       ├── news_storage.py
│       ├── userchoice.py
│       ├── config.py
│       ├── translator.py
│       ├── texttospeech.py
│       ├── textcleaner.py
│       ├── frequencyanalizer.py
│       ├── keywordextractor.py
│       ├── categorydetector.py
│       ├── summary.py
│       └── ...
│
├── UI/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── .env
├── .gitignore
├── requirements.txt
├── Procfile
└── README.md
```

---

# 🔄 Application Workflow

## Manual Mode

```text
User
 ↓
Enter News
 ↓
Select Language
 ↓
Select Voice
 ↓
Clean Text
 ↓
Analyze News
 ↓
Generate Summary
 ↓
Translate Summary
 ↓
Generate Podcast
 ↓
Save Report + MP3
```

## Automatic Mode

```text
User
 ↓
Select Category
 ↓
Select Language
 ↓
Select Voice
 ↓
GNews API
 ↓
Fetch Articles
 ↓
Remove Duplicates
 ↓
Extract Title + Description
 ↓
Generate Summary
 ↓
Translate Summary
 ↓
Generate Podcast
 ↓
Save Report + MP3
```

---

# 🔊 Supported Voice Selection

### English

```text
Male   → en-US-ChristopherNeural
Female → en-US-AriaNeural
```

### Telugu

```text
Male   → te-IN-MohanNeural
Female → te-IN-ShrutiNeural
```

### Hindi

```text
Male   → hi-IN-MadhurNeural
Female → hi-IN-SwaraNeural
```

### Tamil

```text
Male   → ta-IN-ValluvarNeural
Female → ta-IN-PallaviNeural
```

---

# 🛠️ Technologies Used

### Backend

* Python
* FastAPI
* Uvicorn
* Requests
* GNews API
* Python-dotenv

### Natural Language Processing

* Text preprocessing
* Stop-word removal
* Keyword extraction
* Frequency analysis
* Extractive summarization
* Deep Translator

### Text-to-Speech

* Microsoft Edge TTS

### Frontend

* HTML
* CSS
* JavaScript

### Development Tools

* Git
* GitHub
* Virtual Environment
* VS Code

---

# 📦 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/VIGNESHGUNTUKA/News-Analyzer-Podcast-Generator.git
```

```bash
cd News-Analyzer-Podcast-Generator
```

---

## 2. Create a Virtual Environment

The project uses Python 3.11.

```bash
python -m venv .venv
```

### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

---

## 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in the project root.

```env
GNEWS_API_KEY=your_gnews_api_key
```

The API key should not be committed to GitHub.

---

# ▶️ Running the Application

## Run the command-line application

From the project root:

```bash
cd BackEnd
python src/main.py
```

## Run the FastAPI backend

From the project root:

```bash
uvicorn BackEnd.src.app:app --reload
```

The backend will be available locally through the FastAPI server.

---

# 🔌 API Endpoints

The FastAPI backend provides endpoints for:

### Get Headlines

```text
GET /api/headlines
```

### Generate Manual Podcast

```text
POST /api/generate/manual
```

### Generate Automatic Podcast

```text
POST /api/generate/automatic
```

### Get Podcasts

```text
GET /api/podcasts
```

### Play Audio

```text
GET /api/audio/{filename}
```

---

# 📊 Example

A user can select:

```text
Category: Sports
Language: Telugu
Voice: Male
```

NewsPod then:

```text
Fetches Sports News
        ↓
Removes duplicate articles
        ↓
Processes the articles
        ↓
Generates a summary
        ↓
Translates the summary to Telugu
        ↓
Uses the selected Telugu AI voice
        ↓
Creates an MP3 podcast
```

Example output:

```text
SportsPodcast_Telugu_14082026_160006.mp3
```

---

# 🔒 Git Ignore

Sensitive and generated files are excluded from Git:

```text
__pycache__/
*.pyc
output/
.env
*.mp3
*.json
.venv/
```

---

# 🚧 Future Improvements

The following features are planned for future versions:

* [ ] Database integration for podcast history
* [ ] Improved natural-language podcast scripts
* [ ] AI-based news rewriting
* [ ] Better multilingual narration
* [ ] Personalized news recommendations
* [ ] Podcast favorites/bookmarks
* [ ] News source information in the UI
* [ ] Podcast download option
* [ ] User accounts
* [ ] Daily personalized podcasts
* [ ] Multiple podcast durations
* [ ] Cloud deployment

---

# 🎯 Project Goal

The goal of **NewsPod** is to make daily news easier to consume by transforming written news into personalized audio podcasts.

Instead of reading multiple news articles, users can:

```text
Choose a category
       ↓
Choose a language
       ↓
Choose a voice
       ↓
Generate
       ↓
Listen
```

**NewsPod — Your News. Your Language. Your Voice.** 🎙️

---

# 👨‍💻 Author

**Guntuka Vignesh**

B.Tech – Computer Science and Machine Learning

GitHub:

https://github.com/VIGNESHGUNTUKA
