# STOPPING WORDS(IS,WAS,THE,....)
STOP_WORDS = {
    "the", "a", "an", "and", "for",
    "in", "of", "to", "is", "was" ,"after"
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
    }
}