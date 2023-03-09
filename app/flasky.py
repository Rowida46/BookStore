# call create app function & run

from app import create_app  # from __init__.py file -> our entry point


app = create_app('prd')

if __name__ == '__main__':
    app.run()
