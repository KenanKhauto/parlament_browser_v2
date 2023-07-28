

class SpeechDB:
    """
    Represents a speech retrieved from a MongoDB document.

    @ivar document: The MongoDB document containing the speech data.
    @ivar id: Unique identifier for the speech.
    @ivar text: Text content of the speech.
    @ivar speaker: Identifier for the speaker who delivered the speech.
    @ivar agenda_item: Agenda item related to the speech.
    @ivar comments: List of comments related to the speech.
    @ivar legislative_period: The legislative period during which the speech was delivered.
    @ivar date: The date the speech was delivered.

    """
    def __init__(self, mongo_doc) -> None:
        """
        Initializes a speech with the given MongoDB document.

        @param mongo_doc: The MongoDB document containing the speech's data.
        """
        self.document = mongo_doc
        self.id = self.document["_id"]
        self.text = self.document["text"]
        self.speaker = self.document["speaker"]
        self.agenda_item = self.document["agenda_item"]
        self.comments = self.document["comments"]
        self.legislative_period = self.document
        self.date = self.document["date"]

        
    def to_json(self):
        """
        Returns the speech data as a dictionary.

        @return: Speech data as a dictionary.
        """
        return self.document