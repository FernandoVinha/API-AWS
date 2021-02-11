#importa o Flask 
from Flask import Flask
#define o incio do progra
app = Flask("api")
#cria o metodo da api
@app.route("/api", methods=["GET"])
def rreturn():
    return{"funcionado"}
#luping infinito
app.run()