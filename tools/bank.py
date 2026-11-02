#!/usr/bin/env python3
"""Erzeugt app/src/main/assets/typfinder.json (Fragenbank des Typ-Finders).
Alle Fragen stammen aus den Beschreibungen des Buches (S. 10, 14-24, 25-37, 79-82)."""
import json, os
Q = []
def add(**k): Q.append(k)

# ---- Stufe A: Instinkt (Optionen: sp, so, sx) ----
A = [
 ("Du hast einen freien Tag ohne Pflichten. Was zieht dich zuerst?",
  "Zuhause alles ordnen, Gesundheit, Geld, Vorräte, damit ich es bequem und sicher habe.",
  "Etwas mit Menschen aus meinem Umfeld: Verein, Freunde, Nachbarn, eine Gruppe.",
  "Ein einzelner Mensch, bei dem es knistert und in die Tiefe geht."),
 ("Wenn es dir schlecht geht: Was fehlt dir dann am meisten?",
  "Dass ich mir keine Sorgen um Alltag, Geld, Schlaf und Wärme machen muss.",
  "Dass ich dazugehöre und gebraucht werde.",
  "Dass mich jemand wirklich sieht und die Verbindung intensiv ist."),
 ("Was würdest du am schwersten ertragen?",
  "Dass meine Lebensgrundlage unsicher wird.",
  "Dass ich keinen wirklichen Platz mehr in meinem sozialen Umfeld habe.",
  "Dass eine wichtige Verbindung oberflächlich oder bedeutungslos wird."),
 ("Wofür gibst du, wenn du ehrlich bist, am meisten Zeit und Geld aus?",
  "Für Wohnen, Gesundheit, Komfort und Sicherheit.",
  "Für Gruppen, Veranstaltungen, Ehrenämter, Netzwerke.",
  "Für besondere Momente und Reisen mit einzelnen Menschen."),
 ("Du betrittst einen Raum voller Menschen. Worauf achtest du zuerst?",
  "Ob es warm genug ist, wo ich sitzen kann, wo es etwas zu essen gibt.",
  "Wer wie viel Gewicht hat, wer zu wem gehört, wie die Stimmung in der Gruppe ist.",
  "Wo Energie ist, wer mir auffällt und mit wem es spannend werden könnte."),
 ("Wann fühlst du dich am lebendigsten?",
  "Wenn es mir körperlich gut geht, alles geregelt und gemütlich ist.",
  "Wenn ich in einer Gruppe etwas bewege oder zu etwas dazugehöre.",
  "Wenn mit jemandem die Funken sprühen und ein tiefes Gespräch entsteht."),
 ("In welchem Bereich hattest du im Leben die meisten Krisen?",
  "Existenz, Gesundheit, Geld oder Wohnen.",
  "Gruppen: Team, Verein, Familie, meine Rolle darin.",
  "Enge Beziehungen: Verlieben, Trennung, Nähe."),
 ("Du ziehst um. Was ist dir bei der neuen Wohnung am wichtigsten?",
  "Zustand, Sicherheit, Komfort und Kosten.",
  "Nachbarschaft, Gemeinschaft und wie die Gegend angesehen ist.",
  "Dass mein Lieblingsmensch dort mit mir glücklich wird und wir Raum für uns haben."),
 ("Du bist krank und erschöpft. Was brauchst du?",
  "Ruhe, Wärme, vertraute Routinen und alles Nötige im Haus.",
  "Dass mein Umfeld Bescheid weiß und mich nicht vergisst.",
  "Einen Menschen ganz nah bei mir."),
 ("Dein schönster Moment im Urlaub ist ...",
  "... ein gutes Bett, gutes Essen und dass der Plan klappt.",
  "... ein Ausflug mit der Gruppe und neue Leute kennenlernen.",
  "... ein besonderer Moment zu zweit."),
]
for i,(q,a,b,c) in enumerate(A,1):
    add(id=f"A{i:02d}", st="A", q=q, o=[{"t":a,"w":{"sp":2}},{"t":b,"w":{"so":2}},{"t":c,"w":{"sx":2}}])
# Blinder Fleck (der dritte Instinkt wird oft vernachlässigt)
for i,(q,a,b,c) in enumerate([
 ("Was kommt in deinem Leben am ehesten zu kurz?",
  "Mein Alltag: Geld, Gesundheit, Ordnung, Vorsorge.",
  "Gruppen, Netzwerke und Verpflichtungen im Umfeld.",
  "Enge Eins-zu-eins-Beziehungen und Intensität."),
 ("Wo fällt es dir am schwersten, dich zu kümmern?",
  "Um Geld, Haushalt und meine Gesundheit.",
  "Um Kontakte, Termine, Gruppenregeln und Einladungen.",
  "Um Nähe und Tiefe in einzelnen Beziehungen.")],10):
    add(id=f"A{i:02d}", st="A", blind=True, q=q, o=[{"t":a,"w":{"sp":-1.5}},{"t":b,"w":{"so":-1.5}},{"t":c,"w":{"sx":-1.5}}])
add(id="A12", st="A", q="Denk an die letzten Jahre. Wofür hast du wirklich Zeit und Geld gegeben?",
    o=[{"t":"Für Alltag und Sicherheit.","w":{"sp":2}},{"t":"Für Gruppen und Ämter.","w":{"so":2}},{"t":"Für einzelne Beziehungen.","w":{"sx":2}}])


# ---- Stufe S: Seite (Buch S. 8: männlich 5-8 ausrichtend, weiblich 1-4 aufnehmend, die 9 vermittelt) ----
S = [
 ("Worauf richtet sich deine spontane Aufmerksamkeit zuerst?",
  "Auf die äußeren Bedingungen und meine Handlungsmöglichkeiten.",
  "Auf meine eigene Position und die persönliche Bedeutung einer Situation.",
  "Auf das Zusammenführen und Beruhigen der Situation."),
 ("Du lernst eine neue Person kennen. Worauf richtet sich deine Aufmerksamkeit spontan?",
  "Wie sie denkt, was sie beabsichtigt und wie ich sie einschätze.",
  "Wie ich auf sie wirke und welche persönliche Verbindung entsteht.",
  "Ich nehme zunächst die Situation auf und passe mich dem Kontakt an."),
 ("Ein unerwartetes Problem taucht auf. Was tust du typischerweise zuerst?",
  "Ich analysiere die Lage, prüfe Optionen oder greife ein.",
  "Ich ordne ein, was es für mich bedeutet und was jetzt richtig wäre.",
  "Ich lasse die Situation zunächst auf mich wirken und suche einen Weg ohne unnötige Reibung."),
 ("Nach einem Konflikt: Was bleibt bei dir am ehesten hängen?",
  "Die Ursachen, die Argumente, die Grenzen oder die ungelöste Sachfrage.",
  "Die persönliche Bedeutung, die Beziehung oder meine eigene Reaktion.",
  "Der Wunsch, wieder Ruhe zu haben und die Sache hinter mir zu lassen."),
 ("In einer Gruppe fällt dir meistens welche Rolle zu?",
  "Orientierung und Schutz geben, Ziele verfolgen.",
  "Beziehungen gestalten und anderen Entwicklung ermöglichen.",
  "Zwischen den anderen vermitteln und verbinden."),
 ("Welcher Satz passt besser zu dir?",
  "„Ich setze in Bewegung.“",
  "„Ich lasse entstehen.“",
  "„Ich verbinde, was auseinanderstrebt.“"),
]
for i,(q,a,b,c) in enumerate(S,1):
    add(id=f"S{i:02d}", st="S", q=q, o=[{"t":a,"w":{"mann":1}},{"t":b,"w":{"frau":1}},{"t":c,"w":{"neun":1}}])
