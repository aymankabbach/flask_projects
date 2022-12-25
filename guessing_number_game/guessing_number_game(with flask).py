from flask import Flask,render_template,request
import random 
app=Flask(__name__)
random_number=random.randint(1,100)
attempts=5
message=""
def check(user_number):
    global attempts
    if user_number<random_number:
        attempts=attempts-1
        message="too low"
        return message
    elif user_number>random_number:
        attempts=attempts-1
        message="too high"
        return message
    else:
        message="you get it right"
        return message
@app.route('/', methods=['GET','POST'])
def home_page():
    if request.method == 'POST':
        return render_template("home_page.html",attempts=str(attempts),message=check(int(request.form['userguess'])))
    return render_template("home_page.html",attempts=str(attempts), message=message)
if __name__=="__main__":
    app.run(debug=True)