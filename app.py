from flask import Flask
app=Flask(__name__)
@app.route('/',methods=["POST","GET"])
def homepage():
    return "<h1>Welcome BIT</h1>"

if __name__==("__main__"):
    app.run(debug=True,port=2000)

