# STOPPING WORDS(IS,WAS,THE,....)
STOP_WORDS = {
    "the", "a", "an", "and", "for",
    "in", "of", "to", "is", "was", "after", "on", "by",
    "with", "from", "at", "as",
}
# CATEGORY DETECTION 
CATEGORY_KEYWORDS = {

    "Sports": {
        "cricket", "football", "badminton", "tennis", "hockey",
        "match", "player", "team", "score", "tournament",
        "championship", "league", "stadium", "coach", "victory",
        "defeat", "batting", "bowling", "wicket", "innings",
        "goal", "medal", "athlete", "competition", "sports"
    },

    "Health": {
        "health", "doctor", "hospital", "patient", "medicine",
        "medical", "treatment", "disease", "virus", "vaccine",
        "surgery", "healthcare", "diagnosis", "infection",
        "nutrition", "fitness", "mental", "cancer", "therapy",
        "research", "clinic", "epidemic", "wellness"
    },

    "Technology": {
        "technology", "software", "hardware", "computer",
        "internet", "application", "programming", "artificial",
        "intelligence", "machine", "learning", "ai", "robotics",
        "cybersecurity", "cloud", "data", "algorithm",
        "smartphone", "digital", "innovation", "automation",
        "network", "developer", "tech"
    },

    "Politics": {
        "government", "minister", "election", "parliament",
        "policy", "president", "prime", "vote", "political",
        "democracy", "campaign", "leader", "party", "assembly",
        "governor", "legislation", "law", "cabinet", "politics"
    },

    "Business": {
        "business", "market", "stock", "investment", "economy",
        "company", "finance", "profit", "revenue", "trade",
        "industry", "share", "bank", "investor", "startup",
        "funding", "commercial", "economic", "growth", "sales"
    },

    "Entertainment": {
        "movie", "film", "actor", "actress", "music",
        "cinema", "director", "celebrity", "song", "album",
        "show", "television", "series", "streaming", "festival",
        "entertainment", "hollywood", "bollywood", "performance"
    },

    "Science": {
        "science", "space", "astronomy", "physics", "chemistry",
        "biology", "research", "discovery", "laboratory", "galaxy",
        "universe", "nasa", "isro", "planet", "satellite", "experiment"
    },

    "World": {
        "world", "global", "international", "nation", "country",
        "summit", "foreign", "diplomacy", "treaty", "ambassador",
        "border", "united", "nations", "peace", "conflict"
    },

    "General": {
        "news", "today", "report", "update", "headline",
        "breaking", "latest", "daily", "bulletin", "current"
    }
}
# CONNECTORS BETWEEN THE LINES
connectors = [
        "Meanwhile,",
        "In other news,",
        "Moving on,",
        "Additionally,",
        "Another major story,"
    ] 

# Different Voices
voices= {
    "English":{
        "Male": "en-US-ChristopherNeural",
        "Female": "en-US-AriaNeural"
    },
    "Telugu": {
        "Male": "te-IN-MohanNeural",
        "Female": "te-IN-ShrutiNeural"
    },
    "Hindi": {
        "Male": "hi-IN-MadhurNeural",
        "Female": "hi-IN-SwaraNeural"
    },
    "Tamil": {
        "Male": "ta-IN-ValluvarNeural",
        "Female": "ta-IN-PallaviNeural"
    }
}