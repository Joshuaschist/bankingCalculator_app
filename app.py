from flask import Flask, render_template, request
from smart_utils.banking import Account
from smart_utils.calculator import Calculator
from smart_utils.exceptions import LowBalanceError, InvalidOperationError

app = Flask(__name__)

account = Account("Chisom", 1000)
calc = Calculator()

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard", methods=["POST"])
def dashboard():

    try:
        action = request.form["action"]

        if action == "deposit":
            amount = float(request.form["amount"])
            account.deposit(amount)

        elif action == "withdraw":
            amount = float(request.form["amount"])
            account.withdraw(amount)

        elif action == "calculate":
            a = float(request.form["a"])
            b = float(request.form["b"])
            op = request.form["op"]
            result = calc.calculate(op, a, b)
            return f"Calculator Result: {result}"

    except LowBalanceError as e:
        return str(e)

    except InvalidOperationError as e:
        return str(e)

    return render_template("dashboard.html", balance=account.get_balance())


if __name__ == "__main__":
    app.run(debug=True)