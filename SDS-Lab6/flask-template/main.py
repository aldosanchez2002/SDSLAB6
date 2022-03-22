# Alexis Gordon-Martin and Aldo Sanchez
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import answers
from model import grade
from collections import defaultdict

# -- Initialization section --
app = Flask(__name__)

# -- Routes section --
@app.route('/')
def main():
  return render_template("home.html",states=answers.capital_dic)

@app.route('/results', methods=['GET', 'POST'])
def main2():
  if request.method=="GET":
      return "You have not filled out the form."
  else:
    guesses = defaultdict(str)
    for state in answers.capital_dic:
      guesses[state]=request.form[state] 
    result=grade(guesses)
    return render_template("results.html", result=result)

@app.route('/answers')
def index():
  return
  
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080)