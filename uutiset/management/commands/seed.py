from django.core.management.base import BaseCommand
from uutiset.models import Uutinen
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        data = [
            {
                "title": "Ananaskissa pelaa Banjo-Kazooieta!",
                "content": """Voitteko kuvitella? Ananaskissa aloitti pelaamaan maailman parasta peliä. Nyt voimme juhlistaa ja levittää ilosanomaa. 
                Toivottavasti kaikki saavat tietää tästä! Tämän seurauksena voimme varmasti ennustaa, että sodat loppuvat, nälänhätä saadaan kuriin ja kahvin hinta palautuu takaisin normaaliksi. 
                Olemme tulleet tietoisiksi joistakin huhuista, että Banjo-Kazooie ei olisi Ananaskissan lempipeli, mutta näihin emme usko. 
                Jos tämä on kuitenkin totta, olemme varmoja siitä, että kun Ms. Kissa saa ohjaimen käteensä, hänen mielipiteensä tulee varmasti muuttumaan. 
                Uskomme, että ennen kuin peli edes lähtee käyntiin, hän tietää jo, että hänen sekä kaikkien muiden elämät tulevat muuttumaan positiivisella tavalla. 
                Slowrun aikoo kannustaa täysillä tätä peliurakkaa. Jos lähiaikoina koet satunnaista hyvän olon tunnetta, lähes ekstaasiin verrattavaa tunnetta, ei ole syytä huoleen. 
                Tämän on tarkoitus tapahtua. Ja nyt tiedät, mistä se johtuu.""",
                "date": timezone.now(),
                "picture": "images/mushroom1.jpg"
            },
            {
                "title": "Uutuuskohde avattu",
                "content": """Oletko saanut kommentteja pelitovereiltasi, että olisit \"sweaty tryhard\"? 
                Nyt on aikasi koittanut, sillä kohteessa X on avattu uusi tila, joka varmasti olisi sinulle sopiva. 
                Tilassa on yhdistettynä kaksi elinehtoa: pelaaminen ja sauna! Tule pelaamaan ja saunomaan! 
                Eikä haittaa, jos vahingossa tai vaikka tahallisestikin heität ohjaimen, se on jo joltakin lipsunut kädestä aikaisemmin. 
                Materiaalivastuu on meillä, joten pelaa huoletta! Slowrun ymmärtää jos olette turhautuneet pelitovereidesi hitauteen. 
                Emme kuitenkaan vastaa kaverisuhteiden rikkoutumisista.""",
                "date": timezone.now() + timedelta(days=3),
                "picture": "images/mushroom2.jpg"
            },
            {
                "title": "Uusi kahvitekniikka keksitty",
                "content": """Joku todella fiksu henkilö on keksinyt mullistavan tavan valmistaa kahvia. 
                Tämä tapa on suorastaan nerokas, mutta niin yksinkertainen, että kuka tahansa voi tämän menetelmän suorittaa. 
                Tapa menee seuraavasti: runsaan sateen jälkeen poimi mehevä sieni maasta. Tämän jälkeen vie sieni suodattimen päälle ja rutista! 
                Sienestä valuva vesi suodattuu kahvin läpi ja näin saat Sienikahvia™! Mikä tahansa sieni toimii. 
                Konsultoimme kahvin suurkuluttajaa, lempääläläistä tubettajaa Niilo22:sta. Hän suosittelee Sienikahvia™, antaen tälle arvosanan 5/5. 
                Tubettaja käytti sienenään punakärpässientä. Vaikka monia kyseinen sienivalinta voisi epäilyttää, tubettaja totesi tähän vain: \"Ei kannata olla ennakkoluuloton!\". 
                Näiden viisaiden sanojen säestämänä kahvi tippui kuppiin, jossa luki \"Myrkkyä!\". Kahvin juotuaan tubettaja totesi lyhyesti mutta ytimekkäästi: \"On!\". 
                Olemme Slowrunissa hänen kanssaan samaa mieltä. Kokeile Sienikahvia™ vaikka heti!""",
                "date": timezone.now() + timedelta(days=1),
                "picture": "images/mushroom3.jpg"
            },
            {
                "title": "Uusi yhteistyökumppani",
                "content": """Tunnemme suunnattoman paljon nautintoa kerrotessamme uudesta yhteistyökumppanuudesta paikallisen etanaplantaasin kanssa! 
                Olemme odottaneet tätä kauan, ja nyt vihdoinkin tämä saavutus tulee ulos kuorestaan.
                Tietoa etanaplantaaista: tila koostuu (vapaaehtoisista!) etanatyöntekijöistä, ja jollakin konstilla he tuottavat energiaa. 
                Plantaasi ei ole tuottanut vielä yhtään energiayksikköä, mutta emme ole tästä huolissamme. 
                Uskomme että yhteistyömme tuo iloa, tulosta ja hyvää kärsivällisyyden opettelua. Mitä hitaampi, sen parempi! Tätä mieltä olemme Slowrunissa!""",
                "date": timezone.now() + timedelta(days=2),
                "picture": "images/mushroom4.jpg"
            }
        ]

        for item in data:
            Uutinen.objects.create(
                title=item["title"],
                content=item["content"],
                date=item["date"],
                picture=item["picture"]
            )

        self.stdout.write(self.style.SUCCESS("Uutiset luotu!"))