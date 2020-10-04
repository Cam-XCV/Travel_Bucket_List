import pdb
from models.city import *
from models.country import *
from models.sight import *

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

sight_repository.delete_all()
city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("Scotland")
country_2 = Country("Germany")
country_3 = Country("Japan")
country_4 = Country("Italy")
country_repository.save(country_1)
country_repository.save(country_2)
country_repository.save(country_3)
country_repository.save(country_4)

city_1 = City("Glasgow", country_1)
city_2 = City("Berlin", country_2)
city_3 = City("Tokyo", country_3)
city_4 = City("Edinburgh", country_1)
city_5 = City("Pisa", country_4)
city_6 = City("Munich", country_2)
city_repository.save(city_1)
city_repository.save(city_2)
city_repository.save(city_3)
city_repository.save(city_4)
city_repository.save(city_5)
city_repository.save(city_6)


sight_1 = Sight("Kelvingrove Art Gallery", country_1, city_1)
sight_2 = Sight("Brandenburg Gate", country_2, city_2)
sight_3 = Sight("Tokyo Tower", country_3, city_3)
sight_4 = Sight("Edinburgh Castle", country_1, city_4)
sight_5 = Sight("Leaning Tower of Pisa", country_4, city_5)
sight_6 = Sight("Reichstag Building", country_2, city_2)
sight_7 = Sight("Berlin Wall Memorial", country_2, city_2)
sight_repository.save(sight_1)
sight_repository.save(sight_2)
sight_repository.save(sight_3)
sight_repository.save(sight_4)
sight_repository.save(sight_5)
sight_repository.save(sight_6)
sight_repository.save(sight_7)


# print(sight_repository.select_all())
# print(city_repository.select_all())
# print(country_repository.select_all())

# print(country_repository.cities(country_1))

pdb.set_trace()