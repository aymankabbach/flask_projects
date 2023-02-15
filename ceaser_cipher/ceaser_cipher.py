from flask import Flask,render_template,request
app=Flask(__name__)
converted_text=""
shift=0
message=""
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def convert_text_to_array(text):
    array=[]
    for letter in text:
        array.append(letter)
    return array
def coding_the_text(text,shift):
    array=convert_text_to_array(text)
    coded_array=[]
    for letter in array:
        if letter.lower() in alphabet:
            if alphabet.index(letter)+shift>=len(alphabet):
                coded_array.append(alphabet[alphabet.index(letter)-len(alphabet)+shift])
            else:
                coded_array.append(alphabet[alphabet.index(letter)+shift])
        else:
            coded_array.append(letter)
    return coded_array
def convert_the_array_to_text(text,shift):
    coded_array=coding_the_text(text,shift)
    coded_text=coded_array[0]
    for letter in range(1,len(coded_array)):
        coded_text+=coded_array[letter]
    return coded_text
def code(text,shift):
    return convert_the_array_to_text(text,shift)
@app.route('/', methods=['GET','POST'])
def home():
    global message,shift
    if request.method == 'POST':
        try:
            shift=int(request.form['shift'])
            if int((request.form['shift']))>0:
                return render_template("home_page.html", converted_text=code(request.form['usertext'],int(request.form['shift'])))
            elif int((request.form['shift']))<=0:
                message="shift must be positive"
                return render_template("home_page.html", converted_text=converted_text, message="")
        except:
            message="shift must be an integer"
            return render_template("home_page.html", converted_text=converted_text,message=message)
    return render_template("home_page.html", converted_text=converted_text,message=message)
if __name__=="__main__":
    app.run(debug=True)