# Körperliche Hinweise und Ausstrahlung (stehen im Ablauf VOR den Verhaltensfragen). „Weiß nicht“ gibt es bei jeder Frage.
SK = [
 ("Wie ist deine Stimme (falls du das einschätzen kannst)?",
  "Eher tief.", "Eher hoch, hell oder weich.", None),
 ("Wie ist deine Nase?",
  "Eher kräftig oder markant.", "Eher fein und zart.", None),
 ("Welche Körperform hast du eher?",
  "Eine ausgeprägte V-Form: breite Schultern, nach unten schmaler.", "Eher weich und rund, mit breiteren Hüften als Schultern.", None),
 ("Wie ist dein Haaransatz an der Stirn?",
  "Mit Geheimratsecken.", "Eher tief, mit niedriger Stirn.", None),
 ("Unabhängig vom Geschlecht: Wie wirkt dein Gesamtausdruck auf andere?",
  "Eher männlich: kraftvoll, ausrichtend, schützend.", "Eher weiblich: weich, aufnehmend, verbindend.", "Gemischt oder androgyn: beides ist da."),
 ("Und wie schätzt du dich selbst ein, ebenfalls unabhängig vom Geschlecht?",
  "Eher männlich in meinem Wesen und Ausdruck.", "Eher weiblich in meinem Wesen und Ausdruck.", "Gemischt oder androgyn: beides gehört zu mir."),
 ("Wie ist deine Ausdrucksform beim Sprechen?",
  "Direkt, sachlich und entschieden.", "Einfühlsam, bildhaft und beziehungsorientiert.", "Ausgleichend, abwägend und vermittelnd."),
 ("Und deine Körpersprache?",
  "Raumgreifend, mit klaren Gesten und festem Stand.", "Weich, fließend und zugewandt.", "Ruhig, zurückhaltend und angepasst."),
]
SK.insert(4, ("Wie ist deine Blickführung (falls du das bei dir beobachten kannst)?",
  "Eher prüfend und fokussiert, mit etwas Distanz: beobachtend, abschätzend oder situationsabhängig konfrontativ.",
  "Eher persönlich: mit Ausdrucksbewegung, erkennbarer Bewertung oder Resonanz und Aufmerksamkeit für die Reaktion des Gegenübers.",
  "Eher weich und entspannt, peripher wahrnehmend, wenig konfrontativ, aufnehmend."))
for i,(q,a,b,c) in enumerate(SK,1):
    wt=0.5 if i<=4 else 1.0      # Körpermerkmale (1-4) sind nur ein schwacher Hinweis
    o=[{"t":a,"w":{"mann":wt}},{"t":b,"w":{"frau":wt}}]
    if c: o.append({"t":c,"w":({} if "androgyn" in c else {"neun":wt})})
    add(id=f"SK{i:02d}", st="S", body=True, q=q, o=o)

# ---- Blickqualität (Buch S. 95-108) ----
BL = [
 ("Wie würdest du deinen Blick beschreiben? Ist er warm und weich oder eher anders?",
  [("Warm, weich, zugewandt.",{"2":1,"9":1,"4":1,"7":0.5}),
   ("Direkt, klar, eher kühl oder prüfend.",{"8":1,"1":1,"3":1,"5":1,"6":0.5})]),
 ("Welche Beschreibung passt am ehesten zu deinem Blick?",
  [("Liebevoll und weich, mit großen Augen, auf Verbindung aus.",{"2":2}),
   ("Gutmütig und aufnehmend, eher peripher, ohne zu bewerten.",{"9":2}),
   ("Kraftvoll, fordernd und durchdringend. Ich halte den Blickkontakt.",{"8":2}),
   ("Prüfend und fokussiert wie ein Laser. Ich sehe, was nicht stimmt.",{"1":2}),
   ("Kontrolliert, die Augen eng. Ich achte darauf, wie ich wirke.",{"3":2}),
   ("Einschätzend und wachsam, manchmal erschrocken oder ängstlich.",{"6":2}),
   ("Beobachtend, analytisch und vorsichtig. Ich halte Abstand.",{"5":2}),
   ("Tiefgründig und emotional, manchmal traurig.",{"4":2}),
   ("Strahlend, optimistisch und neugierig.",{"7":2})]),
 ("Was geht dir beim ersten Blick auf einen Menschen durch den Kopf?",
  [("„Ich möchte eine persönliche Verbindung herstellen.“",{"2":2}),
   ("„Ich möchte eine entspannte Atmosphäre erhalten.“",{"9":2}),
   ("„Sagst du mir die Wahrheit, und stehst du dazu?“",{"8":2}),
   ("„Ist das richtig und vertretbar?“",{"1":2}),
   ("„Ich möchte positiv und kompetent wirken.“",{"3":2}),
   ("„Ich bin unsicher, wie ich dich einschätzen soll.“",{"6":2}),
   ("„Was steckt dahinter? Ergibt das Sinn?“",{"5":2}),
   ("„Die Begegnung berührt mich, und ich ziehe mich kurz zurück.“",{"4":2}),
   ("„Ich möchte Leichtigkeit und Möglichkeiten vermitteln.“",{"7":2})]),
 ("Wie wirkt dein Blick laut anderen auf sie?",
  [("Warm, persönlich, verbunden.",{"2":2}),
   ("Beruhigend, annehmend, entlastend.",{"9":2}),
   ("Stark, klar, manchmal einschüchternd.",{"8":2}),
   ("Respekteinflößend, aber auch Anspannung und Bewertung.",{"1":2}),
   ("Kompetent und dynamisch, manchmal Leistungsdruck.",{"3":2}),
   ("Aufmerksam, vorsichtig, Vertrauen prüfend.",{"6":2}),
   ("Rätselhaft, respektvoll, distanziert.",{"5":2}),
   ("Faszinierend, nah, manchmal melancholisch.",{"4":2}),
   ("Lebendig, optimistisch, ansteckend.",{"7":2})]),
]
# ---- Stufe Z: körperliche Hinweise (nur Tendenzen, nie ein Ausschluss: „Nein“ hat bewusst kein Gewicht) ----
ZK = [
 ("Hast oder hattest du eine ausgeprägte Akne?",
  "Ja, deutlich.", {"6":1,"9":1,"1":1,"4":1}),
 ("Kaust du an den Fingernägeln?",
  "Ja, regelmäßig oder früher häufig.", {"9":1,"7":1}),
 ("Hast du rheumatische Beschwerden (zum Beispiel Gelenkschmerzen oder Steifheit)?",
  "Ja.", {"7":1}),
]
add(id="Z1", st="Z", q="Wenn du deine Stirn im Spiegel betrachtest: Wie sehen deine Stirnfalten aus? (Mehrere Antworten sind möglich.)",
    o=[{"t":"Eine ausgeprägte senkrechte Falte zwischen den Augenbrauen (die „Zornesfalte“).","w":{"1":1.5,"9":1.5}},
       {"t":"Querfalten, die wie ein V auf der Stirn angeordnet sind.","w":{"3":1.5}},
       {"t":"Eher glatt oder andere Falten, ohne senkrechte Falte und ohne V.","w":{}}])
for i,(q,yes,w) in enumerate(ZK,2):
    add(id=f"Z{i}", st="Z", q=q, o=[{"t":yes,"w":w},{"t":"Nein oder kaum.","w":{}}])
for i,(q,opts) in enumerate(BL,1):
    add(id=f"BL{i}", st="K", q=q, o=[{"t":t_,"w":w_} for t_,w_ in opts])
