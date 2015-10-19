from asmlearner import app, config
from asmlearner.lib.database.sqlite import DB

from os.path import join



if __name__ == '__main__':
    DB(config.DATABASE).executescript(join(config.PROJECT_DIR, 'init.sql'))
    
    app.secret_key = 'lolthisissecretkeyforthisapp'

    app.debug = True
    app.run(host='0.0.0.0', port=3333)
