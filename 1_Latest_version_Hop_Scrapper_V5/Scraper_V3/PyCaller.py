from a_URLS_Reconstruction import reconstruct_urls_and_extract_buttons
from b_URLS_Validation import validate_urls
from c_PoleStudio_Overview_S import scrape_pole_studio
from d_Workshop_List_SW import scrape_workshops
from e_Workshop_Overview_E import scrape_workshop_details
from f_Klassen_List_SCL import scrape_classes
from g_Klassen_Overview_E_SCL import scrape_class_details
import pandas as pd

def process_urls(urls):
    """
    Prozessiert eine Liste von URLs durch verschiedene Scraping-Funktionen.
    """
    print("Starte URL-Rekonstruktion...")
    reconstructed_urls_list = [reconstruct_urls_and_extract_buttons(url)[1] for url in urls]
    reconstructed_urls = {k: v for d in reconstructed_urls_list for k, v in d.items()}

    print("Konvertiere in DataFrame...")
    reconstructed_urls_df = pd.DataFrame(list(reconstructed_urls.items()), columns=['Kategorie', 'URL'])
    
    print("Validiere URLs...")
    validated_urls_df = validate_urls(reconstructed_urls_df["URL"].to_list())
    validated_urls = validated_urls_df["Valid_URL"].tolist()

    # Aufteilung und Verarbeitung der URLs
    results = {'pole_studio_data': pd.DataFrame(), 'classes_data': pd.DataFrame(), 
               'classes_details': pd.DataFrame(), 'workshops_data': pd.DataFrame(), 
               'workshop_details': pd.DataFrame()}
    
    for url in validated_urls:
        if "/s/" in url:
            print(f"Scrape Pole Studio Daten von {url}...")
            pole_studio_data = scrape_pole_studio(url)
            results['pole_studio_data'] = pd.concat([results['pole_studio_data'], pole_studio_data], ignore_index=True)
        elif "/sw/" in url:
            print(f"Scrape Workshops Daten von {url}...")
            workshop_data = scrape_workshops(url)
            results['workshops_data'] = pd.concat([results['workshops_data'], workshop_data], ignore_index=True)
            for workshop_url in workshop_data['URL_E']:
                print(f"Scrape Workshop Details von {workshop_url}...")
                workshop_detail = scrape_workshop_details(workshop_url)
                if not workshop_detail.empty:
                    results['workshop_details'] = pd.concat([results['workshop_details'], workshop_detail], ignore_index=True)
        elif "/scl/" in url:
            print(f"Scrape Klassen Daten von {url}...")
            classes_data = scrape_classes([url])
            results['classes_data'] = classes_data
            if 'URL_SCL_E' in classes_data.columns:
                print(f"Scrape Klassen Details von {url}...")
                classes_details_list = [scrape_class_details(url_scl_e) for url_scl_e in classes_data['URL_SCL_E']]
                classes_details_df = pd.concat(classes_details_list, ignore_index=True)
                results['classes_details'] = classes_details_df

    print("Verarbeitung abgeschlossen.")
    return results

# Test-Code (Falls benötigt)
# test_urls = ["https://www.eversports.de/s/poda-studio"]  # Beispiel-URL
# test_results = process_urls(test_urls)
# for category, df in test_results.items():
#     print(f"Kategorie: {category}")
#     print(df)
#     print("\n")
