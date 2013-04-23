from flask.ext.script import Manager, Shell
from star import app, config_app, connect_controllers, connect_db
from star import controllers, views

def hookup_app(config_file="development.ini", relative_to="../"):
    app = config_app(config_file=config_file, relative_to=relative_to)
    connect_controllers()
    connect_db()
    return app

def _make_context():
    return dict(app=app, controllers=controllers, views=views)

manager = Manager(hookup_app())

@manager.option('-c', '--config', help='Config file path')
def shell(c):
    Shell(make_context=_make_context)

if __name__ == "__main__":
    manager.run()
