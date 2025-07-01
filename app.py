from flask import Flask, Blueprint
from pass_checker.routes import checker

app=Flask(__name__)

app.register_blueprint(checker)
print("Flask app starting...")

if __name__=='__main__':
    app.run(debug=True)