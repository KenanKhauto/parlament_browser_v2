from bs4 import BeautifulSoup
from app.data.xml_impl.speech_xml import SpeechXML

class AgendaItemXML:
    def __init__(self, soup_document : BeautifulSoup):
        self.document = soup_document
        print(f"Agenda item created!")
        self.id = None
        self.title = None
        self.table_of_contents = []
        self.speeches = []
        self.parse()

    def parse(self):
        self.parse_id()
        self.parse_title()
        self.parse_table_of_contents()
        self.parse_speeches()

    def parse_id(self):
        try:
            self.id = self.document.get("top-id")
        except:
            self.id = "Unknown"
            print("Could not parse id")

    def parse_title(self):
        try:
            self.title = self.document.get("top-id")
        except:
            self.title = "Unknown"
            print("Could not parse title")

    def parse_table_of_contents(self):
        contents = self.document.find_all("p", {"klasse": "T_NaS"})
        if contents is None:
            self.table_of_contents = []
            return
        for content in contents:
            if content.get_text() not in self.table_of_contents:
                self.table_of_contents.append(content.get_text())
    
    def parse_speeches(self):
        speeches = self.document.find_all("rede")
        if speeches is None:
            self.speeches = []
            return
        for speech in speeches:
            self.speeches.append(SpeechXML(speech))

    def __str__(self):
        return f"Agenda Item: {self.title}"
    

