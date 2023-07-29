import pymongo
from backend.app.data.db_impl.speaker_db import SpeakerDB
from backend.app.data.db_impl.speech_db import SpeechDB
from backend.app.data.db_impl.protocol_db import ProtocolDB
from backend.app.data.db_impl.agenda_item_db import AgendaItemDB
from backend.app.data.db_impl.faction_db import FactionDB


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