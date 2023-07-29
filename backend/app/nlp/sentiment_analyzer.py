from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F

class SentimentAnalyzer:
    """
    A class for analyzing the sentiment of a given text.
    
    @ivar tokenizer: The tokenizer used for tokenizing the text.
    @ivar model: The model used for predicting the sentiment.
    @ivar device: The device used for the prediction.
    """

    def __init__(self, model_name="oliverguhr/german-sentiment-bert", device="cuda:0"):
        """
        Initializes the SentimentAnalyzer with the given model name and device.

        @param model_name: The name of the model to use.
        @param device: The device to use for the prediction.
        """

        self.device = device
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(self.device)
        self.model.eval()


    def predict(self, text):
        """
        Predicts the sentiment of the given text.
        
        @param text: The text to analyze.
        @return: A tuple containing the predicted label ids, labels, and prediction scores.
        """
        if isinstance(text, str):
            text = [text]  # Convert single string to list for consistent tensor shape

        batch = self.tokenizer(text, padding=True, truncation=True, max_length=512, return_tensors="pt").to(self.device)

        with torch.no_grad():
            output = self.model(**batch)
            label_ids = torch.argmax(output.logits, dim=1).flatten().tolist()
            prediction_scores = F.softmax(output.logits, dim=1).cpu()  # Move to CPU before converting to numpy
            labels = [self.model.config.id2label[label_id] for label_id in label_ids]

        return label_ids, labels, prediction_scores


if __name__ == "__main__":
    pass
    model = SentimentAnalyzer()
    print(model.predict("Das ist so schlecht"))
    print(model.predict("Die Rechten und die Linken sind auf der gleichen Ebene"))
    
    
