import csv
import json
from operator import attrgetter

class City:
  name = ''
  country = ''
  iso3 = ''
  population = 0
  id = ''
  
  def __eq__(self, other):
    return self.name == other.name and self.country == other.country and self.iso3 == other.iso3
  
  def __hash__(self):
    return hash(('name', self.name, 'country', self.country, 'iso3', self.iso3))
  
class CityEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__

cities = []

f = open("worldcities.txt", "r", encoding="utf8")

csvReader = csv.DictReader(f)
for row in csvReader:
  populationString = row['population']
  population = 0
  if (populationString != ''):
    population = float(populationString)
  if(population > 30000):
    city = City()
    city.name = row['city_ascii']
    city.iso3 = row['iso3']
    city.country = row['country']
    city.population = population
    city.id = row['id']
    cities.append(city)
  
cities.sort(key=attrgetter('name'))
cities = list(set(cities))

jsonFile = open('cities.json', 'w', encoding='utf-8')
jsonString = json.dumps(cities, indent=4, cls=CityEncoder)
jsonFile.write(jsonString)