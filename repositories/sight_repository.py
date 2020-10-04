from db.run_sql import run_sql
from models.city import *
from models.country import *
from models.sight import *

import repositories.city_repository as city_repository
import repositories.country_repository as country_repository

def save(sight):
    sql = "INSERT INTO sights (name, country_id, city_id, visited) VALUES (%s, %s, %s, %s) RETURNING id"
    values = [sight.name, sight.country.id, sight.city.id, sight.visited]
    result = run_sql(sql, values)
    sight.id = result[0]['id']
    return sight

def select_all():
    sights = []
    sql = "SELECT * FROM sights"
    result = run_sql(sql)
    
    for row in result:
        sight = Sight(row["name"], row["country_id"], row["city_id"], row["id"])
        sights.append(sight)

    return sights


def delete_all():
    sql = "DELETE FROM sights"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM sights WHERE id = %s"
    values = [id]
    run_sql(sql, values)
