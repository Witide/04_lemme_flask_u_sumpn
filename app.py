from flask import Flask

my_app = Flask(__name__)

@my_app.route('/')
def root():
    return 'This is the root'
@my_app.route('/beep')
def beep():
    return 'this is beep'
@my_app.route('/boop')
def boop():
    return 'this is boop'
    
if __name__ == '__main__':
    my_app.debug = True
    my_app.run()