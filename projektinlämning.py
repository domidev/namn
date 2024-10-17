from colorama import Fore, Style, init
init(autoreset=True)


#  Skapa spelarklassen.
class Spelare:
    def __init__(self, namn, marker, färg):
        self.namn = namn
        self.marker = marker
        self.färg = färg


# Skapa 3x3 brädan.
class TicTacToeBrädan:
    def __init__(self):
        self.bräda = [' ' for _ in range (9)]
        self.aktiv_spelare = None
    
# Skriv ut 3x3 brädan.
    def skrivut_bräda(self):
        print("=========")
        print(f"{self.färg_marker(0)} I {self.färg_marker(1)} I {self.färg_marker(2)}")
        print("=========")
        print(f"{self.färg_marker(3)} I {self.färg_marker(4)} I {self.färg_marker(5)}")
        print("=========")
        print(f"{self.färg_marker(6)} I {self.färg_marker(7)} I {self.färg_marker(8)}")
        print("=========")
        print()
    
# Färg sätter X och O markörerna, X blir RED och O blir BLUE
    def färg_marker(self, position):
        if self.bräda[position] == 'X':
            return f"{Fore.RED}{self.bräda[position]}{Style.RESET_ALL}"
        elif self.bräda[position] == 'O':
            return f"{Fore.BLUE}{self.bräda[position]}{Style.RESET_ALL}"
        else:
            return self.bräda[position]

# Kolla om den aktiva spelaren har vunnit med hjälp av alla olika möjliga vinstchanser.
    def vinnaren(self, marker):
        vinst_kombinationer = [[0, 1, 2], [3, 4, 5], [6, 7, 8], 
                               [0, 3, 6], [1, 4, 7], [2, 5, 8], 
                               [0, 4, 8], [2, 4, 6]
                               ]
        for kombo in vinst_kombinationer:
            if self.bräda[kombo[0]] == marker and self.bräda[kombo[1]] == marker and self.bräda[kombo[2]] == marker:
                return True
        return False

# Kolla om det är oavgjort 
    def oavgjort(self):
        return ' ' not in self.bräda
    
# Gör drag på den positionen du vill
    def gördrag(self, position, marker):
        if self.bräda[position] == ' ':
            self.bräda[position] = marker
            return True
        else:
            return False
        
# Växlar till annan spelare
    def växlaspelare(self, spelare1, spelare2):
        self.aktiv_spelare = spelare1 if self.aktiv_spelare == spelare2 else spelare2

# Filhantering & Sparar vinnaren och namnet till en txt fil.
    def sparavinnaren(self, vinnarens_namn):
        with open("resultat.txt", "a") as file:
            file.write(f"Winner: {vinnarens_namn}\n")

# Spela spelet
    def spela_spelet(self, spelare1, spelare2): 
        self.aktiv_spelare = spelare1
        spel_igång = True

        while spel_igång:
            self.skrivut_bräda()
            print(f"{self.aktiv_spelare.namn}'s tur att spela ({self.aktiv_spelare.marker})")

            try:
                position = int(input("Välj en position (1-9): ")) - 1
            except ValueError:
                print("Var god välj en siffra mellan 1-9.")
                continue

            if position < 0 or position > 8:
                print("Ogiltig position! Välj en siffra mellan 1 och 9 ")
                continue

            if not self.gördrag(position, self.aktiv_spelare.marker):
                print("Den här positionen är redan tagen. Var god välj igen.")
                continue

#Detta sparar vinnaren i txt filen
            if self.vinnaren(self.aktiv_spelare.marker):
                self.skrivut_bräda()
                print(f"Grattis {self.aktiv_spelare.namn}! Du har vunnit detta spel")
                self.sparavinnaren(self.aktiv_spelare.namn)
                spel_igång = False
            elif self.oavgjort():
                self.skrivut_bräda()
                print("Det blev oavgjort")
                spel_igång = False
            else:
                self.växlaspelare(spelare1, spelare2)

# Sätter igång spelet
if __name__ == "__main__":
    spelare1 = Spelare(input("Ange Spelare 1's namn: "), 'X', Fore.RED)
    spelare2 = Spelare(input("Ange Spelare 2's namn: "), 'O', Fore.BLUE)
    
    spel = TicTacToeBrädan()
    spel.spela_spelet(spelare1, spelare2)