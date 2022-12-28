from flask import Flask,render_template,request
import random 
app=Flask(__name__)
random_number=random.randint(1,100)
attempts=5
message=""
winner=False
game_over=False
def check_game_over():
    global attempts
    if attempts==0:
        return True
    else:
        return False
def check(user_number):
    global attempts,winner
    if user_number<random_number:
        attempts=attempts-1
        message="too low"
        return message
    elif user_number>random_number:
        attempts=attempts-1
        message="too high"
        return message
    else:
        winner=True
        message="you get it right"
        return message
@app.route('/', methods=['GET','POST'])
def home_page():
    global message,game_over,random_number
    if request.method == 'POST':
        message=check(int(request.form['userguess']))
        game_over=check_game_over()
        if game_over:
            return render_template("game_over.html",random_number=str(random_number))
        elif winner:
            return render_template("winning_page.html",message=message)
        else:
            return render_template("home_page.html",attempts=str(attempts),message=message)
    return render_template("home_page.html",attempts=str(attempts),message=message)
if __name__=="__main__":
    app.run(debug=True)