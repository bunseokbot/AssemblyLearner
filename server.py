from asmlearner import app

if __name__ == '__main__':
    app.secret_key = 'lolthisissecretkeyforthisapp'

    app.debug = True
    app.run(host='0.0.0.0', port=3333)
