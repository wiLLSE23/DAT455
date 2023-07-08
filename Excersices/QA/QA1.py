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
