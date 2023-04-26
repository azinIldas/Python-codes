#Scriptsprache: Phthon
import random

# Print zeigt dem Benutzer den Text inherhalb der "()" an.
print('-----------------------------')
print('-- Schere | Stein | Papier --')
print('-----------------------------')

# possibleChoises = Innherhalb der "()" geben wir dem Programm an was zur verfügung steht.
Auswahl = ('Schere', 'Stein', 'Papier')
Spiel = True

# Wir erstellen eine Schleife , indem das Spiel ausgeführt wird, solange es True ist.
while Spiel:

    # Bei der Auswahl, geben wir bei der Auswahl dem Code den Wert 0 ein, 
    # damit bei der Schleife die Zahlen des Computer und des Spieler auswertbar werden.
    SpielerAuswahl = 0

    while not SpielerAuswahl:
        try:
            SpielerAuswahl = int(input('\n[1] Schere | [2] Stein | [3] Papier\n'))
            if SpielerAuswahl not in (1,2,3):
                raise ValueError
        except ValueError:
            SpielerAuswahl = 0

#Wenn das Programm an diesen Schritt gelangt, dann wird der wert des Spieler bei jeder Durchlaufung um -1 verkleinert. 
# Sodass die Zahlen des Geners und des Spieers übereinstimmen können.
    Spieler = Auswahl[SpielerAuswahl-1]

    # Der Gegner(welches unser Compueter ist), erhält bei jedem Match eine zufällige Zahl, 0 = Schere ...
    Gegner = Auswahl[random.randint(0,2)]

# Wenn der Spieler Schere nimmt( 1 - 1 = 0 ) und der Computer auch Schere hat(0), 
# befehlen wir dem Programm ein Unentschieden auszuschreiben.
#Beim Befehl des Print fügen wir nach der '' ein , 
# Gegner ein damit, es die Auswahl des Gegners auch anzeigt. {Gegner} innerhalb der '' würde auch funktionieren.
    if Spieler == Gegner:
        print(f'Unentschieden! Gegner hatte:\n', Gegner)
        
#Wenn die Auswahl des Spieler und des Gegners nicht gleich sind, kommen wir zur ansonsten/else Schleife.
    else:
        #Wir geben an, wenn der Spieler(0 = Schere) hat und der Gegner(1 = Stein) dann verliert der Spieler,
        # anonsten(else: wenn dies nicht zutrifft) gewinnt der Spieler.
        if Spieler == Auswahl[0]:
            if Gegner == Auswahl[1]:
                print(f'Verloren! Gegner hatte:\n', Gegner)
            else:
                print(f'Gewonnen! Gegner hatte:\n', Gegner)
        
        #Wir geben an, wenn der Spieler(1 = Stein) hat und der Gegner(2 = Papier) dann verliert der Spieler, 
        # anonsten(else: wenn dies nicht zutrifft) gewinnt der Spieler.
        elif Spieler == Auswahl[1]:
            if Gegner == Auswahl[2]:
                print(f'Verloren! Gegner hatte:\n', Gegner)
            else:
                print(f'Gewonnen! Gegner hatte:\n', Gegner)
         
       #Wir geben an, wenn der Spieler(2 = Papier) hat und der Gegner(0 = Schere) dann verliert der Spieler, 
       # anonsten(else: wenn dies nicht zutrifft) gewinnt der Spieler.      
        elif Spieler == Auswahl[2]:
            if Gegner == Auswahl[0]:
                print(f'Verloren! Gegner hatte:\n', Gegner)
            else:
                print(f'Gewonnen! Gegner hatte:\n', Gegner)

    # Wenn gewünscht, nach jedem Match, geben wir dem Spieler die Möglichkeit, 
    # eine Revanche zu machen, die abgebrochen werden kann wenn der Spieler Nein/('N') eingibt.
    NeuePartie = ''
    while NeuePartie not in ('J', 'N' ):
        NeuePartie = input('Revanche gefällig?\n[J] Ja | [N] Nein\n')

# das != bringt dazu, das jede Antwort die ungleich als Ja/("J") ist zu einem Spielabbruch führt.
    if (NeuePartie != 'J'):
        
        #Oben haben wir angegeben dass das Spiel True ware = weiterlaufen, 
        # wenn Jedoch die Revanche abgebrochen wrd mit einem ('N'), dann erzwingt das Programm das Spiel zum beenden.
        Spiel = False
