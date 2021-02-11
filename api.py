from flask import Flask
app = Flask("api")
@app.route("/teste", methods=["GET"])
def rreturn():
    return{"funcionado":"bem"}
app.run()