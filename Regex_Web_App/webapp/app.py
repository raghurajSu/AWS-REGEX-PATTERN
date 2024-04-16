# S1-import Flask

from flask import Flask ,render_template,request
import re

# S2-Create a Flask Object and pass __name__
app=Flask(__name__)

##################################################
# S3-Create a route and bind it to a fun
@app.route('/' , methods=["GET","POST"])
def home():
    if request.method=="POST":
        test_string =request.form.get('test_string')
        regex_pattern =request.form.get('regex_pattern')
        matches = find_matches(test_string,regex_pattern)
        return render_template('result.html' ,test_string=test_string,regex_pattern=regex_pattern,matches=matches)
    return render_template('index.html')

@app.route('/results' , methods=["GET","POST"])
def reult():
    test_string =request.form.get('test_string')
    regex_pattern =request.form.get('regex_pattern')
    matches = find_matches(test_string,regex_pattern)
    return render_template('result.html' ,test_string=test_string,regex_pattern=regex_pattern,matches=matches)

def find_matches(test_string,regex_pattern):
    matches=re.findall(regex_pattern,test_string)
    return matches

@app.route("/validator",methods=["GET","POST"])
def validate():
    if request.method == "POST":
        mail=request.form.get("mail")
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",mail):
            result ='Valid email adress :'+mail 
        else:
            result ="Invalid Email Adress"
        
        return render_template("email_validator.html",result=result)
###################################################
# S4-Run the Application
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)