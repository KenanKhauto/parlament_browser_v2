import pymongo
from backend.app.data.db_impl.speaker_db import SpeakerDB
from backend.app.data.db_impl.speech_db import SpeechDB
from backend.app.data.db_impl.protocol_db import ProtocolDB
from backend.app.data.db_impl.agenda_item_db import AgendaItemDB
from backend.app.data.db_impl.faction_db import FactionDB
from datetime import datetime


class DBConnection:

    """
    Establishes a connection to the MongoDB and provides utility methods to retrieve various collections/documents.
    
    @ivar client: The MongoDB client instance.
    @ivar db_name: Name of the database.
    @ivar db: Database object.
    """

    def __init__(self, host="mongodb://localhost:27017/"):
        """
        Initializes the DBConnection with the given MongoDB host or defaults to localhost.
        
        @param host: The MongoDB connection string.
        """
        self.client = pymongo.MongoClient(host)
        self.db_name = "parlament_browser"
        self.db = self.client[self.db_name]


    def get_collection(self, collection_name):
        """
        Retrieves a specific collection from the database.
        
        @param collection_name: Name of the collection.
        @return: MongoDB collection instance.
        """
        return self.db[collection_name]


    def get_speakers(self):
        """
        Retrieves all speakers from the "speakers" collection.
        
        @return: A list of SpeakerDB objects.
        """
        collection = self.get_collection("speakers")
        speakers = []


        for speaker_doc in collection.find():
            speaker = SpeakerDB(speaker_doc)
            speakers.append(speaker)
        return speakers


    def get_speeches(self):
        """
        Retrieves all speeches from the "speeches" collection.
        
        @return: A list of SpeechDB objects.
        """
        collection = self.get_collection("speeches")
        speeches = []
        for speech_doc in collection.find():
            speech = SpeechDB(speech_doc)
            speeches.append(speech)
        return speeches


    def get_protocols(self):
        """
        Retrieves all protocols from the "protocols" collection.
        
        @return: A list of ProtocolDB objects.
        """
        collection = self.get_collection("protocols")
        protocols = []
        for protocol_doc in collection.find():
            protocol = ProtocolDB(protocol_doc)
            protocols.append(protocol)
        return protocols
    

    def get_factions(self):
        """
        Retrieves all factions from the "factions" collection.
        
        @return: A list of FactionDB objects.
        """
        collection = self.get_collection("factions")
        factions = []
        for faction_doc in collection.find():
            faction = FactionDB(faction_doc)
            factions.append(faction)
        return factions


    def get_speech_by_id(self, speech_id):
        """
        Retrieves a specific speech by its ID, along with its associated speaker.
        
        @param speech_id: ID of the desired speech.
        @return: A SpeechDB object or None if not found.
        """
        try:
            speech_doc = self.get_collection("speeches").find_one({"_id": speech_id})
            speech = SpeechDB(speech_doc)
            speaker_id = speech.speaker
            speaker_doc = self.get_collection("speakers").find_one({"_id": speaker_id})
            speaker = SpeakerDB(speaker_doc)
            speech.speaker = speaker
            return speech
        except:
            print(f"Speech with id {speech_id} not found!")
            return None
    
    
    def get_speaker_by_id(self, speaker_id):
        """
        Retrieves a specific speaker by its ID, along with their associated speeches.
        
        @param speaker_id: ID of the desired speaker.
        @return: A SpeakerDB object or None if not found.
        """
        try:
            speaker_doc = self.get_collection("speakers").find_one({"_id": speaker_id})
            speaker = SpeakerDB(speaker_doc)
            speeches = []
            for speech_id in speaker.speeches:
                speech_doc = self.get_collection("speeches").find_one({"_id": speech_id})
                speech = SpeechDB(speech_doc)
                speech.speaker = speaker
                speeches.append(speech)
            speaker.speeches = speeches
            return speaker
        except:
            print(f"Speaker with id {speaker_id} not found!")
            return None
        
    def get_protocol_by_id(self, protocol_id):
        """
        Retrieves a specific protocol by its ID.
        
        @param protocol_id: ID of the desired protocol.
        @return: A ProtocolDB object or None if not found.
        """
        try:
            protocol_doc = self.get_collection("protocols").find_one({"_id": protocol_id})
            protocol = ProtocolDB(protocol_doc)
            return protocol
        except:
            print(f"Protocol with id {protocol_id} not found!")
            return None

    def update_speech(self, speech_id, speech_data):
        """
        Updates a specific speech by its ID.
        
        @param speech_id: ID of the speech to update.
        @param speech_data: The new speech data.
        """
        self.get_collection("speeches").update_one({"_id": speech_id}, {"$set": speech_data})


    def get_sentiment_distribution(self, start_date=None, end_date=None, speaker_id=None):
        """
        Retrieves the sentiment distribution of all speeches in the database.
        
        @param start_date: The start date of the date range to filter by.
        @param end_date: The end date of the date range to filter by.
        @param speaker_id: The ID of the speaker to filter by.
        @return: A dictionary containing the sentiment distribution.
        """
        
        collection = self.get_collection("speeches")
        pipeline = [
            {
                "$match": {
                    "sentiment": {"$exists": True},
                    "sentiment.labels": {"$exists": True}
                }
            }
        ]

        if speaker_id:
            pipeline[0]["$match"]["speaker"] = speaker_id


        if start_date and end_date:
            # Convert start_date and end_date to datetime objects
            start_date = datetime.strptime(start_date, "%d.%m.%Y")
            end_date = datetime.strptime(end_date, "%d.%m.%Y")

            # Add the date filter to the pipeline
            pipeline[0]["$match"]["date"] = {
                "$gte": start_date,
                "$lte": end_date
            }

        pipeline += [
            {
                "$group": {
                    "_id": None,
                    "totalSpeeches": {"$sum": 1},
                    "positiveCount": {
                        "$sum": {
                            "$cond": [{"$in": ["positive", "$sentiment.labels"]}, 1, 0]
                        }
                    },
                    "negativeCount": {
                        "$sum": {
                            "$cond": [{"$in": ["negative", "$sentiment.labels"]}, 1, 0]
                        }
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "totalSpeeches": 1,
                    "positiveCount": 1,
                    "negativeCount": 1
                }
            }
        ]

        summary_data = list(collection.aggregate(pipeline))
        if summary_data:
            sentiment_distribution = {
                "positive": summary_data[0]["positiveCount"],
                "negative": summary_data[0]["negativeCount"],
                "neutral": summary_data[0]["totalSpeeches"] - summary_data[0]["positiveCount"] - summary_data[0]["negativeCount"],
                "totalSpeeches": summary_data[0]["totalSpeeches"]
            }
            return sentiment_distribution
        else:
            return None
        
    
    def get_sentence_sentiment_distribution_in_speech(self, speech_id):
        """
        Retrieves the sentiment distribution of all sentences in the given speech.
        
        @param speech_id: The ID of the speech to analyze.
        @return: A dictionary containing the sentiment distribution.
        """
        collection = self.get_collection("speeches")

        pipeline = [
            {
                "$match": {
                    "_id": speech_id,
                    "sentences.sentiment": {"$exists": True}
                }
            },
            {
                "$project": {
                    "sentences": 1
                }
            },
            {
                "$unwind": "$sentences"
            },
            {
                "$group": {
                    "_id": None,
                    "totalSentences": {"$sum": 1},
                    "positiveCount": {
                        "$sum": {
                            "$cond": [{"$in": ["positive", "$sentences.sentiment.labels"]}, 1, 0]
                        }
                    },
                    "negativeCount": {
                        "$sum": {
                            "$cond": [{"$in": ["negative", "$sentences.sentiment.labels"]}, 1, 0]
                        }
                    }
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "totalSentences": 1,
                    "positiveCount": 1,
                    "negativeCount": 1,
                    "neutralCount": {
                        "$subtract": ["$totalSentences", {"$sum" : ["$positiveCount", "$negativeCount"]}]
                    }
                }
            }
        ]

        
        result = list(collection.aggregate(pipeline))

        if result:
            return result[0]
        else:
            return None


    def get_top_named_entities(self, start_date=None, end_date=None, speaker_id=None):
        collection = self.get_collection("speeches")

        pipeline = [
            {
                "$match": {
                    "entities": {"$exists": True}
                }
            }
        ]

        if speaker_id:
            pipeline[0]["$match"]["speaker"] = speaker_id

        if start_date and end_date:
            # Convert start_date and end_date to datetime objects
            start_date = datetime.strptime(start_date, "%d.%m.%Y")
            end_date = datetime.strptime(end_date, "%d.%m.%Y")

            # Add the date filter to the pipeline
            pipeline[0]["$match"]["date"] = {
                "$gte": start_date,
                "$lte": end_date
            }

        pipeline += [
            {
                "$unwind": "$entities"
            },
            {
                "$group": {
                    "_id": "$entities.text",
                    "count": {"$sum": 1},
                    "label": {"$first": "$entities.label"}
                }
            },
            {
                "$sort": {"count": -1}
            },
            {
                "$group": {
                    "_id": "$label",
                    "top_entities": {"$push": {"entity": "$_id", "count": "$count"}}
                }
            },
            {
                "$project": {
                    "_id": 0,
                    "type": "$_id",
                    "top_entities": {"$slice": ["$top_entities", 10]}
                }
            }
        ]

        result = list(collection.aggregate(pipeline))
        return result