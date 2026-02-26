from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template ("inicio.html")

@app.route("/suma", methods=["GET","POST"])
def sumar():
    
    if request.method == "POST":
     if not request.form.get("numero 1") or not request.form.get("numero 2"):
        return render_template("suma.html", error="Por favor ingrese ambos números")
     else:
      numero1=float(request.form.get("numero 1"))
      numero2=float(request.form.get("numero 2"))
      resultado=numero1+numero2
      return render_template("suma.html", resultado=resultado)
    return render_template("suma.html")

@app.route("/Division", methods=["GET","POST"])
#cambio
def dividir():
    if request.method == "POST":
     if not request.form.get("numero 1") or not request.form.get("numero 2"):
        return render_template("division.html", error="Por favor ingrese ambos números")
     else:
      numero1=float(request.form.get("numero 1"))
      numero2=float(request.form.get("numero 2"))
      if numero2==0:
        return render_template("division.html", error="No se puede dividir por cero")
      resultado=numero1/numero2
      return render_template("division.html", resultado=resultado)
    return render_template("division.html")




if __name__=="__main__":
    app.run(debug=True)
    
