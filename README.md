# Final-project--COVID-19

This project aim for practicing web scraping skills and utilize the usage of pandas for data analysis.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

requests

beautifulsoup4

pandas

```
pip install requests

pip install beautifulsoup4
```

### Running the files

First, run the "WebScraping_nyt.py" to scrape the data from New York Times website. 

This will generate the file "us-states.csv".

Second, run the "MHH-final_project-4.py" with 'us-states.csv' as input.

This will generate 4 figures that present the data in heatmap or stacked bar chart.

```
cd Respiratory

python WebScraping_nyt.py

python MHH-final_project-4.py
```

