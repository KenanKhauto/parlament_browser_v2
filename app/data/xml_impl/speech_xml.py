
from bs4 import BeautifulSoup

class SpeechXML:
    """
    This class is used to create the XML file for the speech.
    """

    def __init__(self, speech_xml: BeautifulSoup, agenda_item):
        """
        This method initializes the class.
        :param speech: The speech.
        """
        self.document = speech_xml
        self.agenda_item = agenda_item
        self.id = None
        self.speaker = None
        self.date = self.agenda_item.protocol.date
        self.comments = []
        self.text = []
        self.parse()

    def parse(self):
        """
        This method parses the speech.
        """
        self.parse_speaker()
        self.parse_comments()
        self.parse_id()
        self.parse_text()

    def parse_text(self):
        """
        This method parses the text.
        """
        text_elements = self.document.find_all("p", {"klasse": "J"})
        if text_elements is None:
            self.text = []
            return
        for element in text_elements:
            self.text.append(element.get_text())

    
    def parse_id(self):
        """
        This method parses the id.
        """
        self.id = self.document.get("id")
    
    def parse_speaker(self):
        """
        This method parses the speaker.
        """
        
        self.speaker_xml = self.document.find("redner")
        #TODO: parse speaker

    def parse_comments(self):
        """
        This method parses the comments.
        """
        comments = self.document.find_all("kommentar")
        if comments is None:
            self.comments = []
            return
        for comment in comments:
            self.comments.append(comment.get_text())
     
    def __eq__(self, __value: object) -> bool:
        """
        This method checks if two objects are equal.
        :param __value: The object to compare.
        :return: True if the objects are equal, False otherwise.
        """
        if not isinstance(__value, SpeechXML):
            return False
        return self.id == __value.id


    def __str__(self) -> str:
        """
        This method returns the string representation of the object.
        :return: The string representation of the object.
        """
        return f"\nSpeech: {self.id} num comments {len(self.comments)} \t {self.date} \n"

    def to_mongo(self):
        """
        This method returns the object as a mongo object.
        :return: The object as a mongo object.
        """
        return {
            "_id": self.id,
            "speaker": self.speaker.id,
            "date": self.date,
            "comments": self.comments,
            "text": self.text,
            "agenda_item": self.agenda_item.id
        }



