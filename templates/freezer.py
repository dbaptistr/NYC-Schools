from frozen_flask import Freezer
from app import app, School

    # app.config['FREEZER_RELATIVE_URLS'] = True
    # app.config['FREEZER_DESTINATION'] = 'docs'

    freezer = Freezer(app)

    if __name__ == '__main__':
        freezer.freeze()