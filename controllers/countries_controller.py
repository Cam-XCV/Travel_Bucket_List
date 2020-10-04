from flask import Flask, render_template, request, redirect
from flask import Blueprint

import repositories.country_repository as country_repository
import repositories.city_repository as cities_repository

from models.country import Country
from models.city import City

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("/countries/index.html", countries=countries)

@countries_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect("/countries")

@countries_blueprint.route("/countries/new", methods=["POST"])
def add_country():
    name = request.form["countryname"]
    country = Country(name)
    country_repository.save(country)
    return redirect("/countries")

@countries_blueprint.route("/countries/<id>")
def show_country(id):
   country = country_repository.select(id)
   cities = country_repository.cities(country)
   return render_template("/countries/show.html", country=country, cities=cities)

@countries_blueprint.route("/countries/<id>/new", methods=["POST"])
def add_city(id):
    country = country_repository.select(id)
    city_name = request.form["cityname"]
    city = City(city_name, country)
    cities_repository.save(city)
    return redirect("/countries/"+id)

@countries_blueprint.route("/countries/<id>/<id2>")
def show_city(id, id2):
    city = cities_repository.select(id2)
    sights = cities_repository.sights(city)
    return render_template("/cities/show.html", city=city, sights=sights)    

@countries_blueprint.route("/countries/<id>/<id2>/delete", methods=["POST"])
def delete_city(id, id2):
    cities_repository.delete(id2)
    return redirect("/countries/"+id)

@countries_blueprint.route("/countries/<id>/<id2>/mark-visit", methods=["POST"])
def mark_city(id, id2):
    city = cities_repository.select(id2)
    city.mark_visited()
    cities_repository.update(city)
    return redirect("/countries/"+id)


