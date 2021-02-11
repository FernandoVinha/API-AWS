from flask import Flask
app = Flask("api")
@app.route("/api", methods=["GET"])
def rreturn():
    return{"funcionado"}
 
    app.run(host='0.0.0.0', port=80)
