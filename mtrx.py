import argparse

class Matrix:
    def __init__(self, width=0, height=0):
        self.representation = [[]]
        self.width = width
        self.height = height
    
    def read(self, input_name):
        try:
            with open(input_name, "r", encoding="UTF-8") as physicFile:
                self.parse(physicFile.read().splitlines())
        except FileNotFoundError: # zjistuje, zda existuje
            print(f"CHYBA: Pozadovany soubor {input_name} neexistuje. Program skonci.")
            exit()
        except PermissionError: # zjistuje pristup k souboru
            print(f"CHYBA: Nemam pristup k {input_name}.Program skonci.")
            exit()
        except ValueError as e: # validuje i pokud se jedna o validni JSON
            print(f"CHYBA: Soubor {input_name} neni validni. Program skonci.\n", e)
            exit()

    def parse(self, lines):
        first = True

        for line in lines:
           arrLine = line.split(" ")
           if first == True:   
                first = False
                self.width = len(arrLine)
           if len (arrLine) != self.width:
               print("Matice v souboru neni zapsana ve spravnem tvaru. Matice nemuze mit na radcich ruzny pocet sloupcu.")
               exit()
           self.representation.append(arrLine)
           self.height = self.height+1


