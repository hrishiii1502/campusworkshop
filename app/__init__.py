"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrq5ro2qv2dcb938630-a.oregon-postgres.render.com",
        database="todo_yflq",
        user="root",
        password="bvyh6Bl9RmoUwK7za1mqbOBWTuivtfhE")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
