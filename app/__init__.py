from flask import Flask

app = Flask(__name__)

if app.config == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views
