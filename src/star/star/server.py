from star.manager import hookup_app
import sys

if __name__ == "__main__":
    config_file = "development.ini"
    # Use the first arg for config file, if specified.
    command_args = sys.argv[1:]
    if command_args:
        config_file = command_args[0]
    app = hookup_app(config_file=config_file)
    app.run(host='127.0.0.1')
