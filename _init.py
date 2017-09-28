from flask import Flask

app = Flask(__name__, instance_relative_config=True)
import app_run
app.config.from_object('config')
app.secret_key = 'Andela cohort 4'