# Beobachtbare Dimensionen des Blicks und der Mimik (Selbstbeobachtung; sanfte Hinweise)
KO = [
 ("Blickkontakt: Was beschreibt dich am besten (falls du das bei dir beobachten kannst)?",
  [("Ich suche den Blickkontakt, um Nähe oder Resonanz herzustellen.",{"2":1,"4":1,"7":0.5}),
   ("Ich halte den Blickkontakt, auch prüfend oder konfrontierend.",{"8":1,"1":1,"6":0.5,"3":0.5}),
   ("Ich weiche dem Blickkontakt eher aus oder nehme ihn nur kurz auf.",{"5":1,"9":1,"4":0.5})]),
 ("Blickfokus: Wie ist dein Blick im Gespräch?",
  [("Er fixiert und prüft.",{"1":1,"8":1,"6":1,"3":0.5}),
   ("Er schweift, nimmt vieles am Rand wahr.",{"9":1,"7":1}),
   ("Er beobachtet ruhig und analysiert.",{"5":1.5,"6":0.5})]),
 ("Mimik: Wie ist deine Mimik meistens?",
  [("Eher kontrolliert.",{"3":1,"1":1,"5":0.5}),
   ("Eher ausdrucksvoll.",{"2":1,"4":1,"7":1}),
   ("Eher ruhig und gleichmäßig.",{"9":1,"5":1})]),
 ("Muskelspannung: Wie wirkt dein Gesicht?",
  [("Angespannt, zum Beispiel um Kiefer, Stirn oder Augen.",{"1":1,"6":1,"3":0.5}),
   ("Kraftvoll und präsent.",{"8":1.5,"3":0.5}),
   ("Entspannt und weich.",{"9":1,"7":0.5,"2":0.5})]),
 ("Bewegungsdynamik: Wie wirkst du in der Bewegung?",
  [("Zielgerichtet.",{"3":1,"8":1,"1":0.5}),
   ("Zurückhaltend.",{"5":1,"4":0.5,"6":0.5}),
   ("Ausgleichend.",{"9":1,"2":0.5})]),
]
for i,(q,opts) in enumerate(KO,1):
    add(id=f"KO{i}", st="K", q=q, o=[{"t":t_,"w":w_} for t_,w_ in opts])

# ---- Stufe B: Zentrum (Optionen: bauch, herz, kopf) ----
B = [
 ("Jemand überschreitet im Alltag deine Grenze. Was passiert zuerst?",
  "Ich reagiere sofort, spürbar im Körper: Ich wehre mich oder halte dagegen.",
  "Ich frage mich, was das über mich aussagt und wie ich gesehen werde.",
  "Ich gehe durch, was daraus folgen kann, und bereite mich vor."),
 ("In einer Krise: Was gibt dir zuerst Halt?",
  "Selbst entscheiden und handeln.",
  "Anerkennung und Resonanz von anderen.",
  "Verstehen, Informationen und ein Plan."),
 ("Welche Grundstimmung begleitet dich bei Druck am ehesten?",
  "Ärger oder Widerstand.",
  "Scham oder Zweifel am eigenen Wert.",
  "Angst oder Unsicherheit."),
 ("Du denkst morgens an einen schwierigen Tag. Was geschieht in dir?",
  "Ich spüre Spannung im Körper und will loslegen oder mich durchsetzen.",
  "Ich überlege, wie ich ankomme und wie andere mich sehen.",
  "Ich gehe im Kopf Möglichkeiten durch und was schiefgehen kann."),
 ("Was ist dir bei einer Entscheidung am wichtigsten?",
  "Dass ich selbst bestimme und mich nicht fremdbestimmen lasse.",
  "Dass es zu mir und meinem Selbstbild passt und wie ich gesehen werde.",
  "Dass ich genug Informationen habe und abgesichert bin."),
 ("Was wirfst du dir nachträglich am ehesten vor?",
  "Dass ich zu heftig reagiert oder zu spät gehandelt habe.",
  "Dass ich mich zu wenig gezeigt oder zu viel Wert auf meine Wirkung gelegt habe.",
  "Dass ich zu lange gezögert, gegrübelt oder mich nicht vorbereitet habe."),
 ("Was strengt dich bei anderen am meisten an?",
  "Wenn mich jemand bevormundet oder herumschubst.",
  "Wenn jemand meinen Wert nicht sieht oder mich übergeht.",
  "Wenn jemand unzuverlässig, sprunghaft oder unberechenbar ist."),
 ("Was beschreibt deinen Blick auf die Welt eher?",
  "Was darf sein, wo sind Grenzen, wer hat die Kontrolle?",
  "Wer mag mich, wer sieht mich, wo ist Resonanz?",
  "Was kann passieren, wem kann ich trauen, was ist der Plan?"),
 ("Was hat dich in der Kindheit am meisten geprägt?",
  "Ich musste mich behaupten, durchsetzen oder mich anpassen, um Ruhe zu haben.",
  "Ich habe früh gelernt, was ich tun muss, um gesehen und gemocht zu werden.",
  "Ich habe früh gelernt, vorsichtig zu sein und mich abzusichern."),
 ("Du sollst eine Rede halten. Wie gehst du vor?",
  "Ich rede aus dem Bauch, mit wenig Notizen.",
  "Ich überlege, wie ich wirke und wie das Publikum mich aufnimmt.",
  "Ich bereite mich gründlich vor und gehe mögliche Einwände durch."),
 ("Streit mit einem Freund. Wie ist das bei dir?",
  "Ich werde schnell laut oder verbissen, die Wut ist spürbar.",
  "Ich fühle mich verletzt und frage mich, was er von mir hält.",
  "Ich überlege erst, was ich sagen kann, und analysiere die Lage."),
 ("Woran merkst du, dass es dir gut geht?",
  "Ich bin kraftvoll und handlungsfähig.",
  "Ich werde gesehen und wertgeschätzt.",
  "Ich habe Überblick und Sicherheit."),
]
for i,(q,a,b,c) in enumerate(B,1):
    add(id=f"B{i:02d}", st="B", q=q, o=[{"t":a,"w":{"bauch":1}},{"t":b,"w":{"herz":1}},{"t":c,"w":{"kopf":1}}])

# ---- Stufe C: Typen unterscheiden (je Zentrum 8 Dreier-Fragen) ----
def tri(prefix, types, items):
    for i,(q,*opts) in enumerate(items,1):
        add(id=f"{prefix}{i:02d}", st="C", ty=types, q=q,
            o=[{"t":t,"w":{str(ty):2}} for ty,t in zip(types,opts)])
