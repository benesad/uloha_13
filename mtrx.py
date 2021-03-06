import argparse

class Matrix:
    def __init__(self, width=0, height=0):
        if width !=0 and height !=0:
            self.representation = [[0 for x in range(width)] for y in range(height)] # make an empty list in given range
        else:
            self.representation = []
        self.width = width
        self.height = height
    
    def read(self, input_name):
        try:
            with open(input_name, "r", encoding="UTF-8") as physicFile:
                self.parse(physicFile.read().splitlines())
        except FileNotFoundError: # try to find out if file exists
            print(f"CHYBA: Pozadovany soubor {input_name} neexistuje. Program skonci.")
            exit()
        except PermissionError: # try to find out if it have an acces
            print(f"CHYBA: Nemam pristup k {input_name}.Program skonci.")
            exit()
        except ValueError as e: # try to validate even if its valid
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

    def save(self, output_file_name):
        try:
            with open(output_file_name, "w", encoding="UTF-8") as physicFile:
                for row_index in range(self.height):
                    row_str = ""
                    for col in self.representation[row_index]:
                        if row_str == "":
                            row_str=str(col)
                        else:
                            row_str += " " + str(col)  # give space between two numbers in a row

                    if row_index!=self.height-1:
                        row_str += '\n'

                    physicFile.write(row_str)
        except PermissionError:
            print(f"CHYBA: Nemuzu ulozit vysledny soubor, protoze nemam pristup k ukladani.")
            exit()
        except:
            print("CHYBA: Vysledny soubor se mi nepodarilo ulozit.")
            exit()