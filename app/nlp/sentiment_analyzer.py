from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F


class SentimentAnalyzer(AutoModelForSequenceClassification):
    def __init__(self, model_name = "oliverguhr/german-sentiment-bert"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name)

    def predict(self, text):
        batch = self.tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt")

        with torch.no_grad():
            output = self.model(**batch)
            label_ids = torch.argmax(output.logits, dim=1).flatten().tolist()
            prediction_scores = F.softmax(output.logits, dim=1)
            labels = [self.model.config.id2label[label_id] for label_id in label_ids]

        return label_ids, labels, prediction_scores
    
