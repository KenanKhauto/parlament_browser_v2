

class AgendaItemDB:
    """
    Represents an agenda item retrieved from a MongoDB document.

    @ivar document: The MongoDB document containing the agenda item data.
    @ivar id: Unique identifier for the agenda item.
    @ivar protocol: Reference to the associated protocol.
    @ivar title: Title of the agenda item.
    @ivar speeches_ids: List of IDs corresponding to speeches associated with the agenda item.
    @ivar table_of_contents: Table of contents for the agenda item.
    @ivar speeches: List of speeches associated with the agenda item.
    """
    def __init__(self, mongo_document, protocol):
        """
        Initializes an agenda item with the given MongoDB document and associated protocol.

        @param mongo_document: The MongoDB document containing the agenda item data.
        @param protocol: Reference to the associated protocol.
        """
        self.document = mongo_document
        self.id = self.document["_id"]
        self.protocol = protocol
        self.title = self.document["title"]
        self.speeches_ids = self.document["speeches"]
        self.table_of_contents = self.document["table_of_contents"]
        self.speeches = self.document["speeches"]

    def to_json(self):
        """
        Converts the agenda item to its JSON representation.

        @return: A dictionary representing the JSON format of the agenda item.
        """
        return self.document