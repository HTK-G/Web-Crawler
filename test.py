import requests
import csv
from bs4 import BeautifulSoup
#import the html processor

url = "https://haorangao.com/"

response = requests.get(url)
response.raise_for_status()

html = response.text

soup = BeautifulSoup(html, "html.parser")

contents = soup.find_all("p")

paras = []

for content in contents:

    content_string = content.get_text(strip = True)
    if content_string:
        paras.append(content_string)

with open("paras.csv", "w", newline= "", encoding= "utf-8") as file:
    writer = csv.writer(file)
    writer.writerow([paras])
    writer.writerow(["index" ,"paragraph"])

    for i, text in enumerate(paras, 1):
        writer.writerow([i, text])

print(f"Wrtie {len(paras)} paragraphs to paras.csv")