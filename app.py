from flask import Flask
from pass_checker.routes import checker  


app = Flask(__name__)
    
app.register_blueprint(checker)   


if __name__ == '__main__':
    app.run(debug=True)
