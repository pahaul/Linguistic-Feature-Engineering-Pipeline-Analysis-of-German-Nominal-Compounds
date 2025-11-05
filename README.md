# Linguistic-Feature-Engineering-Pipeline-Analysis-of-German-Nominal-Compounds
This repository contains the complete ETL pipeline developed for a Bachelor's thesis analyzing the frequency and usage patterns of nominal compounds in German texts from a specific online magazine.


## Project Pipeline

The project follows a five-stage data processing workflow:

**Extraction (Scraping):**

- `scrape.py` downloads raw HTML content from the target online magazine.

**Cleaning (Text Preprocessing):**

- `read.py` processes the HTML files, stripping all structural tags and non-content elements to produce clean, raw text files.

**Linguistic Processing:**

- `pos.py` uses the spaCy library to apply linguistic annotations (Token, Lemma, POS-Tag) to the clean text.

**Transformation (Compound Splitting):**

- `noun.py` isolates all noun lemmas.

- `readsplit.py` then ingests the results of an external compound splitter, separates the base components (e.g., Wasser + Stoff from Wasserstoff), and creates two distinct data streams (Erstglied_R.txt and Zweitglied_R.txt).

**Analysis:**

- `frequenz.py` calculates the Top 100 frequency lists for both the first and second components.

- `evaluation.py` iterates over these frequency lists to determine the varieties of full compounds each top component participates in, generating the final analysis reports.