'''
<tagesordnungspunkt top-id="Tagesordnungspunkt 5">
<p klasse="J">Ich rufe nun auf die Tagesordnungspunkte 5 a bis 5 c sowie Zusatzpunkt 16:</p>
<p klasse="T_NaS">5 a) Zweite und dritte Beratung des von den Abgeordneten Dr. Lars Castellucci, Ansgar Heveling, Dr. Kirsten Kappert-Gonther, Dr. Konstantin von Notz, Petra Pau, Stephan Pilsinger, Benjamin Strasser, Kathrin Vogler und weiteren Abgeordneten eingebrachten Entwurfs eines Gesetzes zur Strafbarkeit der geschäftsmäßigen Hilfe zur Selbsttötung und zur Sicherstellung der Freiverantwortlichkeit der Entscheidung zur Selbsttötung</p>
<p klasse="T_Drs">Drucksache 20/904</p>
<p klasse="T_NaS">Beschlussempfehlung und Bericht des Rechtsausschusses (6. Ausschuss)</p>
<p klasse="T_fett">Drucksache 20/7624</p>
<p klasse="T_NaS">b) Zweite und dritte Beratung des von den Abgeordneten Katrin Helling-Plahr, Dr. Petra Sitte, Helge Lindh, Dr. Till Steffen, Otto Fricke und weiteren Abgeordneten eingebrachten Entwurfs eines Gesetzes zur Regelung der Suizidhilfe</p>
<p klasse="T_Drs">Drucksache 20/2332</p>
<p klasse="T_NaS">Beschlussempfehlung und Bericht des Rechtsausschusses (6. Ausschuss)</p>
<p klasse="T_fett">Drucksache 20/7624</p>
<p klasse="T_NaS">c) Zweite und dritte Beratung des von den Abgeordneten Renate Künast, Dr. Nina Scheer, Katja Keul, Dr. Edgar Franke, Canan Bayram, Lukas Benner, Matthias Gastel, Dirk Heidenblut und weiteren Abgeordneten eingebrachten Entwurfs eines Gesetzes zum Schutz des Rechts auf selbstbestimmtes Sterben und zur Änderung weiterer Gesetze</p>
<p klasse="T_Drs">Drucksache 20/2293</p>
<p klasse="T_NaS">Beschlussempfehlung und Bericht des Rechtsausschusses (6. Ausschuss)</p>
<p klasse="T_fett">Drucksache 20/7624</p>
<p klasse="T_ZP_NaS">ZP 16 Beratung des Antrags der Abgeordneten Dr. Kirsten Kappert-Gonther, Martina Stamm-Fibich, Renate Künast, Ansgar Heveling, Dr. Lars Castellucci, Katrin Helling-Plahr, Benjamin Strasser, Helge Lindh, Stephan Pilsinger, Dr. Nina Scheer, Kathrin Vogler, Dr. Petra Sitte, Kerstin Griese, Lukas Benner, Dr. Konstantin von Notz, Dr. Till Steffen und weiterer Abgeordneter</p>
<p klasse="T_fett">Suizidprävention stärken</p>
<p klasse="T_Drs">Drucksache 20/7630</p>
<p klasse="J">Die Gesetzentwürfe unter den Tagesordnungspunkten 5 b und 5 c wurden im Ausschuss zusammengeführt und liegen in der Ausschussfassung unter dem neuen Titel vor: Entwurf eines Gesetzes zum Schutz des Rechts auf selbstbestimmtes Sterben und zur Regelung der Hilfe zur Selbsttötung sowie zur Änderung weiterer Gesetze.</p>
<p klasse="J">Ich möchte bereits jetzt auf folgende Dinge hinweisen: Für die Aussprache wurde eine Debattenzeit von 90 Minuten vereinbart. Die Redezeit wird in 18 Fünf-Minuten-Blöcke aufgeteilt, wobei die beiden Gruppen jeweils acht und die Fraktion der AfD zwei Fünf-Minuten-Blöcke erhalten sollen. Es soll keine Kurzinterventionen und keine Zwischenfragen geben. Alle Abgeordnete, deren Redewünsche nicht berücksichtigt werden können, haben die Möglichkeit, ihre Redebeiträge zu Protokoll zu geben.<sup>1</sup>
<fussnote>Anlage 2 </fussnote>
</p>
<p klasse="J">Im Hinblick auf die Abstimmungsreihenfolge hat man sich auf folgendes Verfahren verständigt: Zunächst wird über den Gesetzentwurf „Dr. Lars Castellucci und andere“ abgestimmt, anschließend gegebenenfalls über den im Ausschuss zusammengeführten Gesetzentwurf der Abgeordneten Katrin Helling-Plahr, Renate Künast und andere sowie schließlich über den Antrag der Abgeordneten Dr. Kirsten Kappert-Gonther und andere. Bei Annahme des Gesetzentwurfs „Dr. Lars Castellucci und andere“ entfällt die Abstimmung über den Gesetzentwurf der Abgeordneten Katrin Helling-Plahr, Renate Künast und andere. – Ich sehe dazu keinen Widerspruch. Dann ist das so beschlossen.</p>
<p klasse="J">Ich eröffne nun die Aussprache. Das Wort hat zuerst die Abgeordnete Katrin Helling-Plahr für die Gruppe „Helling-Plahr, Künast und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
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
<rede id="ID2011500200">
<p klasse="redner">
<redner id="11004257">
<name>
<titel>Dr.</titel>
<vorname>Lars</vorname>
<nachname>Castellucci</nachname>
<fraktion>SPD</fraktion>
</name>
</redner>Dr. Lars Castellucci (SPD):</p>
<p klasse="J_1">Danke sehr. – Geschätzte Frau Präsidentin! Meine sehr verehrten Damen und Herren! Liebe Kolleginnen und Kollegen! Wir beraten heute abschließend über zwei Gesetzentwürfe zum begleiteten Suizid. Drei Jahre ist das Urteil des Bundesverfassungsgerichts nun her, aber die Menschen wissen nicht, wie sie einen Zugang zu diesem assistierten Suizid erhalten können. Gleichzeitig sind Menschen möglichem Missbrauch auch schutzlos ausgeliefert. Das kann so nicht bleiben. Deswegen haben wir Regelungsbedarf. Die Menschen brauchen Rechtssicherheit, Klarheit, Schutz, und das müssen wir heute leisten.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Das Bundesverfassungsgericht hat klargestellt, dass es zur Selbstbestimmung jedes Menschen gehört, auch über sein Ende entscheiden zu können. Das müssen wir achten. Gleichzeitig hat uns das Gericht mitgegeben, dass wir nicht einfach diese Selbstbestimmung voraussetzen können, sondern es hat gesagt, dass wir als Gesetzgeber – das sind die Worte des Gerichtes – dafür Sorge zu tragen haben, dass es sich bei dem Entschluss, assistierten Suizid zu begehen, wirklich um eine freie Entscheidung handelt.</p>
<p klasse="J">Mit unserem Gesetzentwurf eröffnen wir erstmals Ärztinnen und Ärzten die Möglichkeit, ein todbringendes Mittel für einen assistierten Suizid zu verschreiben, und wir definieren ein Schutzkonzept, das diesen freien Willen der Menschen in den Mittelpunkt stellt.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="O">Wer organisiert regelmäßig Suizidhilfe anbietet und sich nicht an das Schutzkonzept hält, kennt nach unserem Entwurf die Konsequenzen: Er macht sich strafbar. Denn ein Schutzkonzept, bei dem es keine Konsequenzen gibt, wenn man es verletzt, ist kein Schutzkonzept.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Zudem hat unsere Gruppe von Anbeginn einen Antrag zur Suizidprävention vorgelegt. Und, liebe Kolleginnen und Kollegen, das ist das Wichtigste: Niemand in diesem Land soll sich überflüssig fühlen. Niemand in diesem Land soll sich gedrängt fühlen, einen assistierten Suizid zu wählen, weil andere Hilfe nicht erreichbar ist. Bin ich im Alter oder in Krankheit gut versorgt? Kann ich mir das alles noch leisten? Das sind doch Fragen, die hinter Suizidgedanken stecken. Und auf diese Fragen müssen wir sozial- und gesundheitspolitische Antworten geben – bessere sozial- und gesundheitspolitische Antworten! – und dürfen nicht einfach einen Wegweiser zum assistierten Suizid aufstellen.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP, der AfD und der LINKEN)</kommentar>
<p klasse="J">Ich bin froh, dass es gelungen ist, einen gemeinsamen Antrag zu dieser Suizidprävention vorzulegen. Ich werbe schon heute dafür, dass wir einen Weg finden, diesen hier im Parlament auch gut zu begleiten, so breit, wie wir ihn einbringen, beispielsweise in einem fraktionsübergreifenden Parlamentskreis.</p>
<p klasse="J">Wir sollen also dafür Sorge tragen, dass der Entschluss, begleiteten Suizid zu begehen, tatsächlich auf freiem Willen beruht. Was heißt das, und wie geht das? Nun, das Gericht hat uns dazu viele Hinweise gegeben. Ich will einen nennen: Der freie Wille soll dauerhaft sein, er soll fest gefasst sein. – Aber Suizidgedanken schwanken eben meist. Selbst von denen, die Suizid begehen und noch am Leben sind, weil der Suizidversuch gescheitert ist, sagen hinterher 80, 90 Prozent, sie seien froh, dass sie es überlebt haben.</p>
<p klasse="J">Deshalb, liebe Kolleginnen und Kollegen: Was nicht geht, ist, einmal zu einer Beratungsstelle zu gehen, dort einen Beratungsschein zu bekommen und dann sofort das Rezept ausgestellt zu bekommen. So kann man die Dauerhaftigkeit von Suizidwünschen nicht feststellen.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="O">Das verletzt die Vorgaben des Bundesverfassungsgerichtes.</p>
<p klasse="J">Der Zugang zum assistierten Suizid muss ermöglicht werden, ohne daraus ein Modell zu machen. Menschen müssen vor Einflüsterungen oder in akuten persönlichen Krisen geschützt werden und die Hilfe erhalten, die sie benötigen. Lassen Sie uns das Geld, das jetzt für Suizidberatungsstellen vorgesehen ist, in die Suizidprävention investieren!</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN und der Abg. Beatrix von Storch [AfD])</kommentar>
<p klasse="J">Es ist unsere Aufgabe: Wir streiten heute über Paragrafen. Aber die Wirklichkeit werden wir mit diesen Paragrafen kaum erfassen können. Ich mache mir deshalb Sorgen. Ich mache mir Sorgen um die Einsamen, um die Zurückgelassenen, um die, die denken, sie fallen nur noch anderen zur Last, um die, die sich fragen: Ist mein Leben noch etwas wert? Liebe Kolleginnen und Kollegen, solche Fragen müssen Menschen mit sich selbst ausmachen. Aber wir als Gesellschaft sollten ihnen zurufen: Ja, dein Leben ist etwas wert. Jedes Leben in diesem Land ist wertvoll.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP, der AfD und der LINKEN)</kommentar>
<p klasse="O">Deshalb: Lassen Sie uns den begleiteten Suizid ermöglichen, aber nicht fördern!</p>
<p klasse="J">Ich bitte um Zustimmung.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächster Redner: für die AfD-Fraktion Thomas Seitz.</p>
<kommentar>(Beifall bei der AfD)</kommentar>
</rede>
<rede id="ID2011500300">
<p klasse="redner">
<redner id="11004891">
<name>
<vorname>Thomas</vorname>
<nachname>Seitz</nachname>
<fraktion>AfD</fraktion>
</name>
</redner>Thomas Seitz (AfD):</p>
<p klasse="J_1">Sehr geehrte Frau Präsidentin! Sehr geehrte Damen und Herren! Weil es um ethische und nicht politische Fragen geht, wurden die vorgelegten Gesetzentwürfe im Ausschuss weder debattiert, noch wurde darüber abgestimmt. Aber dann sind es doch wieder politische Fragen; denn Sie von den Altparteien haben meine Fraktion von allen Gesprächen und Gruppen ausgeschlossen. An keinem der Gesetzentwürfe waren AfD-Abgeordnete beteiligt.</p>
<kommentar>(Benjamin Strasser [FDP]: Sie hätten ja auch einen vorlegen können! Sie können doch auch einen schreiben! – Zuruf der Abg. Dr. Marie-Agnes Strack-Zimmermann [FDP])</kommentar>
<p klasse="O">Da sich die unterschiedlichen Auffassungen zur Suizidhilfe auch in der AfD-Fraktion widerspiegeln, konnten wir keine eigenen Entwürfe vorlegen, weil keine der Positionen die notwendige Anzahl unterstützender Abgeordneter erreicht.</p>
<p klasse="J">Zur Lösung der Frage, ob und wie Suizidhilfe gesetzlich zu regeln ist, hat die Ausgrenzung der AfD aber offensichtlich nicht beigetragen, wenn man die Kritik der Ärztekammern in den letzten Tagen betrachtet.</p>
<kommentar>(Julia Klöckner [CDU/CSU]: Es geht nicht um die AfD heute! Es geht um betroffene Menschen!)</kommentar>
<p klasse="O">Die Kritik betrifft vor allem den Vorwurf unzureichender Suizidprävention, aber mehrere Landesärztekammern kritisieren auch eine „übereilte Regelung“, und die Landesärztekammer Hessen mahnte gar „dringend“ eine „seriöse Folgenabschätzung“ an. Der Präsident der Bundesärztekammer Klaus Reinhardt wörtlich:</p>
<p klasse="Z">Wenn Künast/Helling-Plahr sich im Bundestag durchsetzen, wird die Bundesärztekammer der Ärzteschaft raten, sich nicht zu beteiligen.</p>
<p klasse="O">Die Bundesärztekammer droht also offen mit einem Boykott. Deutlicher kann man das Ziel einer gesellschaftlichen Befriedung wohl nicht verfehlen, wenn die wichtigste beteiligte Berufsgruppe sich derart äußert.</p>
<kommentar>(Beifall bei der AfD)</kommentar>
<p klasse="J">Wie sieht es konkret aus mit den Gesetzentwürfen?</p>
<p klasse="J">Beim Gesetzentwurf der Gruppe „Castellucci“ wird deutlich, dass die Verfasser die Entscheidung des Bundesverfassungsgerichts, dass der Einzelne selbst entscheiden darf, was sein Verständnis von Lebensqualität und Sinnhaftigkeit seiner Existenz ausmacht, nicht wirklich akzeptieren. Denn nach der Entscheidung müssten Staat und Gesellschaft die Entscheidung des Individuums als Akt autonomer Selbstbestimmung respektieren, und wenn der Gesetzgeber regulierend eingreift, muss er einen zumutbaren Weg zu einem selbstbestimmten Freitod eröffnen. Das kann ich dem Gesetzentwurf nicht entnehmen. Vielmehr wird die kassierte Strafvorschrift des § 217 StGB wiederbelebt.</p>
<p klasse="J">Mit dem Recht auf selbstbestimmtes Sterben ist es aber kaum vereinbar, geschäftsmäßige Suizidhilfe generell unter Strafe zu stellen und nur unter bestimmten Voraussetzungen die Rechtswidrigkeit entfallen zu lassen. Denn ein selbstbestimmtes Sterben in Würde erfordert die Mitwirkung und Unterstützung qualifizierter Berufsträger, deren Tätigkeit praktisch immer auf Wiederholung ausgerichtet und damit zwangsläufig geschäftsmäßig ist. Für die juristischen Laien der Hinweis, dass es hier nur um die Frage einer auf Wiederholung angelegten Tätigkeit geht, nicht um die Frage, ob damit Einnahmen erzielt werden. Letzteres wird durch das Merkmal gewerbsmäßig beschrieben, nicht geschäftsmäßig. Eine solche Strafandrohung untergräbt zumindest faktisch den von der Verfassung geschützten Weg zu einem frei bestimmten Tod und ist deshalb mit erheblicher Wahrscheinlichkeit erneut verfassungswidrig. Allein dieser greifbare Verdacht ist Grund genug, diesen Gesetzentwurf abzulehnen.</p>
<p klasse="J">Der zusammengeführte Antrag der Gruppen „Helling-Plahr“ und „Künast“ verfolgt ein freiheitliches Konzept, das ich als Sprecher der relativ größten Gruppe innerhalb meiner Fraktion befürworte. Das Manko besteht allerdings in einem ungenügenden Schutzkonzept. Der Entwurf für ein Suizidhilfegesetz stellt auf eine Beratungslösung ab, bei der ärztliche Expertise eingeholt werden kann, aber nicht muss. Damit ist dem Missbrauch Tür und Tor geöffnet und wird das Leben psychisch Kranker gefährdet. Denn ob ein Suizidwunsch frei von Willensmängeln und Beeinflussung ist, kann nur von praxiserfahrenen Ärzten, vielfach nur von Fachärzten aus dem Bereich Psychiatrie, Psychotherapie oder Neurologie beurteilt werden. Eine Regelung, die diesen Schutz nicht sicherstellen kann, wird den Vorgaben des Bundesverfassungsgerichts ebenfalls nicht gerecht. Erschwerend kommt hinzu, dass die Gewährleistung des Lebensschutzes bei der Beratungslösung zusätzlich wesentlich von der Ausgestaltung durch die Länder und vor allem dem Umfang der zur Verfügung gestellten Geldmittel abhängt.</p>
<p klasse="J">Ich kann deshalb keinem der beiden Gesetzentwürfe zustimmen. Besser, der Gesetzgeber beschließt heute keine Regulierung der Suizidhilfe als eine schlechte. Und wenn offensichtlich ein großer Teil der Ärzteschaft die Vorschläge derart vehement kritisiert, bedarf es weiterer Diskussion, die sich auch intensiver damit befassen muss, welche juristischen Regelungen überhaupt praktisch umsetzbar sind. Eine ärztliche Begutachtung zu fordern, ist nur dann sinnvoll, wenn es auch Ärzte gibt, die die Begutachtung leisten können.</p>
<p klasse="J">Zum Abschluss noch ein paar Worte zum Antrag auf Drucksache 20/7630. Die Forderung zur Suizidprävention kann man nur unterstützen, auch wenn die AfD-Abgeordneten hier genauso ausgeschlossen wurden. Aber auch hier gilt, dass ein Antrag, der erst am Vorabend der Debatte veröffentlicht wird,</p>
<kommentar>(Dr. Marie-Agnes Strack-Zimmermann [FDP]: Sie hätten doch einen eigenen einbringen können!)</kommentar>
<p klasse="O">dem Thema nicht gerecht wird.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei der AfD sowie des Abg. Robert Farle [fraktionslos])</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: Renate Künast für die Gruppe „Helling-Plahr, Künast und andere“.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD und der FDP)</kommentar>
</rede>
<rede id="ID2011500400">
<p klasse="redner">
<redner id="11003576">
<name>
<vorname>Renate</vorname>
<nachname>Künast</nachname>
<fraktion>BÜNDNIS 90/DIE GRÜNEN</fraktion>
</name>
</redner>Renate Künast (BÜNDNIS 90/DIE GRÜNEN):</p>
<p klasse="J_1">Frau Präsidentin! Liebe Kolleginnen und Kollegen! Warum eine Neuregelung? – Das fragen wir uns, denke ich, alle. Ich habe das Gefühl, wir haben seit dem Bundesverfassungsgerichtsurteil, auch Jahre vorher schon, insbesondere aber seit dem letzten Sommer, fast alle um eine Position gerungen. Es gab viele Orte und Gelegenheiten, wo wir diskutieren konnten. Wir haben um die Fragen gerungen: Was dürfen wir eigentlich entscheiden? Oder was müssen wir entscheiden?</p>
<p klasse="J">Für mich ist der allerwichtigste Punkt: Es braucht eine Neuregelung. Warum? Weil Sterbehilfe stattfindet. Sie findet statt nach der Entscheidung des Bundesverfassungsgerichts. Aber wir haben keinen zumutbaren und gangbaren Weg geregelt, meine Damen und Herren, einen Weg, der tatsächlich nicht so hohe Hürden mit sich bringt, als dass er nicht genommen wird. Und deshalb habe ich – ich will auf Herrn Castellucci Bezug nehmen –, haben wir als Gruppe ein anderes Verständnis. Wissen Sie, der freiverantwortliche Suizid und das Recht, Dritte dabei um Hilfe zu bitten, ist Ausübung des Selbstbestimmungsrechtes,</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="O">ist Ausübung eines Grundrechtes. Ich weiß, dass es uns schwerfällt, wenn man für sich selber, für seine Angehörigen eine andere Vorstellung hat, trotzdem zu sagen: Diese letzte Entscheidung trifft jede und jeder für sich selbst. – Und die Menschen treffen diese übrigens auch, unabhängig davon, ob wir hier heute eine Entscheidung treffen oder nicht. Sie treffen sie im Zweifelsfalle auch so, dass sie sagen: Wenn die Beratung zu kompliziert ist, gehe ich gar nicht erst hin, meine Damen und Herren. – Und wenn das dabei herauskommt, dann hätten wir unseren Job heute nicht gut gemacht.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="J">Wir haben uns entschieden, nicht den Strafrechtsweg zu gehen, und ich sage Ihnen auch, warum: Wenn es ein Grundrecht ist, selber über das Ende des Lebens zu entscheiden und sich dabei einer Hilfe zu bedienen, können wir in das Strafgesetzbuch nicht eine Regelung aufnehmen, die besagt: Die Hilfe zu einem selbstbestimmten, freiverantwortlichen Suizid ist grundsätzlich strafbar, meine Damen und Herren.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="O">Deshalb heißt es „Hilfe“ und nicht „Beihilfe“; denn Beihilfe ist strafbar. Das ist etwas anderes.</p>
<p klasse="J">Und dann – das muss ich auch sagen – bedienen Sie sich einer schlechten juristischen Formulierung; das hat Ihnen ja auch einer der Sachverständigen gesagt. Sie haben an dieser Stelle eine Konstruktion gewählt, meine Damen und Herren, bei der der Tatbestand erst mal erfüllt ist und man dann gucken muss, ob Rechtfertigungsgründe vorliegen. Das ist juristisch völlig widersinnig geregelt: Wenn die suizidwillige Person es sich später anders überlegt oder nach Ablauf einer Frist die Tat begeht, dann ist der Tatbestand erfüllt. Und gegen alle Personen, die geholfen haben, wird ein strafrechtliches Ermittlungsverfahren eingeleitet, weil der Staatsanwalt handeln muss. Ich finde, das ist aus zwei Gründen juristisch widersinnig: Erstens können Sie ein Grundrecht nicht unter Strafe stellen. Und zweitens haben Sie diese Regelung noch so geschrieben, dass Sie damit zwingend die Justiz beschäftigen. Damit helfen Sie weder den Betroffenen, die ein entsprechendes Ansinnen haben, noch den Ärztinnen und Ärzten.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="J">Vor Jahren haben wir hier viel über Druck geredet: dass Menschen frei sein sollen, nicht unter Druck gesetzt werden sollen. Es geht ja nicht nur um die Frage einer psychischen Erkrankung, einer affektiven Störung. Es geht auch um die Frage, ob andere sie unter Druck setzen, meine Damen und Herren. Aber hier haben Sie jetzt eine Konstruktion vorgelegt, wo Betroffene Angst haben, dass jemand, den sie um Hilfe bitten, sich strafbar macht und einem Ermittlungsverfahren ausgesetzt wird. Da haben Sie mit Zitronen gehandelt. Das löst das Problem nicht, das Sie vorgeben zu lösen.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD und der FDP)</kommentar>
<p klasse="J">In der Diskussion sagen ja viele und zu Recht: Das Leben ist wertvoll. – Wir haben in unseren Gesetzentwurf reingeschrieben, dass jedes Leben wertvoll ist und dass das auch Beratungsgrundlage ist, meine Damen und Herren. Aber der Staat hat nicht nur die Aufgabe, Leben zu schützen. Dieser Schutz hat auch eine Grenze; denn es ist ein Grundrecht, selber gehen zu können, meine Damen und Herren. Selbstschädigung ist nicht strafbar. Deshalb muss man auch bei jeder Behandlung unterschreiben, dass man behandelt werden darf. Deshalb darf ein Mensch, selbst wenn die Ärztinnen und Ärzte sagen: „Du hättest noch Chancen“, auch sagen: Nein, ich will es nicht. – und dann sind die Geräte abzuschalten, dann darf nicht behandelt werden, weil das dann strafbar wäre, meine Damen und Herren.</p>
<p klasse="J">Genau den Bereich zwischen einer Schutzvorschrift und gleichzeitig selbstbestimmtem und freiverantwortlichem Handeln müssen wir austarieren, meine Damen und Herren. Und für uns sage ich ganz klar: Wir sagen nicht, dass der Suizid ein Normalfall ist. Wir haben die Aufgabe, Leben zu schützen. Aber wir haben als Abgeordnete auch die Aufgabe, zwischen den Fragen „Was würden wir selber, was würden wir unseren Angehörigen wünschen?“ und „Was darf der Betreffende entscheiden?“ zu trennen. Und es ist ja kein Normalfall, wenn ich zwei Termine wahrnehmen muss.</p>
<p klasse="J">Und auch noch ein Hinweis zu denjenigen, die die Beratung durchführen, meine Damen und Herren. In meinem ersten Beruf bin ich Sozialarbeiterin mit dem Schwerpunkt Psychiatrie/Strafvollzug gewesen. Ich hatte viel mit Suizid, viel mit Menschen mit psychischen Belastungen und Erkrankungen zu tun. Sorry, aber auch Sozialarbeiterinnen und Sozialarbeiter, Psychologinnen und Psychologen, die in solchen Bereichen arbeiten, können feststellen, ob jemand eine Störung hat, nicht freiverantwortlich handelt, meine Damen und Herren.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="J">Ich bitte Sie an dieser Stelle um eines: Sagen Sie Nein dazu, wieder einen gefährlichen Weg zu gehen, der uns nach Karlsruhe bringen kann, meine Damen und Herren. Schaffen Sie mit uns eine Regelung, die die Menschen am Ende tatsächlich nutzen wollen. Wir müssen eine breite Tür für Beratung haben; denn das ermöglicht Selbstbestimmung, aber auch Lebensschutz. Nur das ist der Weg, bei dem wir niemanden alleine lassen.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächster Redner: Ansgar Heveling für die Gruppe „Dr. Castellucci und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
</rede>
<rede id="ID2011500500">
<p klasse="redner">
<redner id="11004056">
<name>
<vorname>Ansgar</vorname>
<nachname>Heveling</nachname>
<fraktion>CDU/CSU</fraktion>
</name>
</redner>Ansgar Heveling (CDU/CSU):</p>
<p klasse="J_1">Frau Präsidentin! Liebe Kolleginnen und Kollegen! 2015, am 2. Juli, dem letzten Sitzungsdonnerstag vor der Sommerpause, hatte der Deutsche Bundestag mit großer Mehrheit entschieden, die geschäftsmäßige Beihilfe zum Suizid als eigenständigen Straftatbestand zu normieren. Heute, am letzten Sitzungsdonnerstag vor der Sommerpause 2023, stehen wir als Deutscher Bundestag wieder vor der Entscheidung, ob und wie wir dem assistierten Suizid Grenzen setzen.</p>
<p klasse="J">Ich bin mir bewusst, das ist für jeden und jede von uns keine leichte Entscheidung, insbesondere weil wir unser Votum vor dem Hintergrund des Urteils des Bundesverfassungsgerichts vom 26. Februar 2020 treffen müssen, mit dem sich die Karlsruher Richter grundlegend und sehr weitgehend zum Umgang mit dem assistierten Suizid geäußert haben. Mit seinem Urteil hat das Bundesverfassungsgericht eine Art Grundrecht auf Suizid und der Hilfe dazu konstituiert. Diese sehr weitgehende Entscheidung bereitet vielen – ich nehme mich da nicht aus – Kopfzerbrechen. Die Frage ist nicht fernliegend: Macht es angesichts dieses weitgehenden Urteils überhaupt Sinn, eine gesetzliche Regelung zur Frage des assistierten Suizids vorzunehmen? Ich habe für mich diese Frage zu Beginn dieser Wahlperiode ganz eindeutig mit Ja beantwortet; denn beim assistierten Suizid geht es nicht nur um eine Frage an den Einzelnen, an sein höchstpersönliches Recht. Assistierter Suizid macht auch etwas mit anderen: mit Angehörigen, mit Mitarbeiterinnen und Mitarbeitern von Einrichtungen, von Pflegeeinrichtungen, Ärztinnen und Ärzten und – ja – auch mit der Gesellschaft insgesamt. Deshalb ist für mich klar geworden: Wir brauchen wieder eine gesetzliche Regelung.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">So weitgehend das Urteil des Bundesverfassungsgerichts ist, so klar spricht es gleichzeitig davon, dass es für das dort postulierte Grundrecht auch Schranken geben kann; denn das Recht auf selbstbestimmtes Sterben wirkt nicht absolut. Es tritt vielmehr in Kollision zur Pflicht des Staates, die Autonomie Suizidwilliger und darüber hinaus auch das höchstrangige Rechtsgut Leben zu schützen.</p>
<p klasse="Z">Der hohe verfassungsrechtliche Rang der Rechtsgüter Autonomie und Leben, die § 217 StGB schützen will, vermag den Einsatz des Strafrechts grundsätzlich zu legitimieren.</p>
<p klasse="O">So das Urteil des Bundesverfassungsgerichts von 2020. Karlsruhe zeigt damit auf, dass der Gesetzgeber Grenzen definieren darf, und das sollte der Gesetzgeber dann auch tun.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Es ist die Motivation meiner Gruppe „Castellucci/Heveling“, für eine neue gesetzliche und strafrechtliche Regelung einzutreten. Dass auch in Deutschland eine strafrechtliche Lösung möglich und naheliegend ist, zeigt die gerade zitierte Passage des Urteils. Mit dem neuen § 217 Strafgesetzbuch bewirken wir den Schutz der Selbstbestimmung; denn Schutz der Selbstbestimmung heißt Schutz von gefährdeten Gruppen, Schutz von denen, deren Selbstbestimmung gefährdet ist: psychisch kranke Menschen, die unter äußerem Druck stehen, behinderte Menschen, Menschen in existenziellen Ausnahmesituationen. Ich finde, diesen Menschen ist die Gesellschaft ihren Schutz schuldig.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Diesen Schutz kann man nur mithilfe des Strafrechts effektiv gewährleisten; denn das Strafrecht setzt Grenzen. Wo sie überschritten werden, ist mit Konsequenzen zu rechnen, und das ist auch richtig so. Das ist auch anders als bei dem Gesetzentwurf „Helling-Plahr/Künast“; er sieht keine Konsequenzen bei Missbrauch vor.</p>
<p klasse="J">Im Übrigen sehen selbst die europäischen Länder das so, in denen die Grenzen für die Suizidbeihilfe weit gefasst sind. Selbst dort werden noch die Grenzen durch Strafrecht gesetzt. Das beste Beispiel ist die Schweiz, wo sich in Artikel 115 des Strafgesetzbuches eine entsprechende Regelung findet.</p>
<kommentar>(Dr. Marie-Agnes Strack-Zimmermann [FDP]: Schweiz ist ein schlechtes Beispiel!)</kommentar>
<p klasse="O">Ebenso ist es in den Niederlanden.</p>
<p klasse="J">Zu unserem § 217 des Strafgesetzbuches gehört deshalb ein ausgewogenes Schutzkonzept, bei dem der autonom gebildete Wille respektiert wird, aber die Feststellung der Selbstbestimmtheit zentraler Schutzaspekt ist, um vor sozialer und wirtschaftlicher Pression zu bewahren.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Deshalb geht es nach wie vor auch nur um die Strafbarkeit der geschäftsmäßigen Beihilfe zum Suizid. Die ethische Grundlage unserer Rechtsordnung würde erodieren, wenn wir es zulassen, dass das wertvollste Rechtsgut, das es gibt – das Leben –, der Logik des Marktes ausgeliefert wird. Es ist kein Ausdruck von Freiheitlichkeit einer Gesellschaft, Sterbehilfeorganisationen mit einer Laisser-faire-Politik zu begegnen.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Das Leben ist kein handelbares Gut und darf es auch nicht werden. Daher geht meine herzliche Bitte an Sie alle: Wenn Sie die Selbstbestimmung und das Rechtsgut Leben zugleich schützen wollen, wenn Sie wollen, dass bei einem solch wertvollen Rechtsgut der Respekt vor der Freiheit und dem Leben zählt, dann stimmen Sie für unseren Gesetzentwurf „Castellucci/Heveling“ und andere. Sagen Sie Ja und nicht Nein. Unser Gesetzentwurf steht dabei fest auf dem Boden unseres Grundgesetzes; denn dieses Grundgesetz ist eine Verfassung des Lebens und nicht des Sterbens.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: für die AfD-Fraktion Beatrix von Storch.</p>
<kommentar>(Beifall bei der AfD)</kommentar>
</rede>
<rede id="ID2011500600">
<p klasse="redner">
<redner id="11004905">
<name>
<vorname>Beatrix</vorname>
<nachname>von Storch</nachname>
<fraktion>AfD</fraktion>
</name>
</redner>Beatrix von Storch (AfD):</p>
<p klasse="J_1">Frau Präsidentin! Meine Damen und Herren! Das Bundesverfassungsgericht hat 2020 das Verbot der geschäftsmäßigen Förderung der Selbsttötung für nichtig erklärt. Damit ist die Büchse der Pandora geöffnet.</p>
<p klasse="J">Den Suizid zu einem Akt persönlicher Autonomie zu erklären, führt uns nach meiner festen Überzeugung auf einen entsetzlichen, tödlichen Pfad. Die Niederlande sind diesen Weg vor uns gegangen. Das Ergebnis ist verheerend: 2021 7 666 Tote durch assistierten Suizid und dort überwiegend durch Tötung auf Verlangen. Das sind 4,5 Prozent aller Sterbefälle dort, 10 Prozent mehr als im letzten Jahr, zehnmal mehr als Verkehrstote. Hochgerechnet auf Deutschland wären das 34 000, dreimal mehr als zurzeit.</p>
<p klasse="J">Als das Suizidhilfegesetz in den Niederlanden beschlossen wurde, ging es um extreme Fälle, in denen Menschen schwerstkrank waren, ohne Überlebensperspektive. Jetzt geht es nicht mehr nur um unheilbar Kranke, es geht immer mehr auch um körperlich gesunde Menschen, die noch ein langes Leben vor sich hätten, die eigentlich Hilfe brauchen und suchen.</p>
<p klasse="J">Die Kingston-Universität hat eine Studie gemacht in den Niederlanden. Dort werden Menschen mit geistiger Behinderung und Autismus legal getötet. Die Studie hat 39 solcher Fälle aus 2012 bis 2021 aufgedeckt bei einer Stichprobe von 900 aus 60 000 Fällen. Wenn man das auf Deutschland hochrechnet, dann wären das in Deutschland 11 500 Menschen, geistig Behinderte und Autisten, die getötet worden wären. Ein besonders trauriges Beispiel aus der Studie: ein junger Mann in seinen 20er-Jahren, der den Grund für seinen Sterbewunsch benennt: soziale Isolation. Er wollte sterben, weil er einsam war.</p>
<p klasse="J">Der Kreis potenziell Betroffener wird damit fast grenzenlos. In Umfragen des Sozio-oekonomischen Panels geben 42 Prozent der Deutschen an, dass sie sich einsam fühlen. Der niederländische Psychiater Dr. Bram Sizzo erklärt die Motivation der Menschen, Assistenz beim Suizid zu suchen – ich zitiere –:</p>
<p klasse="Z">Sie glauben, dass dies das Ende ihrer Probleme und das Ende der Probleme ihrer Familien sein wird.</p>
<p klasse="O">Das heißt, sie nehmen sich das Leben, weil sie ihrer Familie nicht zur Last fallen wollen. Das ist schrecklich.</p>
<p klasse="J">Die vorliegenden Gesetzentwürfe betonen, dass der Suizid aus freien Stücken erfolgen soll, als autonome Entscheidung. Sie sehen also alle die Gefahr, dass Menschen sich unter sozialem Druck das Leben nehmen. Ich glaube nicht, dass sie das verhindern werden; keiner der Entwürfe. Gegen sozialen Druck hilft keine auch doppelte Beratungspflicht und kein Vermerk auf einem Beratungsschein. Gerade in Krisenzeiten wächst der Druck auf Alte und Kranke – nicht nur auf die, aber auf die besonders –, niemandem zur Last zu fallen. Wir werden sehr viel mehr Alte und Kranke haben ohne Familien und sehr viel mehr Krise.</p>
<p klasse="J">Der Bundeskanzler hat von mehr Respekt gesprochen. Die Realität sieht anders aus. Eine häufige Überschrift im Frühjahr war „Wohnungsnot in Deutschland: Rentner leben zu großzügig …“. Die Uni Regensburg hat vorgeschlagen, durch die Erhöhung der Mietpreise die Rentner in kleinere Wohnungen zu zwingen, und in Berlin setzt das Berliner Kirchenstift 110 Senioren vor die Tür.</p>
<p klasse="J">Und dazu kommt: Die gesamte Infrastruktur von Betreuung, Beratung und Pflege von Alten, Kranken und Hilfsbedürftigen und körperlich und geistig kranken Menschen befindet sich in einer existenziellen Krise. Pflegeheime gehen in großer Zahl insolvent. In Hessen schlossen 25 in diesem Jahr. 60 Prozent der Krankenhäuser sind in einer wirtschaftlichen Schieflage; viele werden schließen. Die ortsnahe Versorgung von alten und kranken Menschen ist schon schlecht und wird noch viel schlechter. Die Not wird wachsen. Die durchschnittliche Wartezeit auf einen Therapieplatz für Menschen in einer psychischen Notlage beträgt fünf Monate. Was wird die Folge sein, wenn es angesichts der Krise in der Pflege und der Gesundheitsvorsorge einfacher sein wird, eine wohnortnahe, ergebnisoffene Suizidberatung zu bekommen als einen Pflege- oder Therapieplatz? Noch bevor wir die Suizidprävention stärken, wollen Sie für ergebnisoffene Suizidberatung sorgen.</p>
<p klasse="J">Das sind nicht meine Werte. Wir sollen unser Leben in Freiheit und Verantwortung vor Gott leben. Anfang und Ende des Lebens liegen alleine in Gottes Hand. Daran glaube ich.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei der AfD)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächster Redner: Helge Lindh, Gruppe „Helling-Plahr/Künast und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der SPD und der FDP und des Abg. Lukas Benner [BÜNDNIS 90/DIE GRÜNEN])</kommentar>
</rede>
<rede id="ID2011500700">
<p klasse="redner">
<redner id="11004802">
<name>
<vorname>Helge</vorname>
<nachname>Lindh</nachname>
<fraktion>SPD</fraktion>
</name>
</redner>Helge Lindh (SPD):</p>
<p klasse="J_1">Frau Präsidentin! Liebe Kolleginnen und Kollegen! Sehr geehrte Damen und Herren! Wir können und dürfen nicht den Menschen vor seiner Freiheit schützen. Wir können und dürfen nicht den Menschen vor der Ausübung seiner Freiheit schützen. Und wir können und dürfen nicht, so schwer uns das fallen mag, den Menschen vor sich selbst schützen.</p>
<p klasse="J">Die Mehrheit der Bevölkerung unseres Landes unterstützt in der so brisanten, so berührenden, so existenziellen Frage des Suizids und des assistierten Suizids den Akzent auf Selbstbestimmung – ganz eindeutig. Wir brauchen – ja, wir brauchen! – einen Schutzraum, einen Schutzraum für die Freiheit der Entscheidung, einen Schutzraum, der sowohl die Wahrung des Lebens umfasst, aber eben auch die ganz konsequente Wahrung und Verteidigung der Autonomie und der Selbstbestimmung des Einzelnen, einen Schutzraum für die Identität, Individualität und Integrität der einzelnen Personen und einen Schutzraum jenseits von Kriminalisierung, jenseits von Pathologisierung und jenseits von Stigmatisierung.</p>
<p klasse="J">In diesem Schutzraum der Entscheidung, der auch ein Raum der Beratung ist, hat neues Strafrecht, hat neue Strafbarkeit nichts zu suchen.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="O">In diesem Raum hat der Staat sich zurückzunehmen. Beide Gesetzentwürfe und nahezu alle hier im Raum – jedenfalls die demokratischen Kräfte – sind sich doch einig darin,</p>
<kommentar>(Zurufe der Abg. Dr. Rainer Kraft [AfD] und Beatrix von Storch [AfD])</kommentar>
<p klasse="O">dass wir eine Regelung für einen assistierten Suizid brauchen, der diesen rechtssicher und klar ermöglicht.</p>
<p klasse="J">Im Rahmen der Debatte darüber sprechen wir viel über Einflussnahmen Dritter, über innere und äußere Zwänge, über psychische Störungen, über Werte, unsere Einstellung, unsere Weltanschauung und unsere moralischen Vorstellungen. Aber es gibt viel zu häufig eine große Leerstelle in dieser Debatte. Diese Leerstelle steht für die Lage und die Position derer, um die es geht, die betroffen sind. In all den Debatten sind sie irgendwie an den Rand geraten; das kann aber nicht sein. Was ist die Perspektive, was ist der Blickwinkel derer, die mit dieser Entscheidung ringen, derer, die willig sind oder die überlegen, Suizid zu begehen? Wir reden sehr viel darüber, was wir über Sterben und Tod denken. Was denken aber sie, diejenigen, um die es geht, darüber?</p>
<p klasse="J">Wir haben viele floskelartige Formulierungen, die uns umwabern. Eine davon ist, dass das Sterben zum Leben gehört. Aber was heißt das denn? Das heißt, wenn wir von selbstbestimmtem, autonomem, aber auch gesellschaftlich geborgenem Sterben reden, dann reden wir auch über selbstbestimmtes, autonomes, freies, gesellschaftlich geborgenes Leben. Wir sind dagegen – ich bin entschieden dagegen –, das als Gegensatz aufzubauen, einen Gegensatz zu konstruieren. Nein, das ist nicht so! Deshalb ist unsere Gruppe, unser Gesetzentwurf ganz eindeutig für eine Bejahung des Lebens; wir stehen zu einem Ja zum Leben. Und zwar welchen Lebens? Es geht doch nicht einfach nur um das abstrakte Leben an sich, sondern es geht um ihr Leben und sein Leben, um das Leben konkreter Personen. Wir betonen doch immer in vielen Debatten – und weil es dann so selten passiert, ist es zur Floskel geworden –, dass wir nicht übereinander, sondern miteinander reden sollten. Dann tun wir das doch! Reden wir doch mit denen, die es betrifft!</p>
<p klasse="J">So in der Anhörung hier im Ausschuss im Bundestag Maximilian Schulz, ein Mittdreißiger aus München: Seit der Kindheit ist er schwer chronisch erkrankt, infolge eines medizinischen Unfalls zudem seit einigen Jahren massiv eingeschränkt. Er als jemand, der das Leben bejaht, der das Leben liebt, der an seinem Leben hängt, befürwortet ausdrücklich unseren freiheitlichen Entwurf. Warum tut er das? Weil er diesen als einen mentalen Befreiungsschlag empfindet, weil er darin die Möglichkeit sieht, jetzt freier leben zu können, weil er eines Tages die Möglichkeit haben wird, mit nicht so hohen Hürden selbstbestimmt, frei nach seiner Entscheidung – wenn er es denn will, wenn er so empfindet –, gut beraten und nicht alleingelassen aus dem Leben zu gehen. Das ist für ihn Gewinn von Lebensqualität und Lebenszeitverlängerung; das hat er in dieser Anhörung hier vor allen sehr deutlich gemacht. Das war eine Lehrstunde in Demut und Menschlichkeit.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Er sagte in diesem Beitrag und auch etwa im „Spiegel“, dass er nicht sagen kann, ob er die Möglichkeit ergreifen wird, und dass er in der Vergangenheit schon vor dem Moment stand, aber sich entschieden hat, weiterzuleben. Er sagte, dass er, wenn der Moment des Todes kommt – sei es von selbst oder dass er sich dazu entscheiden wird und dann Hilfe in Anspruch nimmt –, Letzteres tun will in dem Wissen, alles, was möglich war, dem Leben abgerungen zu haben.</p>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Kommen Sie bitte zum Schluss.</p>
<p klasse="redner">
<redner id="11004802">
<name>
<vorname>Helge</vorname>
<nachname>Lindh</nachname>
<fraktion>SPD</fraktion>
</name>
</redner>Helge Lindh (SPD):</p>
<p klasse="J_1">Wir haben ihm, denke ich, beizustehen, ihn zu unterstützen, ihn nicht alleinzulassen, ihm diese Möglichkeiten des Lebens, aber auch die des selbstbestimmten Sterbens zu geben. Aber darüber, was möglich ist, entscheidet niemand sonst außer ihm selbst; nur er selbst.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: Dr. Kirsten Kappert-Gonther für die Gruppe „Dr. Castellucci und andere“.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU und der FDP)</kommentar>
</rede>
<rede id="ID2011500800">
<p klasse="redner">
<redner id="11004773">
<name>
<titel>Dr.</titel>
<vorname>Kirsten</vorname>
<nachname>Kappert-Gonther</nachname>
<fraktion>BÜNDNIS 90/DIE GRÜNEN</fraktion>
</name>
</redner>Dr. Kirsten Kappert-Gonther (BÜNDNIS 90/DIE GRÜNEN):</p>
<p klasse="J_1">Frau Präsidentin! Liebe Kolleginnen und Kollegen! Hier und heute treffen wir alle eine sehr weitreichende Entscheidung. Diese wird nicht nur individuell bedeutsam sein, sondern vor allem darüber entscheiden, wie wir künftig als Gesellschaft mit Menschen in Krisen und Grenzsituationen umgehen.</p>
<p klasse="J">Ich spreche für die Gruppe „Castellucci/Heveling“. Als Fachärztin für Psychiatrie und Psychotherapie habe ich viele suizidale Menschen begleitet. Ich frage mich: Wer von ihnen würde heute nicht mehr leben, wäre der assistierte Suizid als vermeintlich einfache Lösung leichter zu erreichen gewesen als eine Hilfe in Krisen und fürsorgliche Versorgung am Ende des Lebens? Darum habe ich ein großes Unbehagen bezüglich einer staatlich finanzierten Suizidberatungsinfrastruktur, wie sie von der anderen Gruppe vorgeschlagen wurde.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU, der FDP und der AfD und der Abg. Jessica Tatti [DIE LINKE])</kommentar>
<p klasse="J">Der Ausbau der Suizidprävention ist elementar. Ich bin froh, dass es uns, den beiden Gruppen, gelungen ist, einen gemeinsamen Antrag zur Prävention vorzulegen. Ich hoffe sehr, dass dieser Antrag zur Stärkung der Prävention die Zustimmung von Ihnen allen hier in diesem Hause bekommt. Das wäre ein sehr starkes Zeichen.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU, der FDP, der AfD und der LINKEN)</kommentar>
<p klasse="J">Lassen Sie mich nun, liebe Kolleginnen und Kollegen, auf drei zentrale Punkte zu unserem Gesetzentwurf eingehen. Braucht es überhaupt ein Gesetz? Ja; denn aktuell finden in Deutschland Suizidassistenzen statt, ohne klare Regeln und immer häufiger auch in Pflegeheimen. Für Menschen, die ein soziales Netz haben und gut situiert sind, bräuchte es vielleicht kein Gesetz; aber für vulnerable Menschen, die einsam, arm und in existenziellen Krisen sind, für Menschen, die keine adäquate Pflege finden oder psychisch krank sind, braucht es ein Schutzkonzept, einen sicheren Schutz vor Drucksituationen, um ihre Autonomie zu sichern. Das ist auch eine Frage von sozialer Gerechtigkeit.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU, der FDP und der LINKEN)</kommentar>
<p klasse="J">Sehr viele Menschen haben in ihrem Leben suizidale Phasen. Suizidalität entsteht immer im Kontext der Lebenssituation. Auch Liebeskummer kann zu Suizidgedanken führen. Eine einmalige Beratung und nur drei Wochen Wartefrist reichen hier nicht aus.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU, der FDP und der LINKEN)</kommentar>
<p klasse="O">Es braucht ein Schutzkonzept, das sicherstellt, dass ein Suizidwunsch freiverantwortlich und von Dauer ist. Die Sicherung der Selbstbestimmung ist die zentrale Aufgabe der gesetzlichen Regelung.</p>
<p klasse="J">Passen denn nun Selbstbestimmung und Strafrecht zusammen? Wir sagen ganz klar: Kein suizidaler Mensch macht sich strafbar; kein Mensch, der Hilfe zum Sterben in Anspruch nimmt, macht sich strafbar. Strafbar aber macht sich, wer andere zum Suizid drängt. Strafbar machen sich Anbieter geschäftsmäßiger Sterbehilfe, die das Schutzkonzept nicht einhalten und so die Selbstbestimmung gefährden.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU, der FDP, der AfD und der LINKEN)</kommentar>
<p klasse="J">Manche fragen sich, ob eine fachliche psychiatrische und psychotherapeutische Einschätzung nicht etwa paternalistisch sei. Gespräche mit Psychiaterinnen und Psychiatern sowie Psychotherapeutinnen und Psychotherapeuten eröffnen einen Gesprächsraum, der Betroffenen ermöglicht, tabufrei über ihre Gefühle zu sprechen, Motive zu erkennen und sich über Alternativen zu informieren. Das sichert die Selbstbestimmung.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU, der FDP, der AfD und der LINKEN)</kommentar>
<p klasse="J">Darum, liebe Kolleginnen und Kollegen, hat die Bundesärztekammer deutlich kritisiert, dass in dem Gesetzentwurf der anderen Gruppe nichts zur Qualifikation der Beratung festgelegt ist. Suizidale Gefühle sind komplex; sie sind ambivalent und meistens volatil. Fachärztinnen und Fachärzte sowie Psychotherapeutinnen und Psychotherapeutinnen verfügen über die Qualifikation, solche Gespräche zu führen.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU, der FDP und der LINKEN)</kommentar>
<p klasse="O">Wie soll denn ein Stempel vom Amt, den ein Sachbearbeiter einer Behörde ausstellt, wie es von der anderen Gruppe in bestimmten Situationen vorgesehen ist, der Tragweite einer solchen Entscheidung gerecht werden?</p>
<p klasse="J">Als Gesellschaft, als Staat dürfen wir nicht das Signal senden, irgendein Mensch sei überflüssig oder sein Tod sei keine große Sache. Unser Signal ist: Wir respektieren jede Person mit Suizidgedanken. Wir ermöglichen den Zugang zum assistierten Suizid, wie uns vom Verfassungsgericht aufgetragen; aber wir fördern ihn nicht. Wir als Gesellschaft, wir als Vertreterinnen und Vertreter des Staates geben niemanden vorschnell auf, und darum bitte ich Sie, sehr geehrte, liebe Kolleginnen und Kollegen: Stimmen Sie für den Gesetzentwurf „Castellucci/Heveling“.</p>
<p klasse="J">Ich danke Ihnen.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der CDU/CSU, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: Dr. Nina Scheer für die Gruppe „Helling-Plahr, Künast und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
</rede>
<rede id="ID2011500900">
<p klasse="redner">
<redner id="11004396">
<name>
<titel>Dr.</titel>
<vorname>Nina</vorname>
<nachname>Scheer</nachname>
<fraktion>SPD</fraktion>
</name>
</redner>Dr. Nina Scheer (SPD):</p>
<p klasse="J_1">Sehr geehrte Frau Präsidentin! Liebe Kolleginnen und Kollegen! Wir haben als Gesellschaft die Herausforderung, zwei Dinge zusammenzubringen, und zwar sowohl den Schutzauftrag, der in Bezug auf das Leben besteht, als auch all das, was das Leben ausmacht, zu respektieren. Dazu gehört eben auch – das hat das Verfassungsgericht klargestellt – das Recht auf selbstbestimmtes Sterben, und dieses Recht umfasst auch, sich Hilfe von Dritten dazuzuholen. Das gehört mit zu diesem verfassungsgerichtlich bestätigten Grundrecht auf selbstbestimmtes Sterben, und damit gehört es zum Leben, zu unserer Gesellschaft dazu. Diese beiden Dinge müssen wir zusammenbringen.</p>
<p klasse="J">Deswegen möchte ich hier auf ein paar Dinge eingehen, die von denen fälschlich dargestellt wurden, die den Eindruck erwecken wollen, man könnte mit Stigmatisierung und Ausblenden dieses Bereichs, des Rechts auf selbstbestimmtes Sterben, Leben retten. Ich erkläre eindeutig, dass dies nicht der Fall ist, dass das eine Irreführung ist, dass uns das nicht weiterbringt und dass das auch die Menschen fernhalten wird vom Hilfesuchen, von den Möglichkeiten, sich beraten zu lassen. Denn häufig sind es ja Menschen, die aus einer Verzweiflung heraus auf diese Gedanken kommen, und daraus erwächst ein Suizidwunsch.</p>
<p klasse="J">Wie sollen wir diesen Menschen begegnen? Wir haben einen Schutzauftrag. Wir müssen ihnen natürlich irgendwie einen gesellschaftlichen Anknüpfungspunkt bieten, den sie bis dahin verloren haben. Wir müssen einen niedrigschwelligen Anknüpfungspunkt schaffen, ein Beratungsstellennetz, wie wir es in unserem Gesetzentwurf vorsehen.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Das muss natürlich unentgeltlich sein, und das darf natürlich nicht kommerziell betrieben werden, wie das von Vertretern der anderen Gruppe unterstellt wird. Das Beratungsangebot muss so niedrigschwellig sein, dass sich tatsächlich jeder angesprochen fühlt, übrigens auch unter 18-Jährige, auch wenn – das eint beide Gesetzentwürfe – der Anwendungsbereich der Gesetzentwürfe selbstverständlich nur Volljährige umfasst. Es ist ganz wichtig, das noch mal hier festzuhalten. Es muss sich jeder angesprochen fühlen; denn nur so können wir gewährleisten, dass Leben gerettet wird. Alles andere, denke ich, führt uns hier nicht weiter und verfälscht die Sachlage.</p>
<p klasse="J">Ich möchte zurückkommen auf die Frage, wie wir dann mit der Feststellung dieses freien, selbstbestimmten, autonom gefassten und dauerhaften Willens umgehen, die das Verfassungsgericht als Kriterium aufgestellt hat. Das ist genau die Frage: Wie stellen wir den Willen fest, wenn wir uns auf den Weg des Strafrechts begeben, wenn wir im Grundsatz erklären: „Die Herangehensweise im Umgang mit dem Recht auf selbstbestimmtes Sterben ist unter Strafe gestellt. Die Hilfeleistung dazu ist unter Strafe gestellt“?</p>
<p klasse="J">Wenn das der Grundsatz ist, dann halte ich es für sehr naheliegend, dass die Menschen, die sich mit dem Gedanken umgeben oder bei denen er schon sehr weit ausgereift ist, weil sie in einer existenziellen Leidenssituation stecken, etwa aufgrund von Vorerkrankungen, sich nicht an die Gesellschaft wenden, sondern dass sie – in der Stigmatisierung verhaftet, alleingelassen – einen bestimmt nicht würdevollen Weg wählen, weil sie allein gelassen sind.</p>
<p klasse="J">Genau an der Stelle setzt unser Schutzauftrag ein. Wir müssen sagen: Hier haben wir den Schutzauftrag, diesen Menschen zu helfen, ihrem Recht auf selbstbestimmtes Sterben Geltung zu verleihen und diese Hilfe wirklich zu gewähren.</p>
<p klasse="J">Wenn aber das Strafrecht eine Stigmatisierungswirkung entfaltet – und das wird es tun –, dann werden die Ärzte nicht verfügbar sein, dann werden die Beratungsstellen, deren Angebote von uns niedrigschwellig angelegt sind, nicht verfügbar sein. Wenn diese nicht da sind, dann kann auch nicht das Recht auf selbstbestimmtes Sterben verwirklicht werden, dann kann auch nicht demjenigen gesellschaftlich begegnet werden, der möglicherweise doch keinen festen Willen hatte, sondern der wieder zurück ins Leben finden möchte. Auch der wird dann nicht erfasst.</p>
<p klasse="J">Insofern ist es ein Trugschluss, zu glauben, dass mit der Wiederverfestigung eines Straftatbestandes Leben geschützt wird.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="O">Daher bitte ich, den anderen Gesetzentwurf abzulehnen; denn nur so können wir das Recht auf selbstbestimmtes Sterben wirklich erfassen.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächster Redner: Stephan Pilsinger für die Gruppe „Dr. Castellucci und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
</rede>
<rede id="ID2011501000">
<p klasse="redner">
<redner id="11004853">
<name>
<vorname>Stephan</vorname>
<nachname>Pilsinger</nachname>
<fraktion>CDU/CSU</fraktion>
</name>
</redner>Stephan Pilsinger (CDU/CSU):</p>
<p klasse="J_1">Sehr geehrte Frau Präsidentin! Meine Damen und Herren! Wie wichtig es ist, den tatsächlichen autonomen Willen einer vermeintlich suizidwilligen Person festzustellen, bevor ihm das todbringende Medikament verschrieben wird, veranschaulicht das Beispiel des US-Amerikaners Kevin Hines. Den jungen Mann, der an einer bipolaren Störung und schweren Depressionen leidet, hatte plötzlich ein starkes Gefühl ergriffen, jetzt sterben zu wollen. Er sprang von der Golden Gate Bridge in San Francisco – und überlebte, im Gegensatz zu den anderen 99 Prozent der gesprungenen Personen. Er selbst erzählt, dass er noch im freien Fall tief bereut habe, gesprungen zu sein.</p>
<p klasse="J">Drei Jahre lang war Kevin Hines nach seinem Suizidversuch in Krankenhäusern und einer geschlossenen Psychiatrie. Dort heilten nicht nur die gebrochenen Wirbel und Beckenknochen; er fand auch einen Weg, sich mit Medikamenten und einem regelmäßigen Tagesablauf zu stabilisieren. Er hat sich mit seiner Krankheit intensiv auseinandergesetzt und setzt sich selbst zum Ziel, anderen Menschen mit ähnlichen Problemen und Symptomen zu helfen. Seither engagiert sich Kevin Hines im Bereich der Suizidprävention. Wäre Kevin Hines von einem Sterbehilfeverein das schnelle, schmerzfreie Ende in harmonischer Atmosphäre mit einer Pille angeboten worden, hätte er dies in dieser Ausnahmesituation vielleicht angenommen.</p>
<kommentar>(Otto Fricke [FDP]: Aber was hat das jetzt mit den Gesetzen zu tun?)</kommentar>
<p klasse="J">Wissenschaftliche Untersuchungen zeigen: Menschen, die sich selbst das Leben nehmen wollen, entscheiden sich meist nicht frei. Sie sind in einer Ausnahmesituation. Mindestens 90 Prozent der Menschen, die an einem Suizid versterben, haben nach Angaben der Stiftung Deutsche Depressionshilfe eine psychische Erkrankung. 80 bis 90 Prozent der Menschen, die kurzfristig für sich beschließen, Suizid begehen zu wollen, werten das im Nachhinein als Fehlentscheidung</p>
<kommentar>(Otto Fricke [FDP]: Das hat mit beiden Gesetzentwürfen nichts zu tun!)</kommentar>
<p klasse="O">und vollziehen den Suizid dann doch nicht.</p>
<p klasse="J">Wenn man an den assistierten Suizid denkt, dann denkt man meistens an alte, leidende Personen, die am Ende ihres Lebens keine Schmerzen mehr erleiden wollen. Aber darum geht es hier heute nicht.</p>
<kommentar>(Renate Künast [BÜNDNIS 90/DIE GRÜNEN]: Doch!)</kommentar>
<p klasse="O">Seit dem Urteil des Bundesverfassungsgerichts, das beschlossen hat, dass jeder Mensch den Zugang zu einem assistierten Suizid haben muss, ist es derzeit möglich, dass auch Menschen, die jung und gesund sind, einen assistierten Suizid in Anspruch nehmen. Das entspricht, ehrlich gesagt, nicht meinem Weltbild.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD und der AfD)</kommentar>
<p klasse="O">Aber wir haben das Urteil des Bundesverfassungsgerichts nun mal zu akzeptieren. Deswegen ist es wichtig, dass wir heute eine Lösung finden für den aktuell ungeregelten Zustand.</p>
<p klasse="J">Ich arbeite neben meinem Mandat noch als Hausarzt und betreue in dieser Funktion auch Altenheime. Wenn ich dort mit dem Pflegepersonal in Kontakt komme, dann sprechen mich viele relativ fassungslos darauf an, dass Sterbehilfevereine in diesen Einrichtungen tätig sind und Menschen dort durchaus auch ansprechen mit der Frage „Wollen Sie Ihren Angehörigen nicht mehr weiter zur Last fallen?“. Diese Menschen wollten nie jemandem zur Last fallen. Dass diese Menschen einem solchen Druck ausgesetzt sind, dass diese Sterbehilfevereine auf diese Menschen sozusagen losgelassen werden und es keine Regularien gibt, diese Menschen vor diesem Druck zu schützen, das ist untragbar. Deswegen brauchen wir eine Lösung.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der AfD)</kommentar>
<p klasse="J">Ich unterstütze den Gesetzentwurf von Castellucci/Heveling, weil er den assistierten Suizid zwar möglich macht, ihn aber nicht fördert. Wir brauchen ein klar geregeltes Schutzkonzept. Deswegen finde ich es wichtig, dass es klar geregelte Wartezeiten gibt. Wie in dem eben genannten Beispiel ausgeführt, ist der Suizidwunsch oft ein sehr volatiler Gedanke. Das kann ich auch aus meiner ärztlichen Tätigkeit berichten. Deswegen ist es richtig, dass ab dem ersten Beratungsgespräch bis zum Ende, dem assistierten Suizid, eine gewisse Zeit vergeht, um die Dauerhaftigkeit des Suizidwunsches zu überprüfen. Deswegen ist es richtig, dass es Wartezeiten gibt. Deswegen ist es richtig, gewisse Hürden einzuziehen, bevor der assistierte Suizid in Anspruch genommen werden kann.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Und: Ich halte es auch für wichtig, dass man psychiatrische Gespräche einzieht und notwendig macht. Es ist notwendig, psychisch kranke Menschen auch vor dem Druck zu schützen. Es ist auch notwendig, diesen Menschen zu helfen. Es kann doch nicht sein, dass diesen Menschen, die vielfältig unerkannt unter uns leben – Corona hat es doch gezeigt: immer mehr Menschen leiden an psychischen Erkrankungen –, nicht geholfen wird. In einer Zeit, in der man teilweise drei Monate auf einen Psychotherapieplatz warten muss, kann es doch nicht sein, dass der assistierte Suizid schneller möglich ist, als ein Therapieplatz zur Verfügung steht.</p>
<kommentar>(Beifall bei Abgeordneten im ganzen Hause)</kommentar>
<p klasse="O">Deswegen brauchen wir diese psychiatrischen Gespräche.</p>
<p klasse="J">Der Gesetzentwurf der anderen Gruppe ist in meinen Augen viel zu freizügig. Er bietet kein Schutzkonzept. Deswegen ist er abzulehnen.</p>
<p klasse="J">Ich denke, wir müssen heute hier eine Regelung finden, um die Rahmenbedingungen klarzuziehen. Wir müssen das Leben schützen, den assistierten Suizid möglich machen und ein klar geregeltes Schutzkonzept bieten, um Missbrauch zu verhindern. Deswegen bitte ich Sie um Zustimmung für unseren Gesetzentwurf.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: Dr. Petra Sitte für die Gruppe „Helling-Plahr, Künast und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
</rede>
<rede id="ID2011501100">
<p klasse="redner">
<redner id="11003848">
<name>
<titel>Dr.</titel>
<vorname>Petra</vorname>
<nachname>Sitte</nachname>
<fraktion>DIE LINKE</fraktion>
</name>
</redner>Dr. Petra Sitte (DIE LINKE):</p>
<p klasse="J_1">Frau Präsidentin! Meine Damen und Herren! Ja, vor bald acht Jahren wurde hier im Hause ein Gesetz verabschiedet, welches geschäftsmäßige Suizidhilfe unter Strafe stellte. Vor 2015 gab es in 150-jähriger Verfassungsgeschichte Deutschlands nie eine Regelung dazu. Und doch gab es die Grauzone, die durch Sterbehelfer und Sterbehilfevereine mehr oder weniger gut oder schlecht gefüllt wurde.</p>
<p klasse="J">Bei Sterbehilfevereinen muss man Mitglied werden, und für die eigentliche Sterbehilfe dieser Vereine ist eine erhebliche, vierstellige Summe zu zahlen. 2015 nun machte ein deutscher Sterbehilfeverein nicht nur geschäftsmäßig, also auf Wiederholung angelegt, sondern scheinbar auch gewerbsmäßig, also wiederholend und mit Gewinnerzielungsabsicht, sein Angebot. Daraufhin meinte eine Mehrheit des Bundestages, Suizidhilfe praktisch komplett verbieten zu müssen. Das damals verabschiedete Gesetz erklärte das Bundesverfassungsgericht 2020 für verfassungswidrig, weil es – ich zitiere – „Möglichkeiten einer assistierten Selbsttötung“ faktisch entleerte. Das Gesetz wurde für nichtig erklärt.</p>
<p klasse="J">Zwischen 2015 und 2020 suchten Hunderte Menschen Hilfe im Ausland. Dazu mussten sie sowohl körperlich in der Lage sein, aber eben auch finanziell so ausgestattet sein, dass sie das konnten. Wie viele Menschen letztlich von Sterbehilfe abgeschnitten waren, das wissen wir überhaupt nicht. Aber wir ahnen, dass es viele gibt, die vollkommen unnötig leiden mussten.</p>
<p klasse="J">Seit dem Urteil des Bundesverfassungsgerichts 2020 ist Suizidhilfe nun wieder ungeregelt. Eine Regelung – so das Bundesverfassungsgericht – muss sich an der „Vorstellung vom Menschen als einem geistig-sittlichen Wesen“ ausrichten, „das darauf angelegt ist, sich in Freiheit selbst zu bestimmen“. Dem Bundestag liegt nun ein Gesetzentwurf vor, der wörtlich den Paragrafen zur Strafbarkeit der Sterbehilfe enthält, den das Bundesverfassungsgericht abgewiesen hat.</p>
<kommentar>(Dr. Lars Castellucci [SPD]: Weiterlesen! – Benjamin Strasser [FDP]: Das stimmt nicht! Das ist einfach sachlich falsch!)</kommentar>
<p klasse="O">Außerdem erklärt er Menschen, die einen Sterbewunsch äußern und Sterbehilfe wünschen, als Erstes zu Fällen für Psychiatrie und Psychotherapie.</p>
<kommentar>(Dr. Kirsten Kappert-Gonther [BÜNDNIS 90/DIE GRÜNEN]: Das ist falsch!)</kommentar>
<p klasse="J">Meine Damen und Herren, Sie alle haben doch mit solchen Betroffenen gesprochen. Sie wissen doch, was das bedeutet. Dadurch werden sich viele unverstanden und vor den Kopf gestoßen fühlen.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="O">Solche Regelungen, auch mit den Ausnahmen, werden erneut vor Gericht verhandelt werden. Das bedeutet wieder jahrelange Unsicherheit plus die Gefahr, dass wir wieder in eine regelungsfreie Zeit fallen. Regelungen, die bereits für verfassungswidrig erklärt wurden, sollten wir daher heute nicht beschließen.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="J">Das Strafrecht ist schlicht keine Antwort an Menschen, die ihr verfassungsrechtlich geschütztes Persönlichkeitsrecht auch ausüben möchten. Eine umfassend angelegte und lebensweltlich orientierte Beratung wird Hürden abbauen. Sie ist ergebnisoffen und damit suizidpräventiv zugleich. Auch wir haben ein Schutzkonzept. Es stimmt schlicht nicht, dass dem anderen Gesetzentwurf kein Schutzkonzept mit der Beratung zugrunde liegt. Die Lebenssituation, Unterstützungs- und Betreuungsangebote, Hilfsangebote, Handlungsalternativen zur Selbsttötung sollten besprochen, aber eben auch Fragen zu den Folgen einer Selbsttötung beantwortet und fehlgeschlagene Suizidversuche für das persönliche und das familiäre Umfeld thematisiert werden. Sollte sich während der Beratung zeigen, dass man psychiatrische und psychotherapeutische Hilfe braucht, dann ist diese aus dieser Beratung heraus selbstverständlich zu vermitteln. Wir wollen Suizidwünsche eben nicht fördern. Das ist eine unhaltbare Unterstellung,</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="O">die sich aus dem Gesetzestext nicht ableiten lässt. Aber wir wollen Suizidhilfe eben auch nicht kriminalisieren.</p>
<p klasse="J">Und schließlich ist mir Folgendes wichtig – und das ist neu –: Dieses Beratungsangebot, das wir unterbreiten, ist für jeden zugänglich. Es ist niedrigschwellig. Es steht jedem unentgeltlich offen. Ich gehe und meine Gruppe geht davon aus, dass wir genau deswegen jeder Form des Geschäfts mit Suizidhilfe den Boden entziehen. Deshalb bitte ich Sie um Zustimmung zu unserem Gesetzentwurf.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: Kathrin Vogler, Gruppe „Dr. Castellucci und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
</rede>
<rede id="ID2011501200">
<p klasse="redner">
<redner id="11004181">
<name>
<vorname>Kathrin</vorname>
<nachname>Vogler</nachname>
<fraktion>DIE LINKE</fraktion>
</name>
</redner>Kathrin Vogler (DIE LINKE):</p>
<p klasse="J_1">Verehrte Frau Präsidentin! Liebe Kollegen und Kolleginnen! Wir entscheiden hier heute über die Neuregelung der Suizidhilfe, und da unterstütze ich den Gesetzentwurf der Gruppe „Castellucci/Heveling“. Auch wenn wir heute über die Parteigrenzen hinweg argumentieren und abstimmen werden, ist unsere Entscheidung doch eine politische. Es geht nämlich nicht in erster Linie darum, welche Regelung jede und jeder von uns am besten mit dem eigenen Gewissen und der eigenen Weltanschauung vereinbaren kann, sondern eben auch um die Frage, in welchem Land, in welcher Gesellschaft wir leben wollen.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="J">Dabei ist es für mich zentral, wie die Politik mit Menschen umgeht, die nicht auf der Sonnenseite des Lebens stehen. Mir fehlt in der ganzen Debatte häufig ein realistischer Blick auf unsere Gesellschaft. Manchmal wird versucht, ein Bild von Selbstbestimmung zu zeichnen, das vollkommen losgelöst erscheint von den sozialen Bedingungen, von persönlichen und gesellschaftlichen Krisen und von dem Umfeld, in dem wir alle leben. Dieses Welt- und Menschenbild ist meiner Ansicht nach nicht besonders realistisch; es ist geprägt durch den Blick von wohlsituierten Menschen mit hoher Bildung und entsprechendem Selbstbewusstsein.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="J">Wir leben doch in einer Zeit, in der die Menschen mit einer Abfolge von Krisen zu tun haben, die sie ganz oft an den Rand ihrer Kräfte oder sogar darüber hinaus bringen. Die Coronapandemie, die mit der Klimakrise verbundenen Naturkatastrophen, der Krieg und Existenzängste durch Inflation und finanzielle Not setzen viele Menschen unter Druck, und der wirkt sich auch auf die Seele aus. Depressionen, Angststörungen und andere psychische Erkrankungen nehmen zu. Und auch unsere Hilfesysteme sind unter Druck: Mangel an Pflege- und Betreuungskräften, zu wenig Beratungsstellen, lange Wartezeiten bei Schuldenberatungen, Fachärztinnen und Fachärzten, Psychotherapeutinnen und Psychotherapeuten, fehlende Frauenhäuser und Gewaltschutzeinrichtungen sowie Jobcenter, die allzu oft den Druck noch erhöhen, anstatt die Menschen, die als Erwerbslose zu ihnen kommen, zu stärken – das ist doch die Situation.</p>
<p klasse="J">Sehr, sehr viele Menschen denken in solchen Situationen daran, sich das Leben zu nehmen. Wohl jede Person, die Menschen in Not berät, wird damit konfrontiert, dass ihre Ratsuchenden sagen: Ich kann das nicht mehr, ich will so nicht mehr leben.</p>
<p klasse="J">Auf der anderen Seite gibt es natürlich auch diejenigen, die aus wohlüberlegter, freier und dauerhafter Entscheidung ihr Leben beenden wollen und dazu Hilfe suchen. Ihnen dies unter würdevollen Bedingungen zu ermöglichen, das halte ich natürlich für richtig. Und genau das leistet der Gesetzentwurf „Castellucci“.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="J">Es steht uns, liebe Kolleginnen und Kollegen, als Gesetzgeber nicht zu, die Motive Sterbewilliger zu bewerten. Aber wir haben doch die Verantwortung, sicherzustellen, dass die Selbsttötung nicht leichter gemacht wird als der Zugang zu unseren Hilfesystemen.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="O">Wir müssen dafür sorgen, dass niemand durch äußere oder innere Faktoren zum Suizid getrieben wird, ohne dass ein umfassendes und passendes Hilfeangebot gemacht wird.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="O">Und wir müssen sicherstellen, dass die Person, die sich das Leben nehmen möchte, dies wirklich aus freien Stücken tut.</p>
<p klasse="J">Wenn Sie noch unentschieden sind, nehmen Sie sich bitte diese Mail zu Herzen, die ich im April bekommen habe. Mir schrieb ein Freund:</p>
<p klasse="Z">Liebe Kathrin, am vergangenen Mittwoch hat sich meine langjährige Lebensgefährtin für mich völlig überraschend das Leben genommen. Es war ein Freitod, assistiert von der Deutschen Gesellschaft für Humanes Sterben (DGHS). Meine Lebensgefährtin litt seit vielen Jahren unter unklaren Krankheitssymptomen (Fieber, Schwitzen, Atemnot, Kopfschmerzen etc.), hatte sich immer mehr aus dem Leben zurückgezogen und ging überhaupt nicht mehr vor die Tür. … Für mich als Laien deutete einiges auf eine depressive Störung hin. Letzten November stellte sie bei der DGHS den Antrag auf Suizidbegleitung, Anfang Februar kam ein Rechtsanwalt, der ihren Wunsch protokollierte und bestätigte, dass sie bei vollem Bewusstsein und alles wohlüberlegt sei, gleiches bestätigte auch die begleitende Ärztin, die sie Mitte Februar aufsuchte. … Was mich fassungslos macht, ist neben tiefer Trauer über den Tod einer nahen Angehörigen, dass die begleitende Ärztin, eine Radiologin, in ihrer Stellungnahme eine depressive Grundhaltung nicht einmal in Erwägung gezogen hat, geschweige denn ein psychiatrisches Gutachten einforderte. Offensichtlich wurde hier die noch bestehende Gesetzeslücke ausgenutzt, vielleicht ist sogar einer zutiefst labilen Frau der Freitod nahegelegt worden.</p>
<p klasse="J">Liebe Kolleginnen und Kollegen, wenn Sie diese Erfahrung meines Freundes genauso bewegt, wie sie mich bewegt hat, dann lassen Sie uns heute diese Gesetzeslücke schließen. Bitte stimmen Sie für den Gesetzentwurf der Gruppe „Castellucci“.</p>
<kommentar>(Beifall bei Abgeordneten der LINKEN, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächster Redner: Lukas Benner, Gruppe „Helling-Plahr, Künast und andere“.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
</rede>
<rede id="ID2011501300">
<p klasse="redner">
<redner id="11005022">
<name>
<vorname>Lukas</vorname>
<nachname>Benner</nachname>
<fraktion>BÜNDNIS 90/DIE GRÜNEN</fraktion>
</name>
</redner>Lukas Benner (BÜNDNIS 90/DIE GRÜNEN):</p>
<p klasse="J_1">Sehr geehrte Frau Präsidentin! Liebe Kolleginnen und Kollegen! Liebe Zuschauerinnen und Zuschauer! Seit dem wegweisenden Urteil des Bundesverfassungsgerichts sind bereits mehr als drei Jahre vergangen, und deswegen ist es richtig, dass wir heute den Versuch unternehmen, zu einer klaren gesetzlichen Regelung zu kommen. Diese Klarheit schulden wir Suizidwilligen. Wir schulden sie Angehörigen, Ärztinnen und Ärzten, aber wir schulden sie auch der Gesellschaft. Denn machen wir uns nichts vor: Suizidhilfe findet statt, aber nicht mit verlässlichen Regelungen und normierten Schutzkonzepten, nicht so, dass die, die sie brauchen, sie auch erreichen. Sondern im Graubereich, unter riesigem Druck, behaftet mit gesellschaftlichem Stigma und als Tabuthema. So, dass Menschen alleine gelassen werden – und das, obwohl es ein Grundrecht auf selbstbestimmtes Sterben gibt, was das Bundesverfassungsgericht in aller Deutlichkeit gesagt hat.</p>
<p klasse="J">Ich bin der Überzeugung: Wir kommen hier als Gesetzgeber dem Grundrechtsschutz nicht ausreichend nach, und deswegen brauchen wir ein neues, ein eigenes Suizidhilfegesetz. Um dem Recht auf Ausübung des Grundrechts auf selbstbestimmtes Sterben nachzukommen, aber auch und erst recht, um die Freiverantwortlichkeit der Entscheidung sicherzustellen. Ebenso dringlich ist es, dass wir deutlich mehr unternehmen, um Suiziden im Allgemeinen vorzubeugen. Deswegen wollen wir die Bundesregierung mit einem gemeinsamen Antrag beider Gruppen dazu auffordern, Suizidprävention in einem entsprechenden Gesetzentwurf auszuarbeiten.</p>
<p klasse="J">Meine Damen und Herren, wie sollen wir uns als Individuum, als Gesellschaft, als Staat zum Sterbewunsch des Einzelnen verhalten? Der zentrale Satz aus dem Urteil des Bundesverfassungsgerichts hierzu lautet:</p>
<p klasse="Z">Die Entscheidung des Einzelnen, dem eigenen Leben entsprechend seinem Verständnis von Lebensqualität und Sinnhaftigkeit der eigenen Existenz ein Ende zu setzen, … ist im Ausgangspunkt als Akt autonomer Selbstbestimmung von Staat und Gesellschaft zu respektieren.</p>
<p klasse="J">Das heißt, es steht uns nicht zu – als Gesetzgeber, als Verbände und Kirchen, als Staat und als Gesellschaft –, über die Motive des Suizidwunsches zu urteilen.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="O">Wir müssen den Sterbewunsch, sofern er von einem freien Willen getragen ist, respektieren und den Menschen bei dieser schweren Entscheidung die nötige Unterstützung zukommen lassen.</p>
<p klasse="J">Suizidhilfe ist ein zutiefst emotionales Thema. Einzelfälle sind häufig tragisch. Es gibt viel persönliche Betroffenheit. Ich finde aber, wir müssen uns an dieser Stelle auf unsere Aufgabe als Gesetzgeber besinnen. Als solcher dürfen wir nicht anhand von Einzelschicksalen Gesetze für unser Zusammenleben machen, sondern wir müssen dies im Lichte von Rechtsprechung und gesellschaftlicher Realität tun.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="O">Und dem wollen wir mit unserem Gesetzentwurf für ein Suizidhilfegesetz Rechnung tragen. Es ist geprägt von einem doppelten Schutzgedanken: dem Schutz des Grundrechts auf selbstbestimmtes Sterben einerseits und dem Schutz vor nicht freiverantwortlichen Suiziden andererseits.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD und der FDP)</kommentar>
<p klasse="O">Der Entwurf sieht eine Zweiteilung vor zwischen Beratung und Verschreibung. Das passiert an unterschiedlichen Orten mit zeitlichen Abständen.</p>
<p klasse="J">Zuerst zur Beratung. Diese soll in unabhängigen Beratungsstellen stattfinden und allen Menschen unentgeltlich offenstehen. Ganz wichtig dabei ist: Die Beratung soll präventiv wirken. Es gibt keine Pfadabhängigkeit. Sie ist nicht der direkte Weg in den Suizid, sondern sie schafft einen Ort, an dem Menschen über den eigenen Tod sprechen können, einen Ort, an dem sie Hilfe vermittelt bekommen, und einen Ort, wo Austausch stattfindet – ergebnisoffen, nicht bevormundend und vom Grundwert jeden Menschenlebens ausgehend.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="J">Der zweite Teil des Entwurfs betrifft die Verschreibung, die nur für Menschen über 18 Jahren zu erreichen ist. Die Verschreibung ist der Ort, wo die Sicherstellung der Freiverantwortlichkeit stattfindet. Dies leisten Ärztinnen und Ärzte; denn insbesondere das langjährige Vertrauensverhältnis zwischen Ärzten und Patienten schafft den sicheren Raum, um über solche Entscheidungen zu sprechen und eine solche Entscheidung zu treffen.</p>
<p klasse="J">Aber niemand in diesem Land soll dazu verpflichtet werden, Suizidhilfe leisten zu müssen. Wir wollen nicht nur die Autonomie der Sterbewilligen schützen, sondern auch die der Ärztinnen und Ärzte. Es steht jedem frei, Suizidhilfe zu verweigern.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<p klasse="J">Meine Damen und Herren, ich bin überzeugt, dass wir die Anliegen von Suizidwilligen nicht trivialisieren oder moralisch herabsetzen dürfen. Wir sollten sie stattdessen ernst nehmen, sie vor nicht freiverantwortlichen Entscheidungen bewahren und ihnen dabei die bestmögliche Unterstützung zukommen lassen. Vor allen Dingen sollten wir unserer Aufgabe gerecht werden und Grundrechte schützen. Deswegen bitte ich Sie um Zustimmung zu diesem Gesetzentwurf.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei Abgeordneten des BÜNDNISSES 90/DIE GRÜNEN, der SPD, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: Dr. Lina Seitzl für die Gruppe „Dr. Castellucci und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
</rede>
<rede id="ID2011501400">
<p klasse="redner">
<redner id="11005221">
<name>
<titel>Dr.</titel>
<vorname>Lina</vorname>
<nachname>Seitzl</nachname>
<fraktion>SPD</fraktion>
</name>
</redner>Dr. Lina Seitzl (SPD):</p>
<p klasse="J_1">Sehr geehrte Frau Präsidentin! Liebe Kolleginnen und Kollegen! Sehr geehrte Zuschauerinnen und Zuschauer auf den Tribünen! Jeder Mensch hat das Recht, zu entscheiden, selbst aus dem Leben zu scheiden, und dafür auch Hilfe zu erhalten. Der Staat muss dafür Sorge tragen, dass dieses Recht ausgeübt werden kann. Deshalb muss Suizidhilfe im Rahmen unserer Gesetze möglich sein, und deshalb darf geschäftsmäßige Suizidbeihilfe auch nicht generell nicht möglich sein. Das hat das Bundesverfassungsgericht uns so klar als Aufgabe gegeben.</p>
<p klasse="J">Das Gericht hat aber nicht nur das Recht auf selbstbestimmtes Sterben betont. Es hat uns, dem Gesetzgeber, auch die Aufgabe gegeben, eine Regelung zu treffen, um genau zu prüfen, ob dieser Wunsch frei getroffen wird.</p>
<kommentar>(Beifall der Abg. Dagmar Schmidt [Wetzlar] [SPD] und Kathrin Vogler [DIE LINKE])</kommentar>
<p klasse="O">Aus einem Recht auf selbstbestimmtes Sterben darf keine zumindest gefühlte Pflicht zum Sterben werden.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="O">Wenn ältere Menschen aus dem Leben scheiden möchten, weil sie Angst haben, ihren Angehörigen zur Last zu fallen; wenn Menschen Suizid begehen möchten, weil sie vor einer großen Schuldenlast stehen, dann muss der Staat zumindest einen Ausweg bieten aus einer als ausweglos empfundenen Situation, der eben nicht Suizid heißt.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Deshalb kann Suizidassistenz nur dann möglich sein, wenn klar geprüft ist, dass die Entscheidung für den Suizid frei gebildet und autonom getroffen wurde. Daher unterstütze ich den Gesetzentwurf von Castellucci und anderen, weil er diese Schutzpflicht, die der Staat hat, klar benennt und auch sicherstellt.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Der Gesetzentwurf sieht vor, dass zwei fachkundige Personen mit psychiatrischem oder psychotherapeutischem Hintergrund unabhängig voneinander die autonome und dauerhafte Entscheidung feststellen; denn ein Suizid ist unumkehrbar. Deshalb sieht der Gesetzentwurf auch eine Zeit von in der Regel drei Monaten zwischen den beiden Begutachtungen vor, wobei Ausnahmen von dieser Regel zum Beispiel bei weit fortgeschrittenen, lebensverkürzenden Krankheiten durchaus vorgesehen sind.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Und wenn dieses Schutzkonzept möglich und eingehalten ist, dann ist Suizidbeihilfe, auch die geschäftsmäßige, möglich. Damit ermöglicht der Vorschlag Menschen, die autonom entscheiden, aus dem Leben zu scheiden, dafür Unterstützung zu erhalten, und gleichzeitig sichert er den besonderen Schutzauftrag des Staates.</p>
<p klasse="J">Das möchte ich hier auch sagen: Eine Regelung im Strafrecht schließt das Urteil des Bundesverfassungsgerichts übrigens explizit nicht aus.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="O">Es sagt dazu – ich zitiere mit Erlaubnis der Präsidentin –:</p>
<p klasse="Z">Der hohe Rang, den die Verfassung der Autonomie und dem Leben beimisst, ist grundsätzlich geeignet, deren effektiven präventiven Schutz auch mit Mitteln des Strafrechts zu rechtfertigen.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Der Gesetzentwurf, den Lars Castellucci und andere hier vorlegen, verhindert nicht das Recht auf selbstbestimmtes Sterben. Im Gegenteil: Er stärkt dieses Recht, weil er auf etablierte Strukturen zurückgreift, weil er eine autonome Entscheidung voraussetzt, aber auch, weil er Grenzen setzt und damit Missbrauch vorbeugt.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Mindestens ebenso wichtig ist es aber, dass wir dafür sorgen, dass die Menschen sich nicht dazu getrieben fühlen, aus dem Leben zu scheiden. Wir brauchen dringend eine bedarfsgerechte psychotherapeutische, psychiatrische, psychosoziale und palliativmedizinische Betreuung. Ich möchte mich ganz herzlich auch bei denjenigen bedanken, die den Antrag zur Suizidprävention erarbeitet haben.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Schließlich ist es unsere vordringlichste Aufgabe, dafür zu sorgen, dass alle Menschen ein würdiges Leben haben, egal ob im Alter oder mit einer Krankheit. Das ist eine Daueraufgabe, die wir auch in Zeiten leerer Kassen nie aus dem Blick verlieren dürfen.</p>
<p klasse="J">Liebe Kolleginnen und Kollegen, ich bitte Sie: Stimmen Sie dem Gesetzentwurf von Castellucci und anderen zu, damit der Staat nicht Suizid einfacher möglich macht als den Zugang zu Hilfs- und Betreuungsangeboten, die Menschen in Notlagen dringend brauchen.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: Martina Stamm-Fibich für die Gruppe „Helling-Plahr, Künast und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
</rede>
<rede id="ID2011501500">
<p klasse="redner">
<redner id="11004413">
<name>
<vorname>Martina</vorname>
<nachname>Stamm-Fibich</nachname>
<fraktion>SPD</fraktion>
</name>
</redner>Martina Stamm-Fibich (SPD):</p>
<p klasse="J_1">Sehr geehrte Frau Präsidentin! Liebe Kolleginnen und Kollegen! Sehr geehrte Bürgerinnen und Bürger! In den vergangenen Wochen und Monaten haben wir sehr ausgiebig über das Thema Suizidhilfe diskutiert. Bei den Debatten hier im Haus, in der Anhörung, aber auch bei Veranstaltungen im Wahlkreis und im Gespräch mit den einzelnen Bürgerinnen und Bürgern wurde mir eine Sache ganz besonders bewusst: Die Menschen wollen endlich Klarheit darüber, welche Möglichkeiten sie haben, wenn sie irgendwann einmal aus welchen Gründen auch immer nicht mehr weiterleben wollen. Derzeit gibt es diese Klarheit nicht. Nach Umfragen wollen über 70 Prozent, dass wir diese Klarheit schaffen.</p>
<p klasse="J">All den Bürgerinnen und Bürgern, die in den vergangenen Monaten in meiner Sprechstunde waren und die Petitionen zu diesem Thema eingereicht haben, all diesen Menschen kann ich heute keine klare Antwort auf ihre Fragen geben; denn nach dem Urteil des Bundesverfassungsgerichts und der Aufhebung des § 217 Strafgesetzbuch befinden wir uns in einer rechtlichen Grauzone. Zwei Beispiele: Der Nichtanwendungserlass für das Bundesinstitut für Arzneimittel und Medizinprodukte verhindert, dass Sterbewillige an das tödliche Medikament gelangen. Gleichzeitig steht in Berlin ein Arzt vor Gericht, weil er für eine Frau eine Infusion mit einer Überdosis Narkosemittel bereitstellte. Eine Verurteilung wegen Totschlags in mittelbarer Täterschaft ist nicht ausgeschlossen. Diese Zustände sind unhaltbar.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Den Menschen muss die Ausübung ihres Willens möglich sein, ohne dass sich eine Behörde querstellt. Genauso muss es einem Suizidhelfer möglich sein, dass er oder sie Hilfe leistet, ohne mit einem Bein im Gefängnis zu stehen.</p>
<kommentar>(Beifall der Abg. Dr. Paula Piechotta [BÜNDNIS 90/DIE GRÜNEN])</kommentar>
<p klasse="O">Deshalb ist es notwendig, dass wir klare Vorgaben dazu machen, wie Suizidhilfe in Deutschland zu leisten ist. Gleichzeitig muss sichergestellt werden, dass Menschen, die diesen Weg gehen wollen, ein gutes Beratungsangebot finden.</p>
<p klasse="J">Nur wenn wir diese beiden Voraussetzungen schaffen können, können wir vermeiden, dass dubiose Angebote zur Suizidhilfe entstehen. Wir brauchen also unbedingt ein Gesetz. Dabei müssen wir die richtige Balance zwischen Freiheitsrechten des Einzelnen und dem Schutz vor Fremdeinwirkung finden. Einerseits geht es also darum, den niederschwelligen Zugang zur Suizidhilfe sicherzustellen, andererseits müssen wir Vorsorge dafür treffen, dass die Freiverantwortlichkeit und die Dauerhaftigkeit des Sterbewunsches zu jeder Zeit sichergestellt sind. Nur der Gesetzentwurf der Gruppe „Künast/Helling-Plahr“ vereint diese beiden Anforderungen.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Der Entwurf sichert das Recht auf selbstbestimmtes Sterben und bestimmt einen klaren Prozess zur Inanspruchnahme von Suizidhilfe. Gleichzeitig sieht der Entwurf den Aufbau einer umfassenden Beratungsstruktur vor, und er enthält Maßnahmen zum Schutz des Einzelnen. Diese Struktur ist der Garant dafür, dass eine autonome und freie Entscheidung sichergestellt wird, ohne dass der Zugang zur Suizidassistenz über die Maßen eingeschränkt wird.</p>
<p klasse="J">Genau in diesem Punkt liegt der Hauptunterschied zum Entwurf der Gruppe „Castellucci“. Die Hürden in diesem Entwurf sind zu hoch. Ich erinnere an die öffentliche Anhörung im November: Vier von fünf juristischen Sachverständigen haben erhebliche Zweifel am Schutzkonzept des Gesetzentwurfs der Gruppe „Castellucci“ geäußert.</p>
<p klasse="J">Liebe Kolleginnen und Kollegen, das Schlimmste, was uns passieren kann, ist, dass wir heute am Ende ohne Regelung dastehen und dass der angenommene Entwurf sofort wieder vom Bundesverfassungsgericht gekippt wird.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="O">Um das zu verhindern, bitte ich Sie eindringlich um Ihre Unterstützung für den Entwurf der Gruppe „Künast/Helling-Plahr“.</p>
<p klasse="J">Zum Abschluss möchte ich noch für den Antrag zur Suizidprävention werben, den wir nach dieser kontroversen Diskussion über die beiden Gesetzentwürfe – hoffentlich mit großer Mehrheit – beschließen, und mich auch explizit für die gute Zusammenarbeit bedanken. Unabhängig davon, wie die Abstimmung über die Entwürfe zur Suizidhilfe heute ausgeht, ist es unverzichtbar, dass wir die Suizidprävention in Deutschland stärken; denn noch immer nehmen sich in diesem Land auch sehr viele junge Menschen das Leben, und das müssen wir verhindern.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="O">Die im Antrag aufgelisteten Maßnahmen sind wichtige Bausteine, um die Situation entscheidend zu verbessern.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei Abgeordneten der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächste Rednerin: Elisabeth Winkelmeier-Becker für die Gruppe „Dr. Castellucci und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP und der Abg. Jessica Tatti [DIE LINKE])</kommentar>
</rede>
<rede id="ID2011501600">
<p klasse="redner">
<redner id="11003865">
<name>
<vorname>Elisabeth</vorname>
<nachname>Winkelmeier-Becker</nachname>
<fraktion>CDU/CSU</fraktion>
</name>
</redner>Elisabeth Winkelmeier-Becker (CDU/CSU):</p>
<p klasse="J_1">Frau Präsidentin! Liebe Kolleginnen und Kollegen! Vielleicht ist es Ihnen auch so gegangen, dass, wenn Sie im Wahlkreis Menschen auf die heutige Debatte angesprochen haben, oft die Antwort kam: Wenn jemand am Ende seines Lebens eine schwere Erkrankung hat, Schmerzen hat und den Sterbeprozess abkürzen will, dann haben wir dafür Verständnis, wenn er das mit ärztlichem Beistand machen will. – Das sehen sicher viele so, und das ist sicherlich auch etwas, was das Bundesverfassungsgericht geregelt haben will. Deshalb sehen beide Gesetzentwürfe zur Suizidassistenz ein zügiges Verfahren ohne künstliche, überflüssige Hürden vor, wenn aufgrund der Umstände klar ist, dass es sich um eine freiwillige und endgültige Entscheidung des Menschen handelt.</p>
<kommentar>(Beifall bei Abgeordneten der SPD und der Abg. Dr. Kirsten Kappert-Gonther [BÜNDNIS 90/DIE GRÜNEN] und Benjamin Strasser [FDP])</kommentar>
<p klasse="J">Die Antwort zeigt aber noch etwas Wichtiges. Viele gehen davon aus, dass es nur um diese Situation geht. Wir reden aber heute über Krisen in jeder Lebensphase – die gescheiterte Beziehung oder Karriere, die Insolvenz, die bleibende Behinderung, Trauer, Einsamkeit, Angst –, die Suizidgedanken auslösen können. Obwohl es fast immer auch in solchen Situationen Lösungen gibt, die das Leben wieder lebenswert machen können – der neue Freund, der neue Partner, die Entschuldung, die Therapie, der Neuanfang –, lassen wir die Menschen damit manchmal allein, und das dürfen wir nicht tun.</p>
<p klasse="J">Es gibt ein Grundrecht auf selbstbestimmtes Leben und – ja – auch auf selbstbestimmtes Sterben. Aber es gibt auch ein Grundrecht auf Schutz des Lebens, und es ist unsere Verantwortung, den Schutz des höchsten Rechtsguts, das es gibt und über das wir heute sprechen, zu gewährleisten. Auch das hat das Bundesverfassungsgericht postuliert. Wir haben schon gehört, dass es empirisch belegt ist, dass der Wunsch nach einem Suizid volatil ist. Wahrscheinlich haben viele Menschen ihn im Laufe ihres Lebens. Die Menschen, die ihren Suizidversuch überlebt haben, berichten häufig, dass sie darin im Nachhinein einen Fehler sehen. Deshalb darf beim Wunsch nach Suizid die vorschnelle Antwort der Gesellschaft doch nicht sein: „Okay, wir helfen dir bei einem sanften und leichten Tod“, sondern die Antwort muss lauten: Wir helfen dir raus aus der Krise, so gut es geht, damit du wieder Lebensmut gewinnst.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<p klasse="J">Auch andere Situationen machen verletzlich. Die ältere Frau mit dem teuren Heimplatz, der junge Mensch im Rollstuhl, der auf Hilfe angewiesen ist – sie dürfen nicht darüber nachdenken müssen und sollten noch nicht mal zwingend damit konfrontiert sein, ob sie Kosten verursachen, ob sie jemandem zur Last fallen</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP und der Abg. Jessica Tatti [DIE LINKE])</kommentar>
<p klasse="O">und ob der Suizid nicht eine naheliegende Lösung wäre. Niemand soll sich in dieser Situation dafür rechtfertigen müssen, dass er sein Leben ausschöpfen will.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP)</kommentar>
<p klasse="J">Liebe Kollegen und Kolleginnen, wir haben heute oft gehört, dass es um Selbstbestimmung und um Würde geht. Es darf aber nicht die Botschaft unserer Debatte heute sein, dass nur der seine Selbstbestimmung und Würde wahrt, der sich für den Suizid entscheidet. Selbstbestimmung wahrt auch der oder die, der oder die eine Krankheit annimmt und sich auf Hilfsbedürftigkeit einlässt. Auch wer in allem auf Hilfe angewiesen ist, wahrt seine Würde</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP, der AfD und der LINKEN)</kommentar>
<p klasse="O">und darf sich auf die Hilfe unserer Gesellschaft verlassen – nicht nur ein paar Wochen, nicht nur ein paar Monate, sondern solange das Leben dauert.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der FDP und der Abg. Beatrix von Storch [AfD] und Jessica Tatti [DIE LINKE])</kommentar>
<p klasse="J">Hier entscheidet sich auch, in welcher Gesellschaft wir leben wollen und mit welcher Haltung wir Menschen in dieser Situation entgegentreten wollen. Eine humane Gesellschaft darf hier nicht vorschnell auf Hilfe zum Suizid verweisen. Deshalb brauchen wir den wirksamen Schutz des freien Willens durch zwei ärztliche, therapeutische Termine, und zwar bei Fachleuten, die auch Fachleute für Hilfe sind, die Fachleute für Heilung sind, mit einer Wartezeit von drei Monaten – das ist die Zeit, in der man nach anderen Lösungen suchen kann –, dazwischen die zielgenaue Beratung, die die Hilfe in den Mittelpunkt stellt, und dazu die effektive Absicherung auch mit strafrechtlichen Sanktionen. Diesen Schutz sieht der Entwurf „Castellucci/Heveling“ vor. Deshalb bitte ich Sie und euch ganz herzlich, diesen Entwurf zu unterstützen.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei Abgeordneten der CDU/CSU, der SPD, des BÜNDNISSES 90/DIE GRÜNEN, der FDP und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Nächster Redner: Otto Fricke für die Gruppe „Helling-Plahr/Künast und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
</rede>
<rede id="ID2011501700">
<p klasse="redner">
<redner id="11003530">
<name>
<vorname>Otto</vorname>
<nachname>Fricke</nachname>
<fraktion>FDP</fraktion>
</name>
</redner>Otto Fricke (FDP):</p>
<p klasse="J_1">Sehr geschätzte Frau Präsidentin! Meine lieben Kolleginnen und Kollegen! Lassen Sie mich eine Sache an den Anfang stellen: Wir reden in Deutschland zu wenig über den Tod. Das ist ein Satz, den man immer wieder sagen muss, und eine Tatsache, die unserer Gesellschaft – manchmal, glaube ich, auch aufgrund unserer Geschichte – leider viel zu sehr innewohnt. Ich will mich ausdrücklich bei allen Gruppen bedanken, dass sie sich mit diesem Gesetzentwurf des Themas Tod angenommen haben; denn wir müssen über den Tod reden, weil er im Endeffekt Teil unseres Lebens ist. Das sollten wir bei einer solchen Debatte nie vergessen.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD und des BÜNDNISSES 90/DIE GRÜNEN)</kommentar>
<p klasse="J">Wer über das Leben redet, muss auch offen über das Sterben reden. Ich sage das den jungen Zuschauern, die hier sind, ich sage das den älteren Zuschauern, die hier sind, aber auch allen anderen, die uns zuhören oder zusehen: Eine der wichtigsten Aufgaben einer Gesellschaft ist es doch, über solche Dinge zu reden. Das ist die erste Aufgabe, die wir als Mitmenschen haben, damit verstanden wird, wie der Einzelne, der Sorgen, der Probleme hat, zu seinem Leben, aber auch zu seinem Sterben steht. Ich würde allen Gruppen hier ausdrücklich zubilligen, dass sie sagen: Natürlich wollen wir das Leben schützen; aber wir wollen eben auch die freie Entscheidung des Einzelnen in der einen oder anderen Weise schützen. – Darum geht es heute. Darum geht es in dieser Gesellschaft bei diesem Thema.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD und des BÜNDNISSES 90/DIE GRÜNEN und der Abg. Dr. Petra Sitte [DIE LINKE])</kommentar>
<p klasse="J">Als Anwalt kann ich nur sagen: Es ist für mich immer noch ein Thema, bei dem ich merke: Warum reden die Leute nicht über so was? Man redet inzwischen über alles. Ich meine, wir sehen das ja in den elektronischen Medien: Fast jedes Thema ist präsent. Aber sobald es um das Thema Tod geht – Erbschaft, Organspende, Verführung in Richtung Tod –, zucken wir auf einmal zusammen, weil wir nicht darüber reden. Dafür sind diese Debatten gut. Da kann man auch dem Bundesverfassungsgericht mal wieder dankbar sein – die Gewaltenteilung funktioniert –, dass es uns dazu bringt, über dieses Thema zu reden. Deswegen sage ich an der Stelle auch: Wir müssen gucken, dass wir das Bundesverfassungsgericht ernst nehmen, aber als Gesetzgeber auch unsere Meinung einbringen und zusehen, dass wir nicht wieder vor dem Bundesverfassungsgericht landen.</p>
<kommentar>(Beifall bei Abgeordneten der FDP und des BÜNDNISSES 90/DIE GRÜNEN)</kommentar>
<p klasse="J">Aber, meine Damen und Herren, es geht um etwas ganz Entscheidendes – und da unterscheiden sich die beiden Entwürfe dann doch –: Was für einen Staat wollen wir bei diesem Thema? Wollen wir bei diesen höchstpersönlichen Fragen – Leben, Sterben, Tod – einen Staat, der uns Freiheit lässt, oder wollen wir einen Staat, der diese Freiheit erst einmal grundsätzlich einschränkt, der grundsätzlich die Möglichkeit zulässt, dass ein Verdacht ausgesprochen wird, und dann erst erlaubt, dass der Sterbewille auch entsprechend umgesetzt werden kann? Das ist der essenzielle Unterschied. Wir müssen uns fragen: Wie gehe ich in diese Problematik hinein, egal wie der Zugang ist, egal welche Fälle es sind? Das Verfassungsgericht hat gesagt: Es gibt dieses Recht. Das Verfassungsgericht hat das allgemeine Persönlichkeitsrecht als Abwehrrecht gegen den Staat in dem Urteil ausdrücklich so definiert: Es gibt das Recht. Es sagt nicht: Das Recht ist erst mal nicht da, ein entsprechendes Handeln muss dir erlaubt werden, und es ist eine mögliche Straftat in diesem Zusammenhang, die da passiert. – Nein, es ist erst einmal dein Recht, und der Staat muss ganz genau begründen, wann und wo er einschreitet. Das unterscheidet die beiden Gesetzentwürfe ganz essenziell.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="J">Meine Damen und Herren, dann sagt das Verfassungsgericht sehr schön: Es ist eine „Entscheidung des Einzelnen“. Ja, man muss prüfen, wie sie zustande kommt, aber diese Entscheidung ist „Akt autonomer Selbstbestimmung“, und dieser Akt – dazu kommt noch dieser schöne Satz – ist von „Staat und Gesellschaft“, also auch von allen Bürgerinnen und Bürgern, „zu respektieren“. Das genau ist der Gesetzentwurf „Künast/Helling-Plahr“ in Reinform, das wird genau so übernommen.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="J">Wir wollen verhindern, dass sich irgendjemand in unserer Gesellschaft rechtfertigen muss, wenn er nach einem längeren Verfahren mit möglichst viel Prävention – deswegen übrigens auch der Entschließungsantrag von allen – in einer gut organisierten Form das so hinkriegt. Der Kollege Benner von den Grünen hat noch einmal sehr genau dargestellt, wie das Verfahren in unserer Vorlage läuft; dabei will ich gar nicht sagen, dass das in der anderen nicht läuft, ich würde auch nie in irgendeiner Weise unterstellen, dass die anderen nur sagen: Das darfst du nicht selber entscheiden. – Das Wichtige ist ein geordnetes Verfahren, in dem derjenige, der sagt: „Ich trete dem Suizid näher“, die Möglichkeit hat, sich wirklich gut beraten zu lassen, eine gewisse Zeit zum Überlegen bekommt.</p>
<p klasse="J">Eines will ich zum Schluss hier noch mal betonen: Die Rolle des Strafrechts wird weiterhin existieren, auch in unserem Gesetzentwurf.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD und des BÜNDNISSES 90/DIE GRÜNEN)</kommentar>
<p klasse="O">Es wird Nötigung geben, es wird Betrugsfragen und viele andere Dinge geben. Aber wenn schon der Kern mit einem Verdacht versehen wird, kann ich nur sagen: Selbst wenn nachher herauskommt, dass der Verdacht gegenüber dem Arzt – in unserem Gesetzentwurf ist es übrigens der Hausarzt, in Ihrem ist der Hausarzt, dem man Vertrauen entgegenbringt, raus an der Stelle – sich als falsch herausstellt, sorgt er doch schon dafür, dass alle, die mitwirken, unter einem Verdacht stehen, und das wollen wir nicht. Das Strafrecht ist hier nicht die richtige Lösung.</p>
<p klasse="J">Herzlichen Dank.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Letzter Redner: Benjamin Strasser für die Gruppe „Dr. Castellucci und andere“.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
</rede>
<rede id="ID2011501800">
<p klasse="redner">
<redner id="11004908">
<name>
<vorname>Benjamin</vorname>
<nachname>Strasser</nachname>
<fraktion>FDP</fraktion>
</name>
</redner>Benjamin Strasser (FDP):</p>
<p klasse="J_1">Sehr geehrte Frau Präsidentin! Liebe Kolleginnen und Kollegen! Der Umstand, dass wir heute über Regeln diskutieren, nicht nur über das eigene Sterben, sondern über das Sterben von anderen, ist eine Zumutung für viele Kolleginnen und Kollegen hier im Raum, dessen bin ich mir bewusst. Aber, liebe Kolleginnen und Kollegen, wir diskutieren heute nicht mehr über das Ob des assistierten Suizids; diese Frage hat das Bundesverfassungsgericht mit Ja beantwortet. Wir diskutieren nach drei Jahren darüber, ob wir einen unregulierten Zustand wollen oder ob wir Regeln für den assistierten Suizid und Rechtssicherheit für Betroffene schaffen.</p>
<kommentar>(Beifall bei Abgeordneten der SPD und der Abg. Jessica Tatti [DIE LINKE])</kommentar>
<p klasse="O">Deswegen kann es nicht angehen, dass man heute, nach drei Jahren der Debatte, einfach Nein zu allen Vorschlägen sagt, ohne einen eigenen Vorschlag vorzulegen. Das wird der Lage, in der sich die betroffenen Menschen und ihre Angehörigen befinden, nicht gerecht. Wir müssen heute entscheiden.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="J">Es wurde heute oft der Tenor des Urteils des Bundesverfassungsgerichts zitiert. Ja, das Bundesverfassungsgericht hat ein Grundrecht auf selbstbestimmtes Sterben für alle Menschen definiert, aber es hat auch eine Schutzpflicht des Staates für diese Selbstbestimmung vorgeschrieben. Umso bemerkenswerter und verwunderlicher ist die Debatte der letzten Monate und die Selbstzuschreibung der beiden auf dem Tisch liegenden Vorschläge: die Liberalen auf der einen Seite gegen die Konservativen auf der anderen, die, die bevormunden, gegen die, die respektieren, die, die recht haben, gegen die, die unrecht haben. Liebe Kolleginnen und Kollegen, diese Debatte ist mir so zu unterkomplex. Es geht heute nicht um die Frage, ob richtig oder falsch, sondern es geht um eine einzige, aber entscheidende Frage: Wie sichern wir die Selbstbestimmung von allen Menschen in allen Lebenslagen?</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU und des BÜNDNISSES 90/DIE GRÜNEN und der Abg. Jessica Tatti [DIE LINKE])</kommentar>
<p klasse="J">Das Bundesverfassungsgericht sieht das Recht auf selbstbestimmtes Sterben eben nicht nur für schwerstkranke Menschen am Ende des Lebens vor, sondern auch für gesunde Menschen, aber auch für Menschen mit Behinderungen, Menschen, die armutsbetroffen sind, Menschen, die Suchterkrankungen haben, Menschen, die psychische Erkrankungen haben, kurzum Menschen, die in ihrem Alltag auf die Unterstützung und Hilfe von anderen angewiesen sind. Was ist eigentlich mit deren Selbstbestimmung? Wie sichern wir dort tatsächlich eine freie Entscheidung, dass man nicht das Gefühl hat, man ist überflüssig in einer Gesellschaft oder ein Kostenfaktor? Deswegen ist ein Schutz- und Beratungskonzept so entscheidend,</p>
<kommentar>(Beifall der Abg. Dr. Kirsten Kappert-Gonther [BÜNDNIS 90/DIE GRÜNEN])</kommentar>
<p klasse="O">ein Schutz- und Beratungskonzept, das eben nicht nur auf dem Papier im Bundesgesetzblatt steht, sondern das in der Realität mit Leben erfüllt wird, liebe Kolleginnen und Kollegen.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="J">Der Kollege Benner hat in der Debatte zu Recht darauf hingewiesen: Es ist nicht ratsam, heute über Einzelfälle zu diskutieren. – Ja, aber wir müssen uns schon auch die gesellschaftliche Realität anschauen. Dass Drucksituationen bei Menschen entstehen, die nicht auf der Sonnenseite des Lebens stehen, ist keine irrationale Angst, sondern das ist schlicht und einfach ein Fakt.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="J">Schauen wir auf die Länder, die den assistierten Suizid schon länger anbieten. In Kanada, berichtet die Nachrichtenagentur AP im August 2022, wurden Menschen mit Behinderung und Pflegebedürftige mehrfach in den assistierten Suizid getrieben, um die Kosten im Gesundheitswesen zu senken. Einem Patienten mit einer fortschreitenden Gehirnerkrankung, der mit einem Arzt über seine Langzeitpflege sprechen wollte, hielt der Ethikdoktor einer Klinik vor, jeder Tag im Krankenhaus koste über 1 500 Dollar, Langzeitpflege sei nicht sein Job. Zitat: „Mein Job ist es zu sehen, ob Sie ein Interesse an Sterbehilfe haben“; so der Ethikdirektor des Krankenhauses.</p>
<kommentar>(Julia Klöckner [CDU/CSU]: Unglaublich!)</kommentar>
<p klasse="O">Deswegen sieht das Bundesverfassungsgericht eine Gefahr für die Selbstbestimmung des Einzelnen und hat die Tür zum Strafrecht nicht zugemacht.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="O">Deswegen setzen Länder wie die Schweiz, die schon länger den assistierten Suizid anbieten, auf das Strafrecht, liebe Kolleginnen und Kollegen. Keiner würde sagen: Die Schweiz hat ein restriktives Sterbehilferecht. Deswegen habe ich mich als Liberaler dazu entschieden, den Gesetzentwurf der Gruppe um Lars Castellucci zu unterstützen, nicht weil es mir darum geht, Menschen zu bevormunden oder anderen meinen Willen – was ist gutes Leben oder gutes Sterben? – aufzuoktroyieren. Wer wären wir denn, das zu tun?</p>
<p klasse="J">Die relevante Frage ist doch: Was passiert, wenn Schutz- und Beratungskonzepte nicht eingehalten werden? Ein Rechtsstaat, der schweigend und achselzuckend danebensteht, den kann und darf es nicht geben. Da muss es Konsequenzen geben.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="J">Ich könnte jetzt noch etwas zum Kollegen Otto Fricke sagen, der wiederum interessanterweise auf das Strafrecht verweist. Wenn ich nicht will, dass das Damoklesschwert des Strafrechts immer über Menschen schwebt, die Hilfe leisten, Entschuldigung, dann muss ich die Regelungen im Strafrecht klar treffen, sodass jeder weiß, was erlaubt ist und was eben nicht erlaubt ist, liebe Kolleginnen und Kollegen.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
<p klasse="J">Heute ist nicht die Zeit, nicht die Stunde, Nein zu sagen bei dieser schwierigen Entscheidung. Ich bitte Sie: Stimmen Sie unserem Gesetzentwurf zu und finden Sie eine gute Regel, dass Selbstbestimmung für alle Menschen in allen Lebenslagen in der Praxis tatsächlich gilt.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Beifall bei Abgeordneten der FDP, der SPD, der CDU/CSU, des BÜNDNISSES 90/DIE GRÜNEN und der LINKEN)</kommentar>
</rede>
<name>Präsidentin Bärbel Bas:</name>
<p klasse="J_1">Vielen Dank. – Ich schließe die Aussprache und bitte um Aufmerksamkeit für das Abstimmungsprozedere.</p>
<p klasse="J">Wir kommen zu den Abstimmungen, und zu diesen Abstimmungen liegen mehrere Erklärungen nach § 31 unserer Geschäftsordnung vor<sup>1</sup>
<fussnote>Anlagen 3 bis 9 </fussnote> sowie mehrere Reden, die zu Protokoll gegeben worden sind.<sup>2</sup>
<fussnote>Anlage 2 </fussnote>
</p>
<p klasse="J">Alle Abstimmungen über die Gesetzentwürfe und zum Schluss über den Antrag erfolgen namentlich mit den üblichen Stimmkarten. Nach jeder Abstimmung wird die Sitzung während der Auszählung der Stimmen bis zur Verkündung des Ergebnisses jeweils kurz unterbrochen.</p>
<p klasse="J">Wir kommen nun zur ersten namentlichen Abstimmung. Hier geht es um die zweite Beratung des von den Abgeordneten Dr. Lars Castellucci, Ansgar Heveling, Dr. Kirsten Kappert-Gonther und weiteren Abgeordneten eingebrachten Gesetzentwurfs zur Strafbarkeit der geschäftsmäßigen Hilfe zur Selbsttötung und zur Sicherstellung der Freiverantwortlichkeit der Entscheidung zur Selbsttötung. Der Rechtsausschuss hat in seiner Beschlussempfehlung auf Drucksache 20/7624 unter Buchstabe a empfohlen, über den Gesetzentwurf auf Drucksache 20/904 in der Ausschussfassung einen Beschluss im Plenum herbeizuführen, selbst aber keine inhaltliche Empfehlung abgegeben. Ich bitte nun die Schriftführerinnen und Schriftführer, die vorgesehenen Plätze einzunehmen. – Das ist erfolgt. Ich bitte Sie, nach der ersten namentlichen Abstimmung wieder in den Saal zu kommen. Die namentliche Abstimmung ist eröffnet.<sup>1</sup>
<fussnote>Ergebnis Seite 14097 C</fussnote>
</p>
<p klasse="J">Darf ich die Kolleginnen und Kollegen, die draußen in der Lobby stehen und auf weitere Abstimmungen warten, bitten, wieder in den Saal zu kommen, damit ich die Übersicht habe, welche Kolleginnen und Kollegen in der ersten namentlichen Abstimmung noch nicht abgestimmt haben. – Befindet sich noch ein Mitglied hier im Saal, das in der namentlichen Abstimmung zum Gruppenantrag „Dr. Castellucci“ noch nicht abgestimmt hat? – Ja, da sind noch ein paar unterwegs. Dann warte ich noch ein paar Minuten. – Nun erfolgt mein letzter Aufruf an den Kollegen oder die Kollegin, der oder die in der ersten namentlichen Abstimmung – Gruppenantrag „Dr. Castellucci und andere“ – noch nicht abgestimmt hat: Ist noch jemand im Haus, der noch nicht abgestimmt hat? – Ich sehe, dass jetzt alle abgestimmt haben. Dann schließe ich diese erste namentliche Abstimmung und bitte die Schriftführerinnen und Schriftführer, mit der Auszählung zu beginnen. Bis zum Vorliegen des Ergebnisses unterbreche ich diese Sitzung.</p>
<kommentar>(Unterbrechung von 10.59 bis 11.08 Uhr)</kommentar>
<name>Vizepräsidentin Yvonne Magwas:</name>
<p klasse="J_1">Liebe Kolleginnen und Kollegen, ich eröffne die Sitzung wieder.</p>
<p klasse="J">Es liegt mir das von den Schriftführerinnen und Schriftführern ermittelte Ergebnis der namentlichen Abstimmung über den Gesetzentwurf des Abgeordneten Dr. Lars Castellucci und weiterer Abgeordneter in der Ausschussfassung vor: abgegebene Stimmkarten 690. Mit Ja haben gestimmt 304, mit Nein haben gestimmt 363, Enthaltungen gab es 23. Der Gesetzentwurf ist damit in zweiter Beratung abgelehnt. Damit entfällt nach der Geschäftsordnung die weitere Beratung.</p>
<p klasse="AL_Vorspann_1">Endgültiges Ergebnis</p>
<p klasse="AL_Vorspann_2">Abgegebene Stimmen:687;</p>
<p klasse="AL_Vorspann_2">davon</p>
<p klasse="AL_Vorspann_3">ja:302</p>
<p klasse="AL_Vorspann_3">nein:362</p>
<p klasse="AL_Vorspann_3">enthalten:23</p>
<p klasse="AL_Ja-Nein-Enth">Ja</p>
<p klasse="AL_Partei">SPD</p>
<p klasse="AL_Namen">Reem Alabali-Radovan</p>
<p klasse="AL_Namen">Dagmar Andres</p>
<p klasse="AL_Namen">Niels Annen</p>
<p klasse="AL_Namen">Heike Baehrens</p>
<p klasse="AL_Namen">Daniel Baldy</p>
<p klasse="AL_Namen">Nezahat Baradari</p>
<p klasse="AL_Namen">Alexander Bartz</p>
<p klasse="AL_Namen">Jürgen Berghahn</p>
<p klasse="AL_Namen">Dr. Lars Castellucci</p>
<p klasse="AL_Namen">Jürgen Coße</p>
<p klasse="AL_Namen">Felix Döring</p>
<p klasse="AL_Namen">Sebastian Fiedler</p>
<p klasse="AL_Namen">Michael Gerdes</p>
<p klasse="AL_Namen">Martin Gerster</p>
<p klasse="AL_Namen">Angelika Glöckner</p>
<p klasse="AL_Namen">Kerstin Griese</p>
<p klasse="AL_Namen">Uli Grötsch</p>
<p klasse="AL_Namen">Metin Hakverdi</p>
<p klasse="AL_Namen">Hubertus Heil (Peine)</p>
<p klasse="AL_Namen">Frauke Heiligenstadt</p>
<p klasse="AL_Namen">Josip Juratovic</p>
<p klasse="AL_Namen">Oliver Kaczmarek</p>
<p klasse="AL_Namen">Dr. Franziska Kersten</p>
<p klasse="AL_Namen">Helmut Kleebank</p>
<p klasse="AL_Namen">Lars Klingbeil</p>
<p klasse="AL_Namen">Sarah Lahrkamp</p>
<p klasse="AL_Namen">Luiza Licina-Bode</p>
<p klasse="AL_Namen">Bettina Lugk</p>
<p klasse="AL_Namen">Dr. Tanja Machalet</p>
<p klasse="AL_Namen">Parsa Marvi</p>
<p klasse="AL_Namen">Katja Mast</p>
<p klasse="AL_Namen">Takis Mehmet Ali</p>
<p klasse="AL_Namen">Dirk-Ulrich Mende</p>
<p klasse="AL_Namen">Kathrin Michel</p>
<p klasse="AL_Namen">Michelle Müntefering</p>
<p klasse="AL_Namen">Dietmar Nietan</p>
<p klasse="AL_Namen">Jörg Nürnberger</p>
<p klasse="AL_Namen">Aydan Özoğuz</p>
<p klasse="AL_Namen">Mathias Papendieck</p>
<p klasse="AL_Namen">Achim Post (Minden)</p>
<p klasse="AL_Namen">Andreas Rimkus</p>
<p klasse="AL_Namen">Dennis Rohde</p>
<p klasse="AL_Namen">Dr. Martin Rosemann</p>
<p klasse="AL_Namen">Jessica Rosenthal</p>
<p klasse="AL_Namen">Dr. Thorsten Rudolph</p>
<p klasse="AL_Namen">Bernd Rützel</p>
<p klasse="AL_Namen">Ingo Schäfer</p>
<p klasse="AL_Namen">Johannes Schätzl</p>
<p klasse="AL_Namen">Udo Schiefner</p>
<p klasse="AL_Namen">Peggy Schierenbeck</p>
<p klasse="AL_Namen">Dr. Nils Schmid</p>
<p klasse="AL_Namen">Dagmar Schmidt (Wetzlar)</p>
<p klasse="AL_Namen">Daniel Schneider</p>
<p klasse="AL_Namen">Christian Schreider</p>
<p klasse="AL_Namen">Frank Schwabe</p>
<p klasse="AL_Namen">Rita Schwarzelühr-Sutter</p>
<p klasse="AL_Namen">Dr. Lina Seitzl</p>
<p klasse="AL_Namen">Dr. Ralf Stegner</p>
<p klasse="AL_Namen">Anja Troff-Schaffarzyk</p>
<p klasse="AL_Namen">Maja Wallstein</p>
<p klasse="AL_Namen">Dr. Joe Weingarten</p>
<p klasse="AL_Namen">Gülistan Yüksel</p>
<p klasse="AL_Partei">CDU/CSU</p>
<p klasse="AL_Namen">Knut Abraham</p>
<p klasse="AL_Namen">Stephan Albani</p>
<p klasse="AL_Namen">Artur Auernhammer</p>
<p klasse="AL_Namen">Peter Aumer</p>
<p klasse="AL_Namen">Dr. André Berghegger</p>
<p klasse="AL_Namen">Peter Beyer</p>
<p klasse="AL_Namen">Marc Biadacz</p>
<p klasse="AL_Namen">Steffen Bilger</p>
<p klasse="AL_Namen">Silvia Breher</p>
<p klasse="AL_Namen">Heike Brehmer</p>
<p klasse="AL_Namen">Michael Breilmann</p>
<p klasse="AL_Namen">Ralph Brinkhaus</p>
<p klasse="AL_Namen">Dr. Carsten Brodesser</p>
<p klasse="AL_Namen">Dr. Marlon Bröhr</p>
<p klasse="AL_Namen">Gitta Connemann</p>
<p klasse="AL_Namen">Mario Czaja</p>
<p klasse="AL_Namen">Astrid Damerow</p>
<p klasse="AL_Namen">Alexander Dobrindt</p>
<p klasse="AL_Namen">Michael Donth</p>
<p klasse="AL_Namen">Hansjörg Durz</p>
<p klasse="AL_Namen">Ralph Edelhäußer</p>
<p klasse="AL_Namen">Alexander Engelhard</p>
<p klasse="AL_Namen">Thomas Erndl</p>
<p klasse="AL_Namen">Hermann Färber</p>
<p klasse="AL_Namen">Uwe Feiler</p>
<p klasse="AL_Namen">Enak Ferlemann</p>
<p klasse="AL_Namen">Alexander Föhr</p>
<p klasse="AL_Namen">Thorsten Frei</p>
<p klasse="AL_Namen">Dr. Hans-Peter Friedrich (Hof)</p>
<p klasse="AL_Namen">Michael Frieser</p>
<p klasse="AL_Namen">Ingo Gädechens</p>
<p klasse="AL_Namen">Dr. Thomas Gebhart</p>
<p klasse="AL_Namen">Dr. Jonas Geissler</p>
<p klasse="AL_Namen">Fabian Gramling</p>
<p klasse="AL_Namen">Hermann Gröhe</p>
<p klasse="AL_Namen">Michael Grosse-Brömer</p>
<p klasse="AL_Namen">Markus Grübel</p>
<p klasse="AL_Namen">Manfred Grund</p>
<p klasse="AL_Namen">Oliver Grundmann</p>
<p klasse="AL_Namen">Monika Grütters</p>
<p klasse="AL_Namen">Serap Güler</p>
<p klasse="AL_Namen">Fritz Güntzler</p>
<p klasse="AL_Namen">Olav Gutting</p>
<p klasse="AL_Namen">Florian Hahn</p>
<p klasse="AL_Namen">Jürgen Hardt</p>
<p klasse="AL_Namen">Matthias Hauer</p>
<p klasse="AL_Namen">Dr. Stefan Heck</p>
<p klasse="AL_Namen">Mechthild Heil</p>
<p klasse="AL_Namen">Marc Henrichmann</p>
<p klasse="AL_Namen">Ansgar Heveling</p>
<p klasse="AL_Namen">Susanne Hierl</p>
<p klasse="AL_Namen">Christian Hirte</p>
<p klasse="AL_Namen">Alexander Hoffmann</p>
<p klasse="AL_Namen">Dr. Hendrik Hoppenstedt</p>
<p klasse="AL_Namen">Franziska Hoppermann</p>
<p klasse="AL_Namen">Anne Janssen</p>
<p klasse="AL_Namen">Thomas Jarzombek</p>
<p klasse="AL_Namen">Andreas Jung</p>
<p klasse="AL_Namen">Ingmar Jung</p>
<p klasse="AL_Namen">Anja Karliczek</p>
<p klasse="AL_Namen">Ronja Kemmer</p>
<p klasse="AL_Namen">Michael Kießling</p>
<p klasse="AL_Namen">Dr. Georg Kippels</p>
<p klasse="AL_Namen">Dr. Ottilie Klein</p>
<p klasse="AL_Namen">Volkmar Klein</p>
<p klasse="AL_Namen">Julia Klöckner</p>
<p klasse="AL_Namen">Axel Knoerig</p>
<p klasse="AL_Namen">Anne König</p>
<p klasse="AL_Namen">Markus Koob</p>
<p klasse="AL_Namen">Carsten Körber</p>
<p klasse="AL_Namen">Gunther Krichbaum</p>
<p klasse="AL_Namen">Dr. Günter Krings</p>
<p klasse="AL_Namen">Tilman Kuban</p>
<p klasse="AL_Namen">Ulrich Lange</p>
<p klasse="AL_Namen">Armin Laschet</p>
<p klasse="AL_Namen">Dr. Silke Launert</p>
<p klasse="AL_Namen">Jens Lehmann</p>
<p klasse="AL_Namen">Paul Lehrieder</p>
<p klasse="AL_Namen">Dr. Katja Leikert</p>
<p klasse="AL_Namen">Dr. Andreas Lenz</p>
<p klasse="AL_Namen">Andrea Lindholz</p>
<p klasse="AL_Namen">Dr. Carsten Linnemann</p>
<p klasse="AL_Namen">Bernhard Loos</p>
<p klasse="AL_Namen">Klaus Mack</p>
<p klasse="AL_Namen">Andreas Mattfeldt</p>
<p klasse="AL_Namen">Stephan Mayer (Altötting)</p>
<p klasse="AL_Namen">Volker Mayer-Lay</p>
<p klasse="AL_Namen">Dr. Michael Meister</p>
<p klasse="AL_Namen">Friedrich Merz</p>
<p klasse="AL_Namen">Jan Metzler</p>
<p klasse="AL_Namen">Dietrich Monstadt</p>
<p klasse="AL_Namen">Maximilian Mörseburg</p>
<p klasse="AL_Namen">Axel Müller</p>
<p klasse="AL_Namen">Carsten Müller (Braunschweig)</p>
<p klasse="AL_Namen">Stefan Müller (Erlangen)</p>
<p klasse="AL_Namen">Dr. Stefan Nacke</p>
<p klasse="AL_Namen">Petra Nicolaisen</p>
<p klasse="AL_Namen">Wilfried Oellers</p>
<p klasse="AL_Namen">Moritz Oppelt</p>
<p klasse="AL_Namen">Florian Oßner</p>
<p klasse="AL_Namen">Henning Otte</p>
<p klasse="AL_Namen">Stephan Pilsinger</p>
<p klasse="AL_Namen">Dr. Christoph Ploß</p>
<p klasse="AL_Namen">Dr. Martin Plum</p>
<p klasse="AL_Namen">Thomas Rachel</p>
<p klasse="AL_Namen">Alexander Radwan</p>
<p klasse="AL_Namen">Alois Rainer</p>
<p klasse="AL_Namen">Henning Rehbaum</p>
<p klasse="AL_Namen">Dr. Markus Reichel</p>
<p klasse="AL_Namen">Josef Rief</p>
<p klasse="AL_Namen">Lars Rohwer</p>
<p klasse="AL_Namen">Stefan Rouenhoff</p>
<p klasse="AL_Namen">Erwin Rüddel</p>
<p klasse="AL_Namen">Albert Rupprecht</p>
<p klasse="AL_Namen">Catarina dos Santos-Wintz</p>
<p klasse="AL_Namen">Dr. Christiane Schenderlein</p>
<p klasse="AL_Namen">Andreas Scheuer</p>
<p klasse="AL_Namen">Patrick Schnieder</p>
<p klasse="AL_Namen">Nadine Schön</p>
<p klasse="AL_Namen">Felix Schreiner</p>
<p klasse="AL_Namen">Detlef Seif</p>
<p klasse="AL_Namen">Thomas Silberhorn</p>
<p klasse="AL_Namen">Björn Simon</p>
<p klasse="AL_Namen">Dr. Wolfgang Stefinger</p>
<p klasse="AL_Namen">Albert Stegemann</p>
<p klasse="AL_Namen">Johannes Steiniger</p>
<p klasse="AL_Namen">Christian Freiherr von Stetten</p>
<p klasse="AL_Namen">Diana Stöcker</p>
<p klasse="AL_Namen">Stephan Stracke</p>
<p klasse="AL_Namen">Max Straubinger</p>
<p klasse="AL_Namen">Christina Stumpp</p>
<p klasse="AL_Namen">Dr. Hermann-Josef Tebroke</p>
<p klasse="AL_Namen">Hans-Jürgen Thies</p>
<p klasse="AL_Namen">Alexander Throm</p>
<p klasse="AL_Namen">Antje Tillmann</p>
<p klasse="AL_Namen">Markus Uhl</p>
<p klasse="AL_Namen">Dr. Volker Ullrich</p>
<p klasse="AL_Namen">Dr. Oliver Vogt</p>
<p klasse="AL_Namen">Dr. Johann David Wadephul</p>
<p klasse="AL_Namen">Marco Wanderwitz</p>
<p klasse="AL_Namen">Dr. Anja Weisgerber</p>
<p klasse="AL_Namen">Maria-Lena Weiss</p>
<p klasse="AL_Namen">Kai Whittaker</p>
<p klasse="AL_Namen">Annette Widmann-Mauz</p>
<p klasse="AL_Namen">Dr. Klaus Wiener</p>
<p klasse="AL_Namen">Elisabeth Winkelmeier-Becker</p>
<p klasse="AL_Namen">Mechthilde Wittmann</p>
<p klasse="AL_Namen">Mareike Wulf</p>
<p klasse="AL_Namen">Emmi Zeulner</p>
<p klasse="AL_Namen">Paul Ziemiak</p>
<p klasse="AL_Namen">Nicolas Zippelius</p>
<p klasse="AL_Partei">BÜNDNIS 90/ DIE GRÜNEN</p>
<p klasse="AL_Namen">Stephanie Aeffner</p>
<p klasse="AL_Namen">Lisa Badum</p>
<p klasse="AL_Namen">Annalena Baerbock</p>
<p klasse="AL_Namen">Katharina Beck</p>
<p klasse="AL_Namen">Agnieszka Brugger</p>
<p klasse="AL_Namen">Frank Bsirske</p>
<p klasse="AL_Namen">Dr. Anna Christmann</p>
<p klasse="AL_Namen">Dr. Janosch Dahmen</p>
<p klasse="AL_Namen">Ekin Deligöz</p>
<p klasse="AL_Namen">Leon Eckert</p>
<p klasse="AL_Namen">Tessa Ganserer</p>
<p klasse="AL_Namen">Katrin Göring-Eckardt</p>
<p klasse="AL_Namen">Dr. Armin Grau</p>
<p klasse="AL_Namen">Erhard Grundl</p>
<p klasse="AL_Namen">Sabine Grützmacher</p>
<p klasse="AL_Namen">Bernhard Herrmann</p>
<p klasse="AL_Namen">Dr. Anton Hofreiter</p>
<p klasse="AL_Namen">Lamya Kaddor</p>
<p klasse="AL_Namen">Dr. Kirsten Kappert-Gonther</p>
<p klasse="AL_Namen">Sven-Christian Kindler</p>
<p klasse="AL_Namen">Maria Klein-Schmeink</p>
<p klasse="AL_Namen">Laura Kraft</p>
<p klasse="AL_Namen">Christian Kühn (Tübingen)</p>
<p klasse="AL_Namen">Markus Kurth</p>
<p klasse="AL_Namen">Dr. Tobias Lindner</p>
<p klasse="AL_Namen">Max Lucks</p>
<p klasse="AL_Namen">Susanne Menge</p>
<p klasse="AL_Namen">Swantje Henrike Michaelsen</p>
<p klasse="AL_Namen">Boris Mijatovic</p>
<p klasse="AL_Namen">Beate Müller-Gemmeke</p>
<p klasse="AL_Namen">Sara Nanni</p>
<p klasse="AL_Namen">Dr. Konstantin von Notz</p>
<p klasse="AL_Namen">Omid Nouripour</p>
<p klasse="AL_Namen">Dr. Anja Reinalter</p>
<p klasse="AL_Namen">Claudia Roth (Augsburg)</p>
<p klasse="AL_Namen">Corinna Rüffer</p>
<p klasse="AL_Namen">Michael Sacher</p>
<p klasse="AL_Namen">Jamila Schäfer</p>
<p klasse="AL_Namen">Dr. Sebastian Schäfer</p>
<p klasse="AL_Namen">Kordula Schulz-Asche</p>
<p klasse="AL_Namen">Melis Sekmen</p>
<p klasse="AL_Namen">Nyke Slawik</p>
<p klasse="AL_Namen">Dr. Wolfgang Strengmann-Kuhn</p>
<p klasse="AL_Namen">Katrin Uhlig</p>
<p klasse="AL_Namen">Johannes Wagner</p>
<p klasse="AL_Namen">Stefan Wenzel</p>
<p klasse="AL_Partei">FDP</p>
<p klasse="AL_Namen">Renata Alt</p>
<p klasse="AL_Namen">Jens Beeck</p>
<p klasse="AL_Namen">Carl-Julius Cronenberg</p>
<p klasse="AL_Namen">Christian Dürr</p>
<p klasse="AL_Namen">Thomas Hacker</p>
<p klasse="AL_Namen">Manuel Höferlin</p>
<p klasse="AL_Namen">Dr. Ann-Veruschka Jurisch</p>
<p klasse="AL_Namen">Pascal Kober</p>
<p klasse="AL_Namen">Ulrich Lechte</p>
<p klasse="AL_Namen">Lars Lindemann</p>
<p klasse="AL_Namen">Michael Georg Link (Heilbronn)</p>
<p klasse="AL_Namen">Till Mansmann</p>
<p klasse="AL_Namen">Christoph Meyer</p>
<p klasse="AL_Namen">Maximilian Mordhorst</p>
<p klasse="AL_Namen">Christian Sauter</p>
<p klasse="AL_Namen">Matthias Seestern-Pauly</p>
<p klasse="AL_Namen">Dr. Stephan Seiter</p>
<p klasse="AL_Namen">Rainer Semet</p>
<p klasse="AL_Namen">Judith Skudelny</p>
<p klasse="AL_Namen">Bettina Stark-Watzinger</p>
<p klasse="AL_Namen">Konrad Stockmeier</p>
<p klasse="AL_Namen">Benjamin Strasser</p>
<p klasse="AL_Namen">Linda Teuteberg</p>
<p klasse="AL_Namen">Michael Theurer</p>
<p klasse="AL_Namen">Nico Tippelt</p>
<p klasse="AL_Namen">Dr. Florian Toncar</p>
<p klasse="AL_Namen">Dr. Andrew Ullmann</p>
<p klasse="AL_Namen">Dr. Volker Wissing</p>
<p klasse="AL_Partei">AfD</p>
<p klasse="AL_Namen">Dr. Alexander Gauland</p>
<p klasse="AL_Namen">Albrecht Glaser</p>
<p klasse="AL_Namen">Fabian Jacobi</p>
<p klasse="AL_Namen">Barbara Lenk</p>
<p klasse="AL_Namen">Jan Ralf Nolte</p>
<p klasse="AL_Partei">DIE LINKE</p>
<p klasse="AL_Namen">Gökay Akbulut</p>
<p klasse="AL_Namen">Clara Bünger</p>
<p klasse="AL_Namen">Sevim Dağdelen</p>
<p klasse="AL_Namen">Ates Gürpinar</p>
<p klasse="AL_Namen">Pascal Meiser</p>
<p klasse="AL_Namen">Amira Mohamed Ali</p>
<p klasse="AL_Namen">Petra Pau</p>
<p klasse="AL_Namen">Victor Perli</p>
<p klasse="AL_Namen">Martina Renner</p>
<p klasse="AL_Namen">Jessica Tatti</p>
<p klasse="AL_Namen">Kathrin Vogler</p>
<p klasse="AL_Ja-Nein-Enth">Nein</p>
<p klasse="AL_Partei">SPD</p>
<p klasse="AL_Namen">Sanae Abdi</p>
<p klasse="AL_Namen">Adis Ahmetovic</p>
<p klasse="AL_Namen">Ulrike Bahr</p>
<p klasse="AL_Namen">Sören Bartol</p>
<p klasse="AL_Namen">Bärbel Bas</p>
<p klasse="AL_Namen">Dr. Holger Becker</p>
<p klasse="AL_Namen">Bengt Bergt</p>
<p klasse="AL_Namen">Jakob Blankenburg</p>
<p klasse="AL_Namen">Leni Breymaier</p>
<p klasse="AL_Namen">Bernhard Daldrup</p>
<p klasse="AL_Namen">Dr. Daniela De Ridder</p>
<p klasse="AL_Namen">Hakan Demir</p>
<p klasse="AL_Namen">Dr. Karamba Diaby</p>
<p klasse="AL_Namen">Martin Diedenhofen</p>
<p klasse="AL_Namen">Jan Dieren</p>
<p klasse="AL_Namen">Esther Dilcher</p>
<p klasse="AL_Namen">Sabine Dittmar</p>
<p klasse="AL_Namen">Falko Droßmann</p>
<p klasse="AL_Namen">Axel Echeverria</p>
<p klasse="AL_Namen">Sonja Eichwede</p>
<p klasse="AL_Namen">Heike Engelhardt</p>
<p klasse="AL_Namen">Dr. Wiebke Esdar</p>
<p klasse="AL_Namen">Saskia Esken</p>
<p klasse="AL_Namen">Ariane Fäscher</p>
<p klasse="AL_Namen">Dr. Johannes Fechner</p>
<p klasse="AL_Namen">Dr. Edgar Franke</p>
<p klasse="AL_Namen">Fabian Funke</p>
<p klasse="AL_Namen">Manuel Gava</p>
<p klasse="AL_Namen">Timon Gremmels</p>
<p klasse="AL_Namen">Bettina Hagedorn</p>
<p klasse="AL_Namen">Rita Hagl-Kehl</p>
<p klasse="AL_Namen">Sebastian Hartmann</p>
<p klasse="AL_Namen">Dirk Heidenblut</p>
<p klasse="AL_Namen">Gabriela Heinrich</p>
<p klasse="AL_Namen">Wolfgang Hellmich</p>
<p klasse="AL_Namen">Anke Hennig</p>
<p klasse="AL_Namen">Nadine Heselhaus</p>
<p klasse="AL_Namen">Thomas Hitschler</p>
<p klasse="AL_Namen">Jasmina Hostert</p>
<p klasse="AL_Namen">Verena Hubertz</p>
<p klasse="AL_Namen">Markus Hümpfer</p>
<p klasse="AL_Namen">Frank Junge</p>
<p klasse="AL_Namen">Elisabeth Kaiser</p>
<p klasse="AL_Namen">Carlos Kasper</p>
<p klasse="AL_Namen">Anna Kassautzki</p>
<p klasse="AL_Namen">Gabriele Katzmarek</p>
<p klasse="AL_Namen">Annika Klose</p>
<p klasse="AL_Namen">Tim Klüssendorf</p>
<p klasse="AL_Namen">Dr. Bärbel Kofler</p>
<p klasse="AL_Namen">Anette Kramme</p>
<p klasse="AL_Namen">Dunja Kreiser</p>
<p klasse="AL_Namen">Martin Kröber</p>
<p klasse="AL_Namen">Kevin Kühnert</p>
<p klasse="AL_Namen">Esra Limbacher</p>
<p klasse="AL_Namen">Helge Lindh</p>
<p klasse="AL_Namen">Isabel Mackensen-Geis</p>
<p klasse="AL_Namen">Erik von Malottki</p>
<p klasse="AL_Namen">Holger Mann</p>
<p klasse="AL_Namen">Kaweh Mansoori</p>
<p klasse="AL_Namen">Dr. Zanda Martens</p>
<p klasse="AL_Namen">Dorothee Martin</p>
<p klasse="AL_Namen">Franziska Mascheck</p>
<p klasse="AL_Namen">Andreas Mehltretter</p>
<p klasse="AL_Namen">Robin Mesarosch</p>
<p klasse="AL_Namen">Dr. Matthias Miersch</p>
<p klasse="AL_Namen">Matthias David Mieves</p>
<p klasse="AL_Namen">Susanne Mittag</p>
<p klasse="AL_Namen">Siemtje Möller</p>
<p klasse="AL_Namen">Detlef Müller (Chemnitz)</p>
<p klasse="AL_Namen">Dr. Rolf Mützenich</p>
<p klasse="AL_Namen">Rasha Nasr</p>
<p klasse="AL_Namen">Brian Nickholz</p>
<p klasse="AL_Namen">Lennard Oehl</p>
<p klasse="AL_Namen">Josephine Ortleb</p>
<p klasse="AL_Namen">Mahmut Özdemir (Duisburg)</p>
<p klasse="AL_Namen">Dr. Christos Pantazis</p>
<p klasse="AL_Namen">Wiebke Papenbrock</p>
<p klasse="AL_Namen">Natalie Pawlik</p>
<p klasse="AL_Namen">Jens Peick</p>
<p klasse="AL_Namen">Christian Petry</p>
<p klasse="AL_Namen">Jan Plobner</p>
<p klasse="AL_Namen">Sabine Poschmann</p>
<p klasse="AL_Namen">Ye-One Rhie</p>
<p klasse="AL_Namen">Daniel Rinkert</p>
<p klasse="AL_Namen">Sönke Rix</p>
<p klasse="AL_Namen">Sebastian Roloff</p>
<p klasse="AL_Namen">Michael Roth (Heringen)</p>
<p klasse="AL_Namen">Tina Rudolph</p>
<p klasse="AL_Namen">Sarah Ryglewski</p>
<p klasse="AL_Namen">Johann Saathoff</p>
<p klasse="AL_Namen">Axel Schäfer (Bochum)</p>
<p klasse="AL_Namen">Rebecca Schamber</p>
<p klasse="AL_Namen">Dr. Nina Scheer</p>
<p klasse="AL_Namen">Timo Schisanowski</p>
<p klasse="AL_Namen">Christoph Schmid</p>
<p klasse="AL_Namen">Uwe Schmidt</p>
<p klasse="AL_Namen">Carsten Schneider (Erfurt)</p>
<p klasse="AL_Namen">Johannes Schraps</p>
<p klasse="AL_Namen">Michael Schrodi</p>
<p klasse="AL_Namen">Svenja Schulze</p>
<p klasse="AL_Namen">Andreas Schwarz</p>
<p klasse="AL_Namen">Svenja Stadler</p>
<p klasse="AL_Namen">Martina Stamm-Fibich</p>
<p klasse="AL_Namen">Mathias Stein</p>
<p klasse="AL_Namen">Nadja Sthamer</p>
<p klasse="AL_Namen">Ruppert Stüwe</p>
<p klasse="AL_Namen">Claudia Tausend</p>
<p klasse="AL_Namen">Michael Thews</p>
<p klasse="AL_Namen">Markus Töns</p>
<p klasse="AL_Namen">Carsten Träger</p>
<p klasse="AL_Namen">Ana-Maria Trasnea</p>
<p klasse="AL_Namen">Derya Türk-Nachbaur</p>
<p klasse="AL_Namen">Frank Ullrich</p>
<p klasse="AL_Namen">Marja-Liisa Völlers</p>
<p klasse="AL_Namen">Emily Vontz</p>
<p klasse="AL_Namen">Dirk Vöpel</p>
<p klasse="AL_Namen">Dr. Carolin Wagner</p>
<p klasse="AL_Namen">Hannes Walter</p>
<p klasse="AL_Namen">Carmen Wegge</p>
<p klasse="AL_Namen">Melanie Wegling</p>
<p klasse="AL_Namen">Lena Werner</p>
<p klasse="AL_Namen">Bernd Westphal</p>
<p klasse="AL_Namen">Dirk Wiese</p>
<p klasse="AL_Namen">Dr. Herbert Wollmann</p>
<p klasse="AL_Namen">Stefan Zierke</p>
<p klasse="AL_Namen">Dr. Jens Zimmermann</p>
<p klasse="AL_Namen">Armand Zorn</p>
<p klasse="AL_Namen">Katrin Zschau</p>
<p klasse="AL_Partei">CDU/CSU</p>
<p klasse="AL_Namen">Norbert Maria Altenkamp</p>
<p klasse="AL_Namen">Philipp Amthor</p>
<p klasse="AL_Namen">Dorothee Bär</p>
<p klasse="AL_Namen">Thomas Bareiß</p>
<p klasse="AL_Namen">Melanie Bernstein</p>
<p klasse="AL_Namen">Simone Borchardt</p>
<p klasse="AL_Namen">Michael Brand (Fulda)</p>
<p klasse="AL_Namen">Dr. Reinhard Brandl</p>
<p klasse="AL_Namen">Dr. Helge Braun</p>
<p klasse="AL_Namen">Sebastian Brehm</p>
<p klasse="AL_Namen">Mark Helfrich</p>
<p klasse="AL_Namen">Erich Irlstorfer</p>
<p klasse="AL_Namen">Roderich Kiesewetter</p>
<p klasse="AL_Namen">Jens Koeppen</p>
<p klasse="AL_Namen">Patricia Lips</p>
<p klasse="AL_Namen">Dr. Jan-Marco Luczak</p>
<p klasse="AL_Namen">Daniela Ludwig</p>
<p klasse="AL_Namen">Yvonne Magwas</p>
<p klasse="AL_Namen">Sepp Müller</p>
<p klasse="AL_Namen">Josef Oster</p>
<p klasse="AL_Namen">Kerstin Radomski</p>
<p klasse="AL_Namen">Dr. Peter Ramsauer</p>
<p klasse="AL_Namen">Jana Schimke</p>
<p klasse="AL_Namen">Katrin Staffler</p>
<p klasse="AL_Namen">Dieter Stier</p>
<p klasse="AL_Namen">Astrid Timmermann-Fechter</p>
<p klasse="AL_Namen">Klaus-Peter Willsch</p>
<p klasse="AL_Partei">BÜNDNIS 90/ DIE GRÜNEN</p>
<p klasse="AL_Namen">Luise Amtsberg</p>
<p klasse="AL_Namen">Andreas Audretsch</p>
<p klasse="AL_Namen">Maik Außendorf</p>
<p klasse="AL_Namen">Tobias B. Bacherle</p>
<p klasse="AL_Namen">Felix Banaszak</p>
<p klasse="AL_Namen">Karl Bär</p>
<p klasse="AL_Namen">Lukas Benner</p>
<p klasse="AL_Namen">Dr. Franziska Brantner</p>
<p klasse="AL_Namen">Dr. Sandra Detzer</p>
<p klasse="AL_Namen">Katharina Dröge</p>
<p klasse="AL_Namen">Deborah Düring</p>
<p klasse="AL_Namen">Harald Ebner</p>
<p klasse="AL_Namen">Marcel Emmerich</p>
<p klasse="AL_Namen">Emilia Fester</p>
<p klasse="AL_Namen">Schahina Gambir</p>
<p klasse="AL_Namen">Matthias Gastel</p>
<p klasse="AL_Namen">Kai Gehring</p>
<p klasse="AL_Namen">Stefan Gelbhaar</p>
<p klasse="AL_Namen">Dr. Jan-Niclas Gesenhues</p>
<p klasse="AL_Namen">Dr. Robert Habeck</p>
<p klasse="AL_Namen">Britta Haßelmann</p>
<p klasse="AL_Namen">Linda Heitmann</p>
<p klasse="AL_Namen">Kathrin Henneberger</p>
<p klasse="AL_Namen">Dr. Bettina Hoffmann</p>
<p klasse="AL_Namen">Bruno Hönel</p>
<p klasse="AL_Namen">Dieter Janecek</p>
<p klasse="AL_Namen">Michael Kellner</p>
<p klasse="AL_Namen">Katja Keul</p>
<p klasse="AL_Namen">Misbah Khan</p>
<p klasse="AL_Namen">Philip Krämer</p>
<p klasse="AL_Namen">Renate Künast</p>
<p klasse="AL_Namen">Ricarda Lang</p>
<p klasse="AL_Namen">Sven Lehmann</p>
<p klasse="AL_Namen">Anja Liebert</p>
<p klasse="AL_Namen">Helge Limburg</p>
<p klasse="AL_Namen">Denise Loop</p>
<p klasse="AL_Namen">Dr. Anna Lührmann</p>
<p klasse="AL_Namen">Dr.-Ing. Zoe Mayer</p>
<p klasse="AL_Namen">Dr. Irene Mihalic</p>
<p klasse="AL_Namen">Claudia Müller</p>
<p klasse="AL_Namen">Sascha Müller</p>
<p klasse="AL_Namen">Dr. Ingrid Nestle</p>
<p klasse="AL_Namen">Dr. Ophelia Nick</p>
<p klasse="AL_Namen">Karoline Otte</p>
<p klasse="AL_Namen">Julian Pahlke</p>
<p klasse="AL_Namen">Lisa Paus</p>
<p klasse="AL_Namen">Dr. Paula Piechotta</p>
<p klasse="AL_Namen">Tabea Rößner</p>
<p klasse="AL_Namen">Dr. Manuela Rottmann</p>
<p klasse="AL_Namen">Stefan Schmidt</p>
<p klasse="AL_Namen">Marlene Schönberger</p>
<p klasse="AL_Namen">Christina-Johanne Schröder</p>
<p klasse="AL_Namen">Dr. Anne Monika Spallek</p>
<p klasse="AL_Namen">Merle Spellerberg</p>
<p klasse="AL_Namen">Nina Stahr</p>
<p klasse="AL_Namen">Dr. Till Steffen</p>
<p klasse="AL_Namen">Hanna Steinmüller</p>
<p klasse="AL_Namen">Kassem Taher Saleh</p>
<p klasse="AL_Namen">Awet Tesfaiesus</p>
<p klasse="AL_Namen">Jürgen Trittin</p>
<p klasse="AL_Namen">Dr. Julia Verlinden</p>
<p klasse="AL_Namen">Niklas Wagener</p>
<p klasse="AL_Namen">Robin Wagener</p>
<p klasse="AL_Namen">Saskia Weishaupt</p>
<p klasse="AL_Namen">Tina Winklmann</p>
<p klasse="AL_Partei">FDP</p>
<p klasse="AL_Namen">Valentin Abel</p>
<p klasse="AL_Namen">Muhanad Al-Halak</p>
<p klasse="AL_Namen">Christine Aschenberg-Dugnus</p>
<p klasse="AL_Namen">Nicole Bauer</p>
<p klasse="AL_Namen">Friedhelm Boginski</p>
<p klasse="AL_Namen">Mario Brandenburg (Südpfalz)</p>
<p klasse="AL_Namen">Bijan Djir-Sarai</p>
<p klasse="AL_Namen">Otto Fricke</p>
<p klasse="AL_Namen">Maximilian Funke-Kaiser</p>
<p klasse="AL_Namen">Martin Gassner-Herz</p>
<p klasse="AL_Namen">Knut Gerschau</p>
<p klasse="AL_Namen">Anikó Glogowski-Merten</p>
<p klasse="AL_Namen">Nils Gründer</p>
<p klasse="AL_Namen">Reginald Hanke</p>
<p klasse="AL_Namen">Philipp Hartewig</p>
<p klasse="AL_Namen">Ulrike Harzer</p>
<p klasse="AL_Namen">Peter Heidt</p>
<p klasse="AL_Namen">Katrin Helling-Plahr</p>
<p klasse="AL_Namen">Markus Herbrand</p>
<p klasse="AL_Namen">Torsten Herbst</p>
<p klasse="AL_Namen">Katja Hessel</p>
<p klasse="AL_Namen">Dr. Gero Clemens Hocker</p>
<p klasse="AL_Namen">Dr. Christoph Hoffmann</p>
<p klasse="AL_Namen">Reinhard Houben</p>
<p klasse="AL_Namen">Olaf In der Beek</p>
<p klasse="AL_Namen">Gyde Jensen</p>
<p klasse="AL_Namen">Karsten Klein</p>
<p klasse="AL_Namen">Daniela Kluckert</p>
<p klasse="AL_Namen">Dr. Lukas Köhler</p>
<p klasse="AL_Namen">Michael Kruse</p>
<p klasse="AL_Namen">Wolfgang Kubicki</p>
<p klasse="AL_Namen">Konstantin Kuhle</p>
<p klasse="AL_Namen">Jürgen Lenders</p>
<p klasse="AL_Namen">Dr. Thorsten Lieb</p>
<p klasse="AL_Namen">Christian Lindner</p>
<p klasse="AL_Namen">Oliver Luksic</p>
<p klasse="AL_Namen">Kristine Lütke</p>
<p klasse="AL_Namen">Alexander Müller</p>
<p klasse="AL_Namen">Frank Müller-Rosentritt</p>
<p klasse="AL_Namen">Claudia Raffelhüschen</p>
<p klasse="AL_Namen">Bernd Reuther</p>
<p klasse="AL_Namen">Frank Schäffler</p>
<p klasse="AL_Namen">Ria Schröder</p>
<p klasse="AL_Namen">Anja Schulz</p>
<p klasse="AL_Namen">Dr. Marie-Agnes Strack-Zimmermann</p>
<p klasse="AL_Namen">Jens Teutrine</p>
<p klasse="AL_Namen">Stephan Thomae</p>
<p klasse="AL_Namen">Manfred Todtenhausen</p>
<p klasse="AL_Namen">Gerald Ullrich</p>
<p klasse="AL_Namen">Johannes Vogel</p>
<p klasse="AL_Namen">Sandra Weeser</p>
<p klasse="AL_Namen">Nicole Westig</p>
<p klasse="AL_Partei">AfD</p>
<p klasse="AL_Namen">Dr. Christina Baum</p>
<p klasse="AL_Namen">Dr. Bernd Baumann</p>
<p klasse="AL_Namen">Roger Beckamp</p>
<p klasse="AL_Namen">Marc Bernhard</p>
<p klasse="AL_Namen">Andreas Bleck</p>
<p klasse="AL_Namen">René Bochmann</p>
<p klasse="AL_Namen">Peter Boehringer</p>
<p klasse="AL_Namen">Gereon Bollmann</p>
<p klasse="AL_Namen">Dirk Brandes</p>
<p klasse="AL_Namen">Stephan Brandner</p>
<p klasse="AL_Namen">Jürgen Braun</p>
<p klasse="AL_Namen">Marcus Bühl</p>
<p klasse="AL_Namen">Petr Bystron</p>
<p klasse="AL_Namen">Dr. Gottfried Curio</p>
<p klasse="AL_Namen">Thomas Dietz</p>
<p klasse="AL_Namen">Thomas Ehrhorn</p>
<p klasse="AL_Namen">Dr. Michael Espendiller</p>
<p klasse="AL_Namen">Peter Felser</p>
<p klasse="AL_Namen">Dietmar Friedhoff</p>
<p klasse="AL_Namen">Dr. Götz Frömming</p>
<p klasse="AL_Namen">Hannes Gnauck</p>
<p klasse="AL_Namen">Kay Gottschalk</p>
<p klasse="AL_Namen">Mariana Iris Harder-Kühnel</p>
<p klasse="AL_Namen">Jochen Haug</p>
<p klasse="AL_Namen">Martin Hess</p>
<p klasse="AL_Namen">Karsten Hilse</p>
<p klasse="AL_Namen">Nicole Höchst</p>
<p klasse="AL_Namen">Leif-Erik Holm</p>
<p klasse="AL_Namen">Gerrit Huy</p>
<p klasse="AL_Namen">Steffen Janich</p>
<p klasse="AL_Namen">Dr. Marc Jongen</p>
<p klasse="AL_Namen">Dr. Malte Kaufmann</p>
<p klasse="AL_Namen">Dr. Michael Kaufmann</p>
<p klasse="AL_Namen">Stefan Keuter</p>
<p klasse="AL_Namen">Norbert Kleinwächter</p>
<p klasse="AL_Namen">Enrico Komning</p>
<p klasse="AL_Namen">Jörn König</p>
<p klasse="AL_Namen">Steffen Kotré</p>
<p klasse="AL_Namen">Dr. Rainer Kraft</p>
<p klasse="AL_Namen">Rüdiger Lucassen</p>
<p klasse="AL_Namen">Mike Moncsek</p>
<p klasse="AL_Namen">Matthias Moosdorf</p>
<p klasse="AL_Namen">Edgar Naujok</p>
<p klasse="AL_Namen">Gerold Otten</p>
<p klasse="AL_Namen">Jürgen Pohl</p>
<p klasse="AL_Namen">Stephan Protschka</p>
<p klasse="AL_Namen">Martin Erwin Renner</p>
<p klasse="AL_Namen">Frank Rinck</p>
<p klasse="AL_Namen">Dr. Rainer Rothfuß</p>
<p klasse="AL_Namen">Bernd Schattner</p>
<p klasse="AL_Namen">Ulrike Schielke-Ziesing</p>
<p klasse="AL_Namen">Eugen Schmidt</p>
<p klasse="AL_Namen">Jan Wenzel Schmidt</p>
<p klasse="AL_Namen">Jörg Schneider</p>
<p klasse="AL_Namen">Thomas Seitz</p>
<p klasse="AL_Namen">Martin Sichert</p>
<p klasse="AL_Namen">Dr. Dirk Spaniel</p>
<p klasse="AL_Namen">Klaus Stöber</p>
<p klasse="AL_Namen">Beatrix von Storch</p>
<p klasse="AL_Namen">Dr. Harald Weyel</p>
<p klasse="AL_Namen">Wolfgang Wiehle</p>
<p klasse="AL_Namen">Dr. Christian Wirth</p>
<p klasse="AL_Namen">Kay-Uwe Ziegler</p>
<p klasse="AL_Partei">DIE LINKE</p>
<p klasse="AL_Namen">Ali Al-Dailami</p>
<p klasse="AL_Namen">Dr. Dietmar Bartsch</p>
<p klasse="AL_Namen">Matthias W. Birkwald</p>
<p klasse="AL_Namen">Anke Domscheit-Berg</p>
<p klasse="AL_Namen">Susanne Ferschl</p>
<p klasse="AL_Namen">Nicole Gohlke</p>
<p klasse="AL_Namen">Christian Görke</p>
<p klasse="AL_Namen">Dr. Gregor Gysi</p>
<p klasse="AL_Namen">Susanne Hennig-Wellsow</p>
<p klasse="AL_Namen">Andrej Hunko</p>
<p klasse="AL_Namen">Ina Latendorf</p>
<p klasse="AL_Namen">Caren Lay</p>
<p klasse="AL_Namen">Ralph Lenkert</p>
<p klasse="AL_Namen">Christian Leye</p>
<p klasse="AL_Namen">Dr. Gesine Lötzsch</p>
<p klasse="AL_Namen">Thomas Lutze</p>
<p klasse="AL_Namen">Cornelia Möhring</p>
<p klasse="AL_Namen">Zaklin Nastic</p>
<p klasse="AL_Namen">Sören Pellmann</p>
<p klasse="AL_Namen">Heidi Reichinnek</p>
<p klasse="AL_Namen">Bernd Riexinger</p>
<p klasse="AL_Namen">Dr. Petra Sitte</p>
<p klasse="AL_Namen">Alexander Ulrich</p>
<p klasse="AL_Namen">Dr. Sahra Wagenknecht</p>
<p klasse="AL_Namen">Janine Wissler</p>
<p klasse="AL_Partei">Fraktionslos</p>
<p klasse="AL_Namen">Joana Cotar</p>
<p klasse="AL_Namen">Robert Farle</p>
<p klasse="AL_Namen">Stefan Seidler</p>
<p klasse="AL_Ja-Nein-Enth">Enthalten</p>
<p klasse="AL_Partei">SPD</p>
<p klasse="AL_Namen">Katrin Budde</p>
<p klasse="AL_Namen">Macit Karaahmetoğlu</p>
<p klasse="AL_Namen">Andreas Larem</p>
<p klasse="AL_Namen">Claudia Moll</p>
<p klasse="AL_Namen">Michael Müller</p>
<p klasse="AL_Namen">Marianne Schieder</p>
<p klasse="AL_Partei">CDU/CSU</p>
<p klasse="AL_Namen">Martina Englhardt-Kopf</p>
<p klasse="AL_Namen">Hubert Hüppe</p>
<p klasse="AL_Namen">Dr. Mathias Middelberg</p>
<p klasse="AL_Namen">Dr. Norbert Röttgen</p>
<p klasse="AL_Namen">Dr. Wolfgang Schäuble</p>
<p klasse="AL_Namen">Armin Schwarz</p>
<p klasse="AL_Namen">Kerstin Vieregge</p>
<p klasse="AL_Namen">Christoph de Vries</p>
<p klasse="AL_Namen">Sabine Weiss (Wesel I)</p>
<p klasse="AL_Namen">Tobias Winkler</p>
<p klasse="AL_Partei">BÜNDNIS 90/ DIE GRÜNEN</p>
<p klasse="AL_Namen">Chantal Kopf</p>
<p klasse="AL_Partei">FDP</p>
<p klasse="AL_Namen">Ingo Bodtke</p>
<p klasse="AL_Namen">Karlheinz Busen</p>
<p klasse="AL_Partei">AfD</p>
<p klasse="AL_Namen">Tino Chrupalla</p>
<p klasse="AL_Namen">Dr. Alice Weidel</p>
<p klasse="AL_Partei">Fraktionslos</p>
<p klasse="AL_Namen">Matthias Helferich</p>
<p klasse="AL_Namen">Johannes Huber</p>
<p klasse="J">Wir kommen zur zweiten Beratung der im Ausschuss zusammengeführten Gesetzentwürfe der Abgeordneten Katrin Helling-Plahr, Dr. Petra Sitte, Helge Lindh und weiterer Abgeordneter zur Regelung der Suizidhilfe und der Abgeordneten Renate Künast, Dr. Nina Scheer, Katja Keul und weiterer Abgeordneter zum Schutz des Rechts auf selbstbestimmtes Sterben und zur Änderung weiterer Gesetze in der Ausschussfassung mit dem neuen Titel „Entwurf eines Gesetzes zum Schutz des Rechts auf selbstbestimmtes Sterben und zur Regelung der Hilfe zur Selbsttötung sowie zur Änderung weiterer Gesetze“.</p>
<p klasse="J">Der Rechtsausschuss hat in seiner Beschlussempfehlung auf Drucksache 20/7624 unter Buchstabe b empfohlen, die Gesetzentwürfe auf den Drucksachen 20/2332 und 20/2293 zusammenzuführen und im Plenum einen Beschluss über die vorgelegte Ausschussfassung herbeizuführen, selbst aber keine inhaltliche Empfehlung abgegeben.</p>
<p klasse="J">Die Abstimmung erfolgt wieder namentlich. – Die Urnen sind besetzt, höre ich. Dann eröffne ich die namentliche Abstimmung über den zusammengeführten Gesetzentwurf der Abgeordneten Helling-Plahr, Künast und weiterer Abgeordneter.<sup>1</sup>
<fussnote>Ergebnis Seite 14100 D</fussnote>
</p>
<p klasse="J">Ist ein Mitglied des Hauses anwesend, das seine Stimme noch nicht abgegeben hat? – Dann bitte ich darum, die Stimme jetzt abzugeben.</p>
<p klasse="J">Ich bekomme die Information, dass alle Abgeordneten ihre Stimme abgegeben haben. Dann schließe ich die Abstimmung. Ich bitte die Schriftführerinnen und Schriftführer, mit der Auszählung zu beginnen. Bis das Ergebnis vorliegt, unterbreche ich die Sitzung.</p>
<kommentar>(Unterbrechung von 11.18 bis 11.25 Uhr)</kommentar>
<name>Vizepräsidentin Yvonne Magwas:</name>
<p klasse="J_1">Ich eröffne die Sitzung wieder.</p>
<p klasse="J">Mir liegt das von den Schriftführerinnen und Schriftführern ermittelte Ergebnis der namentlichen Abstimmung über die zusammengeführten Gesetzentwürfe mit dem neuen Titel „Entwurf eines Gesetzes zum Schutz des Rechts auf selbstbestimmtes Sterben und zur Regelung der Hilfe zur Selbsttötung sowie zur Änderung weiterer Gesetze“ vor: abgegebene Stimmkarten 682. Mit Ja haben gestimmt 287, mit Nein haben gestimmt 375, </p>
<kommentar>(Beifall bei Abgeordneten der AfD)</kommentar>
<p klasse="O">Enthaltungen gab es 20. Der Gesetzentwurf „Helling-Plahr/Künast“ ist damit in zweiter Beratung abgelehnt. Damit entfällt nach unserer Geschäftsordnung die weitere Beratung.<sup>1</sup>
<fussnote>Anlage 10 </fussnote>
</p>
<p klasse="AL_Vorspann_1">Endgültiges Ergebnis</p>
<p klasse="AL_Vorspann_2">Abgegebene Stimmen:681;</p>
<p klasse="AL_Vorspann_2">davon</p>
<p klasse="AL_Vorspann_3">ja:286</p>
<p klasse="AL_Vorspann_3">nein:375</p>
<p klasse="AL_Vorspann_3">enthalten:20</p>
<p klasse="AL_Ja-Nein-Enth">Ja</p>
<p klasse="AL_Partei">SPD</p>
<p klasse="AL_Namen">Sanae Abdi</p>
<p klasse="AL_Namen">Adis Ahmetovic</p>
<p klasse="AL_Namen">Ulrike Bahr</p>
<p klasse="AL_Namen">Bärbel Bas</p>
<p klasse="AL_Namen">Dr. Holger Becker</p>
<p klasse="AL_Namen">Bengt Bergt</p>
<p klasse="AL_Namen">Jakob Blankenburg</p>
<p klasse="AL_Namen">Leni Breymaier</p>
<p klasse="AL_Namen">Katrin Budde</p>
<p klasse="AL_Namen">Isabel Cademartori Dujisin</p>
<p klasse="AL_Namen">Bernhard Daldrup</p>
<p klasse="AL_Namen">Dr. Daniela De Ridder</p>
<p klasse="AL_Namen">Hakan Demir</p>
<p klasse="AL_Namen">Dr. Karamba Diaby</p>
<p klasse="AL_Namen">Martin Diedenhofen</p>
<p klasse="AL_Namen">Jan Dieren</p>
<p klasse="AL_Namen">Esther Dilcher</p>
<p klasse="AL_Namen">Falko Droßmann</p>
<p klasse="AL_Namen">Axel Echeverria</p>
<p klasse="AL_Namen">Sonja Eichwede</p>
<p klasse="AL_Namen">Heike Engelhardt</p>
<p klasse="AL_Namen">Dr. Wiebke Esdar</p>
<p klasse="AL_Namen">Saskia Esken</p>
<p klasse="AL_Namen">Ariane Fäscher</p>
<p klasse="AL_Namen">Dr. Edgar Franke</p>
<p klasse="AL_Namen">Fabian Funke</p>
<p klasse="AL_Namen">Manuel Gava</p>
<p klasse="AL_Namen">Michael Gerdes</p>
<p klasse="AL_Namen">Timon Gremmels</p>
<p klasse="AL_Namen">Bettina Hagedorn</p>
<p klasse="AL_Namen">Rita Hagl-Kehl</p>
<p klasse="AL_Namen">Metin Hakverdi</p>
<p klasse="AL_Namen">Sebastian Hartmann</p>
<p klasse="AL_Namen">Dirk Heidenblut</p>
<p klasse="AL_Namen">Gabriela Heinrich</p>
<p klasse="AL_Namen">Wolfgang Hellmich</p>
<p klasse="AL_Namen">Anke Hennig</p>
<p klasse="AL_Namen">Thomas Hitschler</p>
<p klasse="AL_Namen">Jasmina Hostert</p>
<p klasse="AL_Namen">Verena Hubertz</p>
<p klasse="AL_Namen">Markus Hümpfer</p>
<p klasse="AL_Namen">Frank Junge</p>
<p klasse="AL_Namen">Elisabeth Kaiser</p>
<p klasse="AL_Namen">Carlos Kasper</p>
<p klasse="AL_Namen">Anna Kassautzki</p>
<p klasse="AL_Namen">Gabriele Katzmarek</p>
<p klasse="AL_Namen">Helmut Kleebank</p>
<p klasse="AL_Namen">Annika Klose</p>
<p klasse="AL_Namen">Tim Klüssendorf</p>
<p klasse="AL_Namen">Dr. Bärbel Kofler</p>
<p klasse="AL_Namen">Simona Koß</p>
<p klasse="AL_Namen">Anette Kramme</p>
<p klasse="AL_Namen">Dunja Kreiser</p>
<p klasse="AL_Namen">Martin Kröber</p>
<p klasse="AL_Namen">Kevin Kühnert</p>
<p klasse="AL_Namen">Andreas Larem</p>
<p klasse="AL_Namen">Esra Limbacher</p>
<p klasse="AL_Namen">Helge Lindh</p>
<p klasse="AL_Namen">Isabel Mackensen-Geis</p>
<p klasse="AL_Namen">Erik von Malottki</p>
<p klasse="AL_Namen">Holger Mann</p>
<p klasse="AL_Namen">Kaweh Mansoori</p>
<p klasse="AL_Namen">Dr. Zanda Martens</p>
<p klasse="AL_Namen">Dorothee Martin</p>
<p klasse="AL_Namen">Franziska Mascheck</p>
<p klasse="AL_Namen">Andreas Mehltretter</p>
<p klasse="AL_Namen">Dr. Matthias Miersch</p>
<p klasse="AL_Namen">Matthias David Mieves</p>
<p klasse="AL_Namen">Susanne Mittag</p>
<p klasse="AL_Namen">Siemtje Möller</p>
<p klasse="AL_Namen">Michael Müller</p>
<p klasse="AL_Namen">Detlef Müller (Chemnitz)</p>
<p klasse="AL_Namen">Rasha Nasr</p>
<p klasse="AL_Namen">Brian Nickholz</p>
<p klasse="AL_Namen">Josephine Ortleb</p>
<p klasse="AL_Namen">Dr. Christos Pantazis</p>
<p klasse="AL_Namen">Wiebke Papenbrock</p>
<p klasse="AL_Namen">Natalie Pawlik</p>
<p klasse="AL_Namen">Jens Peick</p>
<p klasse="AL_Namen">Christian Petry</p>
<p klasse="AL_Namen">Jan Plobner</p>
<p klasse="AL_Namen">Sabine Poschmann</p>
<p klasse="AL_Namen">Ye-One Rhie</p>
<p klasse="AL_Namen">Daniel Rinkert</p>
<p klasse="AL_Namen">Sönke Rix</p>
<p klasse="AL_Namen">Dennis Rohde</p>
<p klasse="AL_Namen">Sebastian Roloff</p>
<p klasse="AL_Namen">Michael Roth (Heringen)</p>
<p klasse="AL_Namen">Tina Rudolph</p>
<p klasse="AL_Namen">Johann Saathoff</p>
<p klasse="AL_Namen">Axel Schäfer (Bochum)</p>
<p klasse="AL_Namen">Rebecca Schamber</p>
<p klasse="AL_Namen">Dr. Nina Scheer</p>
<p klasse="AL_Namen">Christoph Schmid</p>
<p klasse="AL_Namen">Uwe Schmidt</p>
<p klasse="AL_Namen">Daniel Schneider</p>
<p klasse="AL_Namen">Carsten Schneider (Erfurt)</p>
<p klasse="AL_Namen">Johannes Schraps</p>
<p klasse="AL_Namen">Svenja Schulze</p>
<p klasse="AL_Namen">Andreas Schwarz</p>
<p klasse="AL_Namen">Svenja Stadler</p>
<p klasse="AL_Namen">Martina Stamm-Fibich</p>
<p klasse="AL_Namen">Mathias Stein</p>
<p klasse="AL_Namen">Nadja Sthamer</p>
<p klasse="AL_Namen">Ruppert Stüwe</p>
<p klasse="AL_Namen">Claudia Tausend</p>
<p klasse="AL_Namen">Michael Thews</p>
<p klasse="AL_Namen">Markus Töns</p>
<p klasse="AL_Namen">Carsten Träger</p>
<p klasse="AL_Namen">Ana-Maria Trasnea</p>
<p klasse="AL_Namen">Derya Türk-Nachbaur</p>
<p klasse="AL_Namen">Frank Ullrich</p>
<p klasse="AL_Namen">Marja-Liisa Völlers</p>
<p klasse="AL_Namen">Emily Vontz</p>
<p klasse="AL_Namen">Dirk Vöpel</p>
<p klasse="AL_Namen">Dr. Carolin Wagner</p>
<p klasse="AL_Namen">Hannes Walter</p>
<p klasse="AL_Namen">Carmen Wegge</p>
<p klasse="AL_Namen">Melanie Wegling</p>
<p klasse="AL_Namen">Lena Werner</p>
<p klasse="AL_Namen">Bernd Westphal</p>
<p klasse="AL_Namen">Dirk Wiese</p>
<p klasse="AL_Namen">Dr. Herbert Wollmann</p>
<p klasse="AL_Namen">Stefan Zierke</p>
<p klasse="AL_Namen">Armand Zorn</p>
<p klasse="AL_Namen">Katrin Zschau</p>
<p klasse="AL_Partei">CDU/CSU</p>
<p klasse="AL_Namen">Mark Helfrich</p>
<p klasse="AL_Namen">Roderich Kiesewetter</p>
<p klasse="AL_Namen">Jens Koeppen</p>
<p klasse="AL_Partei">BÜNDNIS 90/ DIE GRÜNEN</p>
<p klasse="AL_Namen">Luise Amtsberg</p>
<p klasse="AL_Namen">Andreas Audretsch</p>
<p klasse="AL_Namen">Maik Außendorf</p>
<p klasse="AL_Namen">Tobias B. Bacherle</p>
<p klasse="AL_Namen">Felix Banaszak</p>
<p klasse="AL_Namen">Karl Bär</p>
<p klasse="AL_Namen">Canan Bayram</p>
<p klasse="AL_Namen">Lukas Benner</p>
<p klasse="AL_Namen">Dr. Franziska Brantner</p>
<p klasse="AL_Namen">Dr. Sandra Detzer</p>
<p klasse="AL_Namen">Katharina Dröge</p>
<p klasse="AL_Namen">Deborah Düring</p>
<p klasse="AL_Namen">Harald Ebner</p>
<p klasse="AL_Namen">Marcel Emmerich</p>
<p klasse="AL_Namen">Emilia Fester</p>
<p klasse="AL_Namen">Schahina Gambir</p>
<p klasse="AL_Namen">Matthias Gastel</p>
<p klasse="AL_Namen">Kai Gehring</p>
<p klasse="AL_Namen">Stefan Gelbhaar</p>
<p klasse="AL_Namen">Dr. Jan-Niclas Gesenhues</p>
<p klasse="AL_Namen">Sabine Grützmacher</p>
<p klasse="AL_Namen">Dr. Robert Habeck</p>
<p klasse="AL_Namen">Britta Haßelmann</p>
<p klasse="AL_Namen">Linda Heitmann</p>
<p klasse="AL_Namen">Kathrin Henneberger</p>
<p klasse="AL_Namen">Dr. Bettina Hoffmann</p>
<p klasse="AL_Namen">Bruno Hönel</p>
<p klasse="AL_Namen">Dieter Janecek</p>
<p klasse="AL_Namen">Katja Keul</p>
<p klasse="AL_Namen">Misbah Khan</p>
<p klasse="AL_Namen">Philip Krämer</p>
<p klasse="AL_Namen">Renate Künast</p>
<p klasse="AL_Namen">Ricarda Lang</p>
<p klasse="AL_Namen">Sven Lehmann</p>
<p klasse="AL_Namen">Anja Liebert</p>
<p klasse="AL_Namen">Helge Limburg</p>
<p klasse="AL_Namen">Denise Loop</p>
<p klasse="AL_Namen">Dr. Anna Lührmann</p>
<p klasse="AL_Namen">Dr.-Ing. Zoe Mayer</p>
<p klasse="AL_Namen">Susanne Menge</p>
<p klasse="AL_Namen">Dr. Irene Mihalic</p>
<p klasse="AL_Namen">Claudia Müller</p>
<p klasse="AL_Namen">Sascha Müller</p>
<p klasse="AL_Namen">Dr. Ingrid Nestle</p>
<p klasse="AL_Namen">Dr. Ophelia Nick</p>
<p klasse="AL_Namen">Karoline Otte</p>
<p klasse="AL_Namen">Julian Pahlke</p>
<p klasse="AL_Namen">Lisa Paus</p>
<p klasse="AL_Namen">Dr. Paula Piechotta</p>
<p klasse="AL_Namen">Tabea Rößner</p>
<p klasse="AL_Namen">Dr. Manuela Rottmann</p>
<p klasse="AL_Namen">Stefan Schmidt</p>
<p klasse="AL_Namen">Marlene Schönberger</p>
<p klasse="AL_Namen">Christina-Johanne Schröder</p>
<p klasse="AL_Namen">Kordula Schulz-Asche</p>
<p klasse="AL_Namen">Dr. Anne Monika Spallek</p>
<p klasse="AL_Namen">Merle Spellerberg</p>
<p klasse="AL_Namen">Nina Stahr</p>
<p klasse="AL_Namen">Dr. Till Steffen</p>
<p klasse="AL_Namen">Hanna Steinmüller</p>
<p klasse="AL_Namen">Kassem Taher Saleh</p>
<p klasse="AL_Namen">Jürgen Trittin</p>
<p klasse="AL_Namen">Dr. Julia Verlinden</p>
<p klasse="AL_Namen">Niklas Wagener</p>
<p klasse="AL_Namen">Robin Wagener</p>
<p klasse="AL_Namen">Saskia Weishaupt</p>
<p klasse="AL_Namen">Tina Winklmann</p>
<p klasse="AL_Partei">FDP</p>
<p klasse="AL_Namen">Valentin Abel</p>
<p klasse="AL_Namen">Muhanad Al-Halak</p>
<p klasse="AL_Namen">Christine Aschenberg-Dugnus</p>
<p klasse="AL_Namen">Nicole Bauer</p>
<p klasse="AL_Namen">Friedhelm Boginski</p>
<p klasse="AL_Namen">Mario Brandenburg (Südpfalz)</p>
<p klasse="AL_Namen">Bijan Djir-Sarai</p>
<p klasse="AL_Namen">Otto Fricke</p>
<p klasse="AL_Namen">Maximilian Funke-Kaiser</p>
<p klasse="AL_Namen">Martin Gassner-Herz</p>
<p klasse="AL_Namen">Knut Gerschau</p>
<p klasse="AL_Namen">Anikó Glogowski-Merten</p>
<p klasse="AL_Namen">Nils Gründer</p>
<p klasse="AL_Namen">Reginald Hanke</p>
<p klasse="AL_Namen">Philipp Hartewig</p>
<p klasse="AL_Namen">Ulrike Harzer</p>
<p klasse="AL_Namen">Peter Heidt</p>
<p klasse="AL_Namen">Katrin Helling-Plahr</p>
<p klasse="AL_Namen">Markus Herbrand</p>
<p klasse="AL_Namen">Torsten Herbst</p>
<p klasse="AL_Namen">Katja Hessel</p>
<p klasse="AL_Namen">Dr. Gero Clemens Hocker</p>
<p klasse="AL_Namen">Dr. Christoph Hoffmann</p>
<p klasse="AL_Namen">Reinhard Houben</p>
<p klasse="AL_Namen">Olaf In der Beek</p>
<p klasse="AL_Namen">Gyde Jensen</p>
<p klasse="AL_Namen">Karsten Klein</p>
<p klasse="AL_Namen">Daniela Kluckert</p>
<p klasse="AL_Namen">Dr. Lukas Köhler</p>
<p klasse="AL_Namen">Michael Kruse</p>
<p klasse="AL_Namen">Wolfgang Kubicki</p>
<p klasse="AL_Namen">Konstantin Kuhle</p>
<p klasse="AL_Namen">Ulrich Lechte</p>
<p klasse="AL_Namen">Jürgen Lenders</p>
<p klasse="AL_Namen">Dr. Thorsten Lieb</p>
<p klasse="AL_Namen">Christian Lindner</p>
<p klasse="AL_Namen">Oliver Luksic</p>
<p klasse="AL_Namen">Kristine Lütke</p>
<p klasse="AL_Namen">Alexander Müller</p>
<p klasse="AL_Namen">Frank Müller-Rosentritt</p>
<p klasse="AL_Namen">Claudia Raffelhüschen</p>
<p klasse="AL_Namen">Bernd Reuther</p>
<p klasse="AL_Namen">Frank Schäffler</p>
<p klasse="AL_Namen">Ria Schröder</p>
<p klasse="AL_Namen">Anja Schulz</p>
<p klasse="AL_Namen">Dr. Marie-Agnes Strack-Zimmermann</p>
<p klasse="AL_Namen">Jens Teutrine</p>
<p klasse="AL_Namen">Stephan Thomae</p>
<p klasse="AL_Namen">Manfred Todtenhausen</p>
<p klasse="AL_Namen">Gerald Ullrich</p>
<p klasse="AL_Namen">Johannes Vogel</p>
<p klasse="AL_Namen">Sandra Weeser</p>
<p klasse="AL_Namen">Nicole Westig</p>
<p klasse="AL_Partei">AfD</p>
<p klasse="AL_Namen">Roger Beckamp</p>
<p klasse="AL_Namen">Dirk Brandes</p>
<p klasse="AL_Namen">Thomas Ehrhorn</p>
<p klasse="AL_Namen">Kay Gottschalk</p>
<p klasse="AL_Namen">Karsten Hilse</p>
<p klasse="AL_Namen">Ulrike Schielke-Ziesing</p>
<p klasse="AL_Namen">Jan Wenzel Schmidt</p>
<p klasse="AL_Partei">DIE LINKE</p>
<p klasse="AL_Namen">Ali Al-Dailami</p>
<p klasse="AL_Namen">Dr. Dietmar Bartsch</p>
<p klasse="AL_Namen">Matthias W. Birkwald</p>
<p klasse="AL_Namen">Clara Bünger</p>
<p klasse="AL_Namen">Anke Domscheit-Berg</p>
<p klasse="AL_Namen">Susanne Ferschl</p>
<p klasse="AL_Namen">Nicole Gohlke</p>
<p klasse="AL_Namen">Christian Görke</p>
<p klasse="AL_Namen">Dr. Gregor Gysi</p>
<p klasse="AL_Namen">Dr. André Hahn</p>
<p klasse="AL_Namen">Susanne Hennig-Wellsow</p>
<p klasse="AL_Namen">Andrej Hunko</p>
<p klasse="AL_Namen">Jan Korte</p>
<p klasse="AL_Namen">Caren Lay</p>
<p klasse="AL_Namen">Ralph Lenkert</p>
<p klasse="AL_Namen">Christian Leye</p>
<p klasse="AL_Namen">Dr. Gesine Lötzsch</p>
<p klasse="AL_Namen">Thomas Lutze</p>
<p klasse="AL_Namen">Amira Mohamed Ali</p>
<p klasse="AL_Namen">Cornelia Möhring</p>
<p klasse="AL_Namen">Zaklin Nastic</p>
<p klasse="AL_Namen">Sören Pellmann</p>
<p klasse="AL_Namen">Heidi Reichinnek</p>
<p klasse="AL_Namen">Bernd Riexinger</p>
<p klasse="AL_Namen">Dr. Petra Sitte</p>
<p klasse="AL_Namen">Alexander Ulrich</p>
<p klasse="AL_Namen">Dr. Sahra Wagenknecht</p>
<p klasse="AL_Namen">Janine Wissler</p>
<p klasse="AL_Partei">Fraktionslos</p>
<p klasse="AL_Namen">Joana Cotar</p>
<p klasse="AL_Namen">Stefan Seidler</p>
<p klasse="AL_Ja-Nein-Enth">Nein</p>
<p klasse="AL_Partei">SPD</p>
<p klasse="AL_Namen">Dagmar Andres</p>
<p klasse="AL_Namen">Niels Annen</p>
<p klasse="AL_Namen">Heike Baehrens</p>
<p klasse="AL_Namen">Daniel Baldy</p>
<p klasse="AL_Namen">Nezahat Baradari</p>
<p klasse="AL_Namen">Sören Bartol</p>
<p klasse="AL_Namen">Alexander Bartz</p>
<p klasse="AL_Namen">Jürgen Berghahn</p>
<p klasse="AL_Namen">Dr. Lars Castellucci</p>
<p klasse="AL_Namen">Jürgen Coße</p>
<p klasse="AL_Namen">Sabine Dittmar</p>
<p klasse="AL_Namen">Dr. Johannes Fechner</p>
<p klasse="AL_Namen">Sebastian Fiedler</p>
<p klasse="AL_Namen">Martin Gerster</p>
<p klasse="AL_Namen">Angelika Glöckner</p>
<p klasse="AL_Namen">Kerstin Griese</p>
<p klasse="AL_Namen">Uli Grötsch</p>
<p klasse="AL_Namen">Hubertus Heil (Peine)</p>
<p klasse="AL_Namen">Frauke Heiligenstadt</p>
<p klasse="AL_Namen">Josip Juratovic</p>
<p klasse="AL_Namen">Oliver Kaczmarek</p>
<p klasse="AL_Namen">Macit Karaahmetoğlu</p>
<p klasse="AL_Namen">Dr. Franziska Kersten</p>
<p klasse="AL_Namen">Dr. Kristian Klinck</p>
<p klasse="AL_Namen">Lars Klingbeil</p>
<p klasse="AL_Namen">Sarah Lahrkamp</p>
<p klasse="AL_Namen">Kevin Leiser</p>
<p klasse="AL_Namen">Luiza Licina-Bode</p>
<p klasse="AL_Namen">Bettina Lugk</p>
<p klasse="AL_Namen">Dr. Tanja Machalet</p>
<p klasse="AL_Namen">Parsa Marvi</p>
<p klasse="AL_Namen">Katja Mast</p>
<p klasse="AL_Namen">Takis Mehmet Ali</p>
<p klasse="AL_Namen">Dirk-Ulrich Mende</p>
<p klasse="AL_Namen">Kathrin Michel</p>
<p klasse="AL_Namen">Claudia Moll</p>
<p klasse="AL_Namen">Michelle Müntefering</p>
<p klasse="AL_Namen">Dietmar Nietan</p>
<p klasse="AL_Namen">Jörg Nürnberger</p>
<p klasse="AL_Namen">Lennard Oehl</p>
<p klasse="AL_Namen">Mahmut Özdemir (Duisburg)</p>
<p klasse="AL_Namen">Aydan Özoğuz</p>
<p klasse="AL_Namen">Achim Post (Minden)</p>
<p klasse="AL_Namen">Andreas Rimkus</p>
<p klasse="AL_Namen">Dr. Martin Rosemann</p>
<p klasse="AL_Namen">Jessica Rosenthal</p>
<p klasse="AL_Namen">Dr. Thorsten Rudolph</p>
<p klasse="AL_Namen">Bernd Rützel</p>
<p klasse="AL_Namen">Sarah Ryglewski</p>
<p klasse="AL_Namen">Ingo Schäfer</p>
<p klasse="AL_Namen">Johannes Schätzl</p>
<p klasse="AL_Namen">Udo Schiefner</p>
<p klasse="AL_Namen">Peggy Schierenbeck</p>
<p klasse="AL_Namen">Dagmar Schmidt (Wetzlar)</p>
<p klasse="AL_Namen">Christian Schreider</p>
<p klasse="AL_Namen">Dr. Lina Seitzl</p>
<p klasse="AL_Namen">Anja Troff-Schaffarzyk</p>
<p klasse="AL_Namen">Maja Wallstein</p>
<p klasse="AL_Namen">Dr. Joe Weingarten</p>
<p klasse="AL_Namen">Gülistan Yüksel</p>
<p klasse="AL_Namen">Dr. Jens Zimmermann</p>
<p klasse="AL_Partei">CDU/CSU</p>
<p klasse="AL_Namen">Knut Abraham</p>
<p klasse="AL_Namen">Stephan Albani</p>
<p klasse="AL_Namen">Norbert Maria Altenkamp</p>
<p klasse="AL_Namen">Philipp Amthor</p>
<p klasse="AL_Namen">Artur Auernhammer</p>
<p klasse="AL_Namen">Peter Aumer</p>
<p klasse="AL_Namen">Dorothee Bär</p>
<p klasse="AL_Namen">Thomas Bareiß</p>
<p klasse="AL_Namen">Dr. André Berghegger</p>
<p klasse="AL_Namen">Melanie Bernstein</p>
<p klasse="AL_Namen">Peter Beyer</p>
<p klasse="AL_Namen">Marc Biadacz</p>
<p klasse="AL_Namen">Steffen Bilger</p>
<p klasse="AL_Namen">Simone Borchardt</p>
<p klasse="AL_Namen">Michael Brand (Fulda)</p>
<p klasse="AL_Namen">Dr. Helge Braun</p>
<p klasse="AL_Namen">Silvia Breher</p>
<p klasse="AL_Namen">Sebastian Brehm</p>
<p klasse="AL_Namen">Heike Brehmer</p>
<p klasse="AL_Namen">Michael Breilmann</p>
<p klasse="AL_Namen">Ralph Brinkhaus</p>
<p klasse="AL_Namen">Dr. Carsten Brodesser</p>
<p klasse="AL_Namen">Dr. Marlon Bröhr</p>
<p klasse="AL_Namen">Gitta Connemann</p>
<p klasse="AL_Namen">Mario Czaja</p>
<p klasse="AL_Namen">Astrid Damerow</p>
<p klasse="AL_Namen">Alexander Dobrindt</p>
<p klasse="AL_Namen">Michael Donth</p>
<p klasse="AL_Namen">Hansjörg Durz</p>
<p klasse="AL_Namen">Ralph Edelhäußer</p>
<p klasse="AL_Namen">Alexander Engelhard</p>
<p klasse="AL_Namen">Martina Englhardt-Kopf</p>
<p klasse="AL_Namen">Hermann Färber</p>
<p klasse="AL_Namen">Uwe Feiler</p>
<p klasse="AL_Namen">Enak Ferlemann</p>
<p klasse="AL_Namen">Thorsten Frei</p>
<p klasse="AL_Namen">Dr. Hans-Peter Friedrich (Hof)</p>
<p klasse="AL_Namen">Michael Frieser</p>
<p klasse="AL_Namen">Ingo Gädechens</p>
<p klasse="AL_Namen">Dr. Thomas Gebhart</p>
<p klasse="AL_Namen">Dr. Jonas Geissler</p>
<p klasse="AL_Namen">Fabian Gramling</p>
<p klasse="AL_Namen">Hermann Gröhe</p>
<p klasse="AL_Namen">Michael Grosse-Brömer</p>
<p klasse="AL_Namen">Markus Grübel</p>
<p klasse="AL_Namen">Manfred Grund</p>
<p klasse="AL_Namen">Oliver Grundmann</p>
<p klasse="AL_Namen">Monika Grütters</p>
<p klasse="AL_Namen">Serap Güler</p>
<p klasse="AL_Namen">Fritz Güntzler</p>
<p klasse="AL_Namen">Olav Gutting</p>
<p klasse="AL_Namen">Florian Hahn</p>
<p klasse="AL_Namen">Jürgen Hardt</p>
<p klasse="AL_Namen">Matthias Hauer</p>
<p klasse="AL_Namen">Dr. Stefan Heck</p>
<p klasse="AL_Namen">Mechthild Heil</p>
<p klasse="AL_Namen">Marc Henrichmann</p>
<p klasse="AL_Namen">Ansgar Heveling</p>
<p klasse="AL_Namen">Susanne Hierl</p>
<p klasse="AL_Namen">Christian Hirte</p>
<p klasse="AL_Namen">Alexander Hoffmann</p>
<p klasse="AL_Namen">Dr. Hendrik Hoppenstedt</p>
<p klasse="AL_Namen">Franziska Hoppermann</p>
<p klasse="AL_Namen">Hubert Hüppe</p>
<p klasse="AL_Namen">Erich Irlstorfer</p>
<p klasse="AL_Namen">Anne Janssen</p>
<p klasse="AL_Namen">Thomas Jarzombek</p>
<p klasse="AL_Namen">Andreas Jung</p>
<p klasse="AL_Namen">Ingmar Jung</p>
<p klasse="AL_Namen">Anja Karliczek</p>
<p klasse="AL_Namen">Ronja Kemmer</p>
<p klasse="AL_Namen">Michael Kießling</p>
<p klasse="AL_Namen">Dr. Georg Kippels</p>
<p klasse="AL_Namen">Dr. Ottilie Klein</p>
<p klasse="AL_Namen">Volkmar Klein</p>
<p klasse="AL_Namen">Julia Klöckner</p>
<p klasse="AL_Namen">Axel Knoerig</p>
<p klasse="AL_Namen">Anne König</p>
<p klasse="AL_Namen">Markus Koob</p>
<p klasse="AL_Namen">Carsten Körber</p>
<p klasse="AL_Namen">Gunther Krichbaum</p>
<p klasse="AL_Namen">Dr. Günter Krings</p>
<p klasse="AL_Namen">Tilman Kuban</p>
<p klasse="AL_Namen">Ulrich Lange</p>
<p klasse="AL_Namen">Armin Laschet</p>
<p klasse="AL_Namen">Dr. Silke Launert</p>
<p klasse="AL_Namen">Jens Lehmann</p>
<p klasse="AL_Namen">Paul Lehrieder</p>
<p klasse="AL_Namen">Dr. Andreas Lenz</p>
<p klasse="AL_Namen">Andrea Lindholz</p>
<p klasse="AL_Namen">Dr. Carsten Linnemann</p>
<p klasse="AL_Namen">Patricia Lips</p>
<p klasse="AL_Namen">Bernhard Loos</p>
<p klasse="AL_Namen">Dr. Jan-Marco Luczak</p>
<p klasse="AL_Namen">Daniela Ludwig</p>
<p klasse="AL_Namen">Klaus Mack</p>
<p klasse="AL_Namen">Yvonne Magwas</p>
<p klasse="AL_Namen">Andreas Mattfeldt</p>
<p klasse="AL_Namen">Stephan Mayer (Altötting)</p>
<p klasse="AL_Namen">Volker Mayer-Lay</p>
<p klasse="AL_Namen">Dr. Michael Meister</p>
<p klasse="AL_Namen">Friedrich Merz</p>
<p klasse="AL_Namen">Jan Metzler</p>
<p klasse="AL_Namen">Dr. Mathias Middelberg</p>
<p klasse="AL_Namen">Dietrich Monstadt</p>
<p klasse="AL_Namen">Maximilian Mörseburg</p>
<p klasse="AL_Namen">Axel Müller</p>
<p klasse="AL_Namen">Sepp Müller</p>
<p klasse="AL_Namen">Carsten Müller (Braunschweig)</p>
<p klasse="AL_Namen">Stefan Müller (Erlangen)</p>
<p klasse="AL_Namen">Dr. Stefan Nacke</p>
<p klasse="AL_Namen">Petra Nicolaisen</p>
<p klasse="AL_Namen">Wilfried Oellers</p>
<p klasse="AL_Namen">Moritz Oppelt</p>
<p klasse="AL_Namen">Florian Oßner</p>
<p klasse="AL_Namen">Henning Otte</p>
<p klasse="AL_Namen">Stephan Pilsinger</p>
<p klasse="AL_Namen">Dr. Christoph Ploß</p>
<p klasse="AL_Namen">Dr. Martin Plum</p>
<p klasse="AL_Namen">Thomas Rachel</p>
<p klasse="AL_Namen">Kerstin Radomski</p>
<p klasse="AL_Namen">Alexander Radwan</p>
<p klasse="AL_Namen">Alois Rainer</p>
<p klasse="AL_Namen">Dr. Peter Ramsauer</p>
<p klasse="AL_Namen">Henning Rehbaum</p>
<p klasse="AL_Namen">Dr. Markus Reichel</p>
<p klasse="AL_Namen">Josef Rief</p>
<p klasse="AL_Namen">Lars Rohwer</p>
<p klasse="AL_Namen">Dr. Norbert Röttgen</p>
<p klasse="AL_Namen">Stefan Rouenhoff</p>
<p klasse="AL_Namen">Erwin Rüddel</p>
<p klasse="AL_Namen">Albert Rupprecht</p>
<p klasse="AL_Namen">Catarina dos Santos-Wintz</p>
<p klasse="AL_Namen">Dr. Wolfgang Schäuble</p>
<p klasse="AL_Namen">Dr. Christiane Schenderlein</p>
<p klasse="AL_Namen">Andreas Scheuer</p>
<p klasse="AL_Namen">Jana Schimke</p>
<p klasse="AL_Namen">Patrick Schnieder</p>
<p klasse="AL_Namen">Nadine Schön</p>
<p klasse="AL_Namen">Armin Schwarz</p>
<p klasse="AL_Namen">Detlef Seif</p>
<p klasse="AL_Namen">Thomas Silberhorn</p>
<p klasse="AL_Namen">Björn Simon</p>
<p klasse="AL_Namen">Tino Sorge</p>
<p klasse="AL_Namen">Katrin Staffler</p>
<p klasse="AL_Namen">Dr. Wolfgang Stefinger</p>
<p klasse="AL_Namen">Albert Stegemann</p>
<p klasse="AL_Namen">Johannes Steiniger</p>
<p klasse="AL_Namen">Christian Freiherr von Stetten</p>
<p klasse="AL_Namen">Dieter Stier</p>
<p klasse="AL_Namen">Diana Stöcker</p>
<p klasse="AL_Namen">Stephan Stracke</p>
<p klasse="AL_Namen">Max Straubinger</p>
<p klasse="AL_Namen">Christina Stumpp</p>
<p klasse="AL_Namen">Dr. Hermann-Josef Tebroke</p>
<p klasse="AL_Namen">Hans-Jürgen Thies</p>
<p klasse="AL_Namen">Alexander Throm</p>
<p klasse="AL_Namen">Antje Tillmann</p>
<p klasse="AL_Namen">Astrid Timmermann-Fechter</p>
<p klasse="AL_Namen">Markus Uhl</p>
<p klasse="AL_Namen">Dr. Volker Ullrich</p>
<p klasse="AL_Namen">Kerstin Vieregge</p>
<p klasse="AL_Namen">Dr. Oliver Vogt</p>
<p klasse="AL_Namen">Christoph de Vries</p>
<p klasse="AL_Namen">Dr. Johann David Wadephul</p>
<p klasse="AL_Namen">Marco Wanderwitz</p>
<p klasse="AL_Namen">Nina Warken</p>
<p klasse="AL_Namen">Dr. Anja Weisgerber</p>
<p klasse="AL_Namen">Sabine Weiss (Wesel I)</p>
<p klasse="AL_Namen">Kai Whittaker</p>
<p klasse="AL_Namen">Annette Widmann-Mauz</p>
<p klasse="AL_Namen">Dr. Klaus Wiener</p>
<p klasse="AL_Namen">Klaus-Peter Willsch</p>
<p klasse="AL_Namen">Elisabeth Winkelmeier-Becker</p>
<p klasse="AL_Namen">Tobias Winkler</p>
<p klasse="AL_Namen">Mechthilde Wittmann</p>
<p klasse="AL_Namen">Mareike Wulf</p>
<p klasse="AL_Namen">Emmi Zeulner</p>
<p klasse="AL_Namen">Paul Ziemiak</p>
<p klasse="AL_Namen">Nicolas Zippelius</p>
<p klasse="AL_Partei">BÜNDNIS 90/ DIE GRÜNEN</p>
<p klasse="AL_Namen">Stephanie Aeffner</p>
<p klasse="AL_Namen">Lisa Badum</p>
<p klasse="AL_Namen">Annalena Baerbock</p>
<p klasse="AL_Namen">Katharina Beck</p>
<p klasse="AL_Namen">Agnieszka Brugger</p>
<p klasse="AL_Namen">Frank Bsirske</p>
<p klasse="AL_Namen">Dr. Janosch Dahmen</p>
<p klasse="AL_Namen">Ekin Deligöz</p>
<p klasse="AL_Namen">Tessa Ganserer</p>
<p klasse="AL_Namen">Katrin Göring-Eckardt</p>
<p klasse="AL_Namen">Dr. Armin Grau</p>
<p klasse="AL_Namen">Erhard Grundl</p>
<p klasse="AL_Namen">Bernhard Herrmann</p>
<p klasse="AL_Namen">Dr. Anton Hofreiter</p>
<p klasse="AL_Namen">Lamya Kaddor</p>
<p klasse="AL_Namen">Dr. Kirsten Kappert-Gonther</p>
<p klasse="AL_Namen">Sven-Christian Kindler</p>
<p klasse="AL_Namen">Maria Klein-Schmeink</p>
<p klasse="AL_Namen">Christian Kühn (Tübingen)</p>
<p klasse="AL_Namen">Markus Kurth</p>
<p klasse="AL_Namen">Max Lucks</p>
<p klasse="AL_Namen">Swantje Henrike Michaelsen</p>
<p klasse="AL_Namen">Boris Mijatovic</p>
<p klasse="AL_Namen">Beate Müller-Gemmeke</p>
<p klasse="AL_Namen">Dr. Konstantin von Notz</p>
<p klasse="AL_Namen">Omid Nouripour</p>
<p klasse="AL_Namen">Filiz Polat</p>
<p klasse="AL_Namen">Claudia Roth (Augsburg)</p>
<p klasse="AL_Namen">Corinna Rüffer</p>
<p klasse="AL_Namen">Michael Sacher</p>
<p klasse="AL_Namen">Melis Sekmen</p>
<p klasse="AL_Namen">Nyke Slawik</p>
<p klasse="AL_Namen">Awet Tesfaiesus</p>
<p klasse="AL_Namen">Johannes Wagner</p>
<p klasse="AL_Namen">Stefan Wenzel</p>
<p klasse="AL_Partei">FDP</p>
<p klasse="AL_Namen">Renata Alt</p>
<p klasse="AL_Namen">Jens Beeck</p>
<p klasse="AL_Namen">Ingo Bodtke</p>
<p klasse="AL_Namen">Sandra Bubendorfer-Licht</p>
<p klasse="AL_Namen">Carl-Julius Cronenberg</p>
<p klasse="AL_Namen">Thomas Hacker</p>
<p klasse="AL_Namen">Manuel Höferlin</p>
<p klasse="AL_Namen">Dr. Ann-Veruschka Jurisch</p>
<p klasse="AL_Namen">Lars Lindemann</p>
<p klasse="AL_Namen">Michael Georg Link (Heilbronn)</p>
<p klasse="AL_Namen">Till Mansmann</p>
<p klasse="AL_Namen">Christoph Meyer</p>
<p klasse="AL_Namen">Maximilian Mordhorst</p>
<p klasse="AL_Namen">Christian Sauter</p>
<p klasse="AL_Namen">Matthias Seestern-Pauly</p>
<p klasse="AL_Namen">Dr. Stephan Seiter</p>
<p klasse="AL_Namen">Rainer Semet</p>
<p klasse="AL_Namen">Judith Skudelny</p>
<p klasse="AL_Namen">Bettina Stark-Watzinger</p>
<p klasse="AL_Namen">Konrad Stockmeier</p>
<p klasse="AL_Namen">Benjamin Strasser</p>
<p klasse="AL_Namen">Linda Teuteberg</p>
<p klasse="AL_Namen">Michael Theurer</p>
<p klasse="AL_Namen">Nico Tippelt</p>
<p klasse="AL_Namen">Dr. Florian Toncar</p>
<p klasse="AL_Namen">Dr. Andrew Ullmann</p>
<p klasse="AL_Namen">Dr. Volker Wissing</p>
<p klasse="AL_Partei">AfD</p>
<p klasse="AL_Namen">Dr. Christina Baum</p>
<p klasse="AL_Namen">Dr. Bernd Baumann</p>
<p klasse="AL_Namen">Marc Bernhard</p>
<p klasse="AL_Namen">Andreas Bleck</p>
<p klasse="AL_Namen">René Bochmann</p>
<p klasse="AL_Namen">Peter Boehringer</p>
<p klasse="AL_Namen">Gereon Bollmann</p>
<p klasse="AL_Namen">Stephan Brandner</p>
<p klasse="AL_Namen">Jürgen Braun</p>
<p klasse="AL_Namen">Marcus Bühl</p>
<p klasse="AL_Namen">Petr Bystron</p>
<p klasse="AL_Namen">Tino Chrupalla</p>
<p klasse="AL_Namen">Dr. Gottfried Curio</p>
<p klasse="AL_Namen">Thomas Dietz</p>
<p klasse="AL_Namen">Dr. Michael Espendiller</p>
<p klasse="AL_Namen">Peter Felser</p>
<p klasse="AL_Namen">Dietmar Friedhoff</p>
<p klasse="AL_Namen">Markus Frohnmaier</p>
<p klasse="AL_Namen">Dr. Götz Frömming</p>
<p klasse="AL_Namen">Dr. Alexander Gauland</p>
<p klasse="AL_Namen">Albrecht Glaser</p>
<p klasse="AL_Namen">Hannes Gnauck</p>
<p klasse="AL_Namen">Mariana Iris Harder-Kühnel</p>
<p klasse="AL_Namen">Jochen Haug</p>
<p klasse="AL_Namen">Martin Hess</p>
<p klasse="AL_Namen">Nicole Höchst</p>
<p klasse="AL_Namen">Leif-Erik Holm</p>
<p klasse="AL_Namen">Gerrit Huy</p>
<p klasse="AL_Namen">Fabian Jacobi</p>
<p klasse="AL_Namen">Steffen Janich</p>
<p klasse="AL_Namen">Dr. Malte Kaufmann</p>
<p klasse="AL_Namen">Dr. Michael Kaufmann</p>
<p klasse="AL_Namen">Stefan Keuter</p>
<p klasse="AL_Namen">Norbert Kleinwächter</p>
<p klasse="AL_Namen">Enrico Komning</p>
<p klasse="AL_Namen">Dr. Rainer Kraft</p>
<p klasse="AL_Namen">Barbara Lenk</p>
<p klasse="AL_Namen">Rüdiger Lucassen</p>
<p klasse="AL_Namen">Mike Moncsek</p>
<p klasse="AL_Namen">Matthias Moosdorf</p>
<p klasse="AL_Namen">Sebastian Münzenmaier</p>
<p klasse="AL_Namen">Edgar Naujok</p>
<p klasse="AL_Namen">Jan Ralf Nolte</p>
<p klasse="AL_Namen">Gerold Otten</p>
<p klasse="AL_Namen">Tobias Matthias Peterka</p>
<p klasse="AL_Namen">Jürgen Pohl</p>
<p klasse="AL_Namen">Stephan Protschka</p>
<p klasse="AL_Namen">Martin Erwin Renner</p>
<p klasse="AL_Namen">Frank Rinck</p>
<p klasse="AL_Namen">Dr. Rainer Rothfuß</p>
<p klasse="AL_Namen">Bernd Schattner</p>
<p klasse="AL_Namen">Eugen Schmidt</p>
<p klasse="AL_Namen">Jörg Schneider</p>
<p klasse="AL_Namen">Thomas Seitz</p>
<p klasse="AL_Namen">Martin Sichert</p>
<p klasse="AL_Namen">Dr. Dirk Spaniel</p>
<p klasse="AL_Namen">Klaus Stöber</p>
<p klasse="AL_Namen">Beatrix von Storch</p>
<p klasse="AL_Namen">Dr. Alice Weidel</p>
<p klasse="AL_Namen">Dr. Harald Weyel</p>
<p klasse="AL_Namen">Wolfgang Wiehle</p>
<p klasse="AL_Namen">Dr. Christian Wirth</p>
<p klasse="AL_Namen">Kay-Uwe Ziegler</p>
<p klasse="AL_Partei">DIE LINKE</p>
<p klasse="AL_Namen">Ates Gürpinar</p>
<p klasse="AL_Namen">Pascal Meiser</p>
<p klasse="AL_Namen">Petra Pau</p>
<p klasse="AL_Namen">Victor Perli</p>
<p klasse="AL_Namen">Martina Renner</p>
<p klasse="AL_Namen">Jessica Tatti</p>
<p klasse="AL_Namen">Kathrin Vogler</p>
<p klasse="AL_Partei">Fraktionslos</p>
<p klasse="AL_Namen">Robert Farle</p>
<p klasse="AL_Namen">Matthias Helferich</p>
<p klasse="AL_Ja-Nein-Enth">Enthalten</p>
<p klasse="AL_Partei">SPD</p>
<p klasse="AL_Namen">Reem Alabali-Radovan</p>
<p klasse="AL_Namen">Felix Döring</p>
<p klasse="AL_Namen">Nadine Heselhaus</p>
<p klasse="AL_Namen">Marianne Schieder</p>
<p klasse="AL_Namen">Rita Schwarzelühr-Sutter</p>
<p klasse="AL_Namen">Dr. Ralf Stegner</p>
<p klasse="AL_Partei">CDU/CSU</p>
<p klasse="AL_Namen">Alexander Föhr</p>
<p klasse="AL_Namen">Josef Oster</p>
<p klasse="AL_Partei">BÜNDNIS 90/ DIE GRÜNEN</p>
<p klasse="AL_Namen">Leon Eckert</p>
<p klasse="AL_Namen">Laura Kraft</p>
<p klasse="AL_Namen">Dr. Tobias Lindner</p>
<p klasse="AL_Namen">Sara Nanni</p>
<p klasse="AL_Namen">Dr. Sebastian Schäfer</p>
<p klasse="AL_Namen">Dr. Wolfgang Strengmann-Kuhn</p>
<p klasse="AL_Namen">Katrin Uhlig</p>
<p klasse="AL_Partei">FDP</p>
<p klasse="AL_Namen">Karlheinz Busen</p>
<p klasse="AL_Partei">AfD</p>
<p klasse="AL_Namen">Jörn König</p>
<p klasse="AL_Partei">DIE LINKE</p>
<p klasse="AL_Namen">Gökay Akbulut</p>
<p klasse="AL_Namen">Sevim Dağdelen</p>
<p klasse="AL_Partei">Fraktionslos</p>
<p klasse="AL_Namen">Johannes Huber</p>
<p klasse="J">Wir kommen nun zur Abstimmung über den Antrag der Abgeordneten Kappert-Gonther, Stamm-Fibich, Künast, Heveling, Dr. Castellucci, Helling-Plahr und weiterer Abgeordneter mit dem Titel „Suizidprävention stärken“. Die Abstimmung erfolgt ebenfalls namentlich. Sind die Urnen besetzt? – Ich sehe, das ist der Fall. Dann eröffne ich die namentliche Abstimmung über den Antrag auf Drucksache 20/7630.</p>
<p klasse="J">Ist ein Mitglied des Hauses anwesend, das seine Stimme noch nicht abgegeben hat?</p>
<p klasse="J">Ich bekomme das Zeichen, dass alle Mitglieder des Hauses ihre Stimme abgegeben haben. Ich schließe damit die Abstimmung und bitte die Schriftführerinnen und Schriftführer, die Stimmen auszuzählen.</p>
<p klasse="J">Ich bitte die Parlamentarischen Geschäftsführer zu mir.</p>
<p klasse="J">Liebe Kolleginnen und Kollegen, ich habe mich gerade mit den Parlamentarischen Geschäftsführern beraten. Eine wirklich sehr große Anzahl an Abgeordneten konnte ihre Stimme nicht abgeben, weil die Urnen relativ schnell geschlossen wurden. Und aus diesem Grund haben wir uns jetzt mehrheitlich dafür entschieden, die dritte Abstimmung zu dem Antrag „Suizidprävention stärken“ zu wiederholen. Die Urnen stehen ab 12 Uhr für 20 Minuten bereit. Bis dahin unterbreche ich die Sitzung und bitte die Schriftführerinnen und Schriftführer, alles entsprechend vorzubereiten.</p>
<p klasse="J">Ich darf die Mitglieder des Hauses auch darüber informieren, dass wir, wenn wir um 12 Uhr die namentliche Abstimmung eröffnen, unmittelbar danach in der Tagesordnung fortfahren. Ich bitte die Rednerinnen und Redner der folgenden Debatte, sich bereitzuhalten.</p>
<p klasse="J">Vielen Dank.</p>
<kommentar>(Unterbrechung von 11.42 bis 12.00 Uhr)</kommentar>
<name>Vizepräsidentin Yvonne Magwas:</name>
<p klasse="J_1">Liebe Kolleginnen und Kollegen, ich eröffne die unterbrochene Sitzung.</p>
<p klasse="J">Wir kommen erneut zur Abstimmung über den Antrag der Abgeordneten Kappert-Gonther, Stamm-Fibich, Künast, Heveling, Dr. Castellucci, Helling-Plahr und weiterer Abgeordneter mit dem Titel „Suizidprävention stärken“. Die Abstimmung erfolgt namentlich. Sie haben jetzt genau 20 Minuten Zeit, Ihre Stimme abzugeben. Ich werde Sie auch vor 12.20 Uhr noch einmal darüber informieren.</p>
<p klasse="J">Die Urnen sind besetzt, und ich eröffne die namentliche Abstimmung über den Antrag auf der Drucksache 20/7630.<sup>1</sup>
<fussnote>Ergebnis Seite 14111 D</fussnote>
</p>
<p klasse="J">Da wir vereinbart haben, mit der Tagesordnung fortzufahren, bitte ich Sie entsprechend, dass wir etwas Ruhe in den Plenarsaal bekommen.</p>
</tagesordnungspunkt>

'''    