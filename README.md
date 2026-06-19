# News Analyzer & Multilingual Podcast Generator

## Overview

News Analyzer & Multilingual Podcast Generator is a Python-based application that can analyze news articles, generate summaries, translate content into multiple languages, and create audio podcasts using text-to-speech technology.

The project supports both manual news analysis and automatic news collection using NewsAPI. Users can either paste their own news article or automatically fetch the latest news from different categories and generate multilingual podcasts.

---

## Features

### Manual News Analysis Mode

* Accepts user-pasted news articles
* Cleans and preprocesses text
* Removes stop words
* Performs word frequency analysis
* Extracts important keywords
* Detects news category automatically
* Generates article summary
* Translates summary into selected language
* Generates podcast audio with timestamp
* Creates detailed analysis report with timestamp

### Automatic News Collection Mode

* Fetches latest news using NewsAPI
* Supports Sports, Health, Technology, and General News categories
* Generates structured news briefs
* Creates multilingual podcasts
* Generates timestamped reports
* Generates timestamped podcast files

### Translation Support

* English
* Telugu
* Hindi
* Tamil

### Podcast Generation

* Text-to-Speech conversion using gTTS
* Multilingual audio generation
* Category-based podcast creation
* Intro and outro narration

### Reporting

* News analysis reports
* Automatic news reports
* Timestamped report generation
* Summary storage for future reference

### Error Handling

* Invalid menu selection handling
* Empty article handling
* API response validation
* Missing news handling
* Translation and audio generation error handling

---

## Technologies Used

* Python
* NewsAPI
* gTTS (Google Text-to-Speech)
* deep-translator
* requests
* python-dotenv

---

## Project Workflow

### Manual News Mode

User Pastes News Article
↓
Text Cleaning
↓
Word Frequency Analysis
↓
Keyword Extraction
↓
Category Detection
↓
Summary Generation
↓
Language Selection
↓
Translation
↓
Podcast Generation
↓
Timestamped Report Generation

---

### Automatic News Mode

User Selects Category
↓
NewsAPI Fetches Latest News
↓
News Brief Generation
↓
Language Selection
↓
Translation
↓
Podcast Generation
↓
Timestamped Report Generation

---

## Supported Categories

* Sports
* Health
* Technology
* General News

---

## Project Structure

```text
News_Podcast/
│
├── src/
│   ├── main.py
│   ├── newscollector.py
│   ├── newsbrief.py
│   ├── translator.py
│   ├── texttospeech.py
│   ├── reportgenerator.py
│   ├── userchoice.py
│   ├── cleaner.py
│   ├── summarizer.py
│   └── config.py
│
├── data/
│   └── JSON files collected from NewsAPI
│
├── output/
│   ├── reports/
│   └── podcasts/
│
├── .env
└── README.md
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-url>
cd News_Podcast
```

### Configure Environment Variables

Create a `.env` file:

```env
NEWS_API_KEY=your_api_key_here
```

---

## How to Run

```bash
python src/main.py
```

---

## Sample Output

### Podcast Introduction

```text
Welcome to today's Sports Podcast.

First, the New York Knicks are expected to visit the White House following their NBA championship victory.

Meanwhile, World Cup 2026 continues to generate excitement around the globe.

Thank you for listening. Stay tuned for more updates.
```

---

## Future Enhancements

* Improved podcast narration
* Additional language support
* Web-based interface
* AI-powered news rewriting
* Personalized news recommendations
* Podcast history management