tri("CB", [8,9,1], [
 ("Eine Entscheidung steht an, und die anderen sehen sie unterschiedlich. Was tust du?",
  "Ich sage klar, was ich will, und halte es aus, wenn es knallt.",
  "Ich sehe alle Seiten und merke erst spät, was ich selbst wollte.",
  "Ich sehe sofort, was falsch läuft, und ärgere mich, wenn es nicht stimmt."),
 ("Welche Aussage trifft deine Motivation eher?",
  "Ich setze Stärke bewusst ein und zeige selten, dass mich etwas verletzt.",
  "Ich stimme oft zu, auch wenn ich eigentlich anders möchte, um Ruhe zu haben.",
  "Ich will richtig handeln und Fehler und Kritik vermeiden."),
 ("Wie klingt dein innerer Satz im Streit?",
  "„Mich schiebt keiner herum.“", "„Lass es gut sein, es ist nicht so wichtig.“", "„So ist es nicht in Ordnung.“"),
 ("Wenn der Druck steigt: Was geschieht?",
  "Ich werde dominanter und übernehme das Kommando.",
  "Ich werde passiv, schiebe auf, ziehe mich in Routine oder Ablenkung zurück.",
  "Ich werde strenger, kritischer mit mir und anderen und kontrolliere mehr."),
 ("Was beschreibt deine Kindheit eher?",
  "Ich musste früh stark sein und habe Schwäche versteckt.",
  "Ich habe früh gelernt, nicht zu stören, und meine Wünsche zurückgestellt.",
  "Ich habe früh gelernt, brav und korrekt zu sein. Fehler waren gefährlich."),
 ("Was sagen andere über dich?",
  "Kraftvoll und direkt, manchmal einschüchternd.",
  "Ruhig und ausgleichend, aber schwer zu fassen und manchmal stur.",
  "Gewissenhaft und anspruchsvoll, wirkt manchmal kritisch."),
 ("Wie kam es zu einer großen Wende in deinem Leben?",
  "Ich habe es gegen Widerstände einfach durchgezogen.",
  "Es hat sich irgendwie ergeben. Ich habe lange gezögert und bin mitgeschwommen.",
  "Ich habe lange abgewogen, was richtig ist, und dann konsequent meine Pflicht getan."),
 ("Wie gehst du mit Ärger um?",
  "Ich zeige ihn offen und es ist schnell wieder vorbei.",
  "Ich spiele ihn herunter und er zeigt sich Tage später als Sturheit.",
  "Ich halte ihn zurück und er zeigt sich als Anspannung, Kritik und Perfektionsdruck."),
])
tri("CH", [2,3,4], [
 ("Was treibt dich im Alltag an, wenn du ehrlich bist?",
  "Ich will gebraucht und gemocht werden und für andere da sein.",
  "Ich will etwas erreichen, vorzeigbare Ergebnisse haben und gut dastehen.",
  "Ich will echt sein, etwas Besonderes ausdrücken und nicht austauschbar sein."),
 ("Welche Frage passt eher zu dir?",
  "Wende ich mich frei zu – oder will ich gebraucht und geliebt werden?",
  "Ist Erfolg mein Ziel – oder der Beweis meines Werts?",
  "Drücke ich mich aus – oder spüre ich dem nach, was fehlt?"),
 ("Wenn der Druck steigt:",
  "Ich helfe noch mehr, werde dann aber gekränkt oder fordernd.",
  "Ich arbeite noch mehr, funktioniere und schiebe Gefühle weg.",
  "Ich ziehe mich in Stimmungen zurück, fühle mich missverstanden und hänge am Fehlenden."),
 ("Was beschreibt deine Kindheit eher?",
  "Ich bekam Zuwendung, wenn ich geholfen habe oder die Bedürfnisse anderer sah.",
  "Ich bekam Anerkennung für Leistung und Erfolge.",
  "Ich fühlte mich anders, unverstanden oder besonders."),
 ("Was sagen andere über dich?",
  "Warmherzig und zugewandt, manchmal vereinnahmend oder empfindlich.",
  "Tüchtig, souverän und anpassungsfähig, manchmal etwas glatt.",
  "Tiefgründig und ausdrucksstark, manchmal launisch oder dramatisch."),
 ("Du bekommst Kritik. Was geschieht?",
  "Ich bin gekränkt, wenn mein Einsatz nicht gesehen wird, sage es aber nicht direkt.",
  "Ich beziehe sie auf meine Leistung und arbeite härter oder verteidige mein Bild.",
  "Ich fühle mich im Wesen getroffen und denke: Er versteht mich nicht."),
 ("Du hast einen freien Tag und nichts zu tun.",
  "Ich überlege, wem ich etwas Gutes tun kann. Ausruhen fällt mir schwer.",
  "Untätigkeit fällt mir schwer. Ich suche Ziele und Aufgaben.",
  "Ich spüre Sehnsucht oder Melancholie und suche nach Bedeutung."),
 ("Du siehst andere, die mehr haben oder können.",
  "Ich schaue, wer mich braucht und mag.",
  "Ich schaue, wo ich stehe, und überlege, wie ich aufholen kann.",
  "Ich spüre Neid oder dass anderen etwas leichter fällt, das mir fehlt."),
])
tri("CK", [5,6,7], [
 ("Wie gehst du im Alltag an neue Dinge heran?",
  "Ich will erst verstehen, bevor ich mich beteilige, und spare meine Energie.",
  "Ich prüfe Risiken, suche Verlässliches und hinterfrage auch meine eigenen Urteile.",
  "Ich sehe Chancen, will mich ungern festlegen und nehme Schweres mit Humor."),
 ("Welche Frage passt eher zu dir?",
  "Ist es echtes Interesse – oder muss ich erst Sicherheit herstellen?",
  "Ist es sachliche Vorsicht – oder will ich Unsicherheit beseitigen?",
  "Ist es echte Neugier – oder will ich Schmerz vermeiden?"),
 ("Wenn der Druck steigt:",
  "Ich ziehe mich zurück, reduziere Kontakte und brauche Zeit allein.",
  "Ich grüble, spiele Katastrophen durch und suche Rückversicherung.",
  "Ich lenke mich ab, plane Neues und flüchte in Aktivität."),
 ("Was beschreibt deine Kindheit eher?",
  "Ich zog mich früh zurück und schützte meine Zeit und meinen Raum.",
  "Ich lernte früh, vorsichtig zu sein und zu prüfen, wem man trauen kann.",
  "Ich lernte, Unangenehmes mit Fröhlichkeit und Ideen zu überspielen."),
 ("Was sagen andere über dich?",
  "Ruhig, distanziert und klug. Ich komme erst spät aus mir heraus.",
  "Aufmerksam, loyal und skeptisch. Ich sehe Schwachstellen.",
  "Optimistisch, spontan und unterhaltsam, aber schwer festzunageln."),
 ("Wie triffst du Entscheidungen?",
  "Ich sammle Informationen, bis ich genug weiß, und entscheide spät.",
  "Ich frage andere, wäge Risiken ab und zweifle auch nach der Entscheidung.",
  "Ich entscheide schnell und halte mir Optionen offen."),
 ("Wie gehst du mit Angst um?",
  "Ich ziehe mich in mein Wissen und meine Welt zurück.",
  "Ich bereite mich vor, suche Verbündete oder gehe ihr offensiv entgegen.",
  "Ich denke an etwas Schönes oder plane etwas Neues."),
 ("Wie sieht dein Lebenslauf aus?",
  "Ich habe vieles gründlich studiert. Mein Wissen und mein Raum sind mir kostbar.",
  "Ich habe mich an verlässliche Menschen und Systeme gehalten und Wechsel gründlich geprüft.",
  "Ich habe viel ausprobiert: Projekte, Reisen, Wechsel, und manches nicht zu Ende gebracht."),
])
# Paare: häufig verwechselte Typen
def pair(prefix, a, b, items):
    for i,(q,x,y) in enumerate(items,1):
        add(id=f"{prefix}{i}", st="C", ty=[a,b], pair=True, q=q,
            o=[{"t":x,"w":{str(a):2}},{"t":y,"w":{str(b):2}}])
pair("P16",1,6,[("Du hältst dich an Regeln, weil ...","... es richtig ist. Ich habe ein inneres Maß.","... sie mir Sicherheit und Orientierung geben."),
 ("Eine Autorität kritisiert dich. Was geschieht?","Ich prüfe, ob sie nach meinem Maßstab recht hat, und ärgere mich über Fehler.","Ich werde unsicher und frage mich, ob ich ihr trauen kann oder bedroht bin."),
 ("Was sagt deine innere Stimme?","Was ich besser machen muss.","Was alles schiefgehen könnte.")])
pair("P38",3,8,[("Worum geht es dir bei Macht?","Um Respekt, Bewunderung und Erfolg.","Um Kontrolle: Mich bestimmt keiner."),
 ("Du stößt auf Widerstand.","Ich passe meine Strategie an, damit ich ans Ziel komme.","Ich gehe direkt dagegen an."),
 ("Wie gehst du mit Gefühlen um?","Ich funktioniere. Gefühle stören beim Erfolg.","Ich zeige Härte, damit niemand meine weiche Seite nutzt.")])
pair("P45",4,5,[("Du ziehst dich zurück. Warum?","Weil ich Gefühle spüre und mich unverstanden fühle.","Um Energie zu sparen und in Ruhe zu denken."),
 ("Wie ist Nähe für dich?","Ich sehne mich nach tiefer Verbindung und spüre, was fehlt.","Ich brauche wenig Nähe. Verpflichtungen bedrohen meine Zeit."),
 ("Wonach suchst du?","Nach Ausdruck und Bedeutung.","Nach Verständnis und Kompetenz.")])
pair("P59",5,9,[("Du brauchst Abstand. Warum?","Ich brauche Zeit zum Denken und klare Grenzen.","Ich will Ruhe und Konflikte vermeiden."),
 ("Wenn Anforderungen steigen:","Ich fühle mich ausgelaugt und ziehe mich zurück.","Ich schiebe auf, werde bequem und lenke mich ab."),
 ("Wie ist das mit deiner Meinung?","Ich habe eine klare Meinung, teile sie aber ungern.","Ich weiß oft nicht, was ich will, wenn andere Meinungen im Raum sind.")])
