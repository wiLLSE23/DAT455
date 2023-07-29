"""Uppgift:
Skapa ett program som ber användaren om en månadslön och sedan 
beräknar (uppskattar) nettolönen över ett år. Ge också 
användaren en översikt över vart deras skattepänger går och
beräkna den effektiva skattesatsen.
Programmet ska räkna med följande skatter och avdrag:
* Kommunalskatt (-)
* Landstingsskatt (-)
* Statlig skatt (-)
* Jobbskatteavdrag (+)
* Public-service avgift (-)
* Begravningsavgift (-)
För att utföra dessa beräkningar behövs följande information:
* Kommunalskattesatsen, 21.12% för Göteborg
* Landstingsskattesatsen, 11.48% för Västra Götaland
* Den statlig skattesatsen, 20%
* Brytpunkten för statlig skatt, 613 900 kr
* Grundavdraget, utegå ifrån 22 208 kr
En användare betalar ingen skatt om de inte tjärnar mer än grundavdraget under ett år.
Gör så här:
  Skissa upp programmet med tomma funktioner först.
  Tips: Skapa en funktion för varje skatt och avdrag.
  Skapa variabler för den informationen som behövs för att utföra beräkningarna.
  Sätt upp grundberäkningen, där alla skatter och avdrag summeras.
  Ta in en input från användaren som ber om månadslön.
  Skriv ut resultat från beräkningen.
  Börja med att implementera de enklare funktionerna,
  och gå över till de längre sen.
  Ge användaren en utskrift för vart deras skattepänger går,
  hur mycket går till kommun, stat, etc.
Skatt- och avdragsberäkningar:
Kommunalskatt:
  Skillnaden mellan grundavdraget och brutto, 
  multiplicerat med kommunalskattesatsen.
Landstingsskatt:
  Skillnaden mellan grundavdraget och brutto, 
  multiplicerat med landstingsskattesatsen.
Statlig skatt:
  Bara om brutto är mer än den statliga brytpunkten.
  Skillnaden mellan den statliga brytpunkten och grundavdraget, 
  multiplicerat med den statlig skattesatsen
Public-service avgift:
  1 % av brutto,
  inte mer än 1 300 kr
Begravningsavgift:
  0.258 % av brutto
Jobbskatteavdrag:
  Brutto överstiger inte 47 775 kr:
    Skillnaden mellan arbetsinkomsten och grundavdraget, 
    multiplicerat med kommunal+landstingsskattesatsen
  Brutto överstiger 47 775 kr men inte 170 100 kr:
    Skillnaden mellan å ena sidan:
    47 775 kr och 38,74 % av arbetsinkomsten mellan 47 775 kr och 170 100 kr,
    och å andra sidan grundavdraget, 
    multiplicerat med kommunal+landstingsskattesatsen
  Brutto överstiger 170 100 kr men inte 424 200 kr:
    Skillnaden mellan å ena sidan:
    95 130 kr och 12,8 % av arbetsinkomsten mellan 170 100 kr och 424 200 kr,
    och å andra sidan grundavdraget, 
    multiplicerat med kommunal+landstingsskattesatsen
  Brutto överstiger 424 200 kr men 710 850 kr:
    Skillnaden mellan 127 680 kr och grundavdraget,
    multiplicerat med kommunal+landstingsskattesatsen
  Brutto överstiger 710 850 kr
    Skillnaden mellan 127 680 kr och grundavdraget,
    multiplicerad med kommunal+landstingsskattesatsen,
    med avdrag för 3 % av de arbetsinkomster som överstiger 710 850 kr
"""

kommunalskattesatsen_gbg = 21.12/100
landstingsskattesatsen_vgr = 11.48/100
statlig_skattesatsen = 20/100
brytpunkten_statlig_skatt = 613900
grundavdraget = 22208

def kommunalskatt(brutto):
    skatt = (brutto - grundavdraget) * kommunalskattesatsen_gbg
    print("din kommunaalskatt är: ", skatt)
    return skatt

def landstingsskatt(brutto):
    return (brutto - grundavdraget) * landstingsskattesatsen_vgr

def statlig_skatt(brutto):
    if brutto > brytpunkten_statlig_skatt:
        return (brytpunkten_statlig_skatt - grundavdraget) * statlig_skattesatsen
    else:
        return 0

def public_service_avgift(brutto):
    if brutto * 0.01 > 1300:
        return 1300
    else:
        return brutto * 0.01

def begravningsavgift(brutto):
    return brutto * 0.00258

def jobbskatteavdrag(brutto):
    if brutto < 47775:
        return (brutto - grundavdraget) * (kommunalskattesatsen_gbg + landstingsskattesatsen_vgr)
    elif brutto < 170100:
        return (47775 - 0.3874 * (brutto - 47775) - grundavdraget) * (kommunalskattesatsen_gbg + landstingsskattesatsen_vgr)
    elif brutto < 424200:
        return (95130 - 0.128 * (brutto - 170100) - grundavdraget) * (kommunalskattesatsen_gbg + landstingsskattesatsen_vgr)
    elif brutto < 710850:
        return (127680 - grundavdraget) * (kommunalskattesatsen_gbg + landstingsskattesatsen_vgr)
    else:
        return (127680 - grundavdraget - 0.03 * (brutto - 710850)) * (kommunalskattesatsen_gbg + landstingsskattesatsen_vgr)

def skatt():
  print("Ange din bruttolön: ")
  brutto = int(input())
  brutto -= kommunalskatt(brutto)
  brutto -= landstingsskatt(brutto)
  brutto -= statlig_skatt(brutto)
  brutto -= public_service_avgift(brutto)
  brutto -= begravningsavgift(brutto)
  brutto += jobbskatteavdrag(brutto)
  print("Din nettolön är: ", brutto)

skatt()