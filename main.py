import pymongo
from backend.app.data.factory import Factory
from backend.app.nlp.sentiment_analyzer import SentimentAnalyzer
from backend.app.database.db_connection import DBConnection

from backend.app.database.db_loader import DBLoader
import time



def main():

    # server = WebServer()
    # server.run()

    
    # factory = Factory()
    # factory.init()
    # print(f"Protocols in factory: {len(factory.protocols)}")
    db = DBConnection()
    



    # sent_dist_mongo = db.get_sentiment_distribution(speaker_id="f5705b51a699d8196ced41cdfe221273b8b6cd84ad08266d35db6c786a559b47")
    # print(f"Sentiment distribution (Mongo): {sent_dist_mongo}") 

    # sent_dist_filter = db.get_sentiment_distribution("01.01.2021", "01.01.2023", speaker_id="f5705b51a699d8196ced41cdfe221273b8b6cd84ad08266d35db6c786a559b47")
    # print(f"Sentiment distribution (Mongo): {sent_dist_filter}") 

    # sent_speecht = db.get_sentence_sentiment_distribution_in_speech("ID2011500700")
    # print(f"Sentiment distribution (Mongo): {sent_speecht}")

    top_entities = db.get_top_named_entities()
    print(len(top_entities))
    for entity in top_entities:
        print(entity)
        print("\n__________________________________________\n")
    # loader = DBLoader()
    # loader.analyze_and_save_speeches()


if __name__ == "__main__":
    main()