pair("P67",6,7,[("Wie ist das mit Angst?","Ich spüre sie und rechne mit Gefahren.","Ich merke sie kaum, weil ich schnell weiterziehe."),
 ("Festlegen:","Ich zweifle, ob es verlässlich genug ist.","Ich möchte mir Optionen offen halten."),
 ("Humor:","Ich löse damit Spannung, bleibe aber wachsam.","Er macht Schweres leichter, und ich gehe weiter.")])
pair("P37",3,7,[("Wofür bist du aktiv?","Für Ziele und Ergebnisse.","Für Erlebnisse und Neues."),
 ("Bei Leerlauf:","Ich fühle mich ohne Leistung wertlos.","Ich langweile mich und suche Abwechslung."),
 ("Dein Auftritt:","Ich achte auf mein Auftreten und passe mich an.","Ich bin spontan und unterhaltsam, ohne viel zu planen.")])
pair("P24",2,4,[("Bedürfnisse:","Die Bedürfnisse anderer spüre ich sofort, meine eigenen kaum.","Meine eigenen Gefühle spüre ich stark, die Bedürfnisse anderer rücken nach hinten."),
 ("Beziehungen:","Ich gebe, um geliebt zu werden.","Ich fürchte, nicht verstanden zu werden."),
 ("Hilfe annehmen:","Hilfe zu erbitten fällt mir schwer.","Ich erwarte, dass jemand merkt, was mir fehlt, ohne dass ich es sage.")])
pair("P23",2,3,[("Was willst du bei anderen erreichen?","Ich will gemocht und gebraucht werden.","Ich will beeindrucken und erfolgreich sein."),
 ("Du passt dich an:","Daran, was der andere braucht.","Daran, was gut ankommt."),
 ("Was freut dich mehr?","Dankbarkeit.","Ergebnisse und Anerkennung.")])
pair("P18",1,8,[("Wie zeigst du Ärger?","Verbissen und kontrolliert.","Laut und offen."),
 ("Regeln:","Sie sind mein Maßstab.","Sie gelten, wenn ich sie sinnvoll finde."),
 ("Gerechtigkeit:","Ich will, dass es korrekt zugeht.","Ich beschütze die Schwächeren und kämpfe.")])
pair("P89",8,9,[("Nach einem Streit:","Ich ruhe mich aus, nachdem ich gekämpft habe.","Ich vermeide den Kampf von vornherein."),
 ("Kontrolle:","Ich will sie behalten.","Ich gebe sie ab, damit Frieden bleibt."),
 ("Entscheidungen:","Ich entscheide schnell.","Ich entscheide spät oder gar nicht.")])
pair("P49",4,9,[("Gefühle:","Sie sind intensiv und deutlich.","Sie sind eher gedämpft."),
 ("Eigene Wünsche:","Ich weiß genau, was mir fehlt.","Ich weiß oft nicht genau, was ich will."),
 ("Rückzug:","Mit Melancholie und Sehnsucht.","Mit Bequemlichkeit und Routine.")])
pair("P12",1,2,[("Du hilfst jemandem:","Weil es richtig ist, und erwarte Sorgfalt.","Weil ich gebraucht werden will."),
 ("Kritik:","Ich kritisiere, was nicht stimmt.","Ich bin verletzt, wenn mein Einsatz nicht gesehen wird."),
 ("Was kommt zuerst?","Die Aufgabe.","Der Mensch.")])
pair("P56",5,6,[("Wie sorgst du für Sicherheit?","Durch Wissen und Rückzug.","Durch Absicherung und Verbündete."),
 ("Misstrauen:","Ich halte Abstand.","Ich prüfe, ob jemand es gut mit mir meint."),
 ("Vor Entscheidungen:","Ich brauche genug Informationen.","Ich suche Rückversicherung bei anderen.")])


# ---- Weitere Typenpaare (Vorlage: Differenzierungen zwischen den Typen, Chestnut; in eigenen Worten) ----
pair("Q13",1,3,[("Wie definierst du Qualität?","Das Beste, was ich leisten kann, ohne Fehler, auch wenn es niemand bemerkt.","Die Erwartungen des Kunden oder Publikums erfüllen und etwas darüber hinausgehen. „Gut genug“ ist gut genug."),
 ("Woran misst du, ob du gut warst?","An meinen inneren Maßstäben. Ich weiß selbst, ob ich einen Fehler gemacht habe.","Daran, wie wichtige Personen reagieren, an Anerkennung und sichtbarem Erfolg.")])
pair("Q14",1,4,[("Worauf achtest du bei einer Aufgabe zuerst?","Auf Struktur, Prozess und Details. Regeln und Standards zählen.","Auf Beziehungen, Authentizität und kreativen Ausdruck. Besonderes zählt mehr als Perfektion."),
 ("Wie fühlt sich dein innerer Kritiker an?","Er kommentiert, wie etwas besser hätte sein können, ohne große Gefühlsreaktion.","Ich spüre tief, dass in mir etwas fehlt oder nicht gut genug ist, mit starker Gefühlsreaktion.")])
pair("Q15",1,5,[("Wie zeigt sich deine Wut?","Als Gereiztheit oder Ärger, wenn andere sich nicht an die richtige Art halten.","Ich bleibe ruhig und unerschütterlich und behalte Gedanken und Gefühle für mich."),
 ("Wie ist das mit Selbstkritik und Energie?","Ich bin sehr selbstkritisch. Mein innerer Kritiker kommentiert fast alles.","Ich spare Energie, brauche viel Privatsphäre und löse mich von Gefühlen. Selbstkritik ist weniger mein Thema.")])
pair("Q17",1,7,[("Was kommt zuerst, Arbeit oder Vergnügen?","Die Arbeit vor dem Vergnügen. Ordnung und Struktur gefallen mir.","Die Planung angenehmer Aktivitäten ist mir wichtiger. Grenzen mag ich nicht."),
 ("Details und Fehler:","Ich bin gut bei Details und achte auf Fehler, die korrigiert werden müssen.","Details ermüden mich schnell. Ich konzentriere mich auf das Positive und die Ideenphase.")])
pair("Q19",1,9,[("Wie sicher bist du dir bei deiner Meinung?","Ich glaube oft zu wissen, wie es richtig geht, und denke eher schwarz-weiß.","Ich sehe viele Grautöne, und es fällt mir schwer, meine eigene Meinung zu finden."),
 ("Wie gehst du mit Regeln und Wegen anderer um?","Ich konfrontiere, wer sich nicht an die Regeln hält. Mein Weg ist mir wichtig.","Ich passe mich gern der Agenda anderer an und weiche Konflikten eher aus.")])
pair("Q25",2,5,[("Wie wirkt Kontakt mit Menschen auf dich?","Er lädt meinen Akku auf. Nein zu sagen fällt mir schwer.","Er kostet mich Energie. Ich sage relativ leicht Nein und brauche Zeit allein."),
 ("Wie gehst du mit Gefühlen um?","Ich fühle meine Emotionen häufig und gehe aktiv auf Beziehungen zu.","Ich löse mich von Emotionen, bin eher analytisch und schütze meine Privatsphäre.")])
pair("Q26",2,6,[("Was beunruhigt dich eher?","Ob andere mich mögen und in positivem Licht sehen.","Allgemeine Sicherheit, Probleme und mögliche Bedrohungen."),
 ("Wie ist dein Verhältnis zu Autoritäten?","Ich möchte eine gute Beziehung und von ihnen gemocht werden.","Ich bin eher misstrauisch oder rebellisch.")])
pair("Q27",2,7,[("Worauf richtest du deine Aufmerksamkeit?","Auf Stimmungen und Bedürfnisse anderer, um positive Verbindungen zu schaffen.","Auf meine eigenen Wünsche und Erfahrungen."),
 ("Wie gehst du mit deinen Bedürfnissen um?","Ich passe mich oft an andere an und gebe eigene Bedürfnisse auf.","Ich tue, was ich will, und halte mir Optionen gern offen.")])
