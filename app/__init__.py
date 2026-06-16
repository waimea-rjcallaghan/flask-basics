#===========================================================
# Flask App
#===========================================================

from flask import Flask, render_template
from dotenv import load_dotenv


# Create the app
app = Flask(__name__)

cats = [
    {
        "id": 13,
        "name": "dave",
        "image": "cat1.jpg"
    },
    {
        "id": 14,
        "name": "ben",
        "image": "cat2.jpg"
    },
    {
        "id": 19,
        "name": "mr bogles",
        "image": "cat3.jpg"
    },
    {
        "id": 68,
        "name": "mr 67",
        "image": "chicken.jpg"
    },
]

def get_cat(id):
    return next((item for item in cats if item["id"] == id), None)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Welcome!
#-----------------------------------------------------------
@app.get("/_base")
def show_base():
    return render_template("pages/_base.jinja")


#-----------------------------------------------------------
# Demo
#-----------------------------------------------------------
@app.get("/demo")
def show_demo_message():
    return render_template("pages/demo.jinja")


#-----------------------------------------------------------
# Welcome!
#-----------------------------------------------------------
@app.get("/")
def show_welcome():
    return render_template("pages/home.jinja")   



#-----------------------------------------------------------
# matching an ID
#-----------------------------------------------------------
@app.get("/thing/<int:id>")
def show_message_with_id(id):
    print(f"found id: {id}")
    return render_template("pages/id.jinja", id=id)   



#-----------------------------------------------------------
# cat list
#-----------------------------------------------------------
@app.get("/cats")
def show_message_with_cats():
   
    return render_template("pages/cats.jinja", cats=cats)     

    
        
@app.get("/cat/<int:id>")
def show_cat(id):
    cat = get_cat(id)

    if cat:
        return render_template("pages/cat.jinja", cat=cat)
    else:
        abort(404)     
        



#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()



