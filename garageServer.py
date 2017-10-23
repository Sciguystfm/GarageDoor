from flask import Flask
app = Flask(__name__)
from garage import toggleDoor, getGarageIsOpen
from flask import render_template

isOpen = getGarageIsOpen()

@app.route("/garageState")
def getGarageState():
    isOpen=getGarageIsOpen()
    return isOpen

@app.route("/garageToggle")
def garageToggle():
    return toggleDoor()

@app.route("/garageUI")
def garageUI():
    return render_template('garageUI.html',isOpen=isOpen)

if __name__ == '__main__':
    app.run()