pair("Q28",2,8,[("Wie wichtig ist dir, wie andere dich sehen?","Sehr wichtig. Ich manage mein Bild.","Es kümmert mich wenig, was andere über mich denken."),
 ("Wie ist das mit Ärger?","Ich verdränge ihn meist, um die Verbindung zu halten.","Ich spüre und äußere ihn leicht, auch in Konflikten.")])
pair("Q29",2,9,[("Wie ist dein Gefühlsleben und dein Tempo?","Ich spüre Gefühle häufig und gehe aktiv auf andere zu.","Ich bin emotional gleichmäßiger, entspannter und warte eher ab."),
 ("Wie ist das mit deiner eigenen Agenda?","Ich habe eine klare Agenda für Beziehungen, auch wenn ich meine Bedürfnisse nicht kenne.","Ich vergesse meine eigene Agenda und weiß oft nicht, was ich will.")])
pair("Q34",3,4,[("Wie gehst du eine Aufgabe an?","Auf dem kürzesten, effizientesten Weg zum Ziel.","Eher nichtlinear, kreativ und organisch."),
 ("Wie gehst du mit Gefühlen um?","Ich betäube sie, um Dinge zu erledigen.","Ich finde, alle Gefühle sollten gefühlt und authentisch ausgedrückt werden.")])
pair("Q35",3,5,[("Worauf stützt du dein Selbstwertgefühl?","Auf Zustimmung und Bewunderung und auf mein Erfolgsbild.","Auf Unabhängigkeit und Objektivität. Das Urteil anderer ist mir weniger wichtig."),
 ("Wie gehst du mit deiner Energie um?","Ich arbeite grenzenlos, auch im Urlaub.","Ich spare Energie und vermeide Aufgaben und Beziehungen, die mich auslaugen.")])
pair("Q36",3,6,[("Wie gehst du auf ein Ziel zu?","Zielstrebig, ohne lange darüber nachzudenken, was schiefgehen könnte.","Ich denke fast immer daran, was schiefgehen könnte, und bereite mich darauf vor."),
 ("Wie trittst du auf?","Zuversichtlich und überzeugend.","Ich zweifle und hinterfrage, auch mich selbst.")])
pair("Q39",3,9,[("Wie ist dein Tempo?","Schnell, entschlossen und vorwärtsgerichtet.","Langsamer. Ich sitze eher auf dem Zaun."),
 ("Wie fühlst du dich im Mittelpunkt?","Ich genieße das Rampenlicht.","Im Mittelpunkt zu stehen ist mir unangenehm.")])
pair("Q46",4,6,[("Wie möchtest du gesehen werden?","Als einzigartig und originell.","Eher als Underdog oder „Jedermann“."),
 ("Wo lebst du hauptsächlich?","In meinen Emotionen, oft Traurigkeit oder Melancholie.","Eher im Kopf: Angst, Zweifel und Sorgen. Ich suche Gewissheit.")])
pair("Q47",4,7,[("Worauf richtest du den Blick?","Auf das, was fehlt. Dunkle Gefühle sind mir vertraut.","Auf das Positive. Ich wandle Negatives in Positives um."),
 ("Wenn jemand leidet:","Ich kann dabeibleiben und mitfühlen.","Es fällt mir schwer, ich lenke lieber auf Positives.")])
pair("Q48",4,8,[("Wie gehst du mit Verletzlichkeit um?","Ich fühle verletzliche Gefühle und finde Trost darin.","Ich leugne Verletzlichkeit und zeige Stärke."),
 ("Wie drückst du Liebe aus?","Durch Gefühle und den Wunsch nach Verbindung.","Durch Schutz und Macht.")])
pair("Q57",5,7,[("Worauf konzentrierst du dich?","Darauf, Energie zu sparen und alles möglichst wirtschaftlich zu tun.","Auf Optionen und angenehme Möglichkeiten."),
 ("Wie siehst du Dinge?","Distanziert und objektiv. Negatives wandle ich nicht in Positives um.","Ich lebe viel in der Zukunft, in Plänen für schöne Aktivitäten.")])
pair("Q58",5,8,[("Wie wirkst du auf andere?","Eher introvertiert, mit zurückhaltender Präsenz.","Extrovertiert, mit großer, spürbarer Energie."),
 ("Denken und Handeln:","Ich denke viel nach, bevor ich handle, eher zu viel.","Ich handle oft, bevor ich nachdenke, und bin impulsiv.")])
pair("Q68",6,8,[("Wie sind Angst und Zweifel?","Ich spüre meist Angst und Verwundbarkeit und zweifle an mir.","Ich habe wenig Angst, zeige Stärke und zweifle selten an mir."),
 ("Tempo:","Ich überdenke Dinge, zögere und bremse mich selbst.","Ich handle schnell und werde ungeduldig, wenn andere langsam sind.")])
pair("Q69",6,9,[("Vertrauen:","Ich bleibe misstrauisch und prüfe, ob jemand vertrauenswürdig ist.","Ich vertraue leicht und verschmelze mit anderen."),
 ("Standpunkte:","Ich denke kontrar und hinterfrage die jeweils vertretene Ansicht.","Ich sehe viele Standpunkte als gleich plausibel und vermittle.")])
pair("Q78",7,8,[("Wie verteidigst du deine Freiheit?","Mit Charme und diplomatischem Ansatz.","Offen und direkt: Angriff ist die beste Verteidigung."),
 ("Projekte:","Die Ideenphase liegt mir mehr. Bei Routine verliere ich den Fokus.","Ich treibe Dinge schnell voran, bis sie abgeschlossen sind.")])
pair("Q79",7,9,[("Wie ist das mit deiner Agenda?","Ich habe eine klare eigene Agenda und weiß, was ich will.","Ich weiß eher, was ich nicht will, und folge oft der Agenda anderer."),
 ("Tempo:","Schnell und energiegeladen, ich suche Aufregung.","Entspannt im Tempo, manchmal träge und unentschlossen.")])

