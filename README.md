# Hall_of_Pole_Version_5
Scraper


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
