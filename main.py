# Turvalliset valinnat verkossa
# Täydennä ohjelmaa vaiheittain kommenttien ohjeiden mukaan.
# Rakenna ohjelmaa yksi vaihe kerrallaan.
# Testaa ohjelmaa aina jokaisen vaiheen jälkeen ennen kuin siirryt eteenpäin.
# Voit käyttää Scratch-versiota apuna ohjelman rakenteen hahmottamisessa.

# VAIHE 1
# Luo pistemäärää varten muuttuja nimeltä pisteet ja aseta sen alkuarvoksi 0.
# Tulosta ohjelman otsikko: Turvalliset valinnat verkossa
# Pyydä käyttäjää painamaan Enteriä aloittaakseen ohjelman.
# Vinkki: käytä input-komentoa.

# TESTAA TÄSSÄ VAIHEESSA
# Ohjelman pitäisi nyt näyttää otsikko ja odottaa Enter-näppäimen painamista.
# Tämä vastaa Scratch-ohjelman aloitusruutua ennen kuin käyttäjä painaa Aloita-painiketta.

# VAIHE 2
# Ensimmäinen kysymys
# Tulosta tyhjä rivi ennen kysymystä.
# Tulosta ensimmäinen kysymys:
# 1. Saat sähköpostin tuntemattomalta lähettäjältä, jossa pyydetään klikkaamaan linkkiä nopeasti. Mitä teet?
# Tulosta vaihtoehto A: Klikkaan linkkiä heti
# Tulosta vaihtoehto B: Tarkistan lähettäjän ja poistan viestin
# Tulosta vaihtoehto C: Lähetän viestin kaverille

# Tallennetaan käyttäjän vastaus muuttujaan vastaus (toteutus valmiina malliksi)
vastaus = input("Valitse A, B tai C: ").strip().upper()

# Kirjoita if-ehto, joka tarkistaa, onko vastaus "B".
# Jos vastaus on oikein:
#     tulosta Oikein!
#     lisää pisteisiin 1
# Muuten:
#     tulosta Väärin.
# Muista sisennys if-rakenteessa.

# TESTAA TÄSSÄ VAIHEESSA
# Ohjelman pitäisi nyt kysyä ensimmäinen kysymys ja antaa palaute.
# Tämä vastaa Scratch-ohjelman Kysymys 1 -vaihetta.

# VAIHE 3
# Toinen kysymys
# Tulosta tyhjä rivi ennen kysymystä.
# Tulosta toinen kysymys:
# 2. Kaveri pyytää salasanaasi, jotta voisi kirjautua puolestasi peliin. Mitä teet?
# Tulosta vaihtoehto A: Annan salasanan, jos kyseessä on hyvä kaveri
# Tulosta vaihtoehto B: En anna salasanaa kenellekään
# Tulosta vaihtoehto C: Annan salasanan vain hetkeksi
# Pyydä käyttäjältä uusi vastaus ja tallenna se taas muuttujaan vastaus.

# Vinkki: katso, mitä teit edellisessä vaiheessa tässä kohdassa.

# Kirjoita if-ehto, joka tarkistaa, onko vastaus "B". (Vinkki: samalla lailla kuin edellisessä vaiheessa)
# Oikea vastaus on taas "B".
# Muista sisennys!

# TESTAA TÄSSÄ VAIHEESSA
# Ohjelman pitäisi nyt kysyä kaksi kysymystä ja laskea pisteet oikein.
# Tämä vastaa Scratch-ohjelman vaiheita Kysymys 1 ja Kysymys 2.

# VAIHE 4
# Kolmas kysymys
# Tulosta tyhjä rivi ennen kysymystä.
# Tulosta kolmas kysymys:
# 3. Millainen on vahva salasana?
# Tulosta vaihtoehto A: Oma nimi ja syntymävuosi
# Tulosta vaihtoehto B: Lyhyt ja helppo sana
# Tulosta vaihtoehto C: Pitkä salasana, jossa on erilaisia merkkejä
# Pyydä käyttäjältä uusi vastaus ja tallenna se muuttujaan vastaus.

# Vinkki: käytä samaa rakennetta kuin aiemmin.

# Kirjoita if-ehto, joka tarkistaa, onko vastaus "C". (Vinkki: samalla lailla kuin edellisessä vaiheessa)
# Muista: tällä kertaa oikea vastaus on "C".
# Muista sisennys.

# TESTAA TÄSSÄ VAIHEESSA
# Ohjelman pitäisi nyt kysyä kaikki kolme kysymystä.
# Tämä vastaa Scratch-ohjelman kaikkia kysymysvaiheita ennen lopetusruutua.

# VAIHE 5
# Lopputulos
# Tulosta tyhjä rivi.
# Tulosta teksti: Peli päättyi.
# Tulosta pistemäärä muodossa:
# Sait X /3 pistettä.
# Vinkki: voit tulostaa pisteet print-komennolla pilkuilla erotettuna,
# ja muista että X kohtaan kannattaa sijoittaa 'pisteet' -muuttujan arvo.

# Kirjoita tähän if-ehto:
# jos pisteet ovat yhtä kuin 3
#     tulosta Loistavaa! Sait kaikki oikein.
# Kirjoita tähän elif-ehto:
# jos pisteet ovat yhtä kuin 2
#     tulosta Hyvä! Osasit jo paljon.
# Kirjoita tähän else-haara:
# muussa tapauksessa
#     tulosta Harjoittele vielä lisää.

# TESTAA TÄSSÄ VAIHEESSA
# Ohjelman pitäisi nyt toimia alusta loppuun asti.
# Tämä vastaa Scratch-ohjelman valmista versiota, jossa näkyy myös lopetusruutu.

# LISÄTEHTÄVÄ
# Lisää ohjelmaan mahdollisuus aloittaa alusta.
# Voit tehdä tämän while-silmukan avulla.
# Kysy käyttäjältä esimerkiksi:
# Haluatko pelata uudelleen? (k/e)
# Tämä vastaa Scratch-ohjelman "Aloita alusta" -toimintoa.