# ---- Stufe D: Untertyp (Optionen sp, so, sx) ----
D = {
1:[("Wie richtet sich deine Strenge?",
   "Nach innen: Ich sorge vor und will Fehler schon im Vorfeld vermeiden.",
   "Ich will ein unanfechtbares Vorbild sein, förmlich, ethisch, prinzipientreu.",
   "Nach außen: Ich will andere oder die Welt verbessern und fordere Perfektion offen ein."),
  ("Es könnte etwas schiefgehen.",
   "Ich mache mir Sorgen und bereite mich besonders gründlich vor.",
   "Ich achte darauf, dass mein Verhalten keine Angriffsfläche bietet.",
   "Ich werde ungeduldig und dränge darauf, dass es besser gemacht wird."),
  ("Wofür kennt man dich?",
   "Für Gewissenhaftigkeit und Vorsorge.",
   "Für Prinzipien und Vorbildlichkeit.",
   "Für Eifer, Leidenschaft und deutliche Kritik.")],
2:[("Wie setzt du Zuwendung ein?",
   "Ich möchte versorgt werden und reagiere manchmal kindlich oder hilflos-charmant.",
   "Ich will in Gruppen eine unentbehrliche Schlüsselfigur sein, mit Netzwerk und Einfluss.",
   "Ich baue intensive Eins-zu-eins-Beziehungen auf und verführe durch Nähe und Charme."),
  ("Wenn du etwas brauchst:",
   "Ich erwarte insgeheim, dass man mich bevorzugt und versorgt.",
   "Ich setze mein Netzwerk und meine Kontakte ein.",
   "Ich werde besonders aufmerksam und charmant gegenüber dem Menschen, der mir wichtig ist."),
  ("Wohin geht dein Ehrgeiz?",
   "Zu Geborgenheit und Fürsorge für mich selbst.",
   "Zu Einfluss in Organisationen und Gruppen.",
   "Zur Eroberung und Faszination eines Menschen.")],
3:[("Wie zeigt sich dein Erfolgsstreben?",
   "Ich arbeite sehr hart, aber leise, ohne es an die große Glocke zu hängen.",
   "Ich liebe Titel, sichtbare Ergebnisse und Repräsentation nach außen.",
   "Ich richte mich darauf aus, für den Partner oder Wunschmenschen attraktiv und begehrenswert zu sein."),
  ("Worauf achtest du bei Anerkennung?",
   "Auf Effizienz und Sicherheit. Ich brauche den Erfolg vor allem für mich selbst.",
   "Auf Status und Rolle in der Gruppe.",
   "Auf Ausstrahlung und Wirkung auf den einen Menschen."),
  ("Wie gehst du mit Selbstdarstellung um?",
   "Ich verzichte auf Auftritte, die angreifbar machen.",
   "Ich genieße das Vorzeigbare.",
   "Ich pflege mein Auftreten und meine Anziehung.")],
4:[("Wie gehst du damit um, dass dir etwas fehlt?",
   "Ich leide im Stillen, ertrage Härte und beschwere mich selten.",
   "In Gruppen fühle ich mich anders, wie ein Außenseiter, und schäme mich.",
   "Ich reagiere mit Wut, Verlangen und Konkurrenz, fordernd und kompromisslos."),
  ("Wenn du dich unzulänglich fühlst:",
   "Ich beiße die Zähne zusammen, halte durch und bitte nicht um Hilfe.",
   "Ich ziehe mich zurück und fühle mich als Opfer von Umständen oder Gruppe.",
   "Ich werde neidisch und trete herausfordernd auf."),
  ("Was passt eher?",
   "Zähigkeit und Ausdauer.",
   "Scham und die Rolle des Unverstandenen.",
   "Konkurrenz und Neid.")],
5:[("Wo findest du deinen Platz?",
   "Ich brauche einen festen Rückzugsraum und reduziere meine Bedürfnisse radikal.",
   "Über Expertenwissen, Theorien und Systeme, nicht emotional.",
   "Ich suche einen einzigen tiefen Menschen, dem ich meine geheimsten Gedanken anvertraue."),
  ("Menschen wollen Zeit von dir.",
   "Ich brauche meine Höhle und meine Grenze.",
   "Ich verbinde mich über Wissen und Kompetenz.",
   "Ich öffne mich einem Vertrauten ganz und teile Geheimnisse."),
  ("Wofür bist du bekannt?",
   "Für ein zurückgezogenes Leben mit wenigen Bedürfnissen.",
   "Für Fachautorität und Expertenrolle.",
   "Für Vertrauen und Verschwiegenheit.")],
6:[("Wie begegnest du Unsicherheit?",
   "Mit Freundlichkeit, Sanftmut und Beziehungen, die mich schützen.",
   "Mit Strukturen, Regeln, Verträgen, an die ich mich strikt halte.",
   "Mit Stärke und Konfrontation. Angriff ist die beste Verteidigung."),
  ("Jemand bedroht dich.",
   "Ich suche Verbündete und baue Beziehung auf.",
   "Ich berufe mich auf Pflicht, Regeln und Zuständigkeiten.",
   "Ich werde mutig, provokant und schüchtere ein."),
  ("Was passt eher?",
   "Warmherzigkeit und Bündnis.",
   "Pflicht und Regeln.",
   "Stärke und Mut.")],
7:[("Wie lebst du deine Begeisterung?",
   "Ich baue ein Netzwerk auf, damit ich immer Zugang zu Genuss, Vorteilen und Sicherheit habe.",
   "Ich stelle eigene Wünsche für eine Gruppe oder Sache zurück. Idealismus.",
   "Ich verliebe mich in Ideen, Visionen und magische Momente."),
  ("Eine Verlockung tut sich auf.",
   "Ich organisiere pragmatisch Vorteile und Kontakte.",
   "Ich verzichte, um für das Wohl der Gruppe da zu sein.",
   "Ich träume von Möglichkeiten und Utopien."),
  ("Wofür brennst du?",
   "Für Genuss und die richtigen Menschen um mich herum.",
   "Für Ideale und Gemeinschaft.",
   "Für Faszination und Visionen.")],
8:[("Wie zeigt sich dein Kampfgeist?",
   "Praktisch: Unabhängigkeit, Schutz und Territorium. Ich spreche wenig und handle direkt.",
   "Ich stehe gegen Ungerechtigkeit für andere auf und wirke wie ein Beschützer.",
   "Intensiv und leidenschaftlich. Ich will emotionale Dominanz und Hingabe."),
  ("Was ist dir wichtig?",
   "Materielle Unabhängigkeit.",
   "Gerechtigkeit für die Schwächeren.",
   "Einfluss und absolute Hingabe des Einen."),
  ("Bedrohung:",
   "Ich sichere mein Überleben und ziehe mich in mein Versteck zurück.",
   "Ich stelle mich schützend vor andere.",
   "Ich werde fordernd und will Kontrolle und Nähe zugleich.")],
9:[("Wie lenkst du dich von deinen eigenen Wünschen ab?",
   "Durch Routinen, Essen, Medien und Gemütlichkeit.",
   "Durch Aktivität und Geselligkeit in Gruppen.",
   "Ich verschmelze mit dem Partner und übernehme seine Wünsche."),
  ("Konflikte drohen.",
   "Ich betäube mich mit Komfort.",
   "Ich bin energisch und fröhlich und packe mit an.",
   "Ich passe mich fast ganz an den Lieblingsmenschen an."),
  ("Wofür kennt man dich?",
   "Für Gemütlichkeit.",
   "Für Mitarbeit und Beteiligung.",
   "Für Harmonie und Verschmelzung mit dem Partner.")],
}
for ty,items in D.items():
    for i,(q,a,b,c) in enumerate(items,1):
        add(id=f"D{ty}{i}", st="D", ty=[ty], q=q, o=[{"t":a,"w":{"sp":2}},{"t":b,"w":{"so":2}},{"t":c,"w":{"sx":2}}])


