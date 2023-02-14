from flask import Flask,render_template,request
app=Flask(__name__)
solution=""
def Calculate_the_discriminant(a,b,c):
    discriminant=(b*b)-(4*a*c)
    return discriminant
def calculate_solution_case_2(discriminant,b,a):
    first_solution=(-b+pow(discriminant,0.5))/(2*a)
    second_solution=(-b-pow(discriminant,0.5))/(2*a)
    return [first_solution,second_solution]
def calculate_solution_case_3(a,b):
    return f"x= {-b/(2*a)}"
def solve_equation(a,b,c):
    if (a==0):
        if (b==0):
            if (c==0):
                return "all numbers are solutions to this equation"
            else:
                return "this equation has no solution"
        else:
            return f"x= {-c/b}"
    else:
        discriminant=Calculate_the_discriminant(a,b,c)
        if (discriminant <0):
            return "this equation has no solution"
        if (discriminant >0):
            solution=calculate_solution_case_2(discriminant,b,a)
            return f"x= {solution[0]}    x= {solution[1]}"
        if (discriminant==0):
            return calculate_solution_case_3(a,b)
@app.route('/',methods=['GET','POST'])
def home():
    global solution
    if request.method == 'POST':
        solution=solve_equation(int(request.form['value a']),int(request.form['value b']),int(request.form['value c']))
        if type(solution)!=str:
            return render_template("home_page.html", solution=str(solution))
        else:
            return render_template("home_page.html", solution=solution)
    return render_template("home_page.html", solution=solution)
if __name__=="__main__":
    app.run(debug=True)