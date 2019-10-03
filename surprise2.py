# Datetime Variablen importieren
from datetime import *

# aktuelles Datum in Variable speichern
curr_date = datetime.today()

# While-Schlefe festlegen
x = 1
while True:

# Abfrage welches Datum herausgefunden werden soll
 event = input("Wann ist ...\n- Weihnachten\n- stand. Hochzeit\n- kirchl. Hochzeit?\n")

# Wenn Eingabe 'Weihnachten': definiere Var cal_date & cal_input entsprechend
# gehe dann zu 'countdown' und geb die Berechnung aus.
 if "Weihnachten" in event:
  cal_date = datetime(2019, 12, 24)
  cal_input = "Weihnachten"

# alternativ: wenn Eingabe 'stand': definiere Var cal_date & cal_input entsprechend
# gehe dann zu 'countdown' und geb die Berechnung aus.
 elif "stand" in event:
  cal_date = datetime(2019, 12, 14)
  cal_input = "zur stand. Hochzeit"

# alternativ: wenn Eingabe 'kirchl': definiere Var cal_date & cal_input entsprechend
# gehe dann zu 'countdown' und geb die Berechnung aus.
 elif "kirch" in event:
  cal_date = datetime(2020, 3, 21)
  cal_input = "zur kirchl. Hochzeit" 

# wenn weder 'Weihnachten', 'stand' oder 'kirch' enthalten sind:
# Fehlermeldung ausgeben, While-Loop neustarten
 elif "Weihnachten" or "stand" or "kirch" not in event:
  print("\nUngueltige Eingabe. Versuche es nochmal\n")
  continue

# Ausgabe wenn Input 'Weihnachten', 'stand' oder 'kirchl' enthält
 countdown = abs(cal_date - curr_date)
 print("\nnoch", countdown.days, "x schlafen bis", cal_input,"\n")

#Variable 'beenden' definieren
 beenden = input("Programm beenden? y/n\n")

# Wenn Var 'beenden' = y:
# beenden
# andernfalls:
# While Schleife neu starten
 if beenden == "y":
  exit()
 elif beenden == "n":
  x += 1