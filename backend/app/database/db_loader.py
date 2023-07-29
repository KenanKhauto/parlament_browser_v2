from torch.multiprocessing import Pool
from backend.app.nlp.sentiment_analyzer import SentimentAnalyzer
from backend.app.database.db_connection import DBConnection
from backend.app.nlp.spacy_text_analyzer import SpacyTextAnalyzer
import torch

def _process_batch(speeches_batch):
        """
        Analyzes a batch of speeches using the SentimentAnalyzer and SpacyTextAnalyzer.
        @param speeches_batch: A list of SpeechDB objects.
        @return: A list of strings containing the results of the analysis.
        """
        db = DBConnection()  # Each process gets its own DB connection
        model = SentimentAnalyzer()
        spacy_analyzer = SpacyTextAnalyzer()
        results = []
        for speech in speeches_batch:
            if not speech.analyzed:
                analyzed_doc = spacy_analyzer.analyze(" ".join(speech.text))
                tokens = spacy_analyzer.get_tokens(analyzed_doc)
                entities = spacy_analyzer.get_entities(analyzed_doc)
                sentences = spacy_analyzer.get_sentences(analyzed_doc)

                if sentences:
                    # Extract texts from the sentences
                    sentence_texts = [sentence["text"] for sentence in sentences]

                    # Get sentiment for all sentences in the speech at once
                    sent_ids_batch, labels_batch, prediction_scores_batch = model.predict(sentence_texts)
                    for index, sentence in enumerate(sentences):
                        sent_ids = sent_ids_batch[index]
                        labels = labels_batch[index]
                        prediction_scores = prediction_scores_batch[index]
                        sentence.update({"sentiment": {"sent_ids": sent_ids, "labels": labels, "prediction_scores": prediction_scores.numpy().tolist()}})
                
                db.update_speech(speech.id, {"tokens": tokens, "entities": entities, "sentences": sentences, "analyzed": True})
                results.append(f"Updated speech {speech.id} with tokens, entities, and sentences.")
                
                sent_ids, labels, prediction_scores = model.predict(" ".join(speech.text))
                db.update_speech(speech.id, {"sentiment": {"sent_ids": sent_ids, "labels": labels, "prediction_scores": prediction_scores.numpy().tolist()}})
                results.append(f"Updated speech {speech.id} with sentiment.")
            else:
                results.append(f"Speech {speech.id} has already been analyzed.")
            
            # Optional: Delete heavy objects and clear memory
            if 'analyzed_doc' in locals():
                del analyzed_doc
            if 'tokens' in locals():
                del tokens
            if 'entities' in locals():
                del entities
            if 'sentences' in locals():
                del sentences
            torch.cuda.empty_cache()

        return results


class DBLoader:
    """
    Class for loading data into the database.
    
    @ivar db: The DBConnection instance.
    @ivar batch_size: The batch size to use for parallel processing.
    @ivar num_processes: The number of processes to use for parallel processing.
    """
    _has_set_start_method = False

    @classmethod
    def set_start_method(cls):
        """
        Sets the start method for the torch multiprocessing module to "spawn" if it has not been set yet.
        """
        if not cls._has_set_start_method:
            torch.multiprocessing.set_start_method('spawn')
            cls._has_set_start_method = True

    def __init__(self, batch_size=50, num_processes=4):
        """
        Initializes the DBLoader with the given batch size and number of processes.
        """
        self.set_start_method()        
        self.db = DBConnection()
        self.batch_size = batch_size
        self.num_processes = num_processes

    def insert_protocols(self, factory):
        """
        Inserts all protocols from the given factory into the database.
        @param factory: The Factory instance containing the protocols to insert.
        """
        for protocol in factory.protocols:
            self.db["protocols"].insert_one(protocol.to_mongo())
            print(f"Inserted protocol {protocol.id} into the database")

    def insert_speeches(self, factory):
        """
        Inserts all speeches from the given factory into the database.
        @param factory: The Factory instance containing the speeches to insert.
        """
        for protocol in factory.protocols:
            for agenda_item in protocol.agenda_items:
                for speech in agenda_item.speeches:
                    self.db.get_collection("speeches").insert_one(speech.to_mongo())
                    print(f"Inserted speech {speech.id} into the database")

       
    def insert_speakers(self, factory):
        """
        Inserts all speakers from the given factory into the database.
        @param factory: The Factory instance containing the speakers to insert.
        """
        for speaker in factory.speakers:
            self.db["speakers"].insert_one(factory.speakers[speaker].to_mongo())
            print(f"Inserted speaker {speaker} into the database")


    def insert_factions(self, factory):
        """
        Inserts all factions from the given factory into the database.
        @param factory: The Factory instance containing the factions to insert.
        """
        for faction in factory.factions:
            self.db["factions"].insert_one(factory.factions[faction].to_mongo())
            print(f"Inserted faction {faction} into the database")
            
    def analyze_and_save_speeches(self):
        """
        Analyzes all speeches in the database using the SentimentAnalyzer and SpacyTextAnalyzer and saves the results.
        """
        speeches = self.db.get_speeches()
        total_speeches = len(speeches)
        speeches_analyzed = 0
        with Pool(self.num_processes) as pool:
            print(f"Using {self.num_processes} processes to analyze speeches...")
            for batch_results in pool.imap(_process_batch, self.batch_generator(speeches, self.batch_size)):
                speeches_analyzed += self.batch_size
                # Print summary after each batch
                print(f"Total speeches analyzed so far: {speeches_analyzed} out of {total_speeches}. Remaining: {total_speeches - speeches_analyzed}.")

    @staticmethod
    def batch_generator(data, batch_size):
        """
        Generates batches of the given size from the given data.
        @param data: The data to generate batches from.
        @param batch_size: The batch size.
        @return: A generator that yields batches of the given size.
        """
        for i in range(0, len(data), batch_size):
            yield data[i:i+batch_size]
    
    


