# Hall of Pole Project Overview

## Introduction
The Hall of Pole project aims to aggregate and process data from various sources related to Pole Dance Studios, primarily focusing on data extraction from web sources and management of this data for further analysis and display on the website. The project uses Python scripts for web scraping, data processing, and database management.


# Installation Guide for Hall of Pole Project

## Prerequisites
Before you begin, ensure you have Python installed on your system. This project is compatible with Python 3.6 and above.

## Step-by-Step Installation

1. **Clone the Repository**
   First, clone the repository to your local machine. Open your terminal and run:
   ```bash
   git clone https://github.com/hamudal/Hall_of_Pole_Version_5/tree/main/1_Latest_version_Hop_Scrapper_V5/Scraper_V3
   cd Scraper_V3

   pip install -r requirements.txt

## Files Description

### a_URLS_Reconstruction.py
- **Purpose**: Extracts and reconstructs specific URLs from a given webpage.
- **Details**: This script uses requests and BeautifulSoup to fetch the content of a webpage and parse HTML. It extracts elements based on specific CSS classes and reconstructs URLs for different sections of the site (e.g., Overview, Classes, Workshops, etc.).

### b_URLS_Validation.py
- **Purpose**: Validates a list of URLs to check their accessibility.
- **Details**: Utilizes requests to send HTTP requests to URLs and verify their status. Incorporates logging to track the validation process, marking URLs as valid or invalid.

### c_PoleStudio_Overview_S.py
- **Purpose**: Scrapes detailed information about Pole Studios from their webpages.
- **Details**: Extracts various data points like studio name, contact information, description, ratings, etc., using requests and BeautifulSoup for HTML parsing.

### d_Workshop_List_SW.py
- **Purpose**: Gathers information about workshops offered by Pole Studios.
- **Details**: Scrapes workshop-related data such as name, date, price, and studio information, compiling it into a structured format.

### e_Workshop_Overview_E.py
- **Purpose**: Extracts detailed information about individual workshops.
- **Details**: Similar to c_PoleStudio_Overview_S.py, but focuses on specific workshops, retrieving details like descriptions, levels, dates, and times.

### f_Class_List_SCL.py
- **Purpose**: Collects data about classes available in different Pole Studios.
- **Details**: Processes multiple URLs to scrape class information, including time, duration, name, and availability.

### g_Klassen_Overview_E_SCL.py
- **Purpose**: Provides detailed insights into specific classes offered.
- **Details**: Extracts comprehensive details of individual classes, including descriptions, instructors, locations, and schedules.

### PyCaller.py
- **Purpose**: Central script to process URLs using the above modules.
- **Details**: Orchestrates the execution of other scripts, managing the flow of data from one module to another, ensuring cohesive data processing.

### SQL_Connection.ipynb
- **Purpose**: Manages database connections and operations.
- **Details**: A Jupyter Notebook that outlines procedures for connecting to, querying, and managing a database storing the scraped data. It provides interactive elements for database operations.

### CSV_Collector.py
- **Purpose**: Aggregates URLs from multiple CSV files.
- **Details**: Searches through CSV files in a specified directory, extracting and combining URLs that match a given pattern. Ensures data consolidation for analysis.

## Best Practices Followed
- Modularity: Each script focuses on a single task, making the codebase more maintainable and scalable.
- Error Handling: Robust error handling to manage exceptions and maintain process flow.
- Code Readability: Clear naming conventions, consistent formatting, and detailed comments.
- Logging: Comprehensive logging in b_URLS_Validation.py for tracking URL validation processes.

## Usage
Each script can be run independently or orchestrated through PyCaller.py, depending on the required operation. Ensure that the Python environment has necessary dependencies installed (requests, pandas, BeautifulSoup, etc.).

---

## Main Frame Overview

The Main Frame serves as the orchestrator for processing URLs and aggregating data from various sources. It's designed to systematically extract, organize, and display data related to Pole Dance Studios.

### Functionality

- **process_and_print_results**: This function processes a given URL and prints the results. It utilizes other scripts for data extraction, handling each URL individually.

- **Data Aggregation**: After processing URLs, the script initializes several DataFrames to store different categories of data like Pole Studio, Workshop, Class details, etc.

- **Looping Through URLs**: It iterates over a list of URLs (e.g., from a CSV file) and calls `process_and_print_results` for each URL. The gathered data is then added to respective DataFrames.

- **Dataframes Initialization**: Separate DataFrames for Pole Studio Data, Workshop Data, Workshop Details, Class Data, and Class Details are initialized and populated with scraped data.

- **Data Display**: Finally, it prints out the collected data for each category, providing a comprehensive overview.

### Sample Output

The Main Frame displays the aggregated data in an organized manner. Here's a glimpse of the output:

