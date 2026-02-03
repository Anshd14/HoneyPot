from transformers import pipeline

class ScamDetector:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="distilbert-base-uncased"
        )

    def analyze(self, text: str):
        result = self.classifier(text)[0]

        label = result['label']
        score = result['score']

        scam_keywords = [
            "lottery",
            "urgent",
            "verify account",
            "bank login",
            "password"
        ]

        if any(word in text.lower() for word in scam_keywords) or label == "NEGATIVE":
            return True, "phishing"

        return False, None
