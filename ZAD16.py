"""
Sparsuj przygotowanego XML (parserem SAX i DOM) i go
zmodyfikuj np. zmień wartość któregoś tag’a i zapisz do nowego
pliku
"""
#!/usr/bin/python
import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.CurrentData = ""
        self.rozklad = ""
        self.miejscowosc = ""
        self.linia = ""
        self.numer = ""
        self.poczatek = ""
        self.koniec = ""

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "rozklad":
            print("***** Rozklad jazdy linii autobusowych *****")
        if tag == "linia":
            nazwa_linii = attributes["nazwa"]
            print("\tNazwa linii:", nazwa_linii)

    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "rozklad":
            print("Rozklad:", self.rozklad)
        elif self.CurrentData == "miejscowosc":
            print("Miejscowosc:", self.miejscowosc)
        elif self.CurrentData == "linia":
            print("Linia:", self.linia)
        elif self.CurrentData == "numer":
            print("\t\tNumer:", self.numer)
        elif self.CurrentData == "poczatek":
            print("\t\tPoczatek:", self.poczatek)
        elif self.CurrentData == "koniec":
            print("\t\tKoniec:", self.koniec)
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "rozklad":
            self.rozklad = content
        elif self.CurrentData == "miejscowosc":
            self.miejscowosc = content
        elif self.CurrentData == "linia":
            self.numer = content
        elif self.CurrentData == "numer":
            self.numer = content
        elif self.CurrentData == "poczatek":
            self.poczatek = content
        elif self.CurrentData == "koniec":
            self.koniec = content


if __name__ == "__main__":
    # create an XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # override the default ContextHandler

Handler = MovieHandler()
parser.setContentHandler(Handler)
parser.parse("xmlparsertest.xml")