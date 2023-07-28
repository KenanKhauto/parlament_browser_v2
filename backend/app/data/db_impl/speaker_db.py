
class SpeakerDB:
    """
    Represents a speaker retrieved from a MongoDB document.

    @ivar document: The MongoDB document containing the speaker's data.
    @ivar id: Unique identifier for the speaker.
    @ivar title: The title or honorific of the speaker.
    @ivar name: Full name of the speaker.
    @ivar first_name: First name of the speaker.
    @ivar last_name: Last name of the speaker.
    @ivar role_long: Long-form role or title of the speaker.
    @ivar role_short: Short-form role or title of the speaker.
    @ivar faction: Faction or party to which the speaker belongs.
    @ivar speeches: List of speeches associated with the speaker.
    """
    def __init__(self, mongo_doc) -> None:
        """
        Initializes a speaker with the given MongoDB document.

        @param mongo_doc: The MongoDB document containing the speaker's data.
        """
        self.document = mongo_doc
        self.id = self.document["_id"]
        self.title = self.document["title"]
        self.name = self.document["name"]
        self.first_name = self.document["first_name"]
        self.last_name = self.document["last_name"]
        self.role_long = self.document["role_long"]
        self.role_short = self.document["role_short"]
        self.faction = self.document["faction"]
        self.speeches = self.document["speeches"]

    def add_speech(self, speech):
        """
        Adds a speech to the speaker's list of speeches.

        @param speech: The speech to be added.
        """
        self.speeches.append(speech)

    def to_json(self):
        """
        Returns the speaker data as a dictionary.

        @return: Speaker data as a dictionary.
        """
        return self.document