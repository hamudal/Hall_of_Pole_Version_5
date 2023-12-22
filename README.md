# Pole Dance Studio Scraper

## Überblick
Dieses Projekt bietet eine Reihe von Python-Skripten zum Extrahieren von Informationen über Pole Dance Studios, Workshops, Klassen und ihre Details von der Eversports-Website. Es nutzt Web-Scraping-Techniken, um nützliche Daten zu sammeln und in strukturierter Form bereitzustellen.

## Features
- Extraktion von Basisinformationen zu Pole Dance Studios.
- Detaillierte Daten zu Workshops und Klassen, einschließlich Trainer, Raum, Zeiten und Verfügbarkeit.
- Validierung von URLs und Rekonstruktion von Detailseiten-URLs.
- Speicherung der extrahierten Daten in strukturierten Pandas DataFrames.

## Installation
Stellen Sie sicher, dass Python 3.x auf Ihrem System installiert ist. Installieren Sie dann die erforderlichen Pakete mit:

```bash
pip install requests beautifulsoup4 pandas



Verwendung
Klonen Sie das Repository und führen Sie das Hauptskript aus, um den Scraping-Prozess zu starten:

git clone https://github.com/your-username/pole-dance-studio-scraper.git
cd pole-dance-studio-scraper
python main.py



Skripte
a_URL_Reconstructor.py: Rekonstruiert URLs für Pole Dance Studios.
aa_URL_Validation.py: Validiert die rekonstruierten URLs.
aaa_PoleStudio_URL_S_Function.py: Scraped Informationen von den Studioseiten.
b_Workshopslist_URL_SW_Function.py: Extrahiert Daten von Workshop-Listen.
c_Workshop_URL_E_Function.py: Scraped detaillierte Informationen von einzelnen Workshops.
d_Klassenlist_SCL_Function.py: Sammelt Informationen zu Klassen.
CallerPy.py: Hauptskript zum Ausführen des Scraping-Prozesses.
Struktur
Die Daten werden in verschiedenen Pandas DataFrames gespeichert:

pole_studio_data: Basisdaten zu Pole Dance Studios.
workshops_data: Informationen zu Workshops.
workshop_details: Detaillierte Daten zu einzelnen Workshops.
classes_data: Informationen zu Klassen.
classes_details: Detaillierte Informationen zu einzelnen Klassen.
Mitwirken
Bei Interesse an einer Mitwirkung oder Verbesserung des Projekts, senden Sie bitte einen Pull Request oder eröffnen ein Issue.