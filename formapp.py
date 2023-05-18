from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template('formapphome.html')
    
    
@app.route("/p1", methods=['GET', 'POST'])
def render_page1():

    if request.method == 'POST': 
        if request.form["lname"] == "":
            lname = ""
        else:
            lname = " " + request.form["lname"] #*
        if request.form["animal"] == "":
            animal = "the townspeople"
            aname = "the townspeople"
        else:
            animal = request.form["animal"] #*
            if request.form["aname"] == "":
                aname = "the " + animal
                animal = "their animal companion; a/an " + animal
            else:
                aname = request.form["aname"] #*
                animal = "their animal companion; a/an " + animal +  " named " + aname
          
        color = request.form["colors"]
        fname = request.form["fname"]
        vehicle = request.form["vehicles"]
        weapon = request.form["weapons"]
        villain = request.form["villains"]        
        
        story = "Once upon a time there was a person named " + fname + lname + ". They were just an ordinary person until one day they found out that " + villain + " had kidnapped " + animal + ". Upon hearing about this, " + fname + " began their epic journey to get " + aname +" back. They took a " + color + " " + vehicle + " and their " + weapon + " and set off on their quest to rescue " + aname +". They traveled through jungles and mountains, fighting dragons and giants on their way, until they came to " + villain +"'s volcano, where they were holding " + aname + " hostage. " + fname + " took their " + vehicle + " up the volcano, dodging flaming rocks along the way. They jumped into the pit to face " + villain +". It was a hard battle but in the end " + fname + " managed to defeat " + villain + " using their " + weapon + " and saved " + aname + ". They lived happily ever after. The End."
    
        return render_template('formapppage1.html', story = story)
    else:
        badRequest = "Error. Try again."
        return render_template('formapppage1.html', badRequest = badRequest)
    

if __name__=="__main__":
    app.run(debug=True)