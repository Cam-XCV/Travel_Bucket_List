from db.run_sql import run_sql
from models.city import *
from models.country import *
from models.sight import *

import repositories.country_repository as country_repository


def save(city):
    sql = "INSERT INTO cities (name, country_id, visited) VALUES (%s, %s, %s) RETURNING id"
    values = [city.name, city.country.id, city.visited]
    result = run_sql(sql, values)
    city.id = result[0]['id']
    return city



def select_all():
    cities = []
    sql = "SELECT * FROM cities"
    result = run_sql(sql)

    for row in result:
        country = country_repository.select(row["country_id"])
        city = City(row["name"], country, row['visited'], row["id"])
        cities.append(city)

    return cities


def select(id):
    city = None
    sql = "SELECT * FROM cities WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    for row in result:
        country = country_repository.select(row["country_id"])
        city = City(row["name"], country, row['visited'], row["id"] )
    return city

def delete_all():
    sql = "DELETE FROM cities"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM cities WHERE id = %s"
    values = [id]
    run_sql(sql, values)


#return all sights in city
def sights(city):
    sights = []
    sql = "SELECT * FROM sights WHERE city_id = %s"
    value = [city.id]
    result = run_sql(sql, value)

    for row in result:
        sight = Sight(row["name"], row["country_id"], row["city_id"], row["id"])
        sights.append(sight)

    return sights

#update city visited value
def update(city):
    sql = "UPDATE cities SET (name, country_id, visited) = (%s, %s, %s) WHERE id = %s"
    values = [city.name, city.country.id, city.visited, city.id]
    run_sql(sql, values)

