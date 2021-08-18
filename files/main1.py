from selectorlib import Extractor
import requests
class Calorie():
    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10*self.weight + 6.5*self.height + 5 - self.temperature*10
        return result

class Temperature():
    url_path = 'https://www.timeanddate.com/weather/'
    yml_path = 'temperature.yaml'
    def __init__(self, country, city):
        self.country = country.replace(" ","-")
        self.city = city.replace(" ","-")
    def _build_url(self):
        url = self.url_path + self.country + '/' + self.city
        return url
    def _scrape(self):
        url = self._build_url()
        extractor = Extractor.from_yaml_file(self.yml_path)
        r = requests.get(url)
        full_content = r.text
        raw_content = extractor.extract(full_content)
        return raw_content

    def get(self):
        scraped_content = self._scrape()
        return float(scraped_content['temp'].replace('\xa0°C', ''))



if __name__ == '__main__':
    temperature = Temperature(country='india', city='nashik').get()
    calorie = Calorie(temperature=temperature, weight=70, height=175, age=32)
    print(calorie.calculate())
    print(temperature)