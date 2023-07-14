import pymongo
from app.data.factory import Factory

def main():
    #factory = Factory()
    #print(f"Number of protocols: {len(factory.protocols)}")
    
    #print(f"Number of speakers: {len(factory.speakers)}")
    
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["parlament_browser"]
    collection = db["speakers"]
    # for protocol in factory.protocols:
    #     db["protocols"].insert_one(protocol.to_mongo())
    #     print(f"Inserted protocol {protocol.id} into the database")
    
    #     for agenda_item in protocol.agenda_items:
    #         for speech in agenda_item.speeches:
    #             db["speeches"].insert_one(speech.to_mongo())
    #             print(f"Inserted speech {speech.id} into the database")

    # for speaker in factory.speakers:
    #     db["speakers"].insert_one(factory.speakers[speaker].to_mongo())
    #     print(f"Inserted speaker {speaker} into the database")   

    # for faction in factory.factions:
    #     db["factions"].insert_one(factory.factions[faction].to_mongo())
    #     print(f"Inserted faction {faction} into the database")

    for speeker in collection.find():
        print(f"{speeker.get('name')} \t {len(speeker.get('speeches'))}")

if __name__ == "__main__":
    main()
