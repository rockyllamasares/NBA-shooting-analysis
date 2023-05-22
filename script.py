import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.basketball-reference.com/leagues/NBA_2022_totals.html"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Find the table in the HTML
    table = soup.find("table", {"id": "totals_stats"})

    # Extract table header and data using pandas
    df = pd.read_html(str(table))[0]

    # Clean up the DataFrame (remove unnecessary columns and rows)
    df = df[df["Rk"] != "Rk"]

    # Save the DataFrame as an Excel file
    df.to_excel("nba_player_stats.xlsx", index=False)
    print("Table data exported to nba_player_stats.xlsx")
else:
    print("Failed to fetch the webpage")