'''
<rede id="ID2011500100">
<p klasse="redner">
<redner id="11004742">
<name>
<vorname>Katrin</vorname>
<nachname>Helling-Plahr</nachname>
<fraktion>FDP</fraktion>
</name>
</redner>Katrin Helling-Plahr (FDP):</p>
<p klasse="J_1">Sehr geehrte Frau Präsidentin! Meine Damen und Herren! Ich habe noch nie so voller Demut hier gestanden wie heute, und ich habe auch noch nie eine Rede gehalten, die so wichtig ist für so unfassbar viele Menschen. Ich habe als Fachanwältin für Medizinrecht so viele Schicksale miterlebt und vielleicht auch zu oft mitgelitten. Diese Menschen, jeder Einzelne ist es, der für meine Gruppe im Mittelpunkt steht.</p>
<p klasse="J">Aus 2017 stammt ein Urteil des Bundesverwaltungsgerichts, das vielen schwerstkranken Menschen Hoffnung gegeben hat. Eine vom Hals abwärts gelähmte Dame, die künstlich beatmet werden musste und unter höchst schmerzhaften Krampfanfällen litt, hatte sich darum bemüht, in Deutschland legal ein Medikament zu bekommen, um ihrem Leben und ihrem Leiden ein Ende zu setzen. Sie starb in der Schweiz. Ihr Ehemann prozessierte und gewann.</p>
<p klasse="J">Natürlich wandten sich in der Folgezeit immer und immer wieder schwerstkranke Menschen an das zuständige Bundesinstitut. Alle Anträge wurden abgelehnt. Die Menschen wurden einfach alleine gelassen, anonym abgestempelt trotz eindeutiger höchstrichterlicher Rechtsprechung – allein mit ihren Schmerzen, ihrer Angst und ihrem Wunsch, gehen zu dürfen.</p>
<p klasse="J">Natürlich wandten sich viele in ihrer Not auch an ihre Angehörigen oder an Ärzte und medizinisches Personal. Sie flehten und bettelten, erlöst zu werden, immer wieder auch bei meinem heutigen Mitarbeiter Max als dereinst 14-jährigem Pflegepraktikanten. Natürlich half meist niemand. Zu groß ist die Angst vor Strafe und Gefängnis.</p>
<p klasse="J">Sie wenden sich auch an uns hier. Es vergeht kein Tag, an dem mir nicht ein Betroffener sein Schicksal schildert und mich voller Hoffnung bittet, dass er irgendwann sterben kann, wie er es für sich als würdevoll empfindet.</p>
<p klasse="J">Das Urteil des Bundesverfassungsgerichts aus dem Jahr 2020 war wegweisend. § 217 Strafgesetzbuch ist Geschichte. Jeder Mensch hat ein Recht auf selbstbestimmtes Sterben und auch ein Recht darauf, hierbei Hilfe in Anspruch zu nehmen. Jeder selbstbestimmte Mensch darf sein Lebensende so gestalten, wie er es für sich als würdig empfindet. Einen gegen die Autonomie gerichteten Lebensschutz kann und darf es nicht geben. Aber es zeigt auch Handlungsbedarf auf. Wie stellen wir sicher, dass jemand tatsächlich selbstbestimmt handelt? Wie schaffen wir ein Auffangnetz, ohne zu bevormunden? Und gehört zu einem Recht auf selbstbestimmtes Sterben nicht ehrlicherweise auch die Möglichkeit, transparent ein entsprechendes Medikament erhalten zu können?</p>
<p klasse="J">Meine Gruppe hat um Antworten gerungen, nun 1 226 Tage lang. Ich bin so vielen Menschen von Union bis Linksfraktion dankbar für die gemeinsame Arbeit. Das Ergebnis steht heute zur Abstimmung. Es lässt niemanden allein.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="O">Es sieht ein flächendeckendes, hochwertiges und umfassendes Beratungsangebot vor, Stellen, an die sich Menschen mit Suizidgedanken wenden können, an denen sie nicht bevormundet werden, ihnen aber gerade auch Hilfe zum Weiterleben vermittelt wird, wo sie an die Hand genommen werden und der Weg in medizinische Versorgung, vielleicht die Palliativmedizin, oder auch zu sozialen Unterstützungsangeboten geebnet wird, ganz individuell zugeschnitten, Stellen, an denen jede selbstbestimmte Entscheidung respektiert wird.</p>
<p klasse="J">Erwachsene, die selbstbestimmt sterben möchten, können sich an einen Arzt ihres Vertrauens wenden und dort die Verschreibung eines Medikaments erbitten. Selbstverständlich ist niemand zur Hilfeleistung verpflichtet. Ist der Arzt grundsätzlich bereit, obliegt es ihm, sich ein umfassendes Bild davon zu machen, ob der Betroffene aus autonom gebildetem, freiem Willen heraus handelt. Durch die vorherige obligatorische Beratung in einer Beratungsstelle gewährleisten wir ebenso Sicherheit wie durch das ärztliche Vieraugenprinzip in bereits existenziellen Leidenssituationen.</p>
<p klasse="J">Wichtig ist uns vor allem, dass wir die Menschen nicht schon wieder alleine lassen – alleine mit ihrem Schmerz, ihrer Angst und ihrem Wunsch, gehen zu dürfen. Deshalb brauchen wir eine rechtssichere Lösung, bei der niemand bezweifelt, dass sie vor dem Bundesverfassungsgericht Bestand haben wird. Deshalb dürfen wir nicht schon wieder mit dem Strafrecht drohen. Deshalb brauchen wir Strukturen, die für jeden Menschen sofort zugänglich sind, ohne monatelange Wartezeiten auf Facharzttermine. Nur über tatsächlichen Zugang können wir im Übrigen auch Menschen helfen, die aus der Bahn geraten sind.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="J">Liebe Kolleginnen und Kollegen, bitte schenken Sie unserem Gesetzentwurf Ihre Stimme! Es gibt so unfassbar viele Menschen dort draußen, die sich die Sicherheit wünschen, selbstbestimmt gehen zu dürfen, wenn für sie der richtige Zeitpunkt gekommen ist.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächster Redner ist Dr. Lars Castellucci für die Gruppe „Dr. Castellucci und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
</rede>

'''    