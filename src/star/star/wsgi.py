from star.manager import hookup_app
import sys

config_file = "prod.ini"
app = hookup_app(config_file=config_file)
