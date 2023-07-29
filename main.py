import pymongo
from backend.app.data.factory import Factory
from backend.app.nlp.sentiment_analyzer import SentimentAnalyzer
from backend.app.database.db_connection import DBConnection
from backend.app.server.webserver import WebServer
from backend.app.database.db_loader import DBLoader




def main():

    # server = WebServer()
    # server.run()
    
    db = DBConnection()
    speeches = db.get_speeches()
    count = 0
    for speech in speeches:
        if not speech.analyzed:
            count += 1
    if count > 0:
        print(f"{count} speeches have not been analyzed yet.")  
    else:
        print("All speeches have been analyzed.")
    # loader = DBLoader()
    # loader.analyze_and_save_speeches()


if __name__ == "__main__":
    main()
