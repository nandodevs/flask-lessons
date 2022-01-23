from flask import Flask, render_template

app = Flask("project")

@app.route("/")
def ola_mundo():
    return render_template("index.html", meu_nome="Sisnando"), 200


@app.route("/informacao/")
@app.route("/informacao/<nome>")
@app.route("/informacao/<nome>/<idade>")

def nova_rota(nome = None, idade=None):
    return u"Nome: {}<br>Idade: {}".format(nome, idade), 200

app.run()

