from db.run_sql import run_sql
from models.city import *
from models.country import *
# from models.sight import *


def save(country):
    sql = "INSERT INTO countries (name) VALUES (%s) RETURNING id"
    values = [country.name]
    result = run_sql(sql, values)
    country.id = result[0]['id']
    return country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    result = run_sql(sql)
    
    for row in result:
        country = Country(row["name"], row["id"])
        countries.append(country)

    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    for row in result:
        country = Country(row["name"], row["id"])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

# return all cities in country
def cities(country):
    cities = []
    sql = 'SELECT * FROM cities WHERE country_id = %s'
    value = [country.id]
    result = run_sql(sql, value)
    
    for row in result:
        city = City(row["name"], country, row['visited'], row["id"])
        cities.append(city)

    return cities

