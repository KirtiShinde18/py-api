from flask import Flask

# --------------
# serevr 
# --------------
app = Flask(__name__)


# --------------
# Routes 🌍
# --------------

@app.route("/", methods=["GET"])
def home():
    return {"message" : "Welcome to flask 🌸"}

# CREATE 
@app.route("/todo/create", methods=["POST"])
def createTodo():
    return {"message" : "Todo create success ✚"}

# READ 
@app.route("/todos", methods=["GET"])
def readTodo():
    return {"message" : "Todo readTodo success 👀"}


# UPDATE 
@app.route("/todo/update", methods=["PUT"])
def updateTodo():
    return {"message" : "Todo update success ✏️"}


# DELETE 
@app.route("/todo/remove", methods=["DELETE"])
def deleteTodo():
    return {"message" : "Todo delete success ❌"}


# -----------------
# serevr start 🌍
# -----------------
if __name__ == "__main__":
    app.run(debug=True)