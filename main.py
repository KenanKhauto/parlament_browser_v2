import pymongo
from app.data.factory import Factory
from app.nlp.sentiment_analyzer import SentimentAnalyzer
from app.database.db_connection import DBConnection
from app.server.webserver import WebServer

def main():

    server = WebServer()
    server.run()
    

    # for speaker in db.get_speakers():
    #     print(f"{speaker.name} \t {len(speaker.speeches)}")
    
    # speaker = db.get_speaker_by_id("4da6b97afb1e31cee4b3076a4e9ce16855301244ba870aca2b2dd5ba86b317af")
    # print(speaker.name)
    # print(speaker.faction)
    # print(speaker.role_long)
    # print(speaker.role_short)
    # print(len(speaker.speeches))

    # factions = db.get_factions()
    # for faction in factions:
    #     print(f"{faction.name} \t {len(faction.members)}")

    # speeches = db.get_speeches()
    # for speech in speeches:
    #     print(f"{speech.id} \n {speech.speaker} \n {speech.agenda_item} \n {speech.text}")
    #     print("--------------------------------------------------")
    
    # protocols = db.get_protocols()
    # for protocol in protocols:
    #     print(f"{protocol.id} \t {protocol.date}  \t {protocol.session_title}")
    #     print("--------------------------------------------------")

    # speech = db.get_speech_by_id("ID2011500200")
    # print(f"{speech.id} \n {speech.speaker.name} \n {speech.agenda_item} \n {speech.text}")

    # for protocol in factory.protocols:
    #     db["protocols"].insert_one(protocol.to_mongo())
    #     print(f"Inserted protocol {protocol.id} into the database")
    
    # for protocol in factory.protocols:
    #     for agenda_item in protocol.agenda_items:
    #         for speech in agenda_item.speeches:
    #             db.get_collection("speeches").insert_one(speech.to_mongo())
    #             print(f"Inserted speech {speech.id} into the database")

    # for speaker in factory.speakers:
    #     db["speakers"].insert_one(factory.speakers[speaker].to_mongo())
    #     print(f"Inserted speaker {speaker} into the database")   

    # for faction in factory.factions:
    #     db["factions"].insert_one(factory.factions[faction].to_mongo())
    #     print(f"Inserted faction {faction} into the database")

    # for speeker in collection.find():
    #     print(f"{speeker.get('name')} \t {len(speeker.get('speeches'))}")

    # speech = db["speeches"].find_one()

    # model = SentimentAnalyzer()
    # sent_ids, labels, prediction_scores = model.predict(" ".join(speech.get("text")))

    # for i, id in enumerate(sent_ids):
    #     print(f"{id} \t {labels[i]} \t {prediction_scores[i][id]}")


if __name__ == "__main__":
    main()
