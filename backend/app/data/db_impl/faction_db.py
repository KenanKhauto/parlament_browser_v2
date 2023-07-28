
class FactionDB:
    """
    Represents a faction retrieved from a MongoDB document.

    @ivar document: The MongoDB document containing the faction data.
    @ivar id: Unique identifier for the faction.
    @ivar name: Name of the faction.
    @ivar members: List of members associated with the faction.
    """
    def __init__(self, mongo_doc) -> None:
        """
        Initializes a faction with the given MongoDB document.

        @param mongo_doc: The MongoDB document containing the faction data.
        """
        self.document = mongo_doc
        self.id = self.document["_id"]
        self.name = self.document["name"]
        self.members = self.document["members"]

    