from flask import Flask,render_template,request
app=Flask(__name__)
converted_text=""
shift=0
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
        if letter in alphabet:
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
    if request.method == 'POST':
        return render_template("home_page.html", converted_text=code(request.form['usertext'],int(request.form['shift'])))
    return render_template("home_page.html", converted_text=converted_text)
if __name__=="__main__":
    app.run(debug=True)