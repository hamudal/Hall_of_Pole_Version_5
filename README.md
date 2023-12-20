# Hall_of_Pole_Version_5
Scraper


# Projektbeschreibung: Entwicklung einer Datenbank für HallOfPole.com

## Einleitung
Ich arbeite derzeit an einem spannenden Projekt, das darauf abzielt, eine umfangreiche Datenbank für die Website HallOfPole.com aufzubauen. Mein Ziel ist es, eine zuverlässige und reichhaltige Informationsquelle zu schaffen, die die Plattform mit wertvollen Daten über Pole Dance Studios, Workshops, Klassen und vieles mehr versorgt.

## Mein Fortschritt bis jetzt
Bislang habe ich in diesem Projekt mehrere Schlüsselelemente erfolgreich entwickelt und implementiert:

- **URL-Rekonstruktion**: Ich habe eine Funktion namens `reconstruct_urls_and_extract_buttons` entwickelt, die spezifische URLs analysiert und nützliche Links extrahiert. Diese Funktion generiert ein Dictionary mit verschiedenen URL-Kategorien, die für das weitere Scraping von Bedeutung sind.

- **Datenstrukturierung**: Ich konvertiere das erzeugte Dictionary in ein DataFrame, um eine effektive Organisation und Strukturierung der gesammelten Daten zu gewährleisten.

- **URL-Validierung**: Mit der Funktion `validate_urls` stelle ich sicher, dass alle erfassten URLs gültig und zuverlässig sind. Dies ist ein entscheidender Schritt, um die Qualität der Daten zu gewährleisten.

- **Datensammlung**: Ich habe spezifische Scraping-Funktionen entwickelt, um detaillierte Informationen über Pole Studios, Workshops und Klassen zu sammeln. Jeder Datensatz wird in einem separaten DataFrame gespeichert, um eine klare Trennung und einfache Verwaltung der Daten zu ermöglichen.

- **Detailinformationen erfassen**: Für tiefergehende Einblicke sammle ich zusätzliche Detailinformationen zu Workshops und Klassen.

## Zukünftige Pläne
Meine nächsten Schritte umfassen:

- **Cloud-Integration**: Die Anbindung unserer Datenpipeline an eine Cloud-Plattform steht bevor. Dies wird eine zentrale und skalierbare Datenverwaltung ermöglichen.

- **Automatisierung**: Ich plane, einen automatisierten Prozess zu implementieren, der regelmäßige Datenupdates ohne manuellen Eingriff ermöglicht.

- **Analyse und Berichterstellung**: Ich werde Analysetools entwickeln, um aus den gesammelten Daten wertvolle Erkenntnisse zu gewinnen und Berichte zu erstellen.

- **Benutzeroberfläche entwickeln**: Ziel ist es, eine intuitive Benutzeroberfläche zu erstellen, über die Nutzer auf die Daten zugreifen und sie effektiv nutzen können.

## Abschlussbemerkung
Durch die Kombination meiner Fähigkeiten im Bereich der Datenerfassung und -verarbeitung mit fortschrittlichen Cloud-Technologien und Automatisierungsstrategien strebe ich danach, HallOfPole.com zu einer zentralen Ressource für die Pole Dance-Gemeinschaft zu machen. Ich bin motiviert, nicht nur eine Datenbank zu erstellen, sondern eine Plattform, die Vernetzung, Lernen und Entwicklung in dieser dynamischen Kunstform unterstützt.




# Technische Dokumentation: HallOfPole.com Datenbeschaffung

## Einleitung
Im Rahmen meines Projekts für HallOfPole.com habe ich eine Reihe von Python-Skripten entwickelt, um Daten von der Website Eversports effizient zu sammeln und zu verarbeiten. Ziel ist es, eine umfassende Datenbank zu erstellen, die wertvolle Informationen über Pole Dance Studios, Workshops und Klassen enthält.

## Technische Details

### URL-Rekonstruktion
- **Skript**: `a_URL_Reconstructor.py`
- **Funktion**: `reconstruct_urls_and_extract_buttons`
- **Prozess**: Die Funktion nimmt eine URL (z.B. `https://www.eversports.de/s/poda-studio`) auf und extrahiert verschiedene URL-Kategorien wie 'Übersicht', 'Klassen', 'Workshops' usw. Diese werden in einem Dictionary `reconstructed_urls` gespeichert.

### Datenstrukturierung
- **Prozess**: Das `reconstructed_urls` Dictionary wird in ein DataFrame `reconstructed_urls_df` umgewandelt, wobei jede Zeile ein Schlüssel-Wert-Paar (Kategorie und URL) darstellt.

### URL-Validierung
- **Skript**: `aa_URL_Validation.py`
- **Funktion**: `validate_urls`
- **Prozess**: Überprüft jede URL aus `reconstructed_urls_df["URL"]` auf Gültigkeit und gibt ein DataFrame `validated_urls_df` zurück, das nur gültige URLs enthält.

### Extraktion spezifischer URLs
- **Prozess**: Spezifische URLs werden aus `validated_urls_df` extrahiert und in Variablen wie `url_s`, `url_scl`, `url_sw` und `url_sp` gespeichert.

### Erstellung eines DataFrames für URL-Kategorien
- **Prozess**: Erstellt ein neues DataFrame `url_categories_df`, wobei jede Spalte eine andere URL-Kategorie repräsentiert.

### Daten-Scraping-Prozesse

#### Pole Studio Scraping
- **Skript**: `aaa_PoleStudio_URL_S_Function.py`
- **Funktion**: `scrape_pole_studio`
- **Prozess**: Scrapet Informationen von der URL für Pole Studios (`url_s`) und speichert diese in `pole_studio_data`.

#### Workshops List Scraping
- **Skript**: `b_Workshopslist_URL_SW_Function.py`
- **Funktion**: `scrape_workshops`
- **Prozess**: Sammelt Informationen über Workshops von der URL `url_sw` und speichert diese in `workshops_data`.

#### Workshop Details Scraping
- **Skript**: `c_Workshop_URL_E_Function.py`
- **Funktion**: `scrape_workshop_details`
- **Prozess**: Extrahiert detaillierte Informationen über einen spezifischen Workshop von der ersten URL in `workshops_data['URL_SW']` und speichert diese in `workshop_details`.

#### Klassen List Scraping
- **Skript**: `d_Klassenlist_SCL_Function.py`
- **Funktion**: `scrape_classes`
- **Prozess**: Scrapet Informationen über Klassen von einer Liste von URLs (`urls_list`, basierend auf `url_scl`) und speichert diese in `classes_data`.

#### Klassen Details Scraping
- **Prozess**: Extrahiert die erste URL aus `classes_data['URL_SCL_E']` und verwendet `scrape_workshop_details`, um detaillierte Informationen zu einer Klasse zu erhalten.
