from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index_page():
   
   
    return render_template("application-form.html")

@app.route("/application", methods=["POST", "GET"])
def application():
	firstname = request.form["firstname"]
	lastname = request.form["lastname"]
	salary = request.form["salary"]
	position = request.form["position"]
	return render_template("application.html", firstname=firstname, lastname=lastname, salary=salary, position=position)
	# , firstname=firstname, lastname=lastname, salary=salary, position=position

    

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)