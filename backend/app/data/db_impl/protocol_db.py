
from backend.app.data.db_impl.agenda_item_db import AgendaItemDB

class ProtocolDB:
    """
    Represents a protocol retrieved from a MongoDB document.

    @ivar document: The MongoDB document containing the protocol data.
    @ivar id: Unique identifier for the protocol.
    @ivar date: Date of the protocol.
    @ivar legislative_period: Legislative period associated with the protocol.
    @ivar session_start: Start time of the session.
    @ivar session_end: End time of the session.
    @ivar session_duration: Duration of the session.
    @ivar session_number: Session number.
    @ivar session_title: Title of the session.
    @ivar agenda_items: List of agenda items associated with the protocol.
    """
    def __init__(self, mongo_document):
        """
        Initializes a protocol with the given MongoDB document.

        @param mongo_document: The MongoDB document containing the protocol data.
        """
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
        """
        Parses the agenda items from the MongoDB document and populates the agenda_items attribute.
        """
        agenda_items = self.document["agenda_items"]
        if len(agenda_items) == 0:
            self.agenda_items = []
            return
        for agenda_item in agenda_items:
            self.agenda_items.append(AgendaItemDB(agenda_item, self))
        

    def to_json(self):
        """
        Returns the protocol data as a dictionary.

        @return: Protocol data as a dictionary.
        """
        return self.document