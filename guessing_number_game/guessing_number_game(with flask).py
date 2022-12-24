from flask import Flask,render_template
import random 
app=Flask(__name__)
random_number=random.randint(1,100)
attempts=5
@app.route('/')
def home_page():
    return render_template("home_page.html",attempts=str(attempts))
if __name__=="__main__":
    app.run(debug=True)