from flask import Flask,render_template,request
app=Flask(__name__)
def solve_equation(a,b):
    if a==0:
        if b==0:
            return "all numbers are solution to the equation"
        else:
            return "no solution to this equation"
    else:
        x=-b/a
        return x
@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        solution=solve_equation(int(request.form['value a']),int(request.form['value b']))
        print(solution)
    return render_template("home_page.html")
if __name__=="__main__":
    app.run(debug=True)