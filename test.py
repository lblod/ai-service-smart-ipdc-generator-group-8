from src.llm.extract import extract_ipdc_data
from contexttimer import Timer

TEST_DATA = '''Belasting op het afzetten of
innemen van de openbare wegenis van 1
januari 2020 tot en met 31 december
2025
Goedgekeurd door de gemeenteraad van
4 mei 2020
Artikel 1
De gemeente Sint-Katelijne-Waver heft met ingang van 1 januari 2020 en voor een termijn eindigend
op 31 december 2025 een belasting op het innemen van de openbare ruimte door het plaatsen van
schutsels, afsluitingen, stellingen, kranen, containers, machines, bouwmaterialen, laad- en
betonbakken, werfwagens, werktuigen en voertuigen ter gelegenheid van het bouwen of verbouwen
van onroerende goederen (inclusief schilderwerken en/of gevelreiniging).
Artikel 2
Alvorens tot de inname mag worden overgegaan, dient men hiervoor de toelating verkregen te
hebben bij het gemeentebestuur.
Artikel 3
De belasting is verschuldigd door de natuurlijke persoon of rechtspersoon die de aanvraag indient en
bij gebreke daaraan degene die de openbare ruimte in gebruik neemt.
De opdrachtgever voor wiens rekening het werk wordt uitgevoerd, is medeverantwoordelijk voor de
volledige betaling van de belasting.
Artikel 4
De belasting bedraagt 0,50 euro per vierkante meter en per kalenderdag zolang de inname van de
oppervlakte van de openbare ruimte blijft bestaan. Een begonnen vierkante meter wordt aanzien als
een volledige vierkante meter. Een begonnen kalenderdag wordt eveneens aanzien als een volledige
kalenderdag.
Luifelvormige constructies voor steenvang worden volledig belast.
Voor het plaatsen van een container bedraagt de belasting forfaitair 7,50 euro per dag.
De minimumaanslag bedraagt evenwel 20 euro per afgeleverde vergunning of inname.
Indien omwille van veiligheidsredenen de openbare weg (voetpad, fietspad, rijweg) geheel of
gedeeltelijk wordt afgesloten, moet een signalisatievergunning aangevraagd worden bij het
gemeentebestuur. In dit geval wordt de belasting voor de eerste dag van afsluiting verhoogd met 50
euro. Per volgende kalenderdag bedraagt de bijkomende belasting 25 euro.
Indien de aanvraag niet ten minste 5 werkdagen op voorhand werd aangevraagd, zal er een extra
kost van 20 euro worden aangerekend voor de spoedprocedure.
Artikel 5
Indien de inname van de openbare ruimte vroeger eindigt dan werd medegedeeld of wanneer de
gevraagde inname niet meer gewenst is, dient de aanvrager de gemeentediensten hiervan minimum 1
werkdag voor de stopzetting van de inname schriftelijk in kennis te stellen, zodat nazicht mogelijk is.
Enkel in die gevallen kan de belasting geheel of gedeeltelijk terugbetaald worden en dit in verhouding
met het aantal dagen effectieve inname.
Indien de inname van de openbare ruimte tijdelijk opgeschort werd naar aanleiding van de
coronamaatregelen tijdens de crisisperiode zoals vastgesteld door de Vlaamse Regering in artikel 4, §
1, eerste lid, 1° van het decreet van 20 maart 2020 over maatregelen in geval van een civiele
noodsituatie met betrekking tot de volksgezondheid, dient de aanvrager het gemeentebestuur hiervan
op de hoogte te stellen, zodat de periode van betaling voor deze inname ook tijdelijk kan opgeschort
worden. Bij hervatting van de werkzaamheden dient de aanvrager dit ten laatste 3 werkdagen op
voorhand opnieuw door te geven aan de dienst openbare werken.

1/3

Artikel 6
Aanvragen ingediend door of in naam van volgende entiteiten zijn vrijgesteld van de belasting:
• Overheid(sinstanties);
• Sociale huisvestingsmaatschappijen;
• Instellingen van openbaar nut zoals o.m. de nuts- en vervoersmaatschappijen;
• Onderwijsinstellingen gesubsidieerd door de overheid;
• Intergemeentelijke verenigingen die vallen onder het decreet intergemeentelijke
samenwerking dd. 6 juli 2001 of latere wijzigingen.
Gelet op het openbare dienst karakter van deze entiteiten is het niet wenselijk hun werking door deze
belasting te bezwaren.
De belasting wordt niet toegepast:
• bij restauratie van gebouwen, door het college van burgemeester en schepenen erkend
als zijnde van architectonische of historische waarde;
• bij heropbouw van door oorlogsfeiten of door brand vernielde of beschadigde gebouwen.
Om voor de vrijstelling in aanmerking te komen, dient de uitvoerder voorafgaandelijk aan de
werfinrichting een plan ter goedkeuring voor te leggen aan de gemeente. De vrijstelling geldt dus niet
voor het bekomen van de toelating op zich.
Afhankelijk van de ingenomen oppervlakte en periode van de inname kan er een waarborg van 400
euro gevraagd worden.
De vrijgestelde entiteit is verplicht om vóór de aanvang van de werken een plaatsbeschrijving van het
openbaar domein ter hoogte van de bouwplaats te laten opstellen door een beëdigd landmeter, de
architect, de aannemer of deze zelf te maken en deze te dienen op de dienst Openbare Werken, bij
voorkeur via mail.
De vrijgestelde entiteit is daarenboven verplicht de waarborg in bewaring te geven bij de financieel
directeur of zijn afgevaardigde voor aanvang van de werken.
De vrijgestelde entiteit moet na het beëindigen van de bouwwerken de waarborg schriftelijk
terugvragen. Indien de openbare weg zich nog in de oorspronkelijke staat van voor de werken
bevindt, wordt de waarborg terug vrijgegeven. Indien dit niet het geval is, wordt de waarborg
verminderd met de door het bestuur gemaakte herstelkosten; Indien de waarborg niet zou volstaan
om de herstelkosten te dekken, wordt een bijkomende vordering aan de bouwheer overgemaakt.
Er geldt een tijdelijke vrijstelling voor handelaars die de parkeerplaats voor hun handelszaak kunnen
aanvragen via het online platform van inname openbaar domein, om zo maximaal mogelijk in te
spelen op de van kracht zijnde maatregelen genomen door de hogere overheid tijdens de
crisisperiode zoals vastgesteld door de Vlaamse Regering in artikel 4, § 1, eerste lid, 1° van het
decreet van 20 maart 2020 over maatregelen in geval van een civiele noodsituatie met betrekking tot
de volksgezondheid. Deze aanvraag is gratis voor de handelaars tot het einde van de ingestelde
maatregelen. De aanvraag betreft zowel de inname als de plaatsing van de verkeersborden door de
gemeentelijke diensten.

2/3

Artikel 7
Op het ogenblik van de aanvraag van de inname wordt het bedrag van de belasting contant in
bewaring gegeven in handen van de financieel directeur of zijn afgevaardigde, tegen afgifte van
ontvangstbewijs.
Op het moment van inname wordt het in bewaring gegeven bedrag van ambtswege als een
verworven contantbelasting geboekt.
Bij gebrek aan een contantbelasting of indien het in bewaring gegeven bedrag niet in
overeenstemming is met de reële belastingschuld, zal van ambtswege tot inkohiering van de gehele of
gedeeltelijke belasting worden overgegaan.
Bij gebreke van een aangifte of bij onvolledige, onjuiste of onnauwkeurige aangifte wordt de
belastingplichtige ambtshalve belast volgens de gegevens waarover het gemeentebestuur beschikt,
onverminderd het recht van bezwaar of beroep. De periode van niet-aangifte of onjuiste aangifte,
dienende tot het berekenen van de aanslag, wordt ambtshalve vastgesteld op verslag van een
beëdigd aangestelde van de gemeente. Deze ambsthalve ingekohierde belasting wordt verhoogd met
50%.
Artikel 8
Indien de inname van de openbare ruimte plaats vindt op parkeerplaatsen waar het regime van de
blauwe zone geldt, is de aanvrager vrijgesteld van het plaatsen van een parkeerschijf zolang men
beschikt over een toelating inname openbaar domein.
Artikel 9
De vestiging, de invordering en de geschillenprocedure gebeurt volgens de modaliteiten vervat in het
decreet van 30 mei 2008 betreffende de vestiging, de invordering en de geschillenprocedure van
provincie- en gemeentebelastingen en latere wijzigingen.
Artikel 10
Dit reglement zal worden bekendgemaakt overeenkomstig artikelen 285 tot en met 288 en artikel 330
van het decreet lokaal bestuur.
Artikel 11
Het technisch reglement waarin de modaliteiten m.b.t. het afzetten en innemen van de openbare
wegenis wordt geregeld, wordt goedgekeurd zoals in bijlage toegevoegd.

3/3'''


if __name__ == '__main__':
    with Timer() as t:
        print(extract_ipdc_data(text=TEST_DATA))
    print(f'Generating response from the LLM took: {t.elapsed} seconds')