D_EXTRA = {
1:[("Wie gehst du mit Wut um?",
   "Ich zeige sie kaum, fühle mich aber innerlich frustriert, wenn etwas gestört wird.",
   "Ich bleibe beherrscht, stelle hohe Ansprüche und will mit gutem Beispiel vorangehen.",
   "Ich bringe Wut und Frust offen zum Ausdruck, wenn meine Verbesserungen auf Widerstand stoßen."),
  ("Was beschreibt dein Ideal am besten?",
   "Gewissenhaft vorbereitet bis ins kleinste Detail und Risiken vorhersehen.",
   "Integrität, Fairness und Prinzipientreue als Vorbild für andere.",
   "Ein idealistisches Bild davon, wie die Dinge sein sollten, und das Gefühl, andere oder die Gesellschaft anpassen zu dürfen.")],
2:[("Wie sehen deine engen Beziehungen aus?",
   "Ich möchte versorgt werden, wirke etwas schüchtern-süß und zögere bei langfristigen Verpflichtungen.",
   "Ich bin gern auf dem Laufenden, hebe mich von der Masse ab und wirke über Kompetenz und Kontakte.",
   "Ich bin hingebungsvoll und leidenschaftlich und finde es schwer, Grenzen zu setzen oder ein Nein zu akzeptieren."),
  ("Wie lenkst du dich von unangenehmen Gefühlen ab?",
   "Ich ziehe mich zurück, wenn ich Ablehnung spüre oder befürchte.",
   "Ich gebe mehr, als ich bekomme, und übernehme eine zentrale Rolle.",
   "Ich konzentriere meine Talente darauf, intensive Beziehungen aufzubauen.")],
3:[("Wie gehst du mit Anerkennung um?",
   "Ich will für harte Arbeit und Exzellenz anerkannt werden, ohne mich anzupreisen.",
   "Ich lese die Normen eines Teams und passe mich geschickt an. Ich stehe gern im Rampenlicht.",
   "Ich konkurriere um die Aufmerksamkeit der mir Nächsten und unterdrücke Gefühle, um für sie attraktiv zu sein."),
  ("Welche Falle kennst du?",
   "Arbeitssucht aus dem Wunsch nach Sicherheit.",
   "Fehler vertuschen, solange das Ergebnis gut aussieht.",
   "Zu glauben, ich sei erfolgreich, wenn die Menschen um mich mich mögen.")],
4:[("Wie gehst du mit Schmerz um?",
   "Ich habe gelernt, stoisch zu leiden, und möchte dafür anerkannt werden, dass ich „hart“ bin.",
   "Ich finde Trost im Leiden und drücke mich ästhetisch aus. Ich fühle mich minderwertig und vergleiche mich.",
   "Ich äußere meine Bedürfnisse laut, wirke eher schamlos als beschämt und rivalisiere."),
  ("Wie erlebst du Mangel?",
   "Ich bin einfühlsam gegenüber leidenden Menschen, teile meinen eigenen Schmerz aber selten.",
   "Ich gebe mir die Schuld und zweifle an mir. Neid und Scham sind stark.",
   "Wut statt Traurigkeit. Ich will die Besten sein, um dem Leid zu entkommen.")],
5:[("Wie lebst du deinen Rückzug?",
   "Ich schütze meine Privatsphäre mit klaren Grenzen und lebe gern ein karges, einsames Leben mit wenigen Freunden.",
   "Ich suche die Essenz und Bedeutung der großen Fragen und teile Werte und Ideale mit Gruppen, nicht aber alltäglichen Raum.",
   "Ich lebe zurückhaltend, aber mit ein oder zwei Menschen erlebe ich eine starke Chemie und riskiere Offenheit."),
  ("Was beschreibt dich besser?",
   "Introvertiert, große Wachsamkeit. Ich habe Angst, meine Privatsphäre zu verlieren.",
   "Ich verbinde mich mit Experten und Gruppen über Wissen, trenne mich aber von alltäglichen Problemen.",
   "Ich teste die Loyalität des einen Menschen und teile ungern.")],
6:[("Wie bearbeitest du Angst?",
   "Ich baue starke Allianzen auf, bin liebevoll, unterdrücke Wut und zögere, Meinungen zu äußern.",
   "Ich arbeite für eine Sache oder setze mich für Schwächere ein und denke eher schwarz-weiß.",
   "Ich werde mutig und durchsetzungsfähig, wirke vielleicht einschüchternd wie ein Achter, doch darunter liegt Angst."),
  ("Und gegenüber Autorität?",
   "Ich suche Beziehungen, die mich schützen.",
   "Ich halte mich an Regeln und eine äußere Autorität, damit jeder weiß, was von ihm erwartet wird.",
   "Ich fordere Autorität heraus, wenn ich glaube, sie missbraucht ihre Macht.")],
7:[("Wie gehst du mit deinen Wünschen um?",
   "Ich sammle eine „Familie“ von Unterstützern um mich und liebe die guten Dinge des Lebens.",
   "Ich opfere eigene Bedürfnisse, um einer Gruppe zu dienen, und verurteile Egoismus bei mir und anderen.",
   "Ich sehe die Welt durch einen rosa Filter, verliebe mich in Möglichkeiten und finde Langweiliges unerträglich."),
  ("Was beschreibt dich besser?",
   "Ich rationalisiere gern, was ich tue.",
   "Ich hoffe, für meine Opferbereitschaft geschätzt zu werden.",
   "Ich möchte die Welt durch meine Beiträge schöner und weniger trist machen.")],
8:[("Wie zeigst du Stärke?",
   "Stark, direkt und produktiv. Ich übernehme die Rolle des Wächters und werde intolerant, wenn meine Bedürfnisse nicht erfüllt werden.",
   "Ich schütze „meine Leute“ vor Machtmissbrauch und zeige nach außen keine Schwäche. Hartes Feedback von engen Verbündeten schätze ich.",
   "Ich bin der Rebell, breche provokant Regeln und will Intensität und Einfluss."),
  ("Wie gehst du mit deinen eigenen Bedürfnissen um?",
   "Sachlich und direkt, ohne Schuldgefühle.",
   "Ich stelle sie zurück und unterstütze lieber andere, manchmal wirke ich wie eine Zwei.",
   "Ich möchte einer guten Sache dienen, am liebsten aus einer Führungsposition.")],
9:[("Wie gehst du mit dir selbst um?",
   "Ich tröste mich mit Essen, Lesen oder Schlafen. Ruhe und Zeit allein sind mir wichtig, und ich kann stur reagieren, wenn mein Gleichgewicht gestört wird.",
   "Ich beteilige mich voll in Gruppen, oft als Vermittler, bewahre eine fröhliche Front und stelle meine Probleme beiseite.",
   "Ich fühle mich sicherer, wenn ich mit anderen zusammen bin, und finde es schwer, allein zu sein."),
  ("Welche Falle kennst du?",
   "Ich werde reizbar oder stur, wenn jemand meinen Komfort stört.",
   "Ich laufe Gefahr, zum Workaholic zu werden, um Stress zu verbergen.",
   "Ich opfere meine Pläne und passe mich den Vorlieben anderer an.")],
}
for ty,items in D_EXTRA.items():
    for i,(q,a,b,c) in enumerate(items,len(D[ty])+1):
        add(id=f"D{ty}{i}", st="D", ty=[ty], q=q, o=[{"t":a,"w":{"sp":2}},{"t":b,"w":{"so":2}},{"t":c,"w":{"sx":2}}])

# ---- Stufe E: Flügel (Beschreibungen S. 16-24) ----
E = {
1:(9,2,"Sachlich, ruhig, prinzipientreu und zurückhaltend. Der innere Kritiker wirkt kontrollierter.","Engagiert, hilfsbereit und menschenorientiert."),
2:(1,3,"Verantwortungsbewusst, idealistisch und pflichtorientiert.","Kontaktfreudig, charmant und wirkungsorientiert."),
3:(2,4,"Überzeugend, beziehungsorientiert und unterstützend. Erfolg über Kontakte und Sympathie.","Eigenständig, anspruchsvoll und individualistisch. Erfolg soll auch besonders und persönlich bedeutsam sein."),
4:(3,5,"Ausdrucksstark, ehrgeizig und präsentationsbewusst. Die eigene Besonderheit soll gesehen werden.","Zurückgezogen, nachdenklich und intensiv. Die innere Welt wird geschützt und durchdacht."),
5:(4,6,"Eigenwillig, kreativ und introspektiv. Wissen verbindet sich mit Tiefe und Individualität.","Systematisch, vorsichtig und sachorientiert. Wissen dient der Sicherheit."),
6:(5,7,"Analytisch, skeptisch und zurückhaltend. Zweifel werden durch Nachdenken bearbeitet.","Kontaktfreudiger, lebhafter und handlungsorientierter."),
7:(6,8,"Gesellig, humorvoll und gemeinschaftsorientiert. Möglichkeiten verbinden sich mit Zugehörigkeit.","Durchsetzungsstark, unabhängig und direkt. Freiheit wird entschlossen verteidigt."),
8:(7,9,"Energiegeladen, unternehmungslustig und offensiv.","Ruhiger, gelassener und beständiger. Stärke zeigt sich durch Präsenz und Standfestigkeit."),
9:(8,1,"Erdverbunden, gelassen und eigenwillig. Mehr Durchsetzungsfähigkeit.","Ordnungsliebend, prinzipientreu und sachlich."),
}
for ty,(lo,hi,a,b) in E.items():
    add(id=f"E{ty}", st="E", ty=[ty], q=f"Welche Färbung passt eher zu dir? (Flügel {lo} oder {hi})",
        o=[{"t":a,"w":{"wl":2}},{"t":b,"w":{"wh":2}}], wing=[lo,hi])

Q.sort(key=lambda q: 0 if q.get("body") else 1) if False else None
body=[q for q in Q if q.get("body")]
rest=[q for q in Q if not q.get("body")]
i0=next(i for i,q in enumerate(rest) if q["st"]=="S")
Q[:]=rest[:i0]+body+rest[i0:]
out=os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","app","src","main","assets","typfinder.json")
json.dump({"version":1,"questions":Q}, open(out,"w",encoding="utf-8"), ensure_ascii=False, separators=(",",":"))
from collections import Counter
print(len(Q), Counter(q["st"] for q in Q))
