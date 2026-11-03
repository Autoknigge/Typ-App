# Enneagramm Typ-Finder (Typ-App)

Android-App (Kotlin): geführte Befragung zu Seite, Instinkt, Typ, Untertyp und Flügel nach dem Buch
„Enneagramm – Matrix des Lebens“ von Marc Krekler. Läuft offline, Werbung über Google AdMob.

- Paket: `de.autoknigge.typfinder`
- Fragenbank: `app/src/main/assets/typfinder.json` (130 Fragen)
- Auswertung: `TypFinder.kt` (deterministisch, nur die Antworten werden gespeichert)
- Build: GitHub Actions, Artefakt „Typfinder“ (signiertes APK und AAB)
- Version: versionCode = 100 + Anzahl der Commits

## Ausgaben
Dieses Repo enthält die einfache, öffentliche App (Typ, Untertyp und Flügel, mit Werbung). Die Pro-Variante mit PDF-Bericht liegt in einem eigenen privaten Repo.

Stand: Fragenkatalog mit neuen Körperfragen (ZA bis ZE), Build auf Zuruf.

Build mit Zusatzfragen zum Untertyp.

Build mit Antwortreihenfolge, Appetit-Satz und Art-Erklärung.
