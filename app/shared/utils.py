from app.shared.models import db
from app.generator.models import Name, Skill, Attribute, Item
from app.account.models import User

from werkzeug.security import generate_password_hash

def populate_db():
    #n1 = Name(name='Nazwa Bohatera pierwszego')
    #n2 = Name(name='Nazwa Bohatera drugiego')
    #n3 = Name(name='Nazwa Bohatera trzeciego')

    
    # Source: https://vallheru.eu/generator-imion.php
    db.session.add_all([
        Name(name="Achivo"),
        Name(name="Geraragipo"),
        Name(name="Filion"),
        Name(name="Kythrid"),
        Name(name="Dantisab"),
        Name(name="Deloff"),
        Name(name="Dymyanki"),
        Name(name="Avenrra"),
        Name(name="Ioandara"),
        Name(name="Zorgafvab"),
        Name(name="Rhina"),
        Name(name="Eldirik"),
        Name(name="Canlight"),
        Name(name="Yaved"),
        Name(name="Ghorwacs"),
        Name(name="Harriel"),
        Name(name="Orrrun"),
        Name(name="Ketrid"),
        Name(name="Besidhard"),
        Name(name="Kharl"),
        Name(name="Arlin"),
        Name(name="Samom"),
        Name(name="Torlad"),
        Name(name="Kacil"),
        Name(name="Airina"),
        Name(name="Pesidonfana"),
        Name(name="Ketolite"),
        Name(name="Hanandil"),
        Name(name="Eria"),
        Name(name="Orriel"),
        Name(name="Adlin"),
        Name(name="Erom"),
        Name(name="Zoruin"),
        Name(name="Eowriel"),
        Name(name="Kylur"),
        Name(name="Gerrid"),
        Name(name="Brunhun"),
        Name(name="Groivo"),
        Name(name="Marhawk"),
        Name(name="Gusgran"),
        Name(name="Khaendil"),
        Name(name="Malllana"),
        Name(name="Amilan"),
        Name(name="Timorin"),
        Name(name="Hilin"),
        Name(name="Nasttram"),
        Name(name="Nastmythe"),
        Name(name="Usnipfit"),
        Name(name="Timorenite"),
        Name(name="Tallavo")
    ])

    

    #db.session.add_all([n1, n2, n3])

    #for i in range(4,6):
    #    db.session.add(Name(name='n'+str(i)))

    u1 = User(id='1', name='admin', password=generate_password_hash('adminadmin'), moderator=True)
    u2 = User(id='2', name='user1', password=generate_password_hash('passpass11'), moderator=False)
    db.session.add_all([u1, u2])

    #a1 = Attribute(name='Cecha pierwsza')
    #a2 = Attribute(name='Cecha druga')
    #a3 = Attribute(name='Cecha trzecia')

    # source: https://wikiarpg.fandom.com/pl/wiki/Cechy_charakteru
    db.session.add_all([
        Attribute(name="Ambitny"),
        Attribute(name="Dobroczyńca"),
        Attribute(name="Gaduła"),
        Attribute(name="Gracz"),
        Attribute(name="Kreatywny"),
        Attribute(name="Odważny"),
        Attribute(name="Pacyfista"),
        Attribute(name="Przedsiębiorczy"),
        Attribute(name="Religijny"),
        Attribute(name="Romantyk"),
        Attribute(name="Wierny"),
        Attribute(name="Zabawowy"),
        Attribute(name="Agresywny"),
        Attribute(name="Amnezja"),
        Attribute(name="Cichy"),
        Attribute(name="Egoista"),
        Attribute(name="Fanatyk religijny"),
        Attribute(name="Fobia"),
        Attribute(name="Hazardzista"),
        Attribute(name="Leniwy"),
        Attribute(name="Materialista"),
        Attribute(name="Ponury"),
        Attribute(name="Uzależniony"),
        Attribute(name="Wredny"),
        Attribute(name="Zdrajca")
    ])

    #for i in range(4,6):
    #    db.session.add(Attribute(name='a'+str(i)))

    #db.session.add_all([a1, a2, a3])

    # s1 = Skill(name='Umiejętność pierwsza')
    # s2 = Skill(name='Umiejętność druga')
    # s3 = Skill(name='Umiejętność trzecia')


    # for i in range(4,6):
    #     db.session.add(Skill(name='s'+str(i)))

    # db.session.add_all([s1, s2, s3])

    # Source: https://grooove.pl/skills/
    db.session.add_all([
        Skill(name="Koncentracja many"),
        Skill(name="Kula ognia"),
        Skill(name="Lodowy pocisk"),
        Skill(name="Porażenie"),
        Skill(name="Sprawność fizyczna"),
        Skill(name="Chwila skupienia"),
        Skill(name="Leczenie ran"),
        Skill(name="Zdrowa atmosfera"),
        Skill(name="Cios krytyczny"),
        Skill(name="Fuzja żywiołów"),
        Skill(name="Duszący pocisk"),
        Skill(name="Wrodzona szybkość"),
        Skill(name="Magiczna osłona"),
        Skill(name="Szadź"),
        Skill(name="Spowalniające uderzenie"),
        Skill(name="Rozładowujący pocisk"),
        Skill(name="Rytualne szaty"),
        Skill(name="Potęga błyskawic"),
        Skill(name="Potęga zimna"),
        Skill(name="Potęga ognia"),
        Skill(name="Przetrwanie"),
        Skill(name="Moc leczenia"),
        Skill(name="Krytyczna potęg"),
        Skill(name="Stopiona skóra"),
        Skill(name="Wyładowanie energii"),
        Skill(name="Apogeum"),
        Skill(name="Wzmocniony pancerz"),
        Skill(name="Determinacja"),
        Skill(name="Mroźne sople"),
        Skill(name="Wytrwałość elementalisty"),
        Skill(name="Lodowa bariera"),
        Skill(name="Elektryczna bariera"),
        Skill(name="Płonąca bariera"),
        Skill(name="Trwałość mocy"),
        Skill(name="Osłabienie"),
        Skill(name="Klątwa"),
        Skill(name="Wewnętrzny spokój"),
        Skill(name="Płatnerstwo"),
        Skill(name="Źródło potęgi"),
        Skill(name="Szybki atak"),
        Skill(name="Pchnięcie mrozu"),
        Skill(name="Gorące uderzenie"),
        Skill(name="Porażający cios"),
        Skill(name="Moc sprawiedliwych"),
        Skill(name="Prowokujący okrzyk"),
        Skill(name="Aura szybkości"),
        Skill(name="Gniew bogów"),
        Skill(name="Skupienie na celu"),
        Skill(name="Błogosławiona ochrona"),
        Skill(name="Strażnik boskich mocy"),
        Skill(name="Aura ochrony"),
        Skill(name="Srebrzysty blask"),
        Skill(name="Hart ducha"),
        Skill(name="Odnowa mocy"),
        Skill(name="Krytyczne uderzenie"),
        Skill(name="Fala leczenia"),
        Skill(name="Krytyczna moc ognia"),
        Skill(name="Krytyczna moc błyskawic"),
        Skill(name="Krytyczna moc zimna"),
        Skill(name="Przeszywające uderzenie"),
        Skill(name="Parowanie"),
        Skill(name="Witalność"),
        Skill(name="Rozpraszający cios"),
        Skill(name="Porażająca tarcza"),
        Skill(name="Splot odporności"),
        Skill(name="Tarcza słońca"),
        Skill(name="Łaska Gerdeth"),
        Skill(name="Niebiańska ochrona"),
        Skill(name="Aura życia"),
        Skill(name="Parada"),
        Skill(name="Strach"),
        Skill(name="Końskie zdrowie"),
        Skill(name="Kula światłości")
    ])

    # source: https://gexe.pl/forum/t/10365,spis-przedmiotow
    db.session.add_all([
        Item(name="Adjatha Wysysacz"),
        Item(name="Albruin"),
        Item(name="Amulet Mistrza Harfiarzy"),
        Item(name="Amulet Seldarine"),
        Item(name="Amulet Szybkości Geparda"),
        Item(name="Amulet blokowania czarów"),
        Item(name="Amulet metaczarów"),
        Item(name="Amulet mocy"),
        Item(name="Amulet ochrony"),
        Item(name="Amulet ochrony przed trucizną"),
        Item(name="Amulet ochrony życia"),
        Item(name="Amulet odporności na magię"),
        Item(name="Amulet tarczy"),
        Item(name="Amulet wilczej jagody"),
        Item(name="Amulet z nefrytem"),
        Item(name="Beljuryl"),
        Item(name="Belm"),
        Item(name="Berło absorpcji"),
        Item(name="Berło dostojnej potęgi"),
        Item(name="Berło przerażenia"),
        Item(name="Berło uderzenia"),
        Item(name="Berło zmartwychwstania"),
        Item(name="Bladozielony kamień Ioun"),
        Item(name="Bransolety Tzu-Zana"),
        Item(name="Bransolety błogosławieństwa"),
        Item(name="Bransolety błyskawicznego uderzenia"),
        Item(name="Bransolety ochrony"),
        Item(name="Bransolety paladyna"),
        Item(name="Bransolety pętania"),
        Item(name="Bransolety łucznictwa"),
        Item(name="Brązowe pantalony"),
        Item(name="Brązowy kamień Ioun"),
        Item(name="Brązowy róg Walhalli"),
        Item(name="Butla Ifrita"),
        Item(name="Buty Elfów"),
        Item(name="Buty Północy"),
        Item(name="Buty Zachodu"),
        Item(name="Buty szybkości"),
        Item(name="Buty eteryczności"),
        Item(name="Buty gorgony"),
        Item(name="Buty przemieszczania"),
        Item(name="Buty ukrycia"),
        Item(name="Buty uników"),
        Item(name="Buty uziemienia")
    ])

    #i1 = Item(name='Przedmiot pierwszy')
    #i2 = Item(name='Przedmiot drugi')
    #i3 = Item(name='Przedmiot trzeci')

    #for i in range(4,6):
    #    db.session.add(Item(name='i'+str(i)))

    #db.session.add_all([i1, i2, i3])
    db.session.commit()
