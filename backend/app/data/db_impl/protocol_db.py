
from backend.app.data.db_impl.agenda_item_db import AgendaItemDB

class ProtocolDB:

    def __init__(self, mongo_document):
        
        self.document = mongo_document
        self.id = self.document["_id"]
        self.date = self.document["date"]
        self.legislative_period = self.document["legislative_period"]
        self.session_start = self.document["session_start"]
        self.session_end = self.document["session_end"]
        self.session_duration = self.document["session_duration"]   
        self.session_number = self.document["session_number"]
        self.session_title = self.document["session_title"]
        self.agenda_items = []

        self.parse_agenda_items()

    def parse_agenda_items(self):
        agenda_items = self.document["agenda_items"]
        if len(agenda_items) == 0:
            self.agenda_items = []
            return
        for agenda_item in agenda_items:
            self.agenda_items.append(AgendaItemDB(agenda_item, self))
        