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
def coding_the_text(shift):
    array=convert_text_to_array()
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
def convert_the_list_to_a_Word(shift):
    coded_array=coding_the_text(shift)
    coded_word=coded_array[0]
    for letter in range(len(coded_array)-1):
        coded_word+=letter
    return coded_word
@app.route('/')
def home():
    return render_template("home_page.html")

if __name__=="__main__":
    app.run(debug=True)