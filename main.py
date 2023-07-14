import pymongo
from app.data.factory import Factory

def main():
    #factory = Factory()
    #print(f"Number of protocols: {len(factory.protocols)}")
    

    
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    db = client["parlament_browser"]
    
    #for protocol in factory.protocols:
        #db["protocols"].insert_one(protocol.to_mongo())
        #print(f"Inserted protocol {protocol.id} into the database")
    
    collection = db["protocols"]
    print(f"Number of protocols in database: {collection.count_documents({})}")

    for protocol in collection.find().sort("date", pymongo.DESCENDING):
        print(protocol.get("date").strftime("%d.%m.%Y"))


    

if __name__ == "__main__":
    main()
