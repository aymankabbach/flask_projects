from flask import Flask
import random 
app=Flask(__name__)
random_number=random.randint(1,100)
@app.route('/')
def home_page():
    return str(random_number)
if __name__=="__main__":
    app.run(debug=True)