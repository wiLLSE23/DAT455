"""
QA-Session 2, Avancerad
Wincent Stålbert Holm
"""
​
"""
Kommunalskatt:
  Skillnaden mellan grundavdraget och brutto, 
  multiplicerat med kommunalskattesatsen.
"""
""
def beräkna_kommunalskatt(brutto, grundavdraget, kommunalskattesatsen):
    skattbart = brutto - grundavdraget
​
    skatt = skattbart * kommunalskattesatsen
​
    return skatt
​
"""
Landstingsskatt:
  Skillnaden mellan grundavdraget och brutto, 
  multiplicerat med landstingsskattesatsen.
"""
def beräkna_landstingskatt(brutto, grundavdraget, landstingsskattesatsen):
    skattbart = brutto - grundavdraget
​
    skatt = skattbart * landstingsskattesatsen
​
    return skatt
​
"""
Statlig skatt:
  Bara om brutto är mer än den statliga brytpunkten.
  Skillnaden mellan brutto och den statliga brytpunkten, 
  multiplicerat med den statlig skattesatsen
"""
def beräkna_statlig_skatt(brutto, statligabrytpunkten, statligaskattesatsen=0.2):
    if brutto > statligabrytpunkten:
        skattbart = brutto - statligabrytpunkten
​
        skatt = skattbart * statligaskattesatsen
    else:
        skatt = 0
​
    return skatt
​
"""
Public-service avgift:
  1 % av brutto,
  inte mer än 1 300 kr
"""
def public_service_avgift(brutto):
    skatt = brutto * 0.01
​
    return 1_300 if skatt > 1_300 else skatt
​
"""
Begravningsavgift:
  0.258 % av brutto
"""
def beräkna_begravningsavgift(brutto):
    return brutto * 0.00258
​
"""
Jobbskatteavdrag:
  Brutto överstiger inte 47 775 kr:
    Skillnaden mellan arbetsinkomsten och grundavdraget, 
    multiplicerat med kommunal+landstingsskattesatsen
​
  Brutto överstiger 47 775 kr men inte 170 100 kr:
    Skillnaden mellan å ena sidan:
    47 775 kr och 38,74 % av arbetsinkomsten mellan 47 775 kr och 170 100 kr,
    och å andra sidan grundavdraget, 
    multiplicerat med kommunal+landstingsskattesatsen
​
  Brutto överstiger 170 100 kr men inte 424 200 kr:
    Skillnaden mellan å ena sidan:
    95 130 kr och 12,8 % av arbetsinkomsten mellan 170 100 kr och 424 200 kr,
    och å andra sidan grundavdraget, 
    multiplicerat med kommunal+landstingsskattesatsen
​
  Brutto överstiger 424 200 kr men 710 850 kr:
    Skillnaden mellan 127 680 kr och grundavdraget,
    multiplicerat med kommunal+landstingsskattesatsen
​
  Brutto överstiger 710 850 kr
    Skillnaden mellan 127 680 kr och grundavdraget,
    multiplicerad med kommunal+landstingsskattesatsen,
    med avdrag för 3 % av de arbetsinkomster som överstiger 710 850 kr
"""
def beräkna_jobbskatteavdrag(brutto, grundavdraget, kommunalskattesatsen, landstingsskattesatsen):
    kommunochlandstingskattesaten = kommunalskattesatsen + landstingsskattesatsen
    
    if brutto < 47_775:
        belopp = brutto - grundavdraget
        avdrag = belopp * kommunochlandstingskattesaten
    elif brutto < 170_100:
        belopp = 47_775 + 0.3874 * (brutto - 47_775) - grundavdraget
        avdrag = belopp * kommunochlandstingskattesaten
    elif brutto < 424_200:
        belopp = 95_130 + 0.128 * (brutto - 170_100) - grundavdraget
        avdrag = belopp * kommunochlandstingskattesaten
    elif brutto < 710_850:
        belopp = 127_680 - grundavdraget
        avdrag = belopp * kommunochlandstingskattesaten
    else:
        belopp = 127_680 - grundavdraget
        avdrag = belopp * kommunochlandstingskattesaten
        avdrag = avdrag - (brutto - 710_850) * 0.03
    
    return 0 if avdrag < 0 else avdrag
