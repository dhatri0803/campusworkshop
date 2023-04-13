"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-cgrpvmndvk4rjsv8jqfg-a",
        database="todo_x1p2",
        user="root",
        password="WsqRSnKsOFYqailYMFbydPVYJ7GL1NQt")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
