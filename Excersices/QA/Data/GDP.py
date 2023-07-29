import matplotlib.pyplot as plt
import csv

def get_data(file_name, country):
  with open(file_name, 'r') as file:
    csvreader = csv.reader(file)
    for row in csvreader:
        if row[0] == country:
            return row[4:]
    print("Country not found")
    return None

def compute_datasets(country, gdp, population):
    dict = {}
    for i in range(0, len(gdp)):
        dict[1959 + i] = gdp[i] / population[i]

        


def plot(gdp_per_capita, years):
