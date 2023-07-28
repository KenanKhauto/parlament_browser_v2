


class FactionXML:
    """
    Represents a faction parsed from XML data.

    @ivar id: Unique identifier for the faction.
    @ivar name: The name of the faction.
    @ivar members: List of members (speakers) belonging to the faction.
    """
    def __init__(self, id, name):
            """
            Initializes a faction with a given ID and name.

            @param id: The unique identifier for the faction.
            @param name: The name of the faction.
            """
            self.id = id
            self.name = name
            self.members = []
    
    
    def add_speaker(self, speaker):
        """
        Adds a speaker to the faction's member list.

        @param speaker: The speaker to be added.
        """
        self.members.append(speaker)


    def to_mongo(self):
        """
        Converts the faction to its MongoDB representation.

        @return: A dictionary representing the MongoDB format of the faction.
        """
        return {
            "_id": self.id,
            "name": self.name,
            "members": [member.id for member in self.members]
        }
    

    def __str__(self) -> str:
        """
        Returns a string representation of the faction.

        @return: A string representation.
        """
        return f"{self.name} ({len(self.members)} members)"
    

    def __eq__(self, __value: object) -> bool:
        """
        Compares two factions for equality based on their IDs.

        @param __value: The other faction to compare with.
        @return: True if both factions are equal, False otherwise.
        """
        if not isinstance(__value, FactionXML):
            return False
        return self.id == __value.id
    