​
​
"""
Ska betala skatt
"""
def ska_betala_skatt(brutto, grundavdraget):
    return brutto > grundavdraget
​
"""
Grundberäkningen
"""
def beräkna_skatt(
        brutto, grundavdraget, kommunalskattesatsen, 
        landstingsskattesatsen, statligaskattesatsen, 
        statligabrytpunkten):
    """
    * Kommunalskatt (-)
    * Landstingsskatt (-)
    * Statlig skatt (-)
    * Jobbskatteavdrag (+)
    * Public-service avgift (-)
    * Begravningsavgift (-)
    """
    netto = brutto
​
    ska_betala = ska_betala_skatt(brutto, grundavdraget)
​
    kommunalskatt = 0 if not ska_betala else beräkna_kommunalskatt(brutto, grundavdraget, kommunalskattesatsen)
    landstingsskatt = 0 if not ska_betala else beräkna_landstingskatt(brutto, grundavdraget, landstingsskattesatsen)
    statligskatt = 0 if not ska_betala else beräkna_statlig_skatt(brutto, statligabrytpunkten, statligaskattesatsen)
    jobbskatteavdrag = 0 if not ska_betala else beräkna_jobbskatteavdrag(brutto, grundavdraget, kommunalskattesatsen, landstingsskattesatsen)
    public_service = 0 if not ska_betala else public_service_avgift(brutto)
    begravningsavgift = 0 if not ska_betala else beräkna_begravningsavgift(brutto)
​
    netto -= kommunalskatt
    netto -= landstingsskatt
    netto -= statligskatt
    netto += jobbskatteavdrag
    netto -= public_service
    netto -= begravningsavgift
​
    effektiva_skatten = 1 - (netto / brutto)
​
    return netto, effektiva_skatten, kommunalskatt, \
            landstingsskatt, statligskatt, jobbskatteavdrag, \
                public_service, begravningsavgift
​
"""
Main
"""
def main():
    månadslön = int(input("Vad är din månadslön? "))
    antal_år = int(input("Hur många år görs beräkningen för? "))
    löneökning = float(input("Hur hör löneökning för du varje år? Ange i %. ")) / 100.0 # 2,5
​
    brutto = månadslön * 12
​
    # C: for (int i = 0; i < antal_år; i++) {...}
    for i in range(antal_år):
        """
        * Kommunalskattesatsen, 21.12% för Göteborg
        * Landstingsskattesatsen, 11.48% för Västra Götaland
        * Den statlig skattesatsen, 20%
        * Brytpunkten för statlig skatt, 613 900 kr
        * Grundavdraget, utegå ifrån 22 208 kr
        """
        kommunalskattesatsen = 0.2112
        landstingsskattesatsen = 0.1148
        statligaskattesatsen = 0.2
        statligabrytpunkten = 613_900
        grundavdraget = 22_208
​
        netto, effektiva_skatt, kommunalskatt, landstingsskatt, \
            statligskatt, jobbskatteavdrag, public_service, begravningsavgift = beräkna_skatt(
            brutto, grundavdraget, kommunalskattesatsen,
            landstingsskattesatsen, statligaskattesatsen,
            statligabrytpunkten)
        
        print(f"{'Efter ':<30} {i} år")
        print(f"{'Brutto:':<30} {brutto:0.2f}")
        print(f"{'Netto:':<30} {netto:0.2f}")
        print(f"{'Kommunalskatt (-)':<30} {kommunalskatt:0.2f}")
        print(f"{'Landstingsskatt (-)':<30} {landstingsskatt:0.2f}")
        print(f"{'Statligskatt (-)':<30} {statligskatt:0.2f}")
        print(f"{'Jobbskatteavdrag (+)':<30} {jobbskatteavdrag:0.2f}")
        print(f"{'Public Service (-)':<30} {public_service:0.2f}")
        print(f"{'Begravningsavgift (-)':<30} {begravningsavgift:0.2f}")
        print(f"{'Effektiva skatten:':<30} {(effektiva_skatt*100):0.2f}%")
​
        brutto *= 1 + löneökning # 1 + 0.035
​
main()
""