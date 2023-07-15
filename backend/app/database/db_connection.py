import pymongo
from backend.app.data.db_impl.speaker_db import SpeakerDB
from backend.app.data.db_impl.speech_db import SpeechDB
from backend.app.data.db_impl.protocol_db import ProtocolDB
from backend.app.data.db_impl.agenda_item_db import AgendaItemDB
from backend.app.data.db_impl.faction_db import FactionDB


class DBConnection:


    def __init__(self, host="mongodb://localhost:27017/"):
        self.client = pymongo.MongoClient(host)
        self.db_name = "parlament_browser"
        self.db = self.client[self.db_name]


    def get_collection(self, collection_name):
        return self.db[collection_name]


    def get_speakers(self):
        collection = self.get_collection("speakers")
        speakers = []


        for speaker_doc in collection.find():
            speaker = SpeakerDB(speaker_doc)
            speakers.append(speaker)
        return speakers


    def get_speeches(self):
        collection = self.get_collection("speeches")
        speeches = []
        for speech_doc in collection.find():
            speech = SpeechDB(speech_doc)
            speeches.append(speech)
        return speeches


    def get_protocols(self):
        collection = self.get_collection("protocols")
        protocols = []
        for protocol_doc in collection.find():
            protocol = ProtocolDB(protocol_doc)
            protocols.append(protocol)
        return protocols
    
    def get_factions(self):
        collection = self.get_collection("factions")
        factions = []
        for faction_doc in collection.find():
            faction = FactionDB(faction_doc)
            factions.append(faction)
        return factions


    def get_speech_by_id(self, speech_id):
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
        try:
            protocol_doc = self.get_collection("protocols").find_one({"_id": protocol_id})
            protocol = ProtocolDB(protocol_doc)
            return protocol
        except:
            print(f"Protocol with id {protocol_id} not found!")
